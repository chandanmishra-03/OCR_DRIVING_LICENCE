import cv2
import pytesseract
from matplotlib import pyplot as plt
import noise_cancellation as nc

path='drive.jpg'

#read image
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#show image
plt.imshow(gray)
plt.title('my picture')
plt.show()

#noise cancellation
img1=nc.process_image_for_ocr(path)

#extract text from image and store as a string
x=pytesseract.image_to_string(img1)

print(x)
type(x)
y=x.split('\n')

z=[]
for i in y:
    if (i!=''):
        z.append(i)
m=[]
for i in range (len(z)):
    if 'Address' in z[i]:
        m.append(i)
    elif 'SIWID' in z[i]:
        m.append(i)
print(m)
y=''
for i in range (m[0],m[1],1):
    
    y=y+z[i]
m=[]
for i in range (len(z)):
    if 'Licence No' in z[i]:
        m.append(z[i])
    elif 'Name' in z[i]:
        m.append(z[i])
    elif 'DOB' in z[i]:
        m.append(z[i])
    elif 'SIWID' in z[i]:
        m.append(z[i])
print(m)
m.insert(2,y)
m
