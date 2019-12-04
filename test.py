from functions import read_image,show_image

def test_readImage():
    assert read_image() ==(40,224,224,3)

def test_showImage():
    assert show_image(1) == True

test_readImage()
test_showImage()
