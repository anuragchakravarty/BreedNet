# BreedNet

🐄 BreedNet – AI-Based Cattle & Buffalo Breed Identification
BreedNet is a mobile-based AI system that identifies cattle and buffalo breeds using images. It leverages computer vision and deep learning to provide fast, accurate, and real-time breed predictions, even in rural environments with limited connectivity.

🚀 Features
📸 Image-Based Breed Detection
Upload or capture animal images for instant prediction

🤖 AI-Powered Classification
Uses CNN-based deep learning models for accurate results

📊 Crossbreed Percentage Prediction
Shows percentage-based breed composition (useful for Indian livestock)

⚡ Fast Response Time
Predictions generated within 2–5 seconds

📱 Mobile-Friendly Design
Works on low-power devices used by field workers

🌐 Offline Support
Stores data locally and syncs when internet is available

🔗 BPA Integration Ready
Designed to integrate with Bharat Pashudhan App workflow

🏗️ System Architecture
BreedNet follows a microservices-based architecture:

API Gateway → Handles requests

Ingestion Service → Accepts image data

AI Model Service → Performs prediction

Persistence Service → Stores data

Reporting Service → Generates insights

🧠 Tech Stack
🔹 Frontend
HTML

CSS

JavaScript

🔹 Backend
Python

FastAPI

Uvicorn

🔹 AI/ML
TensorFlow

Keras

OpenCV

NumPy

Pillow

🔹 Database
SQLite

📂 Project Structure

BreedNet/
│── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
│── backend/
│   ├── main.py
│   ├── model.py
│   └── utils.py
│
│── model/
│   └── Best_Cattle_Breed.h5
│
│── dataset/
│   └── images/
│
│── requirements.txt
│── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
Bash

git clone https://github.com/your-username/BreedNet.git
cd BreedNet
2️⃣ Create Virtual Environment
Bash

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
3️⃣ Install Dependencies
Bash

pip install -r requirements.txt
▶️ Run the Project
Start Backend Server
Bash

uvicorn main:app --reload
Open Frontend
Open index.html in browser

Upload or capture image

🧪 Model Training Details
Image Size: 224 × 224

Batch Size: 32

Epochs: 50

Data Split: 80% Training / 20% Validation

Data Augmentation:
Random Flip

Rotation

Zoom

Evaluation Metrics:
Accuracy

Precision

Recall

F1-Score

Confusion Matrix

📊 Performance
⏱️ Response Time: 2–5 seconds

📈 High classification accuracy on trained breeds

⚡ Optimized for low-resource devices

🎯 Use Cases
Field Level Workers (FLWs)

Farmers

Veterinary Officers

Government Livestock Programs

⚠️ Limitations
Accuracy depends on image quality

Limited to trained breeds

Performance may drop in extreme lighting conditions

🔮 Future Scope
🌍 Multi-language support

🦠 Disease detection

☁️ Cloud analytics dashboard

📱 Full mobile app deployment

📊 Large-scale livestock data insights

👨‍💻 Author
