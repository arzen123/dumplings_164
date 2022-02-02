from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox  

colorfulnesses = ["1+0", "1+1", "4+0", "4+4"]
a3 = 350 * 420
papers = [("картон мат", 230), ("картон мат", 250), ("картон мат", 280), ("картон мат", 300), ("картон мат", 320), ("картон мат", 350),
        ("картон мел", 215), ("картон мел", 235), ("картон мел", 250), ("картон мел", 270), ("картон мел", 295), ("картон мел", 300),
        ("мел мат", 90), ("мел мат", 115), ("мел мат", 130), ("мел мат", 150), ("мел мат", 170), ("мел мат", 200), ("мел мат", 250), ("мел мат", 300), ("мел мат", 350),
        ("мел глян", 90), ("мел глян", 115), ("мел глян", 130), ("мел глян", 150), ("мел глян", 170), ("мел глян", 200), ("мел глян", 250), ("мел глян", 300), ("мел глян", 350),
        ("этикеточная", 1),
        ("офсет", 65), ("офсет", 70), ("офсет", 80), ("офсет", 100), ("офсет", 120), ("офсет", 190)]

def clear():
    circulation_entry.delete(0, END)

def prise(message):
    messagebox.showinfo("GUI Python", message)

def display():
    circulations = circulation.get()
    colorfulness1, colorfulness2 = select1()
    size = select2()
    number_of_porduction = int(a3 / size)
    number_of_paper = int(circulations / number_of_porduction)
    
    list = []
    if paper.get() == "этикеточная 1" or paper.get().startswith('офсет'):
        for word in paper.get().split():
            list.append(word)
    else:
        for word in paper.get().split(','):
            for word in word.split('{'):
                for word in word.split('}'):
                    list.append(word)

    d = list[1]
    p = list[0]
    d = int(d)
    print(d, p)
    price_of_paper, mortgage =select3(number_of_paper, d, p)
    
    if colorfulness1 == 2:
        if colorfulness2 == 0:
            dye = float((number_of_paper * 0.2) / 1000.0)
        else:
            colorfulness2 == 2
            dye = float((number_of_paper * 0.2) * 2 / 1000.0)
    else:
        colorfulness1 == 4
        if colorfulness2 == 0:
            dye = float((number_of_paper * 0.35) / 1000)
        else:
            colorfulness2 == 4
            dye = float((number_of_paper * 0.35) * 2 / 1000)

    price_of_dye = float(dye * 4.84)
    matirial = price_of_dye + price_of_paper
    

#Прилада
    if number_of_paper <= 5000:
       price_makeready = 450
    else:
        makeready = float(2 + (5000 / (number_of_paper - 5000)))
        price_makeready = makeready * 180.00
    
    
    one_cut = number_of_paper / mortgage
    cut = float((((number_of_porduction * one_cut) + (4 * one_cut)) * 0.3 + 30) / 60)
    price_cut = float(3 * cut)
    price_package = float((cut / 2) * 1.5)

#цена
    price_of_add = float((matirial + price_makeready + price_cut + price_package) * 0.4)
    nds = float((matirial + price_makeready + price_cut + price_package + price_of_add) * 0.2)
    price = matirial + price_makeready + price_cut + price_package + price_of_add     
    price_with_nds = matirial + price_makeready + price_cut + price_package + price_of_add + nds  
    message = f'Стоимость материалов = {matirial}. Стоимость приладки = {price_makeready}. Цена резки = {price_cut} Цена упаковки = {price_package}. Цена с НДС = {price_with_nds}, цена без НДС = {price}'

    prise(message)

def select1():
    c = colorfulness.get()
    if c == '1+0':
        colorfulness1 = 2
        colorfulness2 = 0
    elif c == "1+1":
        colorfulness1 = 2
        colorfulness2 = 2
    elif c == "4+0":
        colorfulness1 = 4
        colorfulness2 = 0
    elif c == "4+4":
        colorfulness1 = 4
        colorfulness2 = 4
    return colorfulness1, colorfulness2,
    
def select2():
    size = size1.get() * size2.get()
    return size


def select3(number_of_paper, d, p):
    if p == "офсет":
        print(p)
        if d == 65:
            price_of_paper = number_of_paper * 0.047
            mortgage = 1785
        elif d == 70:
            price_of_paper = number_of_paper * 0.051
            mortgage = 1648
        elif d == 80:
            price_of_paper = number_of_paper * 0.076
            mortgage = 1415
        elif d == 100:
            price_of_paper = number_of_paper * 0.089
            mortgage = 1200
        elif d == 120:
            price_of_paper = number_of_paper * 0.098
            mortgage = 1000
        elif d == 190:
            price_of_paper = number_of_paper * 0.128
            mortgage = 681
        print(d, price_of_paper, mortgage)
    elif p == "этикеточная":
        price_of_paper = number_of_paper * 0.114
        mortgage = 2142
    elif p == "мел глян":
        if d == 90:
            price_of_paper = number_of_paper * 0.091
            mortgage = 2500
        elif d == 115:
            price_of_paper = number_of_paper * 0.091
            mortgage = 1875
        elif d == 130:
            price_of_paper = number_of_paper * 0.085
            mortgage = 1666
        elif d == 150:
            price_of_paper = number_of_paper * 0.144
            mortgage = 1363
        elif d == 170:
            price_of_paper = number_of_paper * 0.165
            mortgage = 1200
        elif d == 200:
            price_of_paper = number_of_paper * 0.145
            mortgage = 882
        elif d == 250:
            price_of_paper = number_of_paper * 0.522
            mortgage = 789
        elif d == 300:
            price_of_paper = number_of_paper * 0.321
            mortgage = 681
        elif d == 350:
            price_of_paper = number_of_paper * 0.321
            mortgage = 681
    elif p == "мел мат":
        if d == 90:
            price_of_paper = number_of_paper * 0.09
            mortgage = 2307
        elif d == 115:
            price_of_paper = number_of_paper *0.102
            mortgage = 1666
        elif d == 130:
            price_of_paper = number_of_paper * 0.112
            mortgage = 1363
        elif d == 150:
            price_of_paper = number_of_paper * 0.123
            mortgage = 1153
        elif d == 170:
            price_of_paper = number_of_paper * 0.152
            mortgage = 1071
        elif d == 200:
            price_of_paper = number_of_paper * 0.172
            mortgage = 789
        elif d == 250:
            price_of_paper = number_of_paper * 0.199
            mortgage = 652
        elif d == 300:
            price_of_paper = number_of_paper * 0.321
            mortgage = 483
        elif d == 350:
            price_of_paper = number_of_paper * 0.321
            mortgage = 483
    elif p == "картон мел":
        if d == 215:
            mortgage = 491
            price_of_paper = number_of_paper * 0.233
        elif d == 235:
            mortgage = 416
            price_of_paper = number_of_paper * 0.304
        elif d == 250:
            mortgage = 394
            price_of_paper = number_of_paper * 0.33
        elif d == 270:
            mortgage = 365
            price_of_paper = number_of_paper * 0.35
        elif d == 295:
            mortgage = 294
            price_of_paper = number_of_paper * 0.37
        elif d == 300:
            mortgage = 267
            price_of_paper = number_of_paper * 0.4
    elif p == "картон мат":
        if d == 230:
            mortgage = 526
            price_of_paper = number_of_paper * 0.233
        elif d == 250:
            mortgage = 476
            price_of_paper = number_of_paper * 0.304
        elif d == 280:
            mortgage = 416
            price_of_paper = number_of_paper * 0.33
        elif d == 300:
            mortgage = 384
            price_of_paper = number_of_paper * 0.35
        elif d == 320:
            mortgage = 361
            price_of_paper = number_of_paper * 0.37
        elif d == 350:
            mortgage = 333
            price_of_paper = number_of_paper * 0.4
    return price_of_paper, mortgage


root = Tk()
root.title("GUI на Python")
root.geometry("500x500")

paper = Combobox(root)
paper.set( "Выберите бумагу" )
paper['value'] = papers
paper.grid(column=0, row=2)  

size1 = IntVar()
size2 = IntVar()

size1_label = Label(text="по высоте")
size2_label = Label(text="по шрине")

size1_label.grid(row=3, column=0, sticky="w")
size2_label.grid(row=5, column=0, sticky="w")

size1_entry = Entry(textvariable=size1)
size2_entry = Entry(textvariable=size2)
size1_entry.grid(row=4, column=0, sticky="w")
size2_entry.grid(row=6, column=0, sticky="w")

colorfulness = Combobox(root)
colorfulness.set( "Выберите карсочность" )
colorfulness['value'] = colorfulnesses
colorfulness.grid(column=0, row=7)  

circulation = IntVar()

circulation_label = Label(text="Тираж")
circulation_label.grid(row=0, column=0, sticky='w')

circulation_entry = Entry(textvariable=circulation)
circulation_entry.grid(row=1, column=0, sticky='w')

message_button = Button(text="Посчитать", command=display)
message_button2 = Button(text="Отчистить", command=clear)


message_button.grid(row=0, column=5)
message_button2.grid(row=0, column=6)

   
root.mainloop()
