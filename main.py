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

food_frame = tkinter.LabelFrame(left_frame, text='Food', bd=5, relief=tkinter.RIDGE)
food_frame.config(bg=LEVEL_2,font=('Arial',13,'bold'))
food_frame.pack(side=tkinter.LEFT)

drinks_frame = tkinter.LabelFrame(left_frame, text='Drinks', bd=10, relief=tkinter.RIDGE)
drinks_frame.config(bg=LEVEL_2,font=('Arial',13,'bold'))
drinks_frame.pack(side=tkinter.LEFT)

cakes_frame = tkinter.LabelFrame(left_frame, text='Cakes', bd=10, relief=tkinter.RIDGE)
cakes_frame.pack(side=tkinter.LEFT)

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

e_amala,e_pounded_yam,e_jollof_rice,e_fufu,e_fried_rice,e_pepper_soup,e_yam = [tkinter.StringVar]*7



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
amala_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_amala)
amala_entry.grid(row=0,column=1)

pounded_yam_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
pounded_yam_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_pounded_yam)
pounded_yam_entry.grid(row=1,column=1)

jollof_rice_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
jollof_rice_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_jollof_rice)
jollof_rice_entry.grid(row=2,column=1)

fufu_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
fufu_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_fufu)
fufu_entry.grid(row=3,column=1)

fried_rice_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
fried_rice_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_fried_rice)
fried_rice_entry.grid(row=4,column=1)

pepper_soup_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
pepper_soup_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_pepper_soup)
pepper_soup_entry.grid(row=5,column=1)

yam_entry = tkinter.Entry(food_frame,font=('arial',18,'bold'),bd=7)
yam_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_yam)
yam_entry.grid(row=6,column=1)


e_coke,e_fanta,e_zobo,e_kunu,e_sprite,e_malt,e_tea = [tkinter.StringVar]*7

# Drinks frame items
coke = tkinter.Checkbutton(drinks_frame,text='Coke',font=('Arial',13,'bold'))
coke.config(onvalue=1,offvalue=0,variable=var8,bg=LEVEL_2)
coke.grid(row=0,column=0,sticky=tkinter.W)

fanta = tkinter.Checkbutton(drinks_frame,text='Fanta',font=('Arial',13,'bold'))
fanta.config(onvalue=1,offvalue=0,variable=var9,bg=LEVEL_2)
fanta.grid(row=1,column=0,sticky=tkinter.W)

zobo = tkinter.Checkbutton(drinks_frame,text='Zobo',font=('Arial',13,'bold'))
zobo.config(onvalue=1,offvalue=0,variable=var10,bg=LEVEL_2)
zobo.grid(row=2,column=0,sticky=tkinter.W)

kunu = tkinter.Checkbutton(drinks_frame,text='Kunu',font=('Arial',13,'bold'))
kunu.config(onvalue=1,offvalue=0,variable=var11,bg=LEVEL_2)
kunu.grid(row=3,column=0,sticky=tkinter.W)

sprite = tkinter.Checkbutton(drinks_frame,text='Sprite',font=('Arial',13,'bold'))
sprite.config(onvalue=1,offvalue=0,variable=var12,bg=LEVEL_2)
sprite.grid(row=4,column=0,sticky=tkinter.W)

malt = tkinter.Checkbutton(drinks_frame,text='Maltina',font=('Arial',13,'bold'))
malt.config(onvalue=1,offvalue=0,variable=var13,bg=LEVEL_2)
malt.grid(row=5,column=0,sticky=tkinter.W)

tea = tkinter.Checkbutton(drinks_frame,text='Tea',font=('Arial',13,'bold'))
tea.config(onvalue=1,offvalue=0,variable=var14,bg=LEVEL_2)
tea.grid(row=6,column=0,sticky=tkinter.W)

# Entry Fields
coke_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
coke_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_coke)
coke_entry.grid(row=0,column=1)

fanta_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
fanta_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_fanta)
fanta_entry.grid(row=1,column=1)

zobo_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
zobo_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_zobo)
zobo_entry.grid(row=2,column=1)

kunu_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
kunu_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_kunu)
kunu_entry.grid(row=3,column=1)

sprite_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
sprite_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_sprite)
sprite_entry.grid(row=4,column=1)

malt_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
malt_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_malt)
malt_entry.grid(row=5,column=1)

tea_entry = tkinter.Entry(drinks_frame,font=('arial',18,'bold'),bd=7)
tea_entry.config(width=6, state=tkinter.DISABLED,textvariable=e_tea)
tea_entry.grid(row=6,column=1)




window.mainloop()