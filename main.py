from PIL import Image, UnidentifiedImageError
from tkinter import filedialog
import os

def resize_image(input_path, output_path, size=(450, 450)):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(size)
            resized_img.save(output_path)
        print("Image resized.")
    except UnidentifiedImageError:
        print("Error: Invalid image file.")
    except Exception as e:
        print(f"Error: {e}")

def get_user_input():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    return width, height

def main():
    file_path = filedialog.askopenfilename(title="Select a file",filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if not file_path:
        print("No file selected.")
        return
    width, height = get_user_input()
    directory, filename = os.path.split(file_path)
    output_path = os.path.join(directory, f"resized_{filename}")
    if os.path.exists(output_path):
        user_input = input("A file with the same name exists. Overwrite? (y/n): ")
        if user_input.lower() != 'y':
            print("Resize canceled.")
            return
    resize_image(file_path, output_path, size=(width, height))

if __name__ == "__main__":
    main()
