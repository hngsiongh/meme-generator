
from util.image import *
import os
from werkzeug.datastructures import FileStorage

# Test Case for verify_file_extension
# ===================================
# Test Case 1: Filename has Incorrect Extension
def test_verify_file_extension_1():
    filename = "wrong.txt"
    assert not (verify_file_extension(filename))

# Test Case 2: Filename is None
def test_verify_file_extension_2():
    filename = None
    assert not (verify_file_extension(filename))

# Test Case 3: Filename is a digit
def test_verify_file_extension_3():
    filename = 123
    assert not (verify_file_extension(filename))

# Test Case 4: Filename is of Supported Extension
def test_verify_file_extension_4():
    filename = "Supported.png"
    assert (verify_file_extension(filename))

# Test Case for verify_file_is_image
# ===================================
# Test Case 1: File is not an Image
def test_verify_file_is_image_1():
    not_img_path = 'tests/image.txt'
    file = None
    with open(not_img_path,'rb') as fp:
        file = FileStorage(fp)
        assert not verify_file_is_image(file)

# Test Case 2: File is an Image
def test_verify_file_is_image_2():
    img_path = 'tests/image.jpg'
    file = None
    with open(img_path,'rb') as fp:
        file = FileStorage(fp)
        assert verify_file_is_image(file)


# Test Case for resize_image_by_width
# ===================================
# Test Case 1: Imagae is Resized
def test_resize_image_by_width_1():
    img_path = 'tests/image_resize.png'
    img = Image.open(img_path)
    original_x, original_y = img.size
    target_width = 500
    resized_img = resize_image_by_width(img,target_width)
    resized_x, resized_y = resized_img.size

    assert resized_x == target_width
    assert resized_y != original_y
    assert resized_x != original_x
    assert resized_y == 569


# Test Case for draw_image
# =========================
# Test Case 1: File is not an image 
def test_draw_image_1():
    not_img_path = 'tests/image.txt'
    file = None
    x = 15
    y = 15
    text = "Random Text"
    is_top_text = True
    with open(not_img_path,'rb') as fp:
        file = FileStorage(fp)
        assert not draw_image(file,file.filename,text,is_top_text)

# Test Case 2: File is an Image, Test Top Text , Output File is Generated
def test_draw_image_2():
    filename = 'result.jpg'
    # Verify that Destination File doesn't Exist
    try:
        os.remove(filename)
    except OSError:
        pass

    img_path = 'tests/image.jpg'
    file = None
    text = "Now I have a Caption Hi"
    is_top_text = True
    with open(img_path,'rb') as fp:
        file = FileStorage(fp)
        output_file_path = draw_image(file,filename,text,is_top_text)
        assert output_file_path
        assert Image.open(output_file_path)
        
        # Remove File Once Verified
        try:
            os.remove(output_file_path)
        except OSError:
            pass

# Test Case 3: File is an Image, Test Bottom Text , Output File is Generated
def test_draw_image_3():
    filename = 'result.png'
    # Verify that Destination File doesn't Exist
    try:
        os.remove(filename)
    except OSError:
        pass

    img_path = 'tests/image_resize.png'
    file = None
    text = "Now I have a Caption Hi"
    with open(img_path,'rb') as fp:
        file = FileStorage(fp)
        output_file_path = draw_image(file,filename,text,False)
        assert output_file_path
        assert Image.open(output_file_path)
        # Remove File Once Verified
        try:
            os.remove(output_file_path)
        except OSError:
            pass

