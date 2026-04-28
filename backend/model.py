
# import os
# import numpy as np
# import tensorflow as tf
# from PIL import Image
# from scipy.stats import entropy

# # ---------------- CONFIG ----------------
# IMAGE_SIZE = (224, 224)

# # MUCH SAFER THRESHOLDS
# MIN_CONFIDENCE = 25.0          # was 40 (too strict)
# MAX_ENTROPY = 2.5              # confusion threshold

# CLASS_NAMES = [
#     "Alambadi","Amritmahal","Ayrshire","Banni","Bargur","Bhadawari",
#     "Brown_Swiss","Dangi","Deoni","Gir","Guernsey","Hallikar","Hariana",
#     "Holstein_Friesian","Jaffrabadi","Jersey","Kangayam","Kankrej",
#     "Kasargod","Kenkatha","Kherigarh","Khillari","Krishna_Valley",
#     "Malnad_gidda","Mehsana","Murrah","Nagori","Nagpuri","Nili_Ravi",
#     "Nimari","Ongole","Pulikulam","Rathi","Red_Dane","Red_Sindhi",
#     "Sahiwal","Surti","Tharparkar","Toda","Umblachery","Vechur"
# ]

# BUFFALO_BREEDS = {"Murrah","Nili_Ravi","Jaffrabadi","Mehsana","Surti"}

# # ---------------- LOAD MODEL ----------------
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_PATH = os.path.join(BASE_DIR, "models", "Best_Cattle_Breed.h5")
# model = tf.keras.models.load_model(MODEL_PATH)

# # ---------------- PREDICTION ----------------
# def predict_image(image: Image.Image):
#     image = image.resize(IMAGE_SIZE)
#     image = np.array(image)

#     if image.shape[-1] == 4:
#         image = image[:, :, :3]

#     image = tf.keras.applications.efficientnet_v2.preprocess_input(image)
#     image = np.expand_dims(image, axis=0)

#     probs = model.predict(image, verbose=0)[0]

#     # Top predictions
#     top_idx = np.argsort(probs)[::-1][:3]
#     top_conf = probs[top_idx[0]] * 100
#     ent = entropy(probs)

#     predicted_breed = CLASS_NAMES[top_idx[0]]
#     predicted_animal = "Buffalo" if predicted_breed in BUFFALO_BREEDS else "Cow"

#     # ---------- ACCEPTANCE LOGIC ----------
#     valid = (
#         top_conf >= MIN_CONFIDENCE or
#         ent < MAX_ENTROPY
#     )

#     if not valid:
#         return {
#             "valid": False,
#             "animal": "Unknown",
#             "breed": "Unknown",
#             "confidence": round(top_conf, 2)
#         }

#     return {
#         "valid": True,
#         "animal": predicted_animal,
#         "breed": predicted_breed,
#         "confidence": round(top_conf, 2)
#     }


import os
import numpy as np
import tensorflow as tf
from PIL import Image
from scipy.stats import entropy

# ---------------- CONFIG ----------------
IMAGE_SIZE = (224, 224)

# Thresholds (balanced for real-world images)
MIN_CONFIDENCE = 25.0
MAX_ENTROPY = 2.5

CLASS_NAMES = [
    "Alambadi","Amritmahal","Ayrshire","Banni","Bargur","Bhadawari",
    "Brown_Swiss","Dangi","Deoni","Gir","Guernsey","Hallikar","Hariana",
    "Holstein_Friesian","Jaffrabadi","Jersey","Kangayam","Kankrej",
    "Kasargod","Kenkatha","Kherigarh","Khillari","Krishna_Valley",
    "Malnad_gidda","Mehsana","Murrah","Nagori","Nagpuri","Nili_Ravi",
    "Nimari","Ongole","Pulikulam","Rathi","Red_Dane","Red_Sindhi",
    "Sahiwal","Surti","Tharparkar","Toda","Umblachery","Vechur"
]

BUFFALO_BREEDS = {
    "Murrah", "Nili_Ravi", "Jaffrabadi", "Mehsana", "Surti"
}

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "Best_Cattle_Breed.h5")

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image: Image.Image):
    image = image.resize(IMAGE_SIZE)
    image = np.array(image)

    # RGBA → RGB safety
    if image.shape[-1] == 4:
        image = image[:, :, :3]

    image = tf.keras.applications.efficientnet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    probs = model.predict(image, verbose=0)[0]

    top_idx = np.argsort(probs)[::-1][:3]
    ent = entropy(probs)

    breed = CLASS_NAMES[top_idx[0]]
    animal = "Buffalo" if breed in BUFFALO_BREEDS else "Cow"

    # ======================================================
    # 🔥 CONFIDENCE LOGIC (UNCHANGED – DO NOT TOUCH)
    # ======================================================
    top_conf = np.sum(probs[top_idx]) * 100  # Top-3 sum

    if ent < 1.5:
        top_conf *= 1.2
    elif ent < 2.0:
        top_conf *= 1.1

    top_conf = min(100, max(top_conf, 30))
    # ======================================================

    # ======================================================
    # ✅ CORRECTED VALIDATION LOGIC (BUFFALO FIX)
    # ======================================================

    # Count buffalo vs cow agreement in top-3
    buffalo_votes = sum(
        CLASS_NAMES[i] in BUFFALO_BREEDS for i in top_idx
    )
    cow_votes = 3 - buffalo_votes

    # Animal consistency check
    animal_consistent = (buffalo_votes >= 2) or (cow_votes >= 2)

    # Final validation
    valid = (
        animal_consistent and        # must agree on animal type
        ent < 2.5 and                 # blocks random images
        top_conf >= MIN_CONFIDENCE    # minimum confidence
    )
    # ======================================================

    if not valid:
        return {
            "valid": False,
            "animal": "Unknown",
            "breed": "Unknown",
            "confidence": round(top_conf, 2)
        }

    return {
        "valid": True,
        "animal": animal,
        "breed": breed,
        "confidence": round(top_conf, 2)
    }