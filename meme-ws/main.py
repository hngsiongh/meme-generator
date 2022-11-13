from flask import Flask, request
from util.image import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'Ok!'

@app.route('/generateMeme', methods=['POST'])
def generateMeme():
    #Key of Data in Form
    meme_image_key = "memeImage"
    top_text_key = "topText"
    bottom_text_key = "btmText"

    #Check Form Data for Image
        # Throw Exception is no Image
    if meme_image_key not in request.files:
        return "No Image Provided!", 400

    #FileStorage Type
    image_file = request.files[meme_image_key]
    
    #Check Form Data for Top Text
        # Top Text Default to Empty String
    top_text = request.form.get(top_text_key,"")
    
    #Check Form Data for Bottom Text
        # Bottom Text Default to Empty String
    btm_text = request.form.get(bottom_text_key,"")

    if not verify_file_extension(image_file.filename):
        return "Unsupported Format!", 400
    


#Endpoint to Accept and Image, Top Text, Btm Text
#Returns an Image

if __name__ == '__main__':
   app.run()