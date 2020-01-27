#Payroll#
#Name,Gross,Tax,Net#
#gross pay = hours worked x hourly pay rate#
#gross = total#
#tax = percentage taken off the gross#
#tax = static variable#
#name = user input#
#gross shaved off by tax end goal is net pay#
def payroll():

    tax = float(0.2)
    hourly_pay =10
    hours_worked = 0
    pay = hourly_pay * hours_worked

    menu = ""
    name = input('Enter Your name: ')

    while(menu != "q"):
        grosspay = hourly_pay * hours_worked
        net = grosspay * tax
        yourpay = grosspay-net
        menu = input(f"Welcome to the menu {name}: Press 1 to enter hours worked, Press q to quit")
        if (menu == "1"):
            hours_worked = int(input("Enter your hours worked"))
    print(f"Your name is: {name} and you worked {hours_worked} hours for a total gross of {grosspay} and net {yourpay}")

payroll()