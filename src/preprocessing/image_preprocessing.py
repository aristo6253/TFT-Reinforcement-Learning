from PIL import Image


def preprocess_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((800, 600))  # Resize the image
        img = img.convert('L')  # Convert the image to grayscale
    return img


image = preprocess_image('data/sample_images/board_1.png')
image.show()
