from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io

app = FastAPI()


@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return JSONResponse(content={"text": text})
