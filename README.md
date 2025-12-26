# Smart Image Processor

A Python-based batch image processing tool that automatically resizes images and converts them to grayscale using a clean, modular pipeline.

## Features
- Batch image processing
- Resize images to 50% of original size
- Convert images to grayscale
- Modular architecture (utils, processor, main)
- Safe handling of invalid files

## Project Structure
Smart Image Processor/
├── main.py
├── processor.py
├── utils.py
├── images/
├── processed_images/
└── requirements.txt

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Place images inside the `images/` folder.

3. Run the program:
python main.py

4. Processed images will be saved in `processed_images/`.

## Technologies Used
- Python
- Pillow (PIL)





