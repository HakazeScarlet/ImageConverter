import io

from PIL import Image
from flask import Flask, request, send_file

app = Flask(__name__)

@app.post('/convert_image')
def convert_image():
    file_storage = request.files.get('image')
    colorful_image = Image.open(io.BytesIO(file_storage.read()))

    grey_image = colorful_image.convert('L')

    grey_image_bytes = io.BytesIO()
    grey_image.save(grey_image_bytes, format=colorful_image.format)
    grey_image_bytes.seek(0)
    gray_image_name = 'grey_' + file_storage.filename
    return send_file(grey_image_bytes, mimetype=file_storage.mimetype, as_attachment=True, download_name=gray_image_name)

if __name__ == '__main__':
    app.run()
