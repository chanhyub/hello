from ctypes.wintypes import SIZE
from tkinter import *
import random
from turtle import color
from PIL import ImageTk,Image
import tkinter.font as tkFont

foodlist = ["짬뽕", "짜장면", "탕수육", "김밥", "라면", "국밥"]

#  예제 1) tkinter 파이썬 GUI 레이블(label)
# tkinter를 사용하여 텍스트를 나타내보자

# 1. 루트화면 (root window) 생성
tk = Tk() 
# 2. 텍스트 표시
fontStyle = tkFont.Font(family="Lucida Grande", size=30)
label = Label(tk, font=fontStyle, text='골라줘!!!!!!!!!!!!!!') 
# 3. 레이블 배치 실행
label.pack()

labelImage =None
photo1,photo2,photo3, photo4, photo5, photo6 = [None] * 6

tk.geometry('800x600')
def event():
    food = random.choice(foodlist)
    if food == "짬뽕":
        labelImage.configure(image = photo1)
    elif food == "짜장면":
        labelImage.configure(image = photo2)
    elif food == "탕수육":
        labelImage.configure(image = photo3)
    if food == "김밥":
        labelImage.configure(image = photo4)
    elif food == "라면":
        labelImage.configure(image = photo5)
    elif food == "국밥":
        labelImage.configure(image = photo6)
    label['text'] = f'{food}'
    
def event2():
    label['text'] = '골라줘!!!!!!!!!!!!!!'

button = Button(tk,text='추천 메뉴',command=event)
button2 = Button(tk,text='처음으로' ,command=event2)
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button2.pack(side=LEFT, padx=10, pady= 10)

photo1 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\짬뽕.jpg"))
photo2 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\짜장면.jpg"))
photo3 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\탕수육.jpg"))
photo4 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\김밥.jpg"))
photo5 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\라면.jpg"))
photo6 = ImageTk.PhotoImage(Image.open("C:\dev\Python\hello\Image\국밥.jpg"))

labelImage = Label(tk,width=1200, height=900, bg="yellow", image = None)
labelImage.pack()
# 4. 메인루프 실행
tk.mainloop()