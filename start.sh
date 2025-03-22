#!/bin/bash

echo "Downloading YOLOv8 model from Google Drive..."
mkdir -p models
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1OjtmQ3BOtk1RzEYIjiPale1uf7l0BZ9p" -O models/best.pt

echo "Starting FastAPI server..."
uvicorn main:app --host=0.0.0.0 --port=10000
