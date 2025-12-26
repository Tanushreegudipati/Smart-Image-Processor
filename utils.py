from PIL import Image

def is_image_file(file):

        if file.lower().endswith(("jpg","png","jpeg")):
            return True
        else:
            return False


def load_img(Path):
    try:
        img = Image.open(Path)
        return img

    except:

       return None

def save_img(image,Path):
    image.save(Path)







