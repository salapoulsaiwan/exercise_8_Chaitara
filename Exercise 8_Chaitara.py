inU = input("please enter your username :")
inP = input("please enter your password :")

if inU == "sommai" and inP == "pi9897":
    print("________welcome to somjit store_________")
    print("--------1.RTX 9000 = 100000 bath--------")
    print("--------2.AMD 9900xt =99999 bath--------")
    print("--------3.intel i9   =80000 bath--------")
    sel = input("what did you choose :")
    amot = int(input("how many :"))
    if sel == "1":
        print(amot,"รายการ ",amot * 100000)
    elif sel == "2":
        print(amot,"รายการ ",amot * 99999)
    elif sel == "3":
        print(amot,"รายการ ",amot * 80000)    
    