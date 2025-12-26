import os
from utils import is_image_file,save_img
from processor import process_image
base = os.getcwd()
input_folder = os.path.join(base, "images")
output_folder = os.path.join(base,"processed_images")
files = os.listdir(input_folder)
for file in files:
    if is_image_file(file) is False:
        continue


    file_path = os.path.join(input_folder,file)
    processed_image = process_image(file_path)

    if processed_image is not None:
        file_name, ext = os.path.splitext(file)
        new_name = f'{file_name}_processed{ext}'

        output_file_path = os.path.join(output_folder,new_name)

        save_img(processed_image,output_file_path)

print("All images Processed and saved in 'processed_images' folder")
