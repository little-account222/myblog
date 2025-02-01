from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def run_ocr_job():
    url = 'https://ocrcodesimpleonlyocr.vercel.app/ocr/'

    data = {
        'firstName': 'Deep',
        'lastName': 'Gohil',
        'mobileNumber': '08104680835',
        'email': 'deepgohil777@gmail.com',
        'date': '02-202-03'
    }

    files = {'image': ('test1.jpeg', open('test1.jpeg', 'rb'), 'image/jpeg')}

    try:
        response = requests.post(url, data=data, files=files)
        files['image'][1].close()  # Close file after sending

        if response.status_code == 200:
            return {"status": "success", "data": response.json()}
        else:
            return {"status": "error", "code": response.status_code, "message": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route("/trigger", methods=["GET"])
def trigger():
    return jsonify(run_ocr_job())

if __name__ == "__main__":
    app.run(debug=True)
