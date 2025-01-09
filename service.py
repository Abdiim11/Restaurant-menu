import pandas as pd
import colorama
colorama.init(autoreset=True)

total = 0
tax = 0
grand_total = 0
money = 0
cost = []
ordered = []

def calculation(price,cust_order):
    global total
    cost.append(price)
    ordered.append(cust_order)
    total+=price

def tax_calculation():
    global total,tax,grand_total
    tax = float(f"{0.05 * total:.2f}")
    grand_total = total + tax
    return grand_total

def money_paid(name):
    global money
    money += float(grand_total)
    print(f"Total is ${grand_total}")
    print(f"*789*670607*{money}# \nEVCPLUS \nMa hubtaa inaad ${money} wax kaga iibsato Hilaac Restaurant \nCASHIER (670607), \nFadlan Geli PIN-kaaga")
    while True:
        pinkaaga = input("")
        if len(pinkaaga) != 4 or not pinkaaga.isdigit():
            print("Pinkaaga waa qalad")
        else:
            print(f"[-EVCPlus-] ${money} ayaad uwareejisey Hilaac Restaurant CASHIER (670607), Tel: \n+252619700793" )
            break
    
def break_fast(name):
    global total
    global grand_total
    file = pd.read_excel("Hilaac Restaurant.xlsx",sheet_name="break fast")
    print(file.to_string(index=False))
    while True:
            service = input(colorama.Fore.YELLOW+"What would you like for break fast (1-5): ")
           
            if service == "1":
                plates=int(input("How many plates would you like: "))
                price = 1.5 * plates
                cust_order=f"{plates} plate(s) of Pancake"
                calculation(price,cust_order)
                tax_calculation()
                
            elif service == "2":
                plates=int(input("How many plates would you like: "))
                price = 1.75 * plates
                cust_order = f"{plates} plate(s) of Bread with soup"
                calculation(price,cust_order)
                tax_calculation()
            
            elif service == "3":
                plates=int(input("How many plates would you like: "))
                price = 1.25 * plates
                cust_order = f"{plates} plate(s) of Bread with Beans"
                calculation(price,cust_order)
                tax_calculation()
            
            elif service == "4":
                plates=int(input("How many plates would you like: "))
                price = 1.5 * plates
                cust_order = f"{plates} plate(s) of Bread with Eggs"
                calculation(price,cust_order)
                tax_calculation()
            
            elif service == "5":
                break
            else:
                print(colorama.Fore.RED+f"Sorry! Mr/Mrs:{name} we don't serve that")
        
def lunch_and_dinner(name):
    global total
    file = pd.read_excel("Hilaac Restaurant.xlsx",sheet_name="lun & din")
    print(file.to_string(index=False))
    while True:
            service = input(colorama.Fore.YELLOW+"What would you like for Lunch and dinner (1-5): ")

            if service == "1":
                plates=int(input("How many plates would you like: "))
                price = 2.5 * plates
                cust_order=f"{plates} plate(s) of Rice with Meat"
                calculation(price,cust_order)
                tax_calculation()

            elif service == "2":
                plates=int(input("How many plates would you like: "))
                price = 3.25 * plates
                cust_order = f"{plates} plate(s) of Rice with steak"
                calculation(price,cust_order)
                tax_calculation()  

            elif service == "3":
                plates=int(input("How many plates would you like: "))
                price = 2.25 * plates
                cust_order = f"{plates} plate(s) of Pasta with meat"
                calculation(price,cust_order)
                tax_calculation()
            
            elif service == "4":
                plates=int(input("How many plates would you like: "))
                price = 1.75 * plates
                cust_order = f"{plates} plate(s) of Pasta with Eggs"
                calculation(price,cust_order)
                tax_calculation() 
            
            elif service == "5":
                break
            else:
                print(colorama.Fore.RED+f"Sorry! Mr/Mrs:{name} we don't serve that")

def drinks(name):
    global total
    file = pd.read_excel("Hilaac Restaurant.xlsx",sheet_name="drinks")
    print(file.to_string(index=False))
    while True:
            service = input(colorama.Fore.YELLOW+"What would you like for Drinks (1-5): ")

            if service == "1":
                plates=int(input("How many cups would you like: "))
                price = 1 * plates
                cust_order=f"{plates} cup(s) of Tea"
                calculation(price,cust_order)
                tax_calculation() 
            
            elif service == "2":
                plates=int(input("How many cups would you like: "))
                price = 1.25 * plates
                cust_order=f"{plates} cup(s) of Coffee"
                calculation(price,cust_order)
                tax_calculation() 
            
            elif service == "3":
                plates=int(input("How many glasses would you like: "))
                price = 2 * plates
                cust_order=f"{plates} glass(es) of Strawberry"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "4":
                plates=int(input("How many glasses would you like: "))
                price = 1.5 * plates
                cust_order=f"{plates} glass(es) of  Mango"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "5":
                break
            else:
                print(colorama.Fore.RED+f"Sorry! Mr/Mrs:{name} we don't serve that")

def fast_food_and_desserts(name):
    global total
    file = pd.read_excel("Hilaac Restaurant.xlsx",sheet_name="f.f & des")
    print(file.to_string(index=False))
    while True:
            service = input(colorama.Fore.YELLOW+"What would you like for fast food an dessert (1-5): ")

            if service =="1":
                plates=int(input("How many Burger would you like: "))
                price = 2.25 * plates
                cust_order=f"{plates} Burger(s)"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "2":
                plates=int(input("How many Shuwerma would you like: "))
                price = 3.25 * plates
                cust_order=f"{plates} Shuwerma(s)"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "3":
                plates=int(input("How many plates would you like: "))
                price = 1.25 * plates
                cust_order=f"{plates} plate(s) of Chips"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "4":
                plates=int(input("How many slices would you like: "))
                price = 1.5 * plates
                cust_order=f"{plates} slice(s) of Cake"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "5":
                plates=int(input("How many Cake would you like: "))
                price = 5.75 * plates
                cust_order=f"{plates} Cake(s)"
                calculation(price,cust_order)
                tax_calculation() 

            elif service == "6":
                break
            else:
                print(colorama.Fore.RED+f"Sorry! Mr/Mrs:{name} we don't serve that")