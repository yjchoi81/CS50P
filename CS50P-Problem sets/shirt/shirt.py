import sys
import os
from PIL import Image, ImageOps

# resizing t-shirt and handling the user's photo file
def resizing(read_image, write_image):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(read_image) as photo:
            size = shirt.size
            fitted_photo = ImageOps.fit(photo, size)

        fitted_photo.paste(shirt, shirt)
        fitted_photo.save(write_image)


    except FileNotFoundError:
        sys.exit('File not found')



# To check command-line arguments and valid extention
def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    read_image = sys.argv[1]
    write_image = sys.argv[2]
    valid_extensions = ('.jpeg', '.jpg', '.png')

    if not read_image.endswith(valid_extensions):
        sys.exit('Invalid input')
    if not write_image.endswith(valid_extensions):
        sys.exit('Invalid output')

    read_ext = os.path.splitext(read_image.lower())[1]
    write_ext = os.path.splitext(write_image.lower())[1]

    if read_ext != write_ext:
        sys.exit('Input and output have different extensions')

    resizing(read_image, write_image)



if __name__ == "__main__":
    main()
