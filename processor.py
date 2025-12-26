from utils import load_img

def resize_half(img):

   return img.resize((img.width // 2, img.height//2))

def to_grayscale(img):

    return img.convert("L")

def process_image(Path):
     img = load_img(Path)

     if not img is None:
       resized_image = resize_half(img)
       processed_image = to_grayscale(resized_image)
       return processed_image
     else:
         return None





