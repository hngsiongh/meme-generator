from flask import Flask, request, send_file
from flask_cors import CORS
import mimetypes
from util.image import *
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'Ok!'

@app.route('/generateMeme', methods=['POST'])
def generate_meme():
    #Key of Data in Form
    meme_image_key = "memeImage"
    top_text_key = "topText"
    bottom_text_key = "btmText"
    max_text_length = 50

    # Check Form Data for Image
    #   Throw Exception is no Image
    if meme_image_key not in request.files:
        return "No Image Provided!", 400

    # FileStorage Type
    image_file = request.files[meme_image_key]
    
    #Check Form Data for Top Text
        # Top Text Default to Empty String
    top_text = request.form.get(top_text_key,"")
    # Reject if Text is too Long or Contains Next Line
    if len(top_text) > max_text_length:
        return "Top Text is too Long", 400
    if len(top_text) != len(top_text.replace('\n','')):
        return "Top Text Doesn't Support New Line", 400
    
    #Check Form Data for Bottom Text
        # Bottom Text Default to Empty String
    btm_text = request.form.get(bottom_text_key,"")
    # Reject if Text is too Long or Contains Next Line
    if len(btm_text) > max_text_length:
        return "Bottom Text is too Long", 400
    if len(btm_text) != len(btm_text.replace('\n','')):
        return "Bottom Text Doesn't Support New Line", 400

    if not verify_file_extension(image_file.filename):
        return "Unsupported File Extension!", 400

    if not verify_file_is_image(image_file):
        return "Unsupported File!", 400

    if len(top_text)!=0 and len(btm_text)!=0:
        des_img_filepath = draw_image(image_file,image_file.filename,top_text,True)
        des_img_filepath = draw_image(des_img_filepath,image_file.filename,btm_text,False)
    elif len(top_text)!=0:
        des_img_filepath = draw_image(image_file,image_file.filename,top_text,True)
    elif len(btm_text)!=0:
        des_img_filepath = draw_image(image_file,image_file.filename,btm_text,False)
    else:
        des_img_filepath = draw_image(image_file,image_file.filename,"",False)
    return send_file(des_img_filepath, mimetype=mimetypes.guess_type(image_file.filename)[0])

if __name__ == '__main__':
   app.run(host="127.0.0.1",port=8999)