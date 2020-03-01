
from PIL import Image
from urllib.request import urlretrieve
import os

link1= "http://sillok.history.go.kr/viewer/imageProxy.do?filePath=/s_img/SILLOK/"
link2 = ['i','x','x','_','d','0','0','0','0','0','0','x','00']

book = ['ta','tb','u','v','w','x','y']
book_volumes = [15,5,127,54,34,16,15]



for num , name in enumerate(book):

    #create folder
    DIRECTORY_NAME = "/home/ubuntu/context/data/"+name
    print(DIRECTORY_NAME)
    try:
        if not (os.path.isdir(DIRECTORY_NAME)):
            os.makedirs(os.path.join(DIRECTORY_NAME))
    except :
        print("Failed to create directory!!!!!")


    if len(name) == 2:
        print(name)
        link_path1 = name
    else:
        link_path1 = name+'a'
        print(link_path1)

    book_volume = book_volumes[num]


    for n in range(book_volume):
        print(n)
        count = 1
        dum = 0

        while dum == 0:
            file_name = "i" + link_path1 + "_d" + str(n + 1).zfill(3) + str(count).zfill(3)
            link = link1 + link_path1 + "/" + file_name
            print(link)
            try:
                print(count)
                urlretrieve(link+'a00.jpg','/home/ubuntu/context/data/'+name+'/'+file_name+'a.jpg')
                Image.open("/home/ubuntu/context/data/"+name+"/"+file_name+"a.jpg")
                urlretrieve(link + 'b00.jpg', "/home/ubuntu/context/data/"+name+"/"+file_name+"b.jpg")
                Image.open("/home/ubuntu/context/data/"+name+"/"+file_name+"b.jpg")
                count = count +1

            except:
                os.remove('/home/ubuntu/context/data/'+name+'/'+file_name+"a.jpg")
                print("count reset")
                dum = 1



