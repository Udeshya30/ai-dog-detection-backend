
#!/bin/bash

mkdir -p models

if [ ! -f models/best.pt ]; then
  echo "Downloading model from Google Drive..."
  gdown --id 1OjtmQ3BOtk1RzEYIjiPale1uf7l0BZ9p -O models/best.pt
fi

uvicorn main:app --host=0.0.0.0 --port=10000
