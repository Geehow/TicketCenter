# Jiahao Yuan
# COP 2500
# Mon Apr 10, 2023
# Final Project- Final.py

def DTS():
    dts = {
    "Medieval Times": {
        "Retail Cost": 70.90,
        "UCF Price": 47.44,
        "Sales Tax": 3.56,      
        "UCF Cost": 51.00,
        "Purchase Limit": 6 }, 
    "Sleuth's Mystery Dinner Show": {
        "Retail Cost": 70.24,
        "UCF Price": 43.19,
        "Sales Tax": 2.81,      
        "UCF Cost": 46.00,
        "Purchase Limit": 6}}
    return dts

def MT():
    mt = {
        "AMC": {
            "Retail Cost": 11.49,
            "UCF Price": 10.00,
            "Sales Tax": 00.00 ,
            "UCF Cost": 10.00,
            "Purchase Limit": 6},
        "Regal": {
            "Retail Cost": 12.08,
            "UCF Price": 10.00,
            "Sales Tax": 00.00 ,
            "UCF Cost": 10.00,
            "Purchase Limit": 6}}
    return mt
            

def TP():
    tp = {
        "Aquatica": {
            "Retail Cost": 42.99,
            "UCF Price": 32.86,
            "Sales Tax": 2.14,
            "UCF Cost": 35.00,
            "Purchase Limit": 4},
        "Busch Gardens": {
            "Retail Cost": 110.20,
            "UCF Price": 69.77,
            "Sales Tax": 5.23,
            "UCF Cost": 75.00,
            "Purchase Limit": 2},
        "Gator Land" : {
            "Retail Cost": 31.94,
            "UCF Price": 18.78,
            "Sales Tax": 1.22,
            "UCF Cost": 20.00,
            "Purchase Limit": 4},
        "Kennedy Space Center": {
            "Retail Cost": 60.71,
            "UCF Price": 25.23,
            "Sales Tax": 1.77,
            "UCF Cost": 27.00,
            "Purchase Limit": 2},
        "Sea World": {
            "Retail Cost": 106.49,
            "UCF Price": 69.48,
            "Sales Tax": 4.52,
            "UCF Cost": 74.00,
            "Purchase Limit": 4},
        "Universal Orlando (1 Day Park to Park)": {
            "Retail Cost": 175.73,
            "UCF Price": 117.37,
            "Sales Tax": 7.63,
            "UCF Cost": 125.00,
            "Purchase Limit": 2},
        "Universal Orlando (1 Day, 1 Park)": {
            "Retail Cost": 117.15,
            "UCF Price": 84.51,
            "Sales Tax": 5.49,
            "UCF Cost": 90.00,
            "Purchase Limit": 2},
        "Universal Orlando (2 Day, 2 Park)": {
            "Retail Cost": 271.56,
            "UCF Price": 145.54,
            "Sales Tax": 9.46,
            "UCF Cost": 155.00,
            "Purchase Limit": 2}}
    return tp

def menu2():
    print ("What tickets would you like to look at?")
    print ("1. Dinner Theater & Shows")
    print ("2. Movie Theater")
    print ("3. Theme Parks")
    print ("4. Exit")
    choice2 = int(input("Enter the number below\n"))
    return choice2

def browse():
    browse_exit = 0
    while (browse_exit !=4):
        browse_exit = menu2()
        if (browse_exit == 1):
            dts= DTS()
            print (dts)
        if (browse_exit == 2):
            mt= MT()
            print(mt)
        if (browse_exit == 3):
            tp= TP()
            print (tp)
        if (browse_exit == 4):
            return

def add_tickets(tickets, DTS, MT, TP):
    ticket = input("What ticket would you like to add?\n")
    if ticket in DTS() or ticket in MT() or ticket in TP():
        num = int(input("How many would you like to buy?\n"))
        cost = 0
        purchase_limit = 0
        if ticket in DTS():
            purchase_limit = DTS()[ticket]["Purchase Limit"]
            ucf_cost = DTS()[ticket]["UCF Cost"]
        elif ticket in MT():
            purchase_limit = MT()[ticket]["Purchase Limit"]
            ucf_cost = MT()[ticket]["UCF Cost"]
        elif ticket in TP():
            purchase_limit = TP()[ticket]["Purchase Limit"]
            ucf_cost = TP()[ticket]["UCF Cost"]
        if num > purchase_limit:
            print ("You can only buy up to " + str(purchase_limit) + " " + ticket + " tickets.")
        else:
            tickets[ticket] = [num, ucf_cost * num]
            print ("Successfully added to cart!")
    else:
        print ("Invalid ticket")
    return tickets

def remove_tickets(tickets):
    remove = input("What ticket would you like to remove?\n")
    if remove in tickets.keys():
        del tickets[remove]
        print ("Successfully removed!")
    else:
        print ("Ticket is not in cart.")
    return tickets

def shopping_cart(tickets):
    print ("Shopping Cart")
    print ("-------------")
    if len(tickets) == 0:
        print ("Your shopping cart is empty")
    else:
        for key in tickets:
            print (key, tickets[key],"\n")

def pay(tickets):
    total = 0
    print ("Checkout")
    print ("--------------------------------")
    if len(tickets) == 0:
        print ("Your shopping cart is empty")
        return
    else:
        for key in tickets:
            num_tickets = tickets[key][0]
            ticket_cost = tickets[key][1]
            print (key, tickets[key])
            total += ticket_cost
        print ("Total cost:", total)
        method = input("How would you like to pay? Cash or Card?\n")
        while (method != "Card"):
            print ("How are you going to pay cash...")
            method = input("How would you like to pay? Cash or Card?\n")
        if (method == "Card"):
            card = input("What is your credit card number?\n")
            card = card.replace(" ","")
            while (len(card) != 16):
                print ("Invalid credit card number.")
                print ("Please try again.")
                card = input("What is your credit card number?\n")
            else:
                cvv = input("What is your CVV?\n")
                while (len(cvv) != 3):
                    print ("Invalid CVV.")
                    cvv = input("What is your CVV?\n")
                else:
                    print ("Thank you for your purchase!")
                    tickets.clear()
                    return tickets
    

def menu():
    print ("Welcome to the UCF Ticket Center!")
    print ("---------------------------------")
    print ("What would you like to do?")
    print ("1. Browse Tickets")
    print ("2. Add Ticket")
    print ("3. Remove Ticket")
    print ("4. Show Shopping Cart")
    print ("5. Pay")
    print ("6. Exit")
    choice = int(input("Enter the number below\n"))
    return choice


def main():
    option = 0
    tickets = {}
    dts = DTS()
    mt = MT()
    tp = TP()
    print ("Welcome to the UCF Ticket Center!")
    print ("---------------------------------")
    student = int(input("What is your UCFID?\n"))
    while len(str(student)) != 7:
        print ("Invalid UCFNID")
        student = int(input("What is your UCFID?\n"))
    else:
        print ("Valid UCFNID") 
    while (option != 6):
        option = menu()
        if (option == 1):
            browse()
        if (option == 2):
            tickets= add_tickets(tickets, DTS, MT, TP)
        if (option == 3):
            tickets = remove_tickets(tickets)
        if (option == 4):
            shopping_cart(tickets)
        if (option == 5):
            pay(tickets)
        if (option == 6):
            print ("Thank you for visiting the UCF Ticket Center!")
            print ("Have a nice day!")

main()
        
        
