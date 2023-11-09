import datetime


LMP = input("The First date of Last Mensuration Period:")
#print(First_date_of_Last_MEN)
#To Calculate Pregnancy Due Date, we need to add 40 weeks from the date of the LMP
LMP = datetime.datetime.strptime(LMP, "%d/%m/%Y")

#DueDate = datetime.timedelta(weeks = 40)
#Due = LMP + DueDate
DueDate = datetime.timedelta(weeks=52)
Months=datetime.timedelta(days=3*30)
day=datetime.timedelta(days=7)
Due=LMP-Months+DueDate+day
print("You will concieve on"+Due.strftime('%d/%m/%Y'))

