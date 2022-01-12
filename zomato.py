import time
import pyqrcode
import png
from pyqrcode import QRCode
import cv2
import random

def syam(str):
    c=input("which catogery you want '1-Mobiles' or '2-Cloths' : ")
    #MOBILES 
    mobiles=[' ** 1.Realme ** AND',' ** 2.Apple **']
    realme=[' 1-Realme 3\n',
            '2-Realme 3pro\n',
            '3-Realme x']
    price_realme=['Rs.13000','Rs.15000','Rs.17000']
    price_apple=['Rs.95000','Rs.80000','Rs.50000']
    apple=['1-Iphone 13\n',
           '2-Iphone x\n',
           '3-Iphone xr']

    #CLOTHS
    cloths=[' **1- Men ** AND',' ** 2-Women **']

    men=[' ** 1-Adidas ** ,',' ** 2-Levis ** AND',' **3-PeterEngland **']
    adidas=[' 1-SHIRTS \n','2-PANTS\n','2-T-SHIRTS']
    levis=[' 1-SHIRTS \n','2-PANTS\n','3-T-SHIRTS']
    peterengland=[' 1-SHIRTS \n','2-PANTS\n','3-T-SHIRTS']

    price_adidas=['Rs.499','Rs.799','Rs.399']
    price_levis=['Rs.650','Rs.840','Rs.450']
    price_peterengland=['Rs.440','Rs.760','Rs.360']

    women=['1-ZARA','2-ALLEN','3-FABINDIA']
    zara=['1-TOPS\n','2-SAREES\n','3-HOODIES']
    allen=['1-TOPS\n','2-SAREES\n','3-HOODIES']
    fabindia=['1-TOPS\n','2-SAREES\n','3-HOODIES']

    price_zara=['Rs.540','Rs.759','Rs.869']
    price_allen=['Rs.660','Rs.860','Rs.940']
    price_fabindia=['Rs.540','Rs.750','Rs.840']
    

    if c=='1':
        print("The brands are: ")
        print(*mobiles)
        anil1()
        user=input("Which brand do you want : " )
        if user=='1':
            anil2()
            print("The models are : ")
            print(*realme)
            s=input("Which model you want: ")
            if s=='1':
                anil3()
                print("The price is:",price_realme[0])
                vi(str)


                    
            elif s=='2':
                anil4()
                print("The price is:",price_realme[1])
                vi(str)
            else:
                anil5()
                print("The price is:",price_realme[2])
                vi(str)
        else:
            print("The models are : ")
            anil9()
            print(*apple)
            g=input("Which model you want: ")
            if g=='1':
                anil6()
                print("The price is:",price_apple[0])
                vi(str)

            elif g=='2':
                anil7()
                print("The price is:",price_apple[1])
                vi(str)
            else:
                anil8()
                print("The price is:",price_apple[2])
                vi(str)
            
    elif c=='2':
        print("the catogeries are: ")
        print(*cloths)
        q=input("Select the catogery you want : ")
        if q=='1':
            print("These are the brands")
            print(*men)
            w=input("Enter which brand you want: ")
            if w=='1':
                print("These are the items in ",w)
                print(*adidas)
                e=input("Enter which item do you want:")
                if e=='1':
                    print("The price is:",price_adidas[0])
                    vi(str)
                elif e=='2':
                    print("The price is:",price_adidas[1])
                    vi(str)
                else:
                    print("The price is:",price_adidas[2])
                    vi(str)
            elif w=='2':
                print("These are the items in ",w)
                print(*levis)
                r=input("Enter which item do you want:")
                if r=='1':
                    print("The price is:",price_levis[0])
                    vi(str)
                elif r=='2':
                    print("The price is:",price_levis[1])
                    vi(str)
                else:
                    print("The price is:",price_levis[2])
                    vi(str)

            else:
                print("These are the items in ",w)
                print(*peterengland)
                t=input("Enter which item do you want:")
                if t=='1':
                    print("The price is:",price_peterengland[0])
                    vi(str)
                elif t=='1':
                    print("The price is:",price_peterengland[1])
                    vi(str)
                else:
                    print("The price is:",price_peterengland[2])
                    vi(str)
        else:
            print("These are the brands")
            print(*women)
            w=input("Enter which brand you want: ")
            if w=='1':
                print("These are the items in ",w)
                print(*zara)
                e=input("Enter which item do you want:")
                if e=='1':
                    print("The price is:",price_zara[0])
                    vi(str)
                elif e=='2':
                    print("The price is:",price_zara[1])
                    vi(str)
                else:
                    print("The price is:",price_zara[2])
                    vi(str)
            elif w=='2':
                print("These are the items in ",w)
                print(*allen)
                r=input("Enter which item do you want:")
                if r=='1':
                    print("The price is:",price_allen[0])
                    vi(str)
                elif r=='2':
                    print("The price is:",price_allen[1])
                    vi(str)
                else:
                    print("The price is:",price_allen[2])
                    vi(str)
            else:
                print("These are the items in ",w)
                print(*fabindia)
                t=input("Enter which item do you want:")
                if t=='1':
                    print("The price is:",price_fabindia[0])
                    a1=input("Do you want to add this item into your cart :")
                    vi(str)
                            
                elif t=='2':
                    print("The price is:",price_fabindia[1])
                    vi(str)
                else:
                    print("The price is:",price_fabindia[2])
                    vi(str)

    else:
        print("sorry...we don't have that item")

def lott(str):
    ch="yes"
    while ch=="yes":
        
        l=[]
        n=int(input("enter no of players:"))
        for i in range(n):
            l.append([])
            for j in range(9):
                l[i].append(random.randint(10,99))
        l1=[]
        co=[]
        for i in range(n*10):
            l1.append(random.randint(10,99))
        for i in l:
            c=0
            for j in i:
                if j in l1:
                    c+=1
            co.append(c)
        i1=co.index(max(co))
        print(l)
        print(l1)
        co.sort()
        print("PLAYER",i1+1,"WINS THE GAME!!!")
        ch=input("Do u want 2 continue the game :(yes/no) ")

    print("THNKS FOR PLAYING>>>>!!!!\n")
    ram(str)

def man(str):
    print("hello",name.upper(),"Welcome to Flipkart...!!!!:")
    print(" These are the catogeries\n ")
    print("1-Shopping")
    print("2-Bingogame\n ")
    d1=input(" Which catogery you want :")
    if d1=='1':
        syam(d1)
    else:
        lott(d1)
def mani(str):
    Dis1()
    print("1-Shopping")
    print("2-Bingogame\n ")
    d1=input(" Which catogery you want :")
    if d1=='1':
        syam(d1)
    else:
        lott(d1)

def ram(str):
    print("1-Main menu")
    print("2-Exit")
    f3=input(" Enter your Choice :")
    if f3=='1':
        mani(str)
    else:
        print(" Thank you")
def vi(str):
    a1=input("Do you want to add this item into your cart :")
    if a1=='yes':
        print("Your catr is Updated.....!!!!")
        print("Please pay\n ")
        Dis()
        ram(str)
    else:
        print("Continue...Shopping\n")
        ram(str)

def Dis():
    print(" After Payment Please Close The  Image Window")
    im = cv2.imread("r.png")                    
    imS = cv2.resize(im, (520, 820))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(" Thanks for Shopping....")

def anil1():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("mob.png")                    
    imS = cv2.resize(im, (650,400))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil2():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("realme.jpg")                    
    imS = cv2.resize(im, (650,400))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil3():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("realme3.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil4():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("realme3pro.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def anil5():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("realmex.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil6():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("iphonex.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil7():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("iphone13.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil8():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("iphonexr.jpg")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil9():
    print("after  seen Please Close The  Image Window\n")
    im = cv2.imread("iphones.jpg")                    
    imS = cv2.resize(im, (650,400))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def Dis1():
    print(" After seen Please Close The  Image Window")
    im = cv2.imread("sh.png")                    
    imS = cv2.resize(im, (650,800))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def anil10():
    print(" After seen Please Close The  Image Window")
    im = cv2.imread("welcome.jpg")                    
    imS = cv2.resize(im, (800,500))
    cv2.imshow("output", imS)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
name=input(" Enter your name:")
anil10()
mani(name)



