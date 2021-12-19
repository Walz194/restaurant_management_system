import tkinter

ROOT = '#A68DAD'
LEVEL_1 = '#DFD3C3'
LEVEL_2 = '#F0ECE3'
LABEL_FRAME = 'red4'
BUTTON = '#A68DAD'

window = tkinter.Tk()
# Setting the shape of the window (widthxheight+x-position+y-position
window.geometry('1270x690+0+0')
window.resizable(width=False, height=False)
window.title('Restaurant Management System')

window.config(bg='#C7B198',pady=20,padx=20)

# *************************     LAYOUT    *********************************#

top_frame = tkinter.Frame(window, bd=10)
top_frame.config(bg=ROOT)
top_frame.pack(side=tkinter.TOP)
# top_frame.grid(row=0,column=0)
# window.grid_columnconfigure(0,weight=1)


title_label = tkinter.Label(top_frame, text='Restaurant Management System', fg='#F0ECE3', bg='#A68DAD')
title_label.config(font=('Arial', 20, 'bold'), width=51)
title_label.grid(row=0, column=0)

# Food Menu Frame
left_frame = tkinter.Frame(window, bd=10, relief=tkinter.RIDGE, bg=LEVEL_1)
left_frame.pack(side=tkinter.LEFT)

cost_frame = tkinter.Frame(left_frame, bd=4, relief=tkinter.RIDGE,bg=LEVEL_2,pady=10)
cost_frame.pack(side=tkinter.BOTTOM)

food_frame = tkinter.LabelFrame(left_frame, text='Food', bd=5, relief=tkinter.RAISED)
food_frame.config(bg=LEVEL_2, font=('Arial', 15, 'bold'), fg=LABEL_FRAME)
food_frame.pack(side=tkinter.LEFT)

drinks_frame = tkinter.LabelFrame(left_frame, text='Drinks', bd=10, relief=tkinter.RIDGE)
drinks_frame.config(bg=LEVEL_2, font=('Arial', 15, 'bold'), fg=LABEL_FRAME)
drinks_frame.pack(side=tkinter.LEFT)

cakes_frame = tkinter.LabelFrame(left_frame, text='Cakes', bd=10, relief=tkinter.RIDGE)
cakes_frame.config(bg=LEVEL_2, font=('Arial', 15, 'bold'), fg=LABEL_FRAME)
cakes_frame.pack(side=tkinter.LEFT)



# Calculator and reciept frame
right_frame = tkinter.Frame(window, bd=10, relief=tkinter.RAISED,bg=LEVEL_1)
right_frame.pack(side=tkinter.RIGHT)

calc_frame = tkinter.Frame(right_frame, bd=1, relief=tkinter.RIDGE,bg=LEVEL_2)
calc_frame.pack(side=tkinter.TOP)

receipt_frame = tkinter.Frame(right_frame, bd=4, relief=tkinter.RIDGE,bg=LEVEL_2)
receipt_frame.pack()

button_frame = tkinter.Frame(right_frame, bd=3, relief=tkinter.RIDGE,bg=LEVEL_2)
button_frame.pack()

# VARIABLES
var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, \
var11, var12, var13, var14, var15, var16, var17, var18, var19, \
var20, var21, var22, var23, var24, var25, var26, var27 = [tkinter.IntVar] * 27

e_amala = tkinter.StringVar()
e_pounded_yam = tkinter.StringVar()
e_jollof_rice = tkinter.StringVar()
e_fufu = tkinter.StringVar()
e_fried_rice = tkinter.StringVar()
e_pepper_soup = tkinter.StringVar()
e_yam = tkinter.StringVar()

e_amala.set('0')
e_pounded_yam.set('0')
e_jollof_rice.set('0')
e_fufu.set('0')
e_fried_rice.set('0')
e_pepper_soup.set('0')
e_yam.set('0')

# food_frame contents
# First Column
amala = tkinter.Checkbutton(food_frame, text='Amala', font=('Arial', 13, 'bold'))
amala.config(onvalue=1, offvalue=0, variable=var1, bg=LEVEL_2)
amala.grid(row=0, column=0, sticky=tkinter.W)

pounded_yam = tkinter.Checkbutton(food_frame, text='Pounded Yam', font=('Arial', 13, 'bold'))
pounded_yam.config(onvalue=1, offvalue=0, variable=var2, bg=LEVEL_2)
pounded_yam.grid(row=1, column=0, sticky=tkinter.W)

jollof_rice = tkinter.Checkbutton(food_frame, text='Jollof Rice', font=('Arial', 13, 'bold'))
jollof_rice.config(onvalue=1, offvalue=0, variable=var3, bg=LEVEL_2)
jollof_rice.grid(row=2, column=0, sticky=tkinter.W)

fufu = tkinter.Checkbutton(food_frame, text='Fufu', font=('Arial', 13, 'bold'))
fufu.config(onvalue=1, offvalue=0, variable=var4, bg=LEVEL_2)
fufu.grid(row=3, column=0, sticky=tkinter.W)

fried_rice = tkinter.Checkbutton(food_frame, text='Fried Rice', font=('Arial', 13, 'bold'))
fried_rice.config(onvalue=1, offvalue=0, variable=var5, bg=LEVEL_2)
fried_rice.grid(row=4, column=0, sticky=tkinter.W)

pepper_soup = tkinter.Checkbutton(food_frame, text='Pepper Soup', font=('Arial', 13, 'bold'))
pepper_soup.config(onvalue=1, offvalue=0, variable=var6, bg=LEVEL_2)
pepper_soup.grid(row=5, column=0, sticky=tkinter.W)

yam = tkinter.Checkbutton(food_frame, text='Yam', font=('Arial', 13, 'bold'))
yam.config(onvalue=1, offvalue=0, variable=var7, bg=LEVEL_2)
yam.grid(row=6, column=0, sticky=tkinter.W)

# Entry Fields
amala_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
amala_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_amala)
amala_entry.grid(row=0, column=1)

pounded_yam_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
pounded_yam_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_pounded_yam)
pounded_yam_entry.grid(row=1, column=1)

jollof_rice_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
jollof_rice_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_jollof_rice)
jollof_rice_entry.grid(row=2, column=1)

fufu_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
fufu_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_fufu)
fufu_entry.grid(row=3, column=1)

fried_rice_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
fried_rice_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_fried_rice)
fried_rice_entry.grid(row=4, column=1)

pepper_soup_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
pepper_soup_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_pepper_soup)
pepper_soup_entry.grid(row=5, column=1)

yam_entry = tkinter.Entry(food_frame, font=('arial', 18, 'bold'), bd=7)
yam_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_yam)
yam_entry.grid(row=6, column=1)


e_coke = tkinter.StringVar()
e_fanta = tkinter.StringVar()
e_zobo = tkinter.StringVar()
e_kunu = tkinter.StringVar()
e_sprite = tkinter.StringVar()
e_malt = tkinter.StringVar()
e_tea = tkinter.StringVar()

e_coke.set('0')
e_fanta.set('0')
e_zobo.set('0')
e_kunu.set('0')
e_sprite.set('0')
e_malt.set('0')
e_tea.set('0')

# Drinks frame items
coke = tkinter.Checkbutton(drinks_frame, text='Coke', font=('Arial', 13, 'bold'))
coke.config(onvalue=1, offvalue=0, variable=var8, bg=LEVEL_2)
coke.grid(row=0, column=0, sticky=tkinter.W)

fanta = tkinter.Checkbutton(drinks_frame, text='Fanta', font=('Arial', 13, 'bold'))
fanta.config(onvalue=1, offvalue=0, variable=var9, bg=LEVEL_2)
fanta.grid(row=1, column=0, sticky=tkinter.W)

zobo = tkinter.Checkbutton(drinks_frame, text='Zobo', font=('Arial', 13, 'bold'))
zobo.config(onvalue=1, offvalue=0, variable=var10, bg=LEVEL_2)
zobo.grid(row=2, column=0, sticky=tkinter.W)

kunu = tkinter.Checkbutton(drinks_frame, text='Kunu', font=('Arial', 13, 'bold'))
kunu.config(onvalue=1, offvalue=0, variable=var11, bg=LEVEL_2)
kunu.grid(row=3, column=0, sticky=tkinter.W)

sprite = tkinter.Checkbutton(drinks_frame, text='Sprite', font=('Arial', 13, 'bold'))
sprite.config(onvalue=1, offvalue=0, variable=var12, bg=LEVEL_2)
sprite.grid(row=4, column=0, sticky=tkinter.W)

malt = tkinter.Checkbutton(drinks_frame, text='Maltina', font=('Arial', 13, 'bold'))
malt.config(onvalue=1, offvalue=0, variable=var13, bg=LEVEL_2)
malt.grid(row=5, column=0, sticky=tkinter.W)

tea = tkinter.Checkbutton(drinks_frame, text='Tea', font=('Arial', 13, 'bold'))
tea.config(onvalue=1, offvalue=0, variable=var14, bg=LEVEL_2)
tea.grid(row=6, column=0, sticky=tkinter.W)

# Entry Fields
coke_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
coke_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_coke)
coke_entry.grid(row=0, column=1)

fanta_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
fanta_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_fanta)
fanta_entry.grid(row=1, column=1)

zobo_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
zobo_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_zobo)
zobo_entry.grid(row=2, column=1)

kunu_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
kunu_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_kunu)
kunu_entry.grid(row=3, column=1)

sprite_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
sprite_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_sprite)
sprite_entry.grid(row=4, column=1)

malt_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
malt_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_malt)
malt_entry.grid(row=5, column=1)

tea_entry = tkinter.Entry(drinks_frame, font=('arial', 18, 'bold'), bd=7)
tea_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_tea)
tea_entry.grid(row=6, column=1)

e_oreo_cake = tkinter.StringVar()
e_apple_cake = tkinter.StringVar()
e_kitkat_cake = tkinter.StringVar()
e_vanilla_cake = tkinter.StringVar()
e_banana_cake = tkinter.StringVar()
e_brownie_cake = tkinter.StringVar()
e_pineapple_cake = tkinter.StringVar()

e_oreo_cake.set('0')
e_apple_cake.set('0')
e_kitkat_cake.set('0')
e_vanilla_cake.set('0')
e_banana_cake.set('0')
e_brownie_cake.set('0')
e_pineapple_cake.set('0')


# Cakes frame items
oreo_cake = tkinter.Checkbutton(cakes_frame, text='Oreo', font=('Arial', 13, 'bold'))
oreo_cake.config(onvalue=1, offvalue=0, variable=var15, bg=LEVEL_2)
oreo_cake.grid(row=0, column=0, sticky=tkinter.W)

apple_cake = tkinter.Checkbutton(cakes_frame, text='Apple', font=('Arial', 13, 'bold'))
apple_cake.config(onvalue=1, offvalue=0, variable=var16, bg=LEVEL_2)
apple_cake.grid(row=1, column=0, sticky=tkinter.W)

kitkat_cake = tkinter.Checkbutton(cakes_frame, text='KitKat', font=('Arial', 13, 'bold'))
kitkat_cake.config(onvalue=1, offvalue=0, variable=var17, bg=LEVEL_2)
kitkat_cake.grid(row=2, column=0, sticky=tkinter.W)

vanilla_cake = tkinter.Checkbutton(cakes_frame, text='Vanilla', font=('Arial', 13, 'bold'))
vanilla_cake.config(onvalue=1, offvalue=0, variable=var18, bg=LEVEL_2)
vanilla_cake.grid(row=3, column=0, sticky=tkinter.W)

banana_cake = tkinter.Checkbutton(cakes_frame, text='Banana', font=('Arial', 13, 'bold'))
banana_cake.config(onvalue=1, offvalue=0, variable=var19, bg=LEVEL_2)
banana_cake.grid(row=4, column=0, sticky=tkinter.W)

brownie_cake = tkinter.Checkbutton(cakes_frame, text='Brownie', font=('Arial', 13, 'bold'))
brownie_cake.config(onvalue=1, offvalue=0, variable=var20, bg=LEVEL_2)
brownie_cake.grid(row=5, column=0, sticky=tkinter.W)

pineapple_cake = tkinter.Checkbutton(cakes_frame, text='Pineapple', font=('Arial', 13, 'bold'))
pineapple_cake.config(onvalue=1, offvalue=0, variable=var21, bg=LEVEL_2)
pineapple_cake.grid(row=6, column=0, sticky=tkinter.W)

# chocolate_cake = tkinter.Checkbutton(cakes_frame, text='Chocolate', font=('Arial', 13, 'bold'))
# chocolate_cake.config(onvalue=1, offvalue=0, variable=var22, bg=LEVEL_2)
# chocolate_cake.grid(row=7, column=0, sticky=tkinter.W)
#
# blackforest_cake = tkinter.Checkbutton(cakes_frame, text='Black Forest', font=('Arial', 13, 'bold'))
# blackforest_cake.config(onvalue=1, offvalue=0, variable=var23, bg=LEVEL_2)
# blackforest_cake.grid(row=8, column=0, sticky=tkinter.W)

# Entry Fields
oreo_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
oreo_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_oreo_cake)
oreo_cake_entry.grid(row=0, column=1)

apple_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
apple_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_apple_cake)
apple_cake_entry.grid(row=1, column=1)

kitkat_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
kitkat_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_kitkat_cake)
kitkat_cake_entry.grid(row=2, column=1)

vanilla_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
vanilla_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_vanilla_cake)
vanilla_cake_entry.grid(row=3, column=1)

banana_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
banana_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_banana_cake)
banana_cake_entry.grid(row=4, column=1)

brownie_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
brownie_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_brownie_cake)
brownie_cake_entry.grid(row=5, column=1)

pineapple_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
pineapple_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_pineapple_cake)
pineapple_cake_entry.grid(row=6, column=1)

# chocolate_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
# chocolate_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_chocolate_cake)
# chocolate_cake_entry.grid(row=7, column=1)
#
# blackforest_cake_entry = tkinter.Entry(cakes_frame, font=('arial', 18, 'bold'), bd=7)
# blackforest_cake_entry.config(width=6, state=tkinter.DISABLED, textvariable=e_blackforest_cake)
# blackforest_cake_entry.grid(row=8, column=1)

# Costlabels entry
e_cost_of_food = tkinter.StringVar()
e_cost_of_drinks = tkinter.StringVar()
e_cost_of_cakes = tkinter.StringVar()
e_subtotal = tkinter.StringVar()
e_servicetax = tkinter.StringVar()
e_totalcost = tkinter.StringVar()

cost_of_food_label = tkinter.Label(cost_frame,text='Cost of Food',font=('Arial',16,'bold'))
cost_of_food_label.config(bg=LEVEL_2)
cost_of_food_label.grid(row=0,column=0)

cost_of_food_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_cost_of_food)
cost_of_food_text.grid(row=0,column=1,padx=40)

cost_of_drinks_label = tkinter.Label(cost_frame,text='Cost of Drinks',font=('Arial',16,'bold'))
cost_of_drinks_label.config(bg=LEVEL_2)
cost_of_drinks_label.grid(row=1,column=0)

cost_of_drinks_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_cost_of_drinks)
cost_of_drinks_text.grid(row=1,column=1,padx=40)


cost_of_cakes_label = tkinter.Label(cost_frame,text='Cost of Cakes',font=('Arial',16,'bold'))
cost_of_cakes_label.config(bg=LEVEL_2)
cost_of_cakes_label.grid(row=2,column=0)

cost_of_cakes_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_cost_of_cakes)
cost_of_cakes_text.grid(row=2,column=1,padx=40)


subtotal_label = tkinter.Label(cost_frame,text='Subtotal',font=('Arial',16,'bold'))
subtotal_label.config(bg=LEVEL_2)
subtotal_label.grid(row=0,column=2)

subtotal_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_subtotal)
subtotal_text.grid(row=0,column=3,padx=40)


servicetax_label = tkinter.Label(cost_frame,text='Service Tax',font=('Arial',16,'bold'))
servicetax_label.config(bg=LEVEL_2)
servicetax_label.grid(row=1,column=2)

servicetax_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_servicetax)
servicetax_text.grid(row=1,column=3,padx=40)

totalcost_label = tkinter.Label(cost_frame,text='Total Cost',font=('Arial',16,'bold'))
totalcost_label.config(bg=LEVEL_2)
totalcost_label.grid(row=2,column=2)

totalcost_text = tkinter.Entry(cost_frame,font=('Arial',13,'bold'),bd=6,width=14,state='readonly',textvariable=e_totalcost)
totalcost_text.grid(row=2,column=3,padx=40)



# Button Frame
total_button = tkinter.Button(button_frame,text='Total',font=('Arial',14,'bold'),fg='white',bg=BUTTON,bd=3)
total_button.grid(row=0,column=0,padx=5)

receipt_button = tkinter.Button(button_frame,text='Receipt',font=('Arial',14,'bold'),fg='white',bg=BUTTON,bd=3)
receipt_button.grid(row=0,column=1,padx=5)

save_button = tkinter.Button(button_frame,text='Save',font=('Arial',14,'bold'),fg='white',bg=BUTTON,bd=3)
save_button.grid(row=0,column=2,padx=5)

send_button = tkinter.Button(button_frame,text='Send',font=('Arial',14,'bold'),fg='white',bg=BUTTON,bd=3)
send_button.grid(row=0,column=3,padx=5)

reset_button = tkinter.Button(button_frame,text='Reset',font=('Arial',14,'bold'),fg='white',bg=BUTTON,bd=3)
reset_button.grid(row=0,column=4,padx=5)

# Textarea for receipt
receipt_text = tkinter.Text(receipt_frame,font=('Arial',12,'bold'),bd=3,width=42,height=13)
receipt_text.grid(row=0,column=0)

# Calculator
calc_field = tkinter.Entry(calc_frame,font=('Arial',13,'bold'),width=32,bd=4)
calc_field.grid(row=0,column=0,columnspan=4)

button7=tkinter.Button(calc_frame,text='7',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button7.grid(row=1,column=0)

button8=tkinter.Button(calc_frame,text='8',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button8.grid(row=1,column=1)

button9=tkinter.Button(calc_frame,text='9',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button9.grid(row=1,column=2)

plus_button=tkinter.Button(calc_frame,text='+',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
plus_button.grid(row=1,column=3)

button4=tkinter.Button(calc_frame,text='4',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button4.grid(row=2,column=0)

button5=tkinter.Button(calc_frame,text='5',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button5.grid(row=2,column=1)

button6=tkinter.Button(calc_frame,text='6',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button6.grid(row=2,column=2)

minus_button=tkinter.Button(calc_frame,text='-',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
minus_button.grid(row=2,column=3)

button1=tkinter.Button(calc_frame,text='1',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button1.grid(row=3,column=0)

button2=tkinter.Button(calc_frame,text='2',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button2.grid(row=3,column=1)

button3=tkinter.Button(calc_frame,text='3',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button3.grid(row=3,column=2)

mult_button=tkinter.Button(calc_frame,text='*',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
mult_button.grid(row=3,column=3)

ans_button=tkinter.Button(calc_frame,text='Ans',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
ans_button.grid(row=4,column=0)

clear_button=tkinter.Button(calc_frame,text='Clear',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
clear_button.grid(row=4,column=1)

button0=tkinter.Button(calc_frame,text='0',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
button0.grid(row=4,column=2)

div_button=tkinter.Button(calc_frame,text='/',font=('Arial',13,'bold'),fg=LEVEL_1,bg=BUTTON,width=6)
div_button.grid(row=4,column=3)




window.mainloop()
