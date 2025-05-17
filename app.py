import io

from PIL import Image
from flask import Flask, request, send_file

app = Flask(__name__)

@app.post('/convert_image')
def convert_image():
    file_storage = request.files.get('image')
    colorful_image = Image.open(io.BytesIO(file_storage.read()))

    gray_image = colorful_image.convert('L')

    gray_image_bytes = io.BytesIO()
    gray_image.save(gray_image_bytes, format=colorful_image.format)
    gray_image_bytes.seek(0)
    gray_image_name = 'gray_' + file_storage.filename
    return send_file(gray_image_bytes, mimetype=file_storage.mimetype, as_attachment=True, download_name=gray_image_name)

if __name__ == '__main__':
    app.run()
