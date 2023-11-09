import datetime


LMP = input("The First date of Last Mensuration Period:")
#print(First_date_of_Last_MEN)
#To Calculate Pregnancy Due Date, we need to add 40 weeks from the date of the LMP
LMP = datetime.datetime.strptime(LMP, "%d/%m/%Y")
DueDate = int(input("Enter mensuration cycle:"))
DueDate = datetime.timedelta(days = DueDate)
cycle = int(input("Enter Period Cycle:"))
day=datetime.timedelta(days=cycle)
#DueDate = datetime.timedelta(weeks=52)
#Months=datetime.timedelta(days=3*30)
#day=datetime.timedelta(days=7)
#Due=LMP-Months+DueDate+day
#print("You will concieve on"+Due.strftime('%d/%m/%Y'))
for i in range(0,cycle+1):
    
    Due = LMP + DueDate + datetime.timedelta(days=i)
    print("Your next period on"+Due.strftime('%d/%m/%Y'))




