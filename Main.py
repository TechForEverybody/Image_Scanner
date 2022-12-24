print("""🚀🚀🚀🚀 Image Scanner 🚀🚀🚀🚀🚀\n""")

import time
import urllib.request
import cv2
import numpy
import PIL.Image
imageURL="http://______________________/shot.jpg"

while True:
    response=urllib.request.urlopen(url=imageURL)
    # print(response)
    imageBytes=bytearray(response.read())
    imageArray=numpy.array(imageBytes,dtype=numpy.uint8)
    print(imageArray)
    imageFrame=cv2.imdecode(imageArray,1)
    cv2.imshow("Scanner Frame",imageFrame)
    print(cv2.waitKey(5))
    savingImage=PIL.Image.fromarray(imageFrame)
    savingImage.save("./Files/image.jpg")
    time.sleep(5)
    # if cv2.waitKey(2)==ord('s'):
    # if cv2.waitKey(1)==ord('q'):
    #     break