from PIL import Image, ImageEnhance, ImageFilter
import os

path = r'C:\Users\Admin\Desktop\project1\imgs'
pathOut = r'C:\Users\Admin\Desktop\project1\editedImgs'


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    #edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
    
    edited_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")
    edit.save(edited_path.replace("/", "\\"))


