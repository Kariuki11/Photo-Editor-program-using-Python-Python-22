# from PIL import Image, ImageEnhance, ImageFilter
# import os

# # path = './PYTHON#22'
# # pathOut = '/Edited things'

# path = 'C:\\Users\\Administrator\\Desktop\\Python#22'
# pathOut = 'C:\\Users\\Administrator\\Desktop\\Python#22\\Edited things'


# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")
    
#     edit = img.filter(ImageFilter.SHARPEN)
    
#     clean_name = os.path.splitext(filename) [0]
    
#     edit.save(f'.{pathOut}/{clean_name}_edited.jpg')

from PIL import Image, ImageEnhance, ImageFilter
import os

# Absolute paths for input and output directories
path = 'C:\\Users\\Administrator\\Desktop\\Python#22'
pathOut = 'C:\\Users\\Administrator\\Desktop\\Python#22\\Edited things'

# Ensure the output directory exists
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    # Check if the item is a file
    if os.path.isfile(os.path.join(path, filename)):
        img = Image.open(os.path.join(path, filename))

        # Apply the sharpen filter to the image
        edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
        
        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = 

        # Extract the file name without extension
        clean_name = os.path.splitext(filename)[0]

        # Save the edited image in the output directory
        edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))
