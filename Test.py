import os #ใช้คำสั่ง cmd
import shutil


p = os.getcwd()

data = str(p) + "\\whatthe.py"
#file = open(data, "w")
#file.write("print('hello world')")
#file.close()

file = open(data, "r")
text = file.read()
print(text)

#shutil.move(str(p) + "\\wow\\" + "Test.py", str(p) + "\\what\\" + "Test.py") #ย้ายไฟล์
#os.mkdir("C:/Users/tsmwn/OneDrive/เดสก์ท็อป/Test Vs/what") 

#os.rename(str(p) + "\\wow\\test2.py", str(p) + "\\wow\\mamameya.py") #เปลี่ยนชื่อ

#os.remove(str(p) + "\\wow\\mamameya.py") #ทิ้งไฟล์ไป
#os.removedirs(str(p) + "\\wow")

print(os.path.isdir("oh_my")) #ดูชื่อไฟล์
print(os.path.isfile("whatthe.py")) #ดูชื่อ folder