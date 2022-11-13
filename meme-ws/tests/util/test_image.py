
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

# Test Case for get_dimension_of_image
# ====================================
# Test Case 1: File is not an image
def test_get_dimension_of_image_1():
    not_img_path = 'tests/image.txt'
    file = None
    with open(not_img_path,'rb') as fp:
        file = FileStorage(fp)
        x, y = get_dimension_of_image(file)
        assert (x==-1)
        assert (y==-1)

# Test Case 2: File is an image, image demension returned
def test_get_dimension_of_image_2():
    img_path = 'tests/image.jpg'
    file = None
    with open(img_path,'rb') as fp:
        file = FileStorage(fp)
        x, y = get_dimension_of_image(file)
        assert (x==1200)
        assert (y==817)

# Test Case for draw_image
# =========================
# Test Case 1: File is not an image 
def test_draw_image_1():
    not_img_path = 'tests/image.txt'
    file = None
    x = 15
    y = 15
    text = "Random Text"
    with open(not_img_path,'rb') as fp:
        file = FileStorage(fp)
        assert not draw_image(file,file.filename,x,y,text)

# Test Case 2: File is an Image, Output File is Generated
def test_draw_image_2():
    filename = 'result.jpg'
    # Verify that Destination File doesn't Exist
    try:
        os.remove(filename)
    except OSError:
        pass

    img_path = 'tests/image.jpg'
    file = None
    x = 15
    y = 15
    text = "Random Text"
    with open(img_path,'rb') as fp:
        file = FileStorage(fp)
        output_file_path = draw_image(img_path,filename,x,y,text)
        assert output_file_path
        assert Image.open(output_file_path)
        
        # Remove File Once Verified
        try:
            os.remove(output_file_path)
        except OSError:
            pass
