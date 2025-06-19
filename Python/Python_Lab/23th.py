total_amount=50000
1="deposit"
2="Withdrawl"
deposit=int(input("Enter how much amount you have to deposit"))
withdrawl=int(input("Enter how much amount you have to withdrawl"))
user=input("Enter _1 to Deposit \n Enter _2 to Withdrawl")
if user==1:
    print(deposit,total_amount+deposit)
elif user==2:
    print(withdrawl,total_amount-withdrawl)