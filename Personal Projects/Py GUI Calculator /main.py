from tkinter import *

def btnClick(number):
    global operator
    operator = operator + str(number)
    input_val.set(operator)

def btnClear():
    global operator
    operator = ''
    input_val.set("")

def btnEqual():
    global operator
    result = str(eval(operator))
    input_val.set(result)
    operator = ''

window = Tk()
window.title("Calculator")

operator = ''
input_val = StringVar()

display_text = Entry(window, font=("arial", 20, "bold"), textvariable=input_val, bd=30, insertwidth=4, bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

# row 1
btn_7 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="7", command= lambda: btnClick(7))
btn_7.grid(row=1, column=0)

btn_8 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="8", command= lambda: btnClick(8))
btn_8.grid(row=1, column=1)

btn_9 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="9", command= lambda: btnClick(9))
btn_9.grid(row=1, column=2)

btn_plus = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+", command= lambda: btnClick('+'))
btn_plus.grid(row=1, column=3)

# row 2
btn_4 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="4", command= lambda: btnClick(4))
btn_4.grid(row=2, column=0)

btn_5 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="5", command= lambda: btnClick(5))
btn_5.grid(row=2, column=1)

btn_6 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="6", command= lambda: btnClick(6))
btn_6.grid(row=2, column=2)

btn_minus = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-", command= lambda: btnClick('-'))
btn_minus.grid(row=2, column=3)

# row 3
btn_1 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="1", command= lambda: btnClick(1))
btn_1.grid(row=3, column=0)

btn_2 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="2", command= lambda: btnClick(2))
btn_2.grid(row=3, column=1)

btn_3 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="3", command= lambda: btnClick(3))
btn_3.grid(row=3, column=2)

btn_multiply = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="*", command= lambda: btnClick('*'))
btn_multiply.grid(row=3, column=3)

# row 4
btn_0 = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="0", command= lambda: btnClick(0))
btn_0.grid(row=4, column=0)

btn_clear = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="C", command=btnClear)
btn_clear.grid(row=4, column=1)

btn_equal = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=", command=btnEqual)
btn_equal.grid(row=4, column=2)

btn_divide = Button(window, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="/", command= lambda: btnClick('/'))
btn_divide.grid(row=4, column=3)


window.mainloop()