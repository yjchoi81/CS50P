coke = 50

while coke > 0:
    print(f"Amount Due: {coke}")
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin == 25 or inserted_coin  == 10 or inserted_coin  == 5:
        coke -= inserted_coin

if coke == 0 :
    print(f"Change Owed: {coke}")
elif coke <0:
    print(f"Change Owed: {-coke}")






