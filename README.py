from cProfile import label
from tkinter import *
from tkinter import messagebox

colorfulnesses = [("1+0", 1), ("1+1", 2), ("4+0", 3), ("4+4", 4)]
sizes = [("a4", 1), ("a5", 2), ("a6", 3), ("другой", 4)]
papers = ["картон мат", "картон мел", "мел мат", "мел глян", "этикеточная", "офсет"]
ofcet_densitys= [65, 70, 80, 100, 120, 190]
mel_densitys = [90, 115, 130, 150, 200, 250, 300]
kar_mel_densitys = [215, 235, 250, 270, 295, 325]
kar_mat_densitys = [230, 250, 280, 300, 320, 350, 400]
a3 = 720 * 520

def clear():
    circulation_entry.delete(0, END)

def display():
    messagebox.showinfo("GUI Python", colorfulness.get())

def select1():
    c = colorfulness.get()
    if c == 1:
        colorfulness1 = 2
        colorfulness2 = 0
    elif c == 2:
        colorfulness1 = 2
        colorfulness2 = 2
    elif c == 3:
        colorfulness1 = 4
        colorfulness2 = 0
    elif c == 4:
        colorfulness1 = 4
        colorfulness2 = 4
    return colorfulness1, colorfulness2,


def select2():
    s = size.get()
    if s == 1:
        size1 = 210
        size2 = 297
    elif s == 2:
        size1 = 148
        size2 = 210
    elif s == 3:
        size1 = 105
        size2 = 148
    elif s == 4:
        size1 = IntVar()
        size2 = IntVar()

        size1_label = Label(text="по высоте")
        size2_label = Label(text="по шрине")

        size1_label.grid(row=6, column=5, sticky="w")
        size2_label.grid(row=7, column=5, sticky="w")

        size1_entry = Entry(textvariable=size1)
        size2_entry = Entry(textvariable=size2)
        size1_entry.grid(row=6, column=6, sticky="w")
        size2_entry.grid(row=7, column=6, sticky="w")
    return size1, size2

def select3(density):
    p = paper.get()
    d = 1
    if p == "офсет":
        
        drop2 = OptionMenu( root , density , *ofcet_densitys)
        drop2.grid(row=7, column=1, padx=15, pady=10)
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
    elif p == "этикеточная":
        price_of_paper = number_of_paper * 0.114
        mortgage = 2142
    elif p == "мел глян":
        drop2 = OptionMenu( root , density , *mel_densitys)
        drop2.grid(row=7, column=1, padx=15, pady=10)
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
    elif p == "мел мат":
        drop2 = OptionMenu( root , density , *mel_densitys)
        drop2.grid(row=7, column=1, padx=15, pady=10)
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
    elif p == "картон мел":
        drop2 = OptionMenu( root , density , *kar_mel_densitys)
        drop2.grid(row=7, column=1, padx=15, pady=10)
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
        elif d == 325:
            mortgage = 267
            price_of_paper = number_of_paper * 0.4
    elif p == "картон мак":
        drop2 = OptionMenu( root , density , *kar_mat_densitys)
        drop2.grid(row=7, column=1, padx=15, pady=10)
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
        elif d == 400:
            mortgage = 285
            price_of_paper = number_of_paper * 0.42
    

root = Tk()
root.title("GUI на Python")
root.geometry("500x500")

density = IntVar()
paper = StringVar()
paper.set( "картон мат" )

drop1 = OptionMenu( root , paper , *papers, command=select3)
drop1.grid(row=7, column=0, padx=15, pady=10)



header1 = Label(text="Выберите красочность", padx=15, pady=10)
header2 = Label(text="Выберите формат", padx=15, pady=10)
header1.grid(row=2, column=0, sticky=W)
header2.grid(row=2, column=1, sticky=W)

colorfulness = IntVar()
size = IntVar()
paper = StringVar()
density = IntVar()


row = 3
for txt, val in colorfulnesses:
    Radiobutton(text=txt, value=val, variable=colorfulness, padx=15, pady=10, command=select1)\
        .grid(row=row, sticky=W)
    row += 1

sel1 = Label(padx=15, pady=10)
sel1.grid(row=row, sticky=W)

row = 3
for txt, val in sizes:
    Radiobutton(text=txt, value=val, variable=size, padx=15, pady=10, command=select2)\
        .grid(row=row, column=1, sticky=W)
    row += 1

sel2 = Label(padx=15, pady=10)
sel2.grid(row=row, column=1, sticky=W)


circulation = IntVar()

circulation_label = Label(text="Тираж",padx=15, pady=10)
circulation_label.grid(row=0, column=0, sticky="w")

circulation_entry = Entry(textvariable=circulation)
circulation_entry.grid(row=1, column=0, sticky="w", padx=15)

message_button = Button(text="Посчитать", command=display)
message_button2 = Button(text="Отчистить", command=clear)

message_button.grid(row=0, column=5, sticky="e")
message_button2.grid(row=0, column=6, sticky="e")


while True:
    #size = size1 * size2
    colorfulness1 = int(input('Красочность первое значение - '))
    colorfulness2 = int(input('Красочность второе значение - '))
    paper = input('Бумага - ')
    if paper.startswith("картон"):
        paper_for_matirial = paper.split(" ")
        paper_for_matirial = paper_for_matirial[0]
    if not paper.startswith("этикеточная"):
        density = int(input('Плотность бумаги -'))

#Расчет количества бумаги   
    number_of_porduction = int(a3 / size)
    number_of_paper = int(circulation / number_of_porduction)




#Расчет краски
    if colorfulness1 == 2:
        if colorfulness2 == 0:
            dye = float((number_of_paper * 0.2) / 1000.0)
        elif colorfulness2 == 2:
            dye = float((number_of_paper * 0.2) * 2 / 1000.0)
        else:
            print(
                'неправильно ввели вторую краскосочность, {colorfulness2} а надо 2 или 4')
    elif colorfulness1 == 4:
        if colorfulness2 == 0:
            dye = float((number_of_paper * 0.35) / 1000)
        elif colorfulness2 == 4:
            dye = float((number_of_paper * 0.35) * 2 / 1000)
        else:
            print(
                'неправильно ввели вторую краскосочность, {colorfulness2} а надо 2 или 4')
    else:
        print(
            'неправильно ввели первую красочность, вы ввели {colorfulness1}, а надо 2 или 4')
    price_of_dye = float(dye * 4.84)
    matirial = price_of_dye + price_of_paper
    print("Стоимость материалов", matirial)

#Прилада
    if number_of_paper <= 5000:
       price_makeready = 450
    else:
        makeready = float(2 + (5000 / (number_of_paper - 5000)))
        price_makeready = makeready * 180.00
    print("Стоимость приладки = ", price_makeready)
    
    one_cut = number_of_paper / mortgage
    cut = float((((number_of_porduction * one_cut) + (4 * one_cut)) * 0.3 + 30) / 60)
    price_cut = float(3 * cut)
    price_package = float((cut / 2) * 1.5)
    print("Цена резки", price_cut, "Цена упаковки", price_package)

#цена
    price_of_add = float((matirial + price_makeready + price_cut + price_package) * 0.4)
    nds = float((matirial + price_makeready + price_cut + price_package + price_of_add) * 0.2)
    price = matirial + price_makeready + price_cut + price_package + price_of_add     
    price_with_nds = matirial + price_makeready + price_cut + price_package + price_of_add + nds  
    print(f'Цена с НДС = {price_with_nds}, цена без НДС = {price}')

    root.mainloop()
