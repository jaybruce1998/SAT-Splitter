from pdf2image import convert_from_path
import os
import cv2
filename=input("Enter the filename: ")
path=filename.split(".")[0]
complete=path+"_complete"
path+='/'
complete+='/'
try:
   os.mkdir(complete)
   os.mkdir(path)
except OSError:
   print("Call tech support...")
pages=convert_from_path(filename, 300)
n=1
for p in range(len(pages)):
   imagename=path+str(p+1)+".png"
   pages[p].save(imagename, "PNG")
   img = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
   height, width = img.shape
   w=width//2
   i=0
   l=0
   while i<height:
      if img[i, 300]==210 and img[i, 400]==210:
         cv2.imwrite(complete+str(n)+".png", img[l:i, :w])
         n+=1
         l=i
         i+=49
      i+=1
   cv2.imwrite(complete+str(n)+".png", img[l:, :w])
   n+=1
   i=0
   l=0
   while i<height:
      if img[i, 1450]==210 and img[i, 1500]==210:
         cv2.imwrite(complete+str(n)+".png", img[l:i, w:])
         n+=1
         l=i
         i+=49
      i+=1
   cv2.imwrite(complete+str(n)+".png", img[l:, w:])
   n+=1