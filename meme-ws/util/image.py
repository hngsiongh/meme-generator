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
        Image.open(filename)
    except IOError:
        return False
    return True


# Resize Image
def resize_image_by_width(img, target_width):
    wpercent = (target_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    return img.resize((target_width, hsize))

# Draw on Image
def draw_image(filepath,filename,text,is_top):
    img = None
    try:
        img = Image.open(filepath)   
    except IOError:
        return False

    # Resize Image
    target_width = 1200
    img = resize_image_by_width(img, target_width)
    x, y = img.size

    draw = ImageDraw.Draw(img)
    font_name = "font.ttf"
    font_size = 100
    font = ImageFont.truetype(font_name, font_size)
    text_box  = draw.textbbox((0,0), text, font=font)
    w = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    mid_point = (x-w)/2
    if is_top:
        draw.text((mid_point,y*0.01),text,(255,255,255),font=font)
    else:
        padding = 100
        draw.text((mid_point,y-text_height-padding),text,(255,255,255),font=font)
    des_filepath = "tests/" + filename
    img.save(des_filepath)

    return des_filepath
