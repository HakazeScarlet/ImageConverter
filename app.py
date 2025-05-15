from flask import Flask, request

app = Flask(__name__)


@app.post('/convert_image')
def convert_image(string):
    string = input()
    string = string.upper()
    return string
    # image = request.files['image']
    # new_image = image.convert("L")
    # return new_image


if __name__ == '__main__':
    app.run()
