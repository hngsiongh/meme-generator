import pytest
import os
from io import BytesIO
from main import app




@pytest.fixture(scope='module')
def test_app():
    app.config.update({
        "TESTING": True,
    })
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


# Test Case for HealthCheck
# =========================
# Test Case 1: Test Healthcheck 200
def test_healthcheck_1(test_app):
    resp = test_app.get('/healthcheck')
    assert resp.data.decode('utf-8') == "Ok!"
    assert resp.status_code == 200

# Test Case for generate_meme
# ==============================
# Test Case 1: No Image Provided
def test_generate_meme_1(test_app):
    resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                         data={'topText': "",
                               'btmText': "",
                               })
    assert resp.status_code == 400
    assert resp.data.decode('utf-8') == "No Image Provided!"

# Test case 2: Top text is too Long
def test_generate_meme_2(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'topText': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25',
                                   'btmText': '',
                                   'memeImage': (buf, "test.jpg")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode('utf-8') == "Top Text is too Long"

# Test case 3: Top text Contains Next Line
def test_generate_meme_3(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'topText': '1,2,3,4,5,\n6,7,8,9,10,11',
                                   'btmText': '',
                                   'memeImage': (buf, "test.jpg")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode('utf-8') == "Top Text Doesn't Support New Line"

# Test case 4: Bottom text is too Long
def test_generate_meme_4(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25',
                                   'topText': '',
                                   'memeImage': (buf, "test.jpg")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode('utf-8') == "Bottom Text is too Long"

# Test case 5: Bottom text Contains Next Line
def test_generate_meme_5(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': '1,2,3,4,5,\n6,7,8,9,10,11',
                                   'topText': '',
                                   'memeImage': (buf, "test.jpg")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode(
            'utf-8') == "Bottom Text Doesn't Support New Line"

# Test case 6: Unsupported File Extension
def test_generate_meme_6(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': '',
                                   'topText': '',
                                   'memeImage': (buf, "test.txt")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode('utf-8') == "Unsupported File Extension!"

# Test case 7: Unsupported File
def test_generate_meme_7(test_app):

    with open('tests/image.txt', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': '',
                                   'topText': '',
                                   'memeImage': (buf, "test.jpg")
                                   })
        assert resp.status_code == 400
        assert resp.data.decode('utf-8') == "Unsupported File!"

# Test case 8: No Caption Text
def test_generate_meme_8(test_app):

    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                      data={'btmText': '',
                            'topText': '',
                            'memeImage': (buf, "image.jpg")
                            })
        assert resp.status_code == 200
        assert resp.mimetype == 'image/jpeg'
        des_path = "image/image.jpg"
        assert os.path.exists(des_path)
        os.remove(des_path)


# Test case 9: Caption Text Added for Top Text
def test_generate_meme_9(test_app):
    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': 'Random Text',
                                   'topText': '',
                                   'memeImage': (buf, "image.jpg")
                                   })
        
        assert resp.status_code == 200
        assert resp.mimetype == 'image/jpeg'
        des_path = "image/image.jpg"
        assert os.path.exists(des_path)
        os.remove(des_path)

# Test case 10: Caption Text Added for Bottom Text
def test_generate_meme_10(test_app):
    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': '',
                                   'topText': 'Random Text',
                                   'memeImage': (buf, "image.jpg")
                                   })
        
        assert resp.status_code == 200
        assert resp.mimetype == 'image/jpeg'
        des_path = "image/image.jpg"
        assert os.path.exists(des_path)
        os.remove(des_path)

# Test case 11: Caption Text Added for Both Top and Bottom Text
def test_generate_meme_11(test_app):
    with open('tests/image.jpg', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': 'Random Text',
                                   'topText': 'Random Text',
                                   'memeImage': (buf, "image.jpg")
                                   })
        
        assert resp.status_code == 200
        assert resp.mimetype == 'image/jpeg'
        des_path = "image/image.jpg"
        assert os.path.exists(des_path)
        os.remove(des_path)

# Test case 12: Caption Text Added for Both Top and Bottom Text For PNG File
def test_generate_meme_12(test_app):
    with open('tests/image_resize.png', 'rb') as file_img:
        buf = BytesIO(file_img.read())

        resp = test_app.post('/generateMeme', content_type='multipart/form-data',
                             data={'btmText': 'Random Text',
                                   'topText': 'Random Text',
                                   'memeImage': (buf, "image_resize.png")
                                   })
        
        assert resp.status_code == 200
        assert resp.mimetype == 'image/png'
        des_path = "image/image_resize.png"
        assert os.path.exists(des_path)
        os.remove(des_path)
