from flask import Flask
from flask import request,redirect,render_template,url_for
from werkzeug.utils import secure_filename
import os
import easyocr
from PIL import ImageFilter
from PIL import Image
import easyocr
import cv2
from matplotlib import pyplot as plt
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './media'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitImage/',methods=['POST',])
def submitImage():
    image = request.files['ocrImage']
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread(filename)
    spacer = 100
    alltext = ''
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        alltext += text + ' '
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        spacer += 15
        #text = pytesseract.image_to_string(img)
    f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.txt','w')
    f.write(alltext)
    f.close()
    return render_template('textFile.html',text=alltext,filename=f)


if __name__ == '__main__':
    app.run('0.0.0.0',8000)
