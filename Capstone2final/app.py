from flask import Flask, render_template, request
import os, pytesseract
from flask_uploads import UploadSet,configure_uploads, IMAGES
from PIL import Image

project_dir = os.path.dirname(os.path.abspath(_file_))

app = Flask(_name_, static_url_path= '', static_folder='static', template_folder ='templates')

photos = UploadSet('photos', IMAGES)

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'images'

#Class for Image to Text
class GetText(object):

    def _init_(self,file):
        #pytesseract.pytesseract.tesseract_cmd = r'/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pytesseract'

        #pytesseract.pytesseract.tesseract_cmd = r"/Library/Frameworks/Python.framework/Versions/3.7/bin/pytesseract"
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/'+ file))

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'there is no photo in form'
        name = request.form['img-name'] + '.jpg'
        photo = request.files['photo']
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        photo.save(path)

        textObject = GetText(name)
        #print('TEXT OBJECT'+ textObject.file)

        return textObject.file
    return render_template('index.html')

if _name_ == '_main_':
    app.run()
    
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#print(pytesseract.image_to_string(Image.open('D:/Flask/alt.jpg')))
