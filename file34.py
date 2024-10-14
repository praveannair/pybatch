customer = [{
    name:"John",
    card:"123456789",
    pin:"1234",
    balance:5000
},
{
    name:"Cathy",
    card:"1235656789",
    pin:"3434",
    balance:5000
}
]

print("*** HDFC ATM ***")

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        amount=int(input("Enter Amount: "))
        balance=balance+amount
        print("You current balance is ",balance)
    elif choice==2:
        amount=int(input("Enter Amount"))
        if balance<amount:
            print("Insufficient Balance")
        else:
            balance=balance-amount
            print("You current balance is ",balance)
    elif choice==3:
        print("You current balance is ",balance)
    elif choice==4:
        break
    else:
        print("Invalid Input")