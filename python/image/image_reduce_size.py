import os
from PIL import Image

path = '/home/ec2-user/environment/warframets/html/static/image/item_image/etc'
path_list = os.listdir(path)

file_list = []
for i, v in enumerate(path_list):
    file_list.append(v)

for i in file_list:
    path_2 = path + '/' + str(i) + '/' + str(i) + '.png'
    path_3 = path + '/' + str(i) + '/' + str(i) + '_Change.png'
    #os.remove(path_3)
    name = str(i) + '.png'
    image_1 = Image.open(path_2)
    resize_image = image_1.resize((310, 453))
    resize_image.save(path_3)