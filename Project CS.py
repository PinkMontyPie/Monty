import webbrowser as wb

line1 = ("="*60)

print(line1)
print("|%23s Welcome to %23s|"%(" "," "))
print("|%21s BU Apple Store %21s|"%(" "," "))
print(line1)

def login():    
    condition = "N"
    print("|%18sPlease Select the menu%18s|"%(" "," "))
    print("|%23s1 = Login%26s|"%(" "," "))
    print("|%23s2 = Register%23s|"%(" "," "))
    print(line1)
    while True:    
        reg = input("Please Choose menu (1-2) : ")
        if reg == "1":
            print(line1)
            print("|%26sLogin%27s|"%(" "," "))
            print(line1)
            print("Please Enter your Username & Password")
            user = input("AppleID : ")
            passw = input("Password : ")
            f = open("users.txt", "r")
            for line in f.readlines():
                us, pw = line.strip().split("|")
                if (user == us) and (passw == pw):
                    print(line1)
                    print("Login successful!")
                    menu()
                    return False
            print(line1)
            print("Wrong username/password")
            print("Please try again")
            print(line1)
            print("|%18sPlease Select the menu%18s|"%(" "," "))
            print("|%23s1 = Login%26s|"%(" "," "))
            print("|%23s2 = Register%23s|"%(" "," "))
            print(line1)
        elif reg == "2":
            print(line1)
            print("|%25sRegister%25s|"%(" "," "))
            print(line1)
            with open("users.txt", "r") as file:
                data = file.read().splitlines()
                dataItem = [i.split("|") for i in data]
            while True:
                if condition == "N": 
                    user = input("Create your AppleID : ")
                    for i in dataItem:
                        for x in i:
                            if x == user :
                                print("Please try again")
                                user = input("Create your AppleID : ")
                            else:
                                condition = "Y"
                else:
                    passw = input("Create your Password : ")

                    with open("users.txt","a") as usera:
                        usera.write("\n%s|%s"%(str(user),str(passw)))
                    print(line1)
                    print("|%19sRegister successful!%19s|"%(" "," "))
                    menu()
                    return False
        else:
            print("Invalid menu")
            
def menu():
    
    allqty = []
    allproduct = []
    allprice = []
    
    def add (menu_name,amount,price,):
        price = amount * price
        allprice.append(price)
        allproduct.append(menu_name)
        allqty.append(amount)

    def con (prod,amount,price):
        print(" ")
        print("Please confirm your order")
        print(" ")
        print("Your order is : x%s %s"%(amount,prod))
        print(" ")
        print("Add to cart?")
        while True:
            decis = input("Yes OR No : ")
            if decis.upper() == "YES":
                add(prod,amount,price,)
                break
            elif decis.upper() == "NO":
                print(" ")
                print("Please order again")
                break
            else :
                print("Invalid Code! Please try again.")

    def View (linkd):
        print(" ")
        print("Do you want to see specs from websites?")
        while True:
            weba = input("Yes OR No : ")
            if weba.upper() == "YES":
                wb.open(linkd)
                print(" ")
                break
            elif weba.upper() == "NO":
                print(" ")
                break
            else :
                print("Invalid Code! Please try again.")

    def printmenu():
        print(line1)
        print("|%15s>> Please Choose Product <<%16s|"%(" "," "))
        print(line1)
        print("|            Mac              |            iPad            |")
        print("|           > 1 <             |            > 2 <           |")
        print(line1)
        print("Shopping cart = 3")
        print("Exit = 4")
        print(line1)

    def mac():      
        print(line1)
        print("|%27s Mac %26s|"%(" "," "))
        print(line1)
        print("|       Macbook Air = 1      |       Macbook Pro = 2       |")
        print("|                  back to main menu = 3                   |")
        while True:
            print(line1)
            print(" ")    
            choose = input("Please select Product (1-3) : ")
            if choose == "1":
                print(" ")
                print(line1)
                print("|%23s Macbook Air %22s|"%(" "," "))
                print(line1)
                View("https://www.apple.com/th/macbook-air/specs/")
                print(line1) 
                print("|%12s What Specs/Capacity do you want? %12s|"%(" "," "))
                print(line1)   
                print("|        M1|256GB = 1        |         M1|512GB = 2        |")
                print("|        29,600 bath         |         38,100 bath         |")
                print(line1)
                print(" ")
                air = input("Please select Specs (1-2) : ")
                if air == "1":
                    print(" ")
                    amount = int(input("How many do you want? : "))
                    con("Macbook Air M1 256GB",amount,29600,)
                elif air == "2":
                    print(" ")
                    amount = int(input("How many do you want? : "))
                    con("Macbook Air M1 512GB",amount,38100)
                print(" ")
                print(line1)
                print("|%15s>> Please Choose model <<%16s|"%(" "," "))
                print(line1)
                print("|       Macbook Air = 1      |       Macbook Pro = 2       |")
                print("|                  back to main menu = 3                   |")
            elif choose == "2":
                print(" ")    
                print(line1)
                print("|%23s Macbook Pro %22s|"%(" "," "))
                print("|%22s Display inch %22s|"%(" "," "))
                print(line1) 
                print("|13 inch| = 1")
                print("|14 inch| = 2")
                print("|16 inch| = 3")
                print(line1)
                print(" ")
                pro = input("Please select Inch (1-3) : ")
                if pro == "1":
                    View("https://www.apple.com/th/macbook-pro-13/specs/")
                    print(line1)
                    print("|%12s What Specs/Capacity do you want? %12s|"%(" "," "))
                    print(line1)
                    print("|        M1|256GB = 1        |         M1|512GB = 2        |")
                    print("|        39,600 bath         |         46,600 bath         |")
                    print(line1)
                    print(" ")
                    pro1 = input("Please select Specs (1-2) : ")
                    if pro1 == "1":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 13 inch M1 256GB",amount,39600)
                    elif pro1 == "2":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 13 inch M1 512GB",amount,46600)
                elif pro == "2":
                    View("https://www.apple.com/th/macbook-pro-14-and-16/specs/")
                    print(line1)
                    print("|%12s What Specs/Capacity do you want? %12s|"%(" "," "))
                    print(line1)
                    print("|       M1Pro|512GB = 1      |         M1Pro|1TB = 2       |")
                    print("|       68,700 bath          |         82,900 bath         |")
                    print(line1)
                    print(" ")
                    pro2 = input("Please select Specs (1-2) : ")
                    if pro2 == "1":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 14 inch M1Pro 512GB",amount,68700)
                    elif pro2 == "2":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 14 inch M1Pro 1TB",amount,82900)
                elif pro == "3":
                    View("https://www.apple.com/th/macbook-pro-14-and-16/specs/")
                    print(line1)
                    print("|%12s What Specs/Capacity do you want? %12s|"%(" "," "))
                    print(line1)
                    print("|   M1Pro|512GB = 1  |  M1Pro|1TB = 2   |  M1Max|1TB = 3   |")
                    print("|   82,900 bath      |  89,900 bath     |  114,400 bath    | ")
                    print(line1)
                    print(" ")  
                    pro3 = input("Please select Specs (1-3) : ")
                    if pro3 == "1":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 16 inch M1Pro 512GB",amount,82900)
                    elif pro3 == "2":
                        print(" ")
                        amount = int(input("How many do you want?: "))
                        con("Macbook Pro 16 inch M1Pro 1TB",amount,89900)
                    elif pro3 == "3":
                        print(" ")
                        amount = int(input("How many do you want? : "))
                        con("Macbook Pro 16 inch M1Max 1TB",amount,114400)
                print(" ")
                print(line1)
                print("|%15s>> Please Choose model <<%16s|"%(" "," "))
                print(line1)
                print("|       Macbook Air = 1      |       Macbook Pro = 2       |")
                print("|                  back to main menu = 3                   |")
            elif choose == "3":
                print(line1)
                print("|%15s>> Please Choose model <<%16s|"%(" "," "))
                print(line1)
                print("|            Mac              |            iPad            |")
                print("|           > 1 <             |            > 2 <           |")
                print(line1)
                print("Shopping cart = 3")
                print("Exit = 4")
                print(line1)
                break
            else :
                    print("Invalid Code! Please try again.")

    def ipad():
        print(line1)
        print("|%26s iPad %26s|"%(" "," "))
        print(line1)
        print("|%15s>> Please Choose model <<%16s|"%(" "," "))
        print(line1)
        print("|         iPad = 1         |          iPad Air = 2         |")
        print("|                  back to main menu = 3                   |")
        while True:
            print(line1)
            print(" ")
            choose = input("Please select Product (1-3) : ")
            if choose == "1":
                print(" ")    
                print(line1)
                print("|%25s iPad %27s|"%(" "," "))
                print("|%25s Color %26s|"%(" "," "))
                print(line1)
                print("|Silver| = 1")
                print("|Space Gray| = 2")
                print(line1)
                print(" ")
                ipad1 = input("Please select Color (1-2) : ")
                print(line1)
                print(" ")
                View("https://www.apple.com/th/ipad-10.2/specs/")
                if ipad1== "1":
                    print(" ")
                    print(line1)
                    print("|%24s Capacity %24s|"%(" "," "))
                    print(line1)
                    print("|         64GB = 1           |          256GB = 2          |")
                    print(line1)
                    print(" ")
                    ipad2 = input("Please select Capacity (1-2) : ")
                    if ipad2 == "1":
                        print(" ")
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1            |       Wifi+Cellular = 2     |")
                        print("|        10,700 bath         |       15,400 bath           |")
                        print(line1)
                        ipadw = input("Please select Specs (1-2) : ")
                        if ipadw == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi 64GB",amount,10700)
                        elif ipadw == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi+Cellular 64GB",amount,15400)
                    elif ipad2 == "2":
                        print(" ")
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        15,900 bath      |        20,600 bath             |")
                        print(line1)
                        print(" ")
                        ipadc = input("Please select Specs (1-2) : ")
                        if ipadc == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi 256GB",amount,15900)
                        elif ipadc == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi+Cellular 256GB",amount,20600)
                elif ipad1 == "2":
                    print(" ")
                    print(line1)
                    print("|%24s Capacity %24s|"%(" "," "))
                    print(line1)
                    print("|         64GB = 1           |          256GB = 2          |")
                    print(line1)
                    print(" ")
                    ipad2 = input("Please select Capacity (1-2) : ")
                    if ipad2 == "1":
                        print(" ")
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        10,700 bath      |        15,400 bath             |")
                        print(line1)
                        print(" ")
                        ipadw = input("Please select Specs (1-2) : ")
                        if ipadw == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Space Gray Wifi|64GB",amount,10700)
                        elif ipadw == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Space Gray Wifi+Cellular 64GB",amount,15400)
                    elif ipad2 == "1":
                        print(" ")
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        15,900 bath      |        20,600 bath             |")
                        print(line1)
                        print(" ")
                        ipadc = input("Please select Specs (1-2) : ")
                        if ipadc == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi 256GB",amount,15900)
                        elif ipadc == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad Silver Wifi+Cellular 256GB",amount,20600)
                print(line1)
                print("|%15s>> Please Choose model <<%16s|"%(" "," "))
                print(line1)
                print("|         iPad = 1         |          iPad Air = 2         |")
                print("|                  back to main menu = 3                   |")
            elif choose == "2":
                print(" ")    
                print(line1)
                print("|%24s iPad air %24s|"%(" "," "))
                print(line1)
                print("|Silver| = 1")
                print("|Space Gray| = 2")
                ipad1 = input("Please select Inch (1-2) : ")
                print(line1)
                print(" ")
                View("https://www.apple.com/th/ipad-air/specs/")
                print(" ")
                print(line1)
                if ipad1== "1":
                    print("|%24s Capacity %24s|"%(" "," "))
                    print(line1)
                    print("|          64GB = 1          |          256GB = 2          |")
                    print(line1)
                    print(" ")
                    ipad2 = input("Please select Capacity (1-2) : ")
                    if ipad2 == "1":
                        print(" ")
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        18,300 bath      |        22,800 bath             |")
                        print(line1)
                        print(" ")
                        ipadw = input("Please select Specs (1-2) : ")
                        if ipadw == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Silver Wifi 64GB",amount,18300)
                        elif ipadw == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Silver Wifi+Cellular 64GB",amount,22800)
                    elif ipad2 == "2":
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1        |         Wifi+Cellular = 2       |")
                        print("|        23,300 bath     |         27,800 bath             |")
                        print(line1)
                        print(" ")
                        ipadc = input("Please select Specs (1-2) : ")
                        if ipadc == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Silver Wifi 256GB",amount,23300)
                        elif ipadc == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Silver Wifi+Cellular 256GB",amount,27800)
                elif ipad1== "2":
                    print("|%24s Capacity %24s|"%(" "," "))
                    print(line1)
                    print("|          64GB = 1          |          256GB = 2          |")
                    print(line1)
                    print(" ")
                    ipad2 = input("Please select Capacity (1-2) : ")
                    print(" ")
                    if ipad2 == "1":
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        18,300 bath      |        22,800 bath             |")
                        print(line1)
                        print(" ")
                        ipadw = input("Please select Specs (1-2) : ")
                        if ipadw == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Space Gray Wifi 64GB",amount,18300)
                        elif ipadw == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Space Gray Wifi+Cellular 64GB",amount,22800)
                    elif ipad2 == "2":
                        print(line1)
                        print("|%26s Specs %25s|"%(" "," "))
                        print(line1)
                        print("|        Wifi = 1         |        Wifi+Cellular = 2       |")
                        print("|        23,300 bath      |        27,800 bath             |")
                        print(line1)
                        print(" ")
                        ipadc = input("Please select Specs (1-2) : ")
                        if ipadc == "1":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Space Gray Wifi 256GB",amount,23300)
                        elif ipadc == "2":
                            print(" ")
                            amount = int(input("How many do you want? : "))
                            con("iPad air Space Gray Wifi+Cellular 256GB",amount,27800)
                print(line1)
                print("|%15s>> Please Choose model <<%16s|"%(" "," "))
                print(line1)
                print("|         iPad = 1         |          iPad Air = 2         |")
                print("|                  back to main menu = 3                   |")
            elif choose == "3":
                print(line1)
                print("|%15s>> Please Choose Product <<%16s|"%(" "," "))
                print(line1)
                print("|            Mac              |            iPad            |")
                print("|           > 1 <             |            > 2 <           |")
                print(line1)
                print("Shopping cart = 3")
                print("Exit = 4")
                print(line1)
                break
            else :
                    print("Invalid Code! Please try again.")

    def sc():
        a = sum(allprice)
        if a == 0:
            print(line1)
            print("Your cart is empty")
            print(line1)
        else:
            member = input("BU Member Card (Y/N): ")
            print(" ")
            if member.upper() == 'Y':   
                discount = sum(allprice) * 0.1
            elif member.upper() == 'N': 
                discount = 0
            print(line1)
            print("|%21s Shopping cart %22s|"%(" "," "))
            print(line1)
            for a in range(len(allproduct)):
                print("x%-3s%-45s฿ %s"%(allqty[a],allproduct[a],allprice[a]))
            print(line1)
            print("Summary Price%37s %0.2f"%(" ",sum(allprice)))
            print("Discount (Member Card)%-27s- %-5.2f"%(" ",discount))
            print("Total%-44s฿ %0.2f"%(" ",sum(allprice)-discount))
            print(line1)    
            print(" ")
            print(line1)
            print("Remove item = 1")
            print("Continue = 2")
            print("Back to Shopping cart = 3")
            print(line1)
            print(" ")
            while True:    
                re = input("Please Choose menu (1-3) : ")
                if re == "1":
                    print(" ")
                    del_data = input("Enter item : ")
                    if del_data in allproduct:
                        deleindx = allproduct.index(del_data)
                        allproduct.pop(deleindx)
                        allprice.pop(deleindx)
                        allqty.pop(deleindx)
                        if member.upper() == 'Y':   
                            discount = sum(allprice) * 0.1
                        elif member.upper() == 'N': 
                            discount = 0
                        print(line1)
                        print('Delete Complete')
                        print(line1)
                        print("|%21s Shopping cart %22s|"%(" "," "))
                        print(line1)
                        for a in range(len(allproduct)):
                            print("x%-3s%-45s฿ %s"%(allqty[a],allproduct[a],allprice[a]))
                        print(line1)
                        print("Summary Price%37s %0.2f"%(" ",sum(allprice)))
                        print("Discount (Member Card)%-27s- %-5.2f"%(" ",(discount)))
                        print("Total%-44s฿ %0.2f"%(" ",sum(allprice)-discount))
                        print(line1)
                        print("Remove item = 1")
                        print("Continue = 2")
                        print("Back to Shopping cart = 3")
                        print(line1)
                    else:
                        print("Invalid name !! ")
                elif re == "2":
                    print(" ")
                    add = input("Enter your address : ")
                    print(" ")
                    card = input("Enter your credit or debit Card number: ")
                    print(" ")
                    exp = input("Enter your Exp date card : ")
                    print(" ")
                    vcc = input("Enter your VCC card : ")
                    print(" ")
                    print(line1)
                    print("|%21s Shopping cart %22s|"%(" "," "))
                    print(line1)
                    for a in range(len(allproduct)):
                        print("x%-3s%-45s฿ %s"%(allqty[a],allproduct[a],allprice[a]))
                    print(line1)
                    print("Summary Price%37s %0.2f"%(" ",sum(allprice)))
                    print("Discount (Member Card)%-27s- %-5.2f"%(" ",discount))
                    print("Total%-44s฿ %0.2f"%(" ",sum(allprice)-discount))
                    print(line1)
                    print("Your Address : %s"%(add))
                    print(line1)
                    print("Your credit or debit Card number : %s"%(card))
                    print("Exp %s VCC %s"%(exp,vcc))
                    print(line1)
                    print(" ")
                    print("Order has been place")
                    print(" ")
                    print(line1)
                    print("|%15s>> Please Choose Product <<%16s|"%(" "," "))
                    print(line1)
                    print("|            Mac              |            iPad            |")
                    print("|           > 1 <             |            > 2 <           |")
                    print(line1)
                    print("Shopping cart = 3")
                    print("Exit = 4")
                    print(line1)
                    break
                elif re == "3":
                    printmenu()
                    break
    printmenu()

    while True:
        print(" ")
        choose = input("Please Choose menu (1-4) : ")
        print(" ")
        if choose== "1":    
            mac()
        elif choose== "2":
            ipad()
        elif choose == "3":
            sc()
        elif choose == "4":
            print("Thank you Shopping :)")
            break
        else:
            print("Invalid menu")
            
first = True
if first == True:
    first = login()