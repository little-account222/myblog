from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Handle CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OCR_URL = "https://ocrcodesimpleonlyocr.vercel.app/ocr/"

@app.get("/cron")
def trigger_ocr():
    data = {
        "firstName": "Deep",
        "lastName": "Gohil",
        "mobileNumber": "08104680835",
        "email": "deepgohil777@gmail.com",
        "date": "02-202-03"
    }
    
    try:
        with open("test1.jpeg", "rb") as image_file:
            files = {"image": ("test1.jpeg", image_file, "image/jpeg")}
            response = requests.post(OCR_URL, data=data, files=files)
            
            if response.status_code == 200:
                return {"status": "success", "data": response.json()}
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))