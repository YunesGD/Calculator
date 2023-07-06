# import tkinter module
from tkinter import *
from tkinter.ttk import *
from math import *
from tkinter import ttk


master = Tk()
master.title('Calculator')
master.resizable(0, 0)

Names = {'Square_Root': sqrt, 'Power': pow, 'log': log, 'Fact': factorial,
         'sin': sin, 'cos': cos, 'tan': tan, 'cot': tan, 'radians': radians}


def ButtonClick(num):
    global op
    op = op + num
    text_input.set(op)


def EQU():
    global op
    result = str(eval(op, Names))
    text_input.set(result)
    op = ''


def Clear():
    global op
    op = ''
    text_input.set(op)


op = ''
text_input = StringVar()

Button_frame = ttk.LabelFrame(master, relief=RIDGE)
Button_frame.grid(row=2, column=1, sticky=E + W + N + S)

Entry_frame = ttk.LabelFrame(master, relief=RIDGE)
Entry_frame.grid(row=0, column=1, sticky=E + W + N + S)


l1 = Label(Entry_frame, text="Enter : ")
l1.grid(row=0, column=0, sticky=W, pady=2)

EntryNum1 = Entry(Entry_frame, textvariable=text_input, width=30)
EntryNum1.grid(row=0, column=1, sticky=N)


#                                                                           C
Button_Clear = Button(Button_frame, text='C', command=Clear)
Button_Clear.grid(row=2, column=3, sticky=W, columnspan=2)

#                                                                           √
Button_Square_Root = Button(
    Button_frame, text='√', command=lambda: ButtonClick('Square_Root('))
Button_Square_Root.grid(row=2, column=0, sticky=W)

#                                                                           ^

Button_Power = Button(Button_frame, text='^',
                      command=lambda: ButtonClick('Power('))
Button_Power.grid(row=2, column=1, sticky=W)

#                                                                           !
Button_Fact = Button(Button_frame, text='!',
                     command=lambda: ButtonClick('Fact('))
Button_Fact.grid(row=2, column=2, sticky=W)


#                                                                           (
Button_Braces = Button(Button_frame, text='(',
                       command=lambda: ButtonClick('('))
Button_Braces.grid(row=4, column=0, sticky=W)

#                                                                           )
Button_Braces = Button(Button_frame, text=')',
                       command=lambda: ButtonClick(')'))
Button_Braces.grid(row=4, column=1, sticky=W)


#                                                                           sin
Button_sin = Button(Button_frame, text='sin',
                    command=lambda: ButtonClick('sin(radians('))
Button_sin.grid(row=3, column=0, sticky=W)

#                                                                           cos
Button_cos = Button(Button_frame, text='cos',
                    command=lambda: ButtonClick('cos(radians('))
Button_cos.grid(row=3, column=1, sticky=W)
#                                                                           tan
Button_tan = Button(Button_frame, text='tan',
                    command=lambda: ButtonClick('tan(radians('))
Button_tan.grid(row=3, column=2, sticky=W)

#                                                                           cot
Button_cot = Button(Button_frame, text='cot', command=lambda: ButtonClick(
    '1/tan(radians('))
Button_cot.grid(row=3, column=3, sticky=W)

#                                                                           log
Button_log = Button(Button_frame, text='log',
                    command=lambda: ButtonClick('log('))
Button_log.grid(row=4, column=2, sticky=W)

#                                                                           ,
Button_Virgo = Button(Button_frame, text=',', command=lambda: ButtonClick(','))
Button_Virgo.grid(row=8, column=0, sticky=W)

#                                                                           =
Button_Equal = Button(Button_frame, text='=', command=EQU)
Button_Equal.grid(row=8, column=3, sticky=W)

#                                                                           +
Button_Add = Button(Button_frame, text='+', command=lambda: ButtonClick('+'))
Button_Add.grid(row=7, column=3, sticky=W)

#                                                                           -
Button_Sub = Button(Button_frame, text='-', command=lambda: ButtonClick('-'))
Button_Sub.grid(row=6, column=3, sticky=W)

#                                                                           x
Button_multi = Button(Button_frame, text='x', command=lambda: ButtonClick('*'))
Button_multi.grid(row=5, column=3, sticky=W)

#                                                                           ÷
Button_divid = Button(Button_frame, text='÷',
                      command=lambda: ButtonClick('/'))
Button_divid.grid(row=4, column=3, sticky=W)

#                                                                           .
Button_dot = Button(Button_frame, text='.', command=lambda: ButtonClick('.'))
Button_dot.grid(row=8, column=2, sticky=W)

#                                                                           0
Button_Zero = Button(Button_frame, text='0', command=lambda: ButtonClick('0'))
Button_Zero.grid(row=8, column=1, sticky=W)

#                                                                           1
Button_one = Button(Button_frame, text='1',  command=lambda: ButtonClick('1'))
Button_one.grid(row=7, column=0, sticky=W)

#                                                                           2
Button_two = Button(Button_frame, text='2', command=lambda: ButtonClick('2'))
Button_two.grid(row=7, column=1, sticky=W)

#                                                                           3
Button_three = Button(Button_frame, text='3', command=lambda: ButtonClick('3'))
Button_three.grid(row=7, column=2, sticky=W)

#                                                                           4
Button_four = Button(Button_frame, text='4',  command=lambda: ButtonClick('4'))
Button_four.grid(row=6, column=0, sticky=W)

#                                                                           5
Button_five = Button(Button_frame, text='5', command=lambda: ButtonClick('5'))
Button_five.grid(row=6, column=1, sticky=W)

#                                                                           6
Button_six = Button(Button_frame, text='6',  command=lambda: ButtonClick('6'))
Button_six.grid(row=6, column=2, sticky=W)

#                                                                           7
Button_seven = Button(Button_frame, text='7', command=lambda: ButtonClick('7'))
Button_seven.grid(row=5, column=0, sticky=W)

#                                                                           8
Button_eiteh = Button(Button_frame, text='8', command=lambda: ButtonClick('8'))
Button_eiteh.grid(row=5, column=1, sticky=W)

#                                                                           9
Button_nine = Button(Button_frame,  text='9', command=lambda: ButtonClick('9'))
Button_nine.grid(row=5, column=2, sticky=W)


mainloop()
