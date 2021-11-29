BACKGROUND_COLOR = "#B1DDC6"


#
# ---------------GUI Creation--------------
import pandas
from random import *
from tkinter import *
df = pandas.read_csv("french_words.csv")
window = Tk()
window.title("Flashy")
window.minsize(2000,2000)
window.config(padx=250,pady=20)
window.config(bg = BACKGROUND_COLOR)
canvas = Canvas(width=800, height=670,bg = BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=2,row=0,columnspan=2)
card_back = PhotoImage(file = "images/card_back.png")
card_front = PhotoImage(file = "images/card_front.png")
correct_sign = PhotoImage(file ="images/right.png")
wrong_sign = PhotoImage(file= "images/wrong.png")

board = canvas.create_image(400,400,image = '')
language = canvas.create_text(400,250,text = "")
word= canvas.create_text(400,400,text='')



def suru():
    sn = randint(0,len(df))
    french_t(sn)

def french_t(sn):
    canvas.itemconfig(board,image = card_front)
    canvas.itemconfig(language,text="French",fill='black',font=("Arial",40,'italic'))
    canvas.itemconfig(word, text=df['French'][sn], fill='black', font=("Arial", 60, 'bold'))
    window.after(3000, english_t,sn)

def english_t(sn):
    canvas.itemconfig(board, image=card_back)
    canvas.itemconfig(language, text="English", fill='white', font=("Arial", 40, 'italic'))
    canvas.itemconfig(word, text=df['English'][sn], fill='white', font=("Arial", 60, 'bold'))
    df.drop([sn],inplace=True)
    df.reset_index(drop=True,inplace=True)





right = Button(image = correct_sign,bg = BACKGROUND_COLOR,command=suru,highlightthickness=0,bd=0)
right.grid(column=2,row=1)

wrong = Button(image = wrong_sign,bg=BACKGROUND_COLOR,command=suru,highlightthickness=0,bd=0)
wrong.grid(column=3,row=1)
suru()


# right.grid(column=4,row=4)
window.mainloop()
df.reset_index(drop=True)
print(df)
df.to_csv('words_to_learn.csv')