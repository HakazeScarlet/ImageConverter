import io

from flask import Flask, request, send_file
from PIL import Image
app = Flask(__name__)

@app.post('/convert_image')
def convert_image():
    file_storage = request.files.get('image')
    colorful_image_bytes = Image.open(io.BytesIO(file_storage.read()))

    grey_image = colorful_image_bytes.convert('L')

    grey_image_bytes = io.BytesIO()
    grey_image.save(grey_image_bytes, format='JPEG')
    grey_image_bytes.seek(0)
    return send_file(grey_image_bytes, mimetype='image/jpeg', as_attachment=True, download_name=file_storage.filename)

if __name__ == '__main__':
    app.run()
