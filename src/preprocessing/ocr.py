import pytesseract
from PIL import Image # Rmv later


def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text


# text = extract_text(Image.open('data/sample_images/board_1.png'))
# print(text)

Image.open('data/sample_images/board_1.png').show()

# import pytesseract
# from PIL import Image


# def extract_text(image_path):
#     image = Image.open(image_path)
#     text = pytesseract.image_to_string(image)
#     return text


# text = extract_text('data/sample_images/board_1.png')
# print(text)
