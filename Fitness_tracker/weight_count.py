from tkinter import *
from tkinter import ttk

def open_wl():
    style= ttk.Style()
    style.theme_use('clam')

    top=Toplevel()
    top.title("Weight loss")
    top.state("zoomed")
    label=Label(top,text="Tips to lose Weight in a Healthy Way:",font=15)
    label.pack(anchor=NW)
    l1=Label(top,text="\n  1.Cardohydrates should make up half of your daily calorie requirement")
    l2=Label(top,text="  2.Your diet should consist of 30 percent of protein")
    l3=Label(top,text="  3.Your diet must consist of 20 percent of healthy fats")
    l4=Label(top,text="  4.Vitamins like A, E, B12, D, calcium and iron\n")

    l1.pack(anchor=NW)
    l2.pack(anchor=NW)
    l3.pack(anchor=NW)
    l4.pack(anchor=NW)
    
    l7=Label(top,text="Diet plan to lose weight:\n",font=20)
    l7.pack(anchor=CENTER)

    tree_frame=Frame(top)
    tree_frame.pack(pady=20)
    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)
    my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

    my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

    my_tree.column("#0", width=20,  minwidth=25)
    my_tree.column("Day",anchor=CENTER,width=30)
    my_tree.column("food_pre_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_pre_lunch",anchor=CENTER, width=150)
    my_tree.column("food_lunch",anchor=CENTER, width=150)
    my_tree.column("food_snacks",anchor=CENTER, width=150)
    my_tree.column("food_dinner",anchor=CENTER, width=300)
    
    my_tree.heading("#0", text='', anchor=CENTER)
    my_tree.heading("Day",text="Day", anchor=CENTER)
    my_tree.heading("food_pre_breakfast",text="Pre Breakfast", anchor=CENTER)
    my_tree.heading("food_breakfast",text='Breakfast', anchor=CENTER)
    my_tree.heading("food_pre_lunch",text='Pre Lunch', anchor=CENTER)
    my_tree.heading("food_lunch",text='Lunch', anchor=CENTER)
    my_tree.heading("food_snacks",text='Snacks', anchor=CENTER)
    my_tree.heading("food_dinner",text='Dinner', anchor=CENTER)

    food=[
        ['1','Cucumber Detox Water','Oats Porridge in Skimmed Milk','Skimmed Milk Panner','Dal,Gajar Matar Sabzi,Roti','Cut Fruits, Buttermilk','Dal,Lauki Sabzi,Roti'],
        ['2','Cucumber Detox Water','Curd, Mixed Vegetable Stuffed Roti','Skim Milk Yoghurt','Lentil Curry,Methi Rice','Apple,buttermillk','Sauteed Vegetables with Paneer,Roti'],
        ['3','Cucumber Detox Water','Skim Milk Yoghurt, Multigrain Toast','Skimmed Milk Panner','Sauteed Vegetables with Paneer,Roti','Banana,Buttermilk','Lentil Curry, Methi Rice'],
        ['4','Cucumber Detox Water','Fruit and Nuts Yogurt Smoothie','Skim Milk Yoghurt','Green Gram Whole Dal Cooked,Bhindi sabzi','Orange, Buttermilk','Palak Chole, Steamed Rice'],
        ['5','Cucumber Detox Water','Skimmed Milk, Peas Poha','Skimmed Milk Panner','Low Fat Paneer Curry, Missi Roti','Papaya, Buttermilk','Curd, Aloo Baingan Tamatar Ki Sabzi'],
        ['6','Cucumber Detox Water','Mixed Sambar, Idli','Skim Milk Yoghurt','Curd, Aloo Baingan Tamatar Ki Sabzi','Cut Fruits, Buttermilk','Green Gram Whole Dal Cooked, Bhindi sabzi'],
        ['7','Cucumber Detox Water','Besan Chilla','Skimmed Milk Panner','Palak Chole, Steamed Rice','Apple, Buttermilk','Low Fat Paneer Curry, Missi Roti']
    ]

    count=0
    for i in food:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        count+=1

    a=7
    my_tree.insert(0,index='end',iid=a,values=('','nearly 0 cal','200cal per serving','215cal per 30g','157cal in 1 1/2 cup','200cal per serving','100cal per 50g'),tags='child')
    my_tree.insert(1,index='end',iid=(a+1),values=('','nearly 0 cal','200cal per serving','137cal in 1 cup','250cal per serving','50 cal per 100 ml','250 cal per serving'),tags='child')
    my_tree.insert(2,index='end',iid=(a+2),values=('','nearly 0 cal','230cal per serving','215cal per 30','200cal per serving','68 cal per 100 ml','350 cal per serving'),tags='child')
    my_tree.insert(3,index='end',iid=(a+3),values=('','nearly 0 cal','200cal per serving','137cal in 1 cup','200cal per serving','57 cal per 100 ml','300 cal per serving'),tags='child')
    my_tree.insert(4,index='end',iid=(a+4),values=('','nearly 0 cal','220cal per serving','215cal per 30','300cal per serving','62 cal per 100 ml','220 cal per serving'),tags='child')
    my_tree.insert(5,index='end',iid=(a+5),values=('','nearly 0 cal','250cal per serving','137cal in 1 cup','220cal per serving','55 cal per 100 ml','250 cal per serving'),tags='child')
    my_tree.insert(6,index='end',iid=(a+6),values=('','nearly 0 cal','150cal per serving','215cal per 30','200cal per serving','50 cal per 100 ml','230 cal per serving'),tags='child')

    my_tree.tag_configure('child',background='#DACEB7' )
    my_tree.pack()
    tree_scroll.config(command=my_tree.yview)

    l8=Label(top,text="your total colorie intake per week = 1500 x 7 cal = 10,500 cal")
    l8.pack(anchor=CENTER)
    top.mainloop()

def open_wg():
    style= ttk.Style()
    style.theme_use('clam')

    top=Toplevel()
    top.state('zoomed')
    top.title("Weight gain")
    root.title('diet plan')
    label=Label(top,text="Tips to Gain Weight in a Healthy Way:",font=15)
    label.pack(anchor=NW)
    l1=Label(top,text="\n  1.High-Calorie Food")
    l2= Label(top,text="  2.Consume Healthy Carbs")
    l3= Label(top,text="  3.Protein Rich Food")
    l4= Label(top,text="  4.Reduce Stress")
    l5= Label(top,text="  5.Strength Training")
    l6= Label(top,text="  6.Get Good Sleep\n")
    l1.pack(anchor=NW)
    l2.pack(anchor=NW)
    l3.pack(anchor=NW)
    l4.pack(anchor=NW)
    l5.pack(anchor=NW)
    l6.pack(anchor=NW)

    l7=Label(top,text="Diet plan for weight gain\n",font=15)
    l7.pack(anchor=CENTER)

    tree_frame=Frame(top)
    tree_frame.pack(pady=20)
    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)
    my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)

    my_tree['columns']=('Day','food_pre_breakfast','food_breakfast','food_pre_lunch','food_lunch','food_snacks', 'food_dinner')

    my_tree.column("#0", width=20,  minwidth=25)
    my_tree.column("Day",anchor=CENTER,width=30)
    my_tree.column("food_pre_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_breakfast",anchor=CENTER, width=150)
    my_tree.column("food_pre_lunch",anchor=CENTER, width=150)
    my_tree.column("food_lunch",anchor=CENTER, width=300)
    my_tree.column("food_snacks",anchor=CENTER, width=150)
    my_tree.column("food_dinner",anchor=CENTER, width=300)
    
    my_tree.heading("#0", text='', anchor=CENTER)
    my_tree.heading("Day",text="Day", anchor=CENTER)
    my_tree.heading("food_pre_breakfast",text="Pre Breakfast", anchor=CENTER)
    my_tree.heading("food_breakfast",text='Breakfast', anchor=CENTER)
    my_tree.heading("food_pre_lunch",text='Pre Lunch', anchor=CENTER)
    my_tree.heading("food_lunch",text='Lunch', anchor=CENTER)
    my_tree.heading("food_snacks",text='Snacks', anchor=CENTER)
    my_tree.heading("food_dinner",text='Dinner', anchor=CENTER)

    food=[
        [1,'Almonds soaked overnight','Oats Banana Pancakes','Coconut water','Multigrain roti along with palak chicken','Bananas','Brown rice, peas paneer curry, sprouts vegetable salad'],
        [2,'Almonds soaked overnight','Oatmeal with Greek Yogurt & Seasonal fruits','Lassi','Multigrain roti, fish curry/vegetable curry','Toast with Jam','Broken wheat khichidi along with egg white'],
        [3,'Almonds soaked overnight','Poached Eggs, Protein Shake','Buttermilk','Quinoa upma, chicken and broccoli salad','Mixed Nuts & Dried Fruits','vegetable curry, brown rice, cucumber raita'],
        [4,'Almonds soaked overnight','Oatmeal with Honey','Coconut water','Grilled Chicken/Salad & Whole Grain Bread','Toast with Peanut Butter','Methi Chicken/Brown Rice, Broccoli, Protein Shake'],
        [5,'Almonds soaked overnight','Scrambled Egg & Smoothie','Lassi','(Grilled chicken) vegetable roti rolls Green Salad','Mixed Nuts & Dried Fruits','Spring Onion, Peppers & Broccoli Chocolate Milk'],
        [6,'Almonds soaked overnight','Oatmeal & Orange Juice','Buttermilk','Black Beans, Peppers & Greek Yogurt','Apple with peanut butter','Sweet Potato Protein Shake'],
        [7,'Almonds soaked overnight','Oatmeal with Nuts Smoothie','Coconut water','Whole wheat (pasta with chicken) and Green Salad','Granola or Cereal','boiled green peas salad with Brown Rice']
    ]

    count=0
    for i in food:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        count+=1
    
    a=7
    my_tree.insert(0,index='end',iid=a,values=('','7cal per almond','71cal per pancake','19cal per 100ml','200cal per serving','105cal','300cal'),tags='child')
    my_tree.insert(1,index='end',iid=(a+1),values=('','7cal per almond','100cal per serving','112cal per 100 ml','200cal per serving','50cal','250cal'),tags='child')
    my_tree.insert(2,index='end',iid=(a+2),values=('','7cal per almond','57cal per egg','20cal per 200 ml','100cal per 250g','50cal per 25g','250cal per serving'),tags='child')
    my_tree.insert(3,index='end',iid=(a+3),values=('','7cal per almond','100cal','19cal per 100ml','250cal per serving','100cal per serving','200cal per 100ml'),tags='child')
    my_tree.insert(4,index='end',iid=(a+4),values=('','7cal per almond','112cal per 100ml','200cal per 100ml','250cal per serving','50cal per 25g','250 cal per 100 ml'),tags='child')
    my_tree.insert(5,index='end',iid=(a+5),values=('','7cal per almond','100cal per serving','19cal per 100ml','100cal per 100g','50cal per 25g','200cal per serving'),tags='child')
    my_tree.insert(6,index='end',iid=(a+6),values=('','7cal per almond','250cal per 100ml','19cal per 100ml','200cal per serving','100cal per 50g','200cal per serving'),tags='child')
    
    my_tree.tag_configure('child',background='#DACEB7' )
    my_tree.pack()
    tree_scroll.config(command=my_tree.yview)
    
    l8=Label(top,text="your total colorie intake per week = 2500 x 7 cal = 17,500 cal")
    l8.pack(anchor=CENTER)
    top.mainloop()

root = Tk()
root.title('diet plan')
root.geometry("200x150")
b1=Button(root, text="Weight loss",width=10,command=open_wl).pack(pady=20)
b2=Button(root, text='Weight gain',width=10,command=open_wg).pack(pady=20)
root.mainloop()
