import pandas as pd
import service as sr
import pystyle
import colorama


def custom_service(total,tax,grand_total, cost,ordered):
    data = {
        "Order":ordered,
        "Price":[f"${costs}" for costs in cost]
    }
    df = pd.DataFrame(data)
    newd = pd.concat([df,pd.DataFrame({
        "Order":[""],
        "Price":[""]
    })])
    vari = pd.DataFrame({
        "Order":["Total","Tax","Grad Total"],
        "Price":[f"${total}" ,f"${tax}",f"${grand_total}"]
    })
   
    newc = pd.concat([newd,vari])
    newc.to_excel(f"{name}.xlsx",index=False)
    print(f"Thanks Mr/Mrs:{name}")

print(colorama.Fore.BLUE+pystyle.Box.Lines("Welcome Hilaac Restaurant"))
while True:
    name = input(colorama.Fore.YELLOW+"Please enter your name: ")
    if  name.isdigit():
        print(colorama.Fore.RED+"This name is no valid")
    else:
        print("")
        break
    
def restaurant_order():
    file = pd.read_excel("Hilaac Restaurant.xlsx")
    print(file.to_string(index=False))
    order = input(colorama.Fore.YELLOW+f"Mr/Mrs:{name} what would you like (1-5):")
    print("")

    if order == "1":
        sr.break_fast(name)
        
    elif order == "2":
        sr.lunch_and_dinner(name)
        
    elif order == "3":
        sr.drinks(name)
        
    elif order == "4":
        sr.fast_food_and_desserts(name)
        
    elif order == "5":
        print(colorama.Fore.YELLOW+f"Mr/Mrs:{name} thank you")

    else:
        print(colorama.Fore.RED+f"Sorry! Mr/Mrs:{name} we don't serve that")
    
restaurant_order()

while True:
    print("")
    print("would you like anything else ")
    to_menu = input("\n1. Yes \n2. No \n: ")
    if to_menu == "1":
        restaurant_order()

    elif to_menu == "2":
        break

sr.money_paid(name)
custom_service(sr.total, sr.tax, sr.grand_total, sr.cost, sr.ordered)

