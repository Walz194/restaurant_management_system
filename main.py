import tkinter

ROOT = '#A68DAD'
LEVEL_1 = '#DFD3C3'
LEVEL_2 = '#F0ECE3'

window = tkinter.Tk()
# Setting the shape of the window (widthxheight+x-position+y-position
window.geometry('1270x690+0+0')
window.resizable(width=False,height=False)
window.title('Restaurant Management System')

window.config(bg='#C7B198')

# *************************     LAYOUT    *********************************#

top_frame = tkinter.Frame(window,bd=10,relief=tkinter.RAISED)
top_frame.config(bg=ROOT)
top_frame.pack(side=tkinter.TOP)
# top_frame.grid(row=0,column=0)
# window.grid_columnconfigure(0,weight=1)


title_label = tkinter.Label(top_frame,text='Restaurant Management System',fg='#F0ECE3',bg='#A68DAD')
title_label.config(font=('Arial',20,'bold'),width=51)
title_label.grid(row=0,column=0)

# Food Menu Frame
left_frame = tkinter.Frame(window, bd=10, relief=tkinter.RIDGE,bg=LEVEL_1)
left_frame.pack(side=tkinter.LEFT)

food_frame = tkinter.LabelFrame(left_frame, text='Food', bd=10, relief=tkinter.RIDGE)
food_frame.config(bg=LEVEL_2)
food_frame.pack(side=tkinter.LEFT)

drinks_frame = tkinter.LabelFrame(left_frame, text='Drinks', bd=10, relief=tkinter.RIDGE)
food_frame.pack(side=tkinter.LEFT)

cakes_frame = tkinter.LabelFrame(left_frame, text='Cakes', bd=10, relief=tkinter.RIDGE)
food_frame.pack(side=tkinter.LEFT)

cost_frame = tkinter.Frame(left_frame, bd=4, relief=tkinter.RIDGE)
cost_frame.pack(side=tkinter.BOTTOM)


# Calculator and reciept frame
right_frame = tkinter.Frame(window, bd=15, relief=tkinter.RAISED)
right_frame.pack(side=tkinter.RIGHT)

calc_frame = tkinter.Frame(right_frame, bd=1,relief=tkinter.RIDGE)
calc_frame.pack(side=tkinter.TOP)

receipt_frame = tkinter.Frame(right_frame,bd=4,relief=tkinter.RIDGE)
receipt_frame.pack()

button_frame = tkinter.Frame(right_frame,bd=3,relief=tkinter.RIDGE)
button_frame.pack()


# VARIABLES
var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,\
var11,var12,var13,var14,var15,var16,var17,var18,var19,\
var20,var21,var22,var23,var24,var25,var26,var27 = [tkinter.IntVar]*27



# food_frame contents
# First Column
amala = tkinter.Checkbutton(food_frame,text='Amala',font=('Arial',13,'bold'))
amala.config(onvalue=1,offvalue=0,variable=var1,bg=LEVEL_2)
amala.grid(row=0,column=0,sticky=tkinter.W)

pounded_yam = tkinter.Checkbutton(food_frame,text='Pounded Yam',font=('Arial',13,'bold'))
pounded_yam.config(onvalue=1,offvalue=0,variable=var2,bg=LEVEL_2)
pounded_yam.grid(row=1,column=0,sticky=tkinter.W)

jollof_rice = tkinter.Checkbutton(food_frame,text='Jollof Rice',font=('Arial',13,'bold'))
jollof_rice.config(onvalue=1,offvalue=0,variable=var3,bg=LEVEL_2)
jollof_rice.grid(row=2,column=0,sticky=tkinter.W)

fufu = tkinter.Checkbutton(food_frame,text='Fufu',font=('Arial',13,'bold'))
fufu.config(onvalue=1,offvalue=0,variable=var4,bg=LEVEL_2)
fufu.grid(row=3,column=0,sticky=tkinter.W)

fried_rice = tkinter.Checkbutton(food_frame,text='Fried Rice',font=('Arial',13,'bold'))
fried_rice.config(onvalue=1,offvalue=0,variable=var5,bg=LEVEL_2)
fried_rice.grid(row=4,column=0,sticky=tkinter.W)

pepper_soup = tkinter.Checkbutton(food_frame,text='Pepper Soup',font=('Arial',13,'bold'))
pepper_soup.config(onvalue=1,offvalue=0,variable=var6,bg=LEVEL_2)
pepper_soup.grid(row=5,column=0,sticky=tkinter.W)

yam = tkinter.Checkbutton(food_frame,text='Yam',font=('Arial',13,'bold'))
yam.config(onvalue=1,offvalue=0,variable=var7,bg=LEVEL_2)
yam.grid(row=6,column=0,sticky=tkinter.W)

# Entry Fields
amala_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
amala_entry.grid(row=0,column=1)




window.mainloop()