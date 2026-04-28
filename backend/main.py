from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from model import predict_image
from db import create_table, insert_scan, get_all_scans, clear_scans

app = FastAPI(
    title="BreedNet AI API",
    version="1.1.0"
)

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- STARTUP ----------------
create_table()

# ---------------- HEALTH ----------------
@app.get("/")
def health():
    return {"status": "BreedNet backend running 🚀"}

# ---------------- PREDICT ----------------
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid image format"
        )

    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        result = predict_image(image)

        if not result["valid"]:
            raise HTTPException(
                status_code=400,
                detail="Image is not recognized as cattle or is too unclear"
            )

        # ✅ SAVE RESULT TO DATABASE
        insert_scan(
            result["animal"],
            result["breed"],
            result["confidence"]
        )

        return result

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# ---------------- HISTORY ----------------
@app.get("/history")
def history():
    return get_all_scans()

# ---------------- CLEAR HISTORY ----------------
@app.delete("/history")
def clear_history():
    clear_scans()
    return {"status": "History cleared"}
