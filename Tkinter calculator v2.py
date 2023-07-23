'''Python program Calculator using tkinter. To view history see the python launcher before closing.
    This program has been made by Anadi Agrawal'''


from tkinter import *

root = Tk()
root.title('Calculator')
root.iconbitmap("D:\\Python Programs\\Python Programs\\main progs\\Calculator.ico")


a = Entry(root, width=55, borderwidth=5, fg='blue')
a.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

def buttonclick(number):
    a.insert(END,(number))
    

def button_clear():
    a.delete(0,END)

def button_equal():
    
    txt = a.get().split(' ')

    for num in txt:
        print(num,end=' ')
    
    for i in range(len(txt)):
        if i%2 ==1:
            if txt[i] == '+':
                res = int(txt[i-1]) + int(txt [i+1])
                txt[i+1] = str(res)
            if txt[i] == '-':
                res = int(txt[i-1]) - int(txt [i+1])
                txt[i+1] = str(res)
            if txt[i] == 'X':
                res = int(txt[i-1]) * int(txt [i+1])
                txt[i+1] = str(res)
            if txt[i] == '/':
                res = int(txt[i-1]) / int(txt [i+1])
                txt[i+1] = str(res)
        
    print('= ',res)    
    a.delete(0,END)
    a.insert(END,(res))
    
    
    
        

button0 = Button(root, text='0', padx=40, pady=20, command= lambda: buttonclick(0)).grid(row=4 , column=1 )
button1 = Button(root, text='1', padx=40, pady=20, command= lambda: buttonclick(1)).grid(row=3 , column=0 )
button2 = Button(root, text='2', padx=40, pady=20, command= lambda: buttonclick(2)).grid(row=3 , column=1 )
button3 = Button(root, text='3', padx=40, pady=20, command= lambda: buttonclick(3)).grid(row=3 , column=2 )
button4 = Button(root, text='4', padx=40, pady=20, command= lambda: buttonclick(4)).grid(row=2 , column=0 )
button5 = Button(root, text='5', padx=40, pady=20, command= lambda: buttonclick(5)).grid(row=2 , column=1 )
button6 = Button(root, text='6', padx=40, pady=20, command= lambda: buttonclick(6)).grid(row=2 , column=2 )
button7 = Button(root, text='7', padx=40, pady=20, command= lambda: buttonclick(7)).grid(row=1 , column=0 )
button8 = Button(root, text='8', padx=40, pady=20, command= lambda: buttonclick(8)).grid(row=1 , column=1 )
button9 = Button(root, text='9', padx=40, pady=20, command= lambda: buttonclick(9)).grid(row=1 , column=2 )

buttonadd = Button(root, text='+', padx=39, pady=20, command= lambda: buttonclick(' + ')).grid(row=4 , column=0 )
buttonsub = Button(root, text='-', padx=40.49, pady=20, command= lambda: buttonclick(' - ')).grid(row=4 , column=2 )
buttondivide = Button(root, text='/', padx=40, pady=20, command= lambda: buttonclick(' / ')).grid(row=5 , column=1 )
buttonmultiply = Button(root, text='X', padx=39.5, pady=20, command= lambda: buttonclick(' X ')).grid(row=5 , column=0 )
buttonclear = Button(root, text='Clear', padx=30, pady=52, command= button_clear,bg='orange').grid(row=1 , column=4, rowspan=2 )
buttonequal = Button(root, text='=', padx=40, pady=52, command= button_equal,bg='light green').grid(row=3 , column=4 ,rowspan=2)

buttonthanks = Button(root, text='Made by Anadi Agrawal', padx=29, pady=20, bg='light blue').grid(row=5 , column=2 , columnspan=3)

root.mainloop()