from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://udeshya30.github.io/UdWebPlay/"],#["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("models/best.pt")

def image_to_base64(image_np):
    from PIL import Image
    import numpy as np
    buffer = io.BytesIO()
    image = Image.fromarray(image_np)
    image.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model(image)

    dog_count = len(results[0].boxes)
    image_base64 = image_to_base64(results[0].plot())

    return {
        "detected": dog_count > 0,
        "message": f"{dog_count} dog(s) detected 🐶" if dog_count else "No dog found ❌",
        "count": dog_count,
        "image_base64": image_base64
    }
