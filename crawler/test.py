
from PIL import Image
import os

link1= "http://sillok.history.go.kr/viewer/imageProxy.do?filePath=/s_img/SILLOK/"
link2 = ['i','x','x','_','d','0','0','0','0','0','0','x','00']

book = ['a','b','c','d','e','f','g','h','i','j','k','l','m','na','nb','oa','ob','p','q','ra','rb','sa','sb','ts','tb','u','v','w','x','y']
book_volumes = [15,6,36,163,13,14,49,8,297,63,105,2,34,221,42,187,187,50,21,22,28,65,65,15,5,127,54,34,16,15]



for num , name in enumerate(book):

    #create folder
    DIRECTORY_NAME = "/home/ubuntu/context/data/"+name
    os.makedirs(os.path.join(DIRECTORY_NAME))
