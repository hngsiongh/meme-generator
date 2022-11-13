from PIL import Image, ImageFont, ImageDraw

# Make Sure File Extension is PNG or JPEG
def verify_file_extension(filename):
    if not filename:
        return False
    if not isinstance(filename, str):
        return False
    if filename.lower().endswith(('.png', '.jpeg', 'jpg')):
        return True
    return False

# Make Sure File is an Image
def verify_file_is_image(filename):
    try:
        im=Image.open(filename)
    except IOError:
        return False
    return True

# Get Width/Height of Image
def get_dimension_of_image(filename):
    try:
        im=Image.open(filename)
        return im.size # Return width/height
    except IOError:
        return -1,-1

# Draw on Image
def draw_image(filepath,filename,x,y,text):
    img = None
    try:
        img = Image.open(filepath)   
    except IOError:
        return False
    draw = ImageDraw.Draw(img)
    
    font_name = "font.ttf"
    font_size = 16
    font = ImageFont.truetype(font_name, font_size)
    draw.text((x,y),text,(255,255,255),font=font)

    des_filepath = "tests/" + filename
    img.save(des_filepath)

    return des_filepath
