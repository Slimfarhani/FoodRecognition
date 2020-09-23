import os
from PIL import Image
directory = r'C:\Users\slimw\Downloads\Brik'
saveDirectory = r'C:\Users\slimw\Downloads\Brik-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\brik'+str(i)+'.jpg')
directory = r'C:\Users\slimw\Downloads\Couscous'
saveDirectory = r'C:\Users\slimw\Downloads\Couscous-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\couscous'+str(i)+'.jpg')
directory = r'C:\Users\slimw\Downloads\SaladeMechouia'
saveDirectory = r'C:\Users\slimw\Downloads\SaladeMechouia-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\saladeMechouia'+str(i)+'.jpg')
directory = r'C:\Users\slimw\Downloads\Mloukhiya'
saveDirectory = r'C:\Users\slimw\Downloads\Mloukhiya-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\mloukhiya'+str(i)+'.jpg')
directory = r'C:\Users\slimw\Downloads\Lablabi'
saveDirectory = r'C:\Users\slimw\Downloads\Lablabi-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\lablabi'+str(i)+'.jpg')
directory = r'C:\Users\slimw\Downloads\Ojja'
saveDirectory = r'C:\Users\slimw\Downloads\Ojja-resized'
i = 0
for filename in os.listdir(directory):
    i +=1
    Image.open(directory+'\\'+filename)\
        .resize((128, 128), resample=Image.LANCZOS).convert('RGB')\
        .save(saveDirectory+'\\ojja'+str(i)+'.jpg')