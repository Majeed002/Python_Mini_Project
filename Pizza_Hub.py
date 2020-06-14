from tkinter import *
#import pymysql
import datetime



P_win=Tk()
P_win.geometry("1300x770")
P_win.title("MENU WINDOW")
P_win.configure(background='khaki1')
P_win.resizable(0,0)
##################################################################################################################################################################

#conn= pymysql.connect(host="localhost",user="root",password="",database="pizza_planet")
#cursor=conn.cursor()

##################################################################################################################################################################

name_var=StringVar()
mobile_var=StringVar()
p1_var=IntVar()
p2_var=IntVar()
p3_var=IntVar()
p4_var=IntVar()
p5_var=IntVar()
p6_var=IntVar()
p7_var=IntVar()
p8_var=IntVar()
cd1_var=IntVar()
cd2_var=IntVar()
cd3_var=IntVar()
total_var=IntVar()

##################################################################################################################################################################

def p1_quantity():
    p1_sum=p1_var.get()
    P_e1.delete(0,END)
    total1=p1_sum+1
    P_e1.insert(END,total1)

def p2_quantity():
    p2_sum=p2_var.get()
    P_e2.delete(0,END)
    total2=p2_sum+1
    P_e2.insert(END,total2)

def p3_quantity():
    p3_sum=p3_var.get()
    P_e3.delete(0,END)
    total3=p3_sum+1
    P_e3.insert(END,total3)
    
def p4_quantity():
    p4_sum=p4_var.get()
    P_e4.delete(0,END)
    total4=p4_sum+1
    P_e4.insert(END,total4)

def p5_quantity():
    p5_sum=p5_var.get()
    P_e5.delete(0,END)
    total5=p5_sum+1
    P_e5.insert(END,total5)

def p6_quantity():
    p6_sum=p6_var.get()
    P_e6.delete(0,END)
    total6=p6_sum+1
    P_e6.insert(END,total6)

def p7_quantity():
    p7_sum=p7_var.get()
    P_e7.delete(0,END)
    total7=p7_sum+1
    P_e7.insert(END,total7)

def p8_quantity():
    p8_sum=p8_var.get()
    P_e8.delete(0,END)
    total8=p8_sum+1
    P_e8.insert(END,total8)

def cd1_quantity():
    cd1_sum=cd1_var.get()
    CD_e1.delete(0,END)
    total9=cd1_sum+1
    CD_e1.insert(END,total9)

def cd2_quantity():
    cd2_sum=cd2_var.get()
    CD_e2.delete(0,END)
    total10=cd2_sum+1
    CD_e2.insert(END,total10)

def cd3_quantity():
    cd3_sum=cd3_var.get()
    CD_e3.delete(0,END)
    total11=cd3_sum+1
    CD_e3.insert(END,total11)

def total_price():
    p1_sum=p1_var.get()*199
    p2_sum=p2_var.get()*209
    p3_sum=p3_var.get()*229
    p4_sum=p4_var.get()*249
    p5_sum=p5_var.get()*259
    p6_sum=p6_var.get()*259
    p7_sum=p7_var.get()*289
    p8_sum=p8_var.get()*299
    cd1_sum=cd1_var.get()*49
    cd2_sum=cd2_var.get()*49
    cd3_sum=cd3_var.get()*49
    Total_entry.delete(0,END)
    total=p1_sum+p2_sum+p3_sum+p4_sum+p5_sum+p6_sum+p7_sum+p8_sum+cd1_sum+cd2_sum+cd3_sum
    Total_entry.insert(END,total)

reset=0
def clear():
    P_e1.delete(0,END)
    P_e1.insert(END,reset)
    P_e2.delete(0,END)
    P_e2.insert(END,reset)
    P_e3.delete(0,END)
    P_e3.insert(END,reset)
    P_e4.delete(0,END)
    P_e4.insert(END,reset)
    P_e5.delete(0,END)
    P_e5.insert(END,reset)
    P_e6.delete(0,END)
    P_e6.insert(END,reset)
    P_e7.delete(0,END)
    P_e7.insert(END,reset)
    P_e8.delete(0,END)
    P_e8.insert(END,reset)
    CD_e1.delete(0,END)
    CD_e1.insert(END,reset)
    CD_e2.delete(0,END)
    CD_e2.insert(END,reset)
    CD_e3.delete(0,END)
    CD_e3.insert(END,reset)
    Total_entry.delete(0,END)
    Total_entry.insert(END,reset)
    name_entry.delete(0,END)
    mobile_entry.delete(0,END)

def order_window():
    B_win=Tk()
    B_win.geometry("700x700")
    B_win.title("BILL WINDOW")
    B_win.configure(background='white smoke')

    m_name = Label(B_win,text="BILL",bg="white smoke",font=("arial", 30,"bold"))
    m_name.place(x=100,y=40)
    

    item_label = Label(B_win,text="Item Name",bg="white smoke",font=("Arial",20,"bold"))
    item_label.place(x=100,y=140)

    bill_1name = Label(B_win,text="Veggie Italiano",bg="white smoke",font=("Arial",15,"bold"))
    bill_1name.place(x=120,y=190)
    _x1 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x1.place(x=340,y=190)
    pizza1=p1_var.get()
    bill_1 = Label(B_win,text=pizza1,bg="white smoke",font=("Arial",15,"bold"))
    bill_1.place(x=400,y=190)
    _eq1 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq1.place(x=455,y=190)
    bill_var1=IntVar()
    cost_1=pizza1*199
    tot_1ent = Entry(B_win,text="0",textvariable=bill_var1,width=10,font=("Arial",15,"bold"))
    tot_1ent.place(x=500,y=190)
    tot_1ent.delete(0,END)
    tot_1ent.insert(END,cost_1)

    #*************************

    bill_2name = Label(B_win,text="Classic Corn",bg="white smoke",font=("Arial",15,"bold"))
    bill_2name.place(x=120,y=220)
    _x2 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x2.place(x=340,y=220)
    pizza2=p2_var.get()
    bill_2 = Label(B_win,text=pizza2,bg="white smoke",font=("Arial",15,"bold"))
    bill_2.place(x=400,y=220)
    _eq2 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq2.place(x=455,y=220)
    bill_var2=IntVar()
    cost_2=pizza2*209
    tot_2ent = Entry(B_win,text="0",textvariable=bill_var2,width=10,font=("Arial",15,"bold"))
    tot_2ent.place(x=500,y=220)
    tot_2ent.delete(0,END)
    tot_2ent.insert(END,cost_2)

    #*********************************
    
    bill_3name = Label(B_win,text="Soya Masala",bg="white smoke",font=("Arial",15,"bold"))
    bill_3name.place(x=120,y=250)
    _x3 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x3.place(x=340,y=250)
    pizza3=p3_var.get()
    bill_3 = Label(B_win,text=pizza3,bg="white smoke",font=("Arial",15,"bold"))
    bill_3.place(x=400,y=250)
    _eq3 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq3.place(x=455,y=250)
    bill_var3=IntVar()
    cost_3=pizza3*229
    tot_3ent = Entry(B_win,text="0",textvariable=bill_var3,width=10,font=("Arial",15,"bold"))
    tot_3ent.place(x=500,y=250)
    tot_3ent.delete(0,END)
    tot_3ent.insert(END,cost_3)

    #*****************************

    bill_4name = Label(B_win,text="Paneer Masala",bg="white smoke",font=("Arial",15,"bold"))
    bill_4name.place(x=120,y=280)
    _x4 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x4.place(x=340,y=280)
    pizza4=p4_var.get()
    bill_4 = Label(B_win,text=pizza4,bg="white smoke",font=("Arial",15,"bold"))
    bill_4.place(x=400,y=280)
    _eq4 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq4.place(x=455,y=280)
    bill_var4=IntVar()
    cost_4=pizza4*249
    tot_4ent = Entry(B_win,text="0",textvariable=bill_var4,width=10,font=("Arial",15,"bold"))
    tot_4ent.place(x=500,y=280)
    tot_4ent.delete(0,END)
    tot_4ent.insert(END,cost_4)

    #*********************

    bill_5name = Label(B_win,text="Chicken Italiano",bg="white smoke",font=("Arial",15,"bold"))
    bill_5name.place(x=120,y=310)
    _x5 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x5.place(x=340,y=310)
    pizza5=p5_var.get()
    bill_5 = Label(B_win,text=pizza5,bg="white smoke",font=("Arial",15,"bold"))
    bill_5.place(x=400,y=310)
    _eq5 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq5.place(x=455,y=310)
    bill_var5=IntVar()
    cost_5=pizza5*259
    tot_5ent = Entry(B_win,text="0",textvariable=bill_var5,width=10,font=("Arial",15,"bold"))
    tot_5ent.place(x=500,y=310)
    tot_5ent.delete(0,END)
    tot_5ent.insert(END,cost_5)

    #*************************

    bill_6name = Label(B_win,text="Chicken Sausage",bg="white smoke",font=("Arial",15,"bold"))
    bill_6name.place(x=120,y=340)
    _x6 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x6.place(x=340,y=340)
    pizza6=p6_var.get()
    bill_6 = Label(B_win,text=pizza6,bg="white smoke",font=("Arial",15,"bold"))
    bill_6.place(x=400,y=340)
    _eq6 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq6.place(x=455,y=340)
    bill_var6=IntVar()
    cost_6=pizza6*259
    tot_6ent = Entry(B_win,text="0",textvariable=bill_var6,width=10,font=("Arial",15,"bold"))
    tot_6ent.place(x=500,y=340)
    tot_6ent.delete(0,END)
    tot_6ent.insert(END,cost_6)

    #*************************

    bill_7name = Label(B_win,text="Lebanese Chicken",bg="white smoke",font=("Arial",15,"bold"))
    bill_7name.place(x=120,y=370)
    _x7 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x7.place(x=340,y=370)
    pizza7=p7_var.get()
    bill_7 = Label(B_win,text=pizza7,bg="white smoke",font=("Arial",15,"bold"))
    bill_7.place(x=400,y=370)
    _eq7 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq7.place(x=455,y=370)
    bill_var7=IntVar()
    cost_7=pizza7*289
    tot_7ent = Entry(B_win,text="0",textvariable=bill_var7,width=10,font=("Arial",15,"bold"))
    tot_7ent.place(x=500,y=370)
    tot_7ent.delete(0,END)
    tot_7ent.insert(END,cost_7)

    #*************************

    bill_8name = Label(B_win,text="Chicken Supreme",bg="white smoke",font=("Arial",15,"bold"))
    bill_8name.place(x=120,y=400)
    _x8 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x8.place(x=340,y=400)
    pizza8=p8_var.get()
    bill_8 = Label(B_win,text=pizza8,bg="white smoke",font=("Arial",15,"bold"))
    bill_8.place(x=400,y=400)
    _eq8 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq8.place(x=455,y=400)
    bill_var8=IntVar()
    cost_8=pizza8*299
    tot_8ent = Entry(B_win,text="0",textvariable=bill_var8,width=10,font=("Arial",15,"bold"))
    tot_8ent.place(x=500,y=400)
    tot_8ent.delete(0,END)
    tot_8ent.insert(END,cost_8)

    #*************************

    bill_9name = Label(B_win,text="Pepsi 250ml",bg="white smoke",font=("Arial",15,"bold"))
    bill_9name.place(x=120,y=430)
    _x9 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x9.place(x=340,y=430)
    cold_drink1=cd1_var.get()
    bill_9 = Label(B_win,text=cold_drink1,bg="white smoke",font=("Arial",15,"bold"))
    bill_9.place(x=400,y=430)
    _eq9 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq9.place(x=455,y=430)
    bill_var9=IntVar()
    cost_9=cold_drink1*49
    tot_9ent = Entry(B_win,text="0",textvariable=bill_var9,width=10,font=("Arial",15,"bold"))
    tot_9ent.place(x=500,y=430)
    tot_9ent.delete(0,END)
    tot_9ent.insert(END,cost_9)

    #*************************

    bill_10name = Label(B_win,text="7-UP 250ml",bg="white smoke",font=("Arial",15,"bold"))
    bill_10name.place(x=120,y=460)
    _x10 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x10.place(x=340,y=460)
    cold_drink2=cd2_var.get()
    bill_10 = Label(B_win,text=cold_drink2,bg="white smoke",font=("Arial",15,"bold"))
    bill_10.place(x=400,y=460)
    _eq10 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq10.place(x=455,y=460)
    bill_var10=IntVar()
    cost_10=cold_drink2*49
    tot_10ent = Entry(B_win,text="0",textvariable=bill_var10,width=10,font=("Arial",15,"bold"))
    tot_10ent.place(x=500,y=460)
    tot_10ent.delete(0,END)
    tot_10ent.insert(END,cost_10)

    #*************************

    bill_11name = Label(B_win,text="Mirinda 250ml",bg="white smoke",font=("Arial",15,"bold"))
    bill_11name.place(x=120,y=490)
    _x11 = Label(B_win,text="x",bg="white smoke",font=("Arial",15,"bold"))
    _x11.place(x=340,y=490)
    cold_drink3=cd3_var.get()
    bill_11 = Label(B_win,text=cold_drink3,bg="white smoke",font=("Arial",15,"bold"))
    bill_11.place(x=400,y=490)
    _eq11 = Label(B_win,text="=",bg="white smoke",font=("Arial",15,"bold"))
    _eq11.place(x=455,y=490)
    bill_var11=IntVar()
    cost_11=cold_drink2*49
    tot_11ent = Entry(B_win,text="0",textvariable=bill_var11,width=10,font=("Arial",15,"bold"))
    tot_11ent.place(x=500,y=490)
    tot_11ent.delete(0,END)
    tot_11ent.insert(END,cost_11)

    #*************************

    _eqtotal = Label(B_win,text="Total",bg="white smoke",font=("Arial",15,"bold"))
    _eqtotal.place(x=440,y=540)
    bill_var12=IntVar()
    total_cost=cost_1 + cost_2 + cost_3 + cost_4 + cost_5 + cost_6 + cost_7 + cost_8 + cost_9 + cost_10 + cost_11
    tot_ent = Entry(B_win,textvariable=bill_var12,width=10,font=("Arial",15,"bold"))
    tot_ent.place(x=500,y=540)
    #tot_ent.delete(0,END)
    tot_ent.insert(END,total_cost)
    
    #****************
    def done():
        B_win.destroy()
       
    done = Button(B_win,text="Exit",font=("Arial",20,"bold"),command=done)
    done.pack(side=BOTTOM)
    
    #*****************

    
    user_name = name_var.get()
    mobile_no = mobile_var.get()
    order_cost= tot_ent.get()
    
    sql="INSERT INTO order_details(username,mobileno,ord_cost) VALUES (%s,%s,%s)"
    b=(user_name,mobile_no,order_cost)
    cursor.execute(sql,b)
    conn.commit()
    #***********



    
    B_win.mainloop()

    
    
   
##################################################################################################################################################################
photo_title=PhotoImage(file = './Images/title.png')
titleimg_label=Label(P_win,image=photo_title,bg='khaki1',compound=TOP,borderwidth=1)
titleimg_label.place(x = 20, y = 10)
title_label=Label(P_win,text="PIZZA PLANET",bg='khaki1',fg='lightgoldenrod4',font="Arial  40 italic")
title_label.place(x = 225, y = 40)
title_label=Label(P_win,text="GRAB A BITE TODAY...",bg='khaki1',fg='lightgoldenrod4',font="Arial  15 italic")
title_label.place(x = 225, y = 95)

##################################################################################################################################################################
photo_dnt=PhotoImage(file = './Images/date&time.png')
timeimg_label=Label(P_win,image=photo_dnt,compound=TOP,bg='khaki1',borderwidth=1)
timeimg_label.place(x = 20, y = 130)
time_label=Label(P_win,text="DATE & TIME:",bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
time_label.place(x = 100, y = 140)
time_entry=Entry(P_win,textvar="",font='Arial 15',width=24)
time_entry.place(x = 100, y= 170)
now = datetime.datetime.now()
time_entry.insert(0,now)

photo_name=PhotoImage(file = './Images/name.png')
nameimg_label=Label(P_win,image=photo_name,compound=TOP,bg='khaki1',borderwidth=1)
nameimg_label.place(x = 420, y = 130)
name_label=Label(P_win,text="NAME:",bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
name_label.place(x = 500, y = 140)
name_entry=Entry(P_win,textvar=name_var,font='Arial 15',width=15)
name_entry.place(x = 500, y= 170)

photo_phone=PhotoImage(file = './Images/phone.png')
phoneimg_label=Label(P_win,image=photo_phone,compound=TOP,bg='khaki1',borderwidth=1)
phoneimg_label.place(x = 720, y = 130)
mobile_label=Label(P_win,text="MOBILE No.:",bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
mobile_label.place(x = 800, y = 140)
mobile_entry=Entry(P_win,textvar=mobile_var,font='Arial 15',width=15)
mobile_entry.place(x = 800, y= 170)

##################################################################################################################################################################
photo_pizza=PhotoImage(file = './Images/pizza.png')
pizzaimg_label=Label(P_win,image=photo_pizza,compound=TOP,borderwidth=1)
pizzaimg_label.place(x = 40, y = 215)
Pizza_label=Label(P_win,text='PIZZA',bg='khaki1',fg='darkgoldenrod4',font='Arial 25')
Pizza_label.place(x = 100,y = 225)

photo_drinks=PhotoImage(file = './Images/drinks.png')
drinksimg_label=Label(P_win,image=photo_drinks,compound=TOP,borderwidth=1)
drinksimg_label.place(x = 660, y = 215)
Drinks_label=Label(P_win,text='DRINKS',bg='khaki1',fg='darkgoldenrod4',font='Arial 25')
Drinks_label.place(x = 720,y = 225)

##################################################################################################################################################################
photo1=PhotoImage(file = './Images/veg-italiano.png')
P_b1=Button(P_win,image=photo1,compound=TOP,borderwidth=1,command=p1_quantity)
P_b1.place(x = 40, y = 280)
P_l1=Label(P_win,text='Veggie Italiano \n Rs.199/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l1.place(x = 180, y = 280)
P_lq1=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq1.place(x = 178, y = 330)
P_e1=Entry(P_win,textvar=p1_var,width=8,font='Arial 10 ')
P_e1.place(x = 232, y = 337)

photo2=PhotoImage(file = './Images/classic-corn.png')
P_b2=Button(P_win,image=photo2,compound=TOP,borderwidth=1,command=p2_quantity)
P_b2.place(x = 40, y = 400)
P_l2=Label(P_win,text='Classic Corn\nRs.209/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l2.place(x = 180, y = 400)
P_lq2=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq2.place(x = 178, y = 450)
P_e2=Entry(P_win,textvar=p2_var,width=8,font='Arial 10 ')
P_e2.place(x = 232, y = 457)

photo3=PhotoImage(file = './Images/soya-masala.png')
P_b3=Button(P_win,image=photo3,compound=TOP,borderwidth=1,command=p3_quantity)
P_b3.place(x = 40, y = 520)
P_l3=Label(P_win,text='Soya Masala\nRs.229/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l3.place(x = 180, y = 520)
P_lq3=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq3.place(x = 178, y = 570)
P_e3=Entry(P_win,textvar=p3_var,width=8,font='Arial 10 ')
P_e3.place(x = 232, y = 577)                      

photo4=PhotoImage(file = './Images/paneer-masala.png')
P_b4=Button(P_win,image=photo4,compound=TOP,borderwidth=1,command=p4_quantity)
P_b4.place(x = 40, y = 640)
P_l4=Label(P_win,text='Paneer Masala\nRs.249/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l4.place(x = 180, y = 640)
P_lq4=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq4.place(x = 178, y = 690)
P_e4=Entry(P_win,textvar=p4_var,width=8,font='Arial 10 ')
P_e4.place(x = 232, y = 697)

photo5=PhotoImage(file = './Images/chicken-italiano.png')
P_b5=Button(P_win,image=photo5,compound=TOP,borderwidth=1,command=p5_quantity)
P_b5.place(x = 340, y = 280)
P_l5=Label(P_win,text='Chicken Italiano\nRs.259/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l5.place(x = 480, y = 280)
P_lq5=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq5.place(x = 478, y = 330)
P_e5=Entry(P_win,textvar=p5_var,width=8,font='Arial 10 ')
P_e5.place(x = 532, y = 337)

photo6=PhotoImage(file = './Images/chicken-sausage.png')
P_b6=Button(P_win,image=photo6,compound=TOP,borderwidth=1,command=p6_quantity)
P_b6.place(x = 340, y = 400)
P_l6=Label(P_win,text='Chicken Sausage\nRs.259/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l6.place(x = 473, y = 400)
P_lq6=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq6.place(x = 478, y = 450)
P_e6=Entry(P_win,textvar=p6_var,width=8,font='Arial 10 ')
P_e6.place(x = 532, y = 457)


photo7=PhotoImage(file = './Images/lebanese-chicken.png')
P_b7=Button(P_win,image=photo7,compound=TOP,borderwidth=1,command=p7_quantity)
P_b7.place(x = 340, y = 520)
P_l7=Label(P_win,text='Lebanese Chicken\nRs.289/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l7.place(x = 473, y = 520)
P_lq7=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq7.place(x = 478, y = 570)
P_e7=Entry(P_win,textvar=p7_var,width=8,font='Arial 10 ')
P_e7.place(x = 532, y = 577)

photo8=PhotoImage(file = './Images/chicken-supreme.png')
P_b8=Button(P_win,image=photo8,compound=TOP,borderwidth=1,command=p8_quantity)
P_b8.place(x = 340, y = 640)
P_l8=Label(P_win,text='Chicken Supreme\nRs.299/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_l8.place(x = 473, y = 640)
P_lq8=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
P_lq8.place(x = 478, y = 690)
P_e8=Entry(P_win,textvar=p8_var,width=8,font='Arial 10 ')
P_e8.place(x = 532, y = 697)

photo9=PhotoImage(file = './Images/pepsi.png')
CD_b1=Button(P_win,image=photo9,compound=TOP,borderwidth=1,command=cd1_quantity)
CD_b1.place(x = 660, y = 280)
CD_l1=Label(P_win,text='Pepsi 250ml\nRs.49/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_l1.place(x = 810, y = 280)
CD_lq1=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_lq1.place(x = 808, y = 330)
CD_e1=Entry(P_win,textvar=cd1_var,width=8,font='Arial 10 ')
CD_e1.place(x = 862, y = 337)

photo10=PhotoImage(file = './Images/7-up.png')
CD_b2=Button(P_win,image=photo10,compound=TOP,borderwidth=1,command=cd2_quantity)
CD_b2.place(x = 660, y = 400)
CD_l2=Label(P_win,text='7-UP 250ml\nRs.49/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_l2.place(x = 810, y = 400)
CD_lq2=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_lq2.place(x = 808, y = 450)
CD_e2=Entry(P_win,textvar=cd2_var,width=8,font='Arial 10 ')
CD_e2.place(x = 862, y = 457)

photo11=PhotoImage(file = './Images/mirinda.png')
CD_b3=Button(P_win,image=photo11,compound=TOP,borderwidth=1,command=cd3_quantity)
CD_b3.place(x = 660, y = 520)
CD_l3=Label(P_win,text='Mirinda 250ml\nRs.49/-',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_l3.place(x = 810, y = 520)
CD_lq3=Label(P_win,text='Qty. :',bg='khaki1',fg='darkgoldenrod4',font='Arial 15')
CD_lq3.place(x = 808, y = 570)
CD_e3=Entry(P_win,textvar=cd3_var,width=8,font='Arial 10 ')
CD_e3.place(x = 862, y = 577)

##################################################################################################################################################################


Total_button=Button(P_win,text='TOTAL PRICE',bg='khaki3',fg='white',activebackground='khaki2',activeforeground='darkgoldenrod4',font='Arial 16',command=total_price)
Total_button.place(x = 960,y = 320)

Total_entry=Entry(P_win,textvar=total_var,font='Arial 20',width=10)
Total_entry.place(x = 1120,y = 325)

Order_button=Button(P_win,text='    ORDER    ',bg='khaki3',fg='white',activebackground='khaki2',activeforeground='darkgoldenrod4',font='Arial 17 ',command=order_window)
Order_button.place(x = 960,y = 420)

Clear_button=Button(P_win,text='    CLEAR      ',bg='khaki3',fg='white',activebackground='khaki2',activeforeground='darkgoldenrod4',font='Arial 17',command=clear)
Clear_button.place(x = 960,y = 520)

##################################################################################################################################################################
P_win.mainloop()
