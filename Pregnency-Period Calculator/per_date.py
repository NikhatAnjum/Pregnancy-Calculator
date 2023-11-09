from datetime import datetime, timedelta

def calculate_dates(lmp_date, cycle_length):
    try:
        # Convert the LMP date to a datetime object
        lmp_date = datetime.strptime(lmp_date, "%Y-%m-%d")

        # Calculate the next period date by adding the cycle length to LMP date
        next_period_date = lmp_date + timedelta(days=cycle_length)

        # Calculate the probable ovulation date (midway through the cycle)
        ovulation_date = lmp_date + timedelta(days=cycle_length // 2)

        return next_period_date.strftime("%Y-%m-%d"), ovulation_date.strftime("%Y-%m-%d")

    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Input LMP date and cycle length from the user
lmp_date = input("Enter your last menstrual period date (YYYY-MM-DD): ")
cycle_length = int(input("Enter your average cycle length (in days): "))

# Calculate and display the next period and ovulation dates
next_period_date, ovulation_date = calculate_dates(lmp_date, cycle_length)
if next_period_date != "Invalid date format. Please use YYYY-MM-DD.":
    print(f"Your next period is expected on {next_period_date}")
    print(f"Your most probable ovulation date is on {ovulation_date}")
else:
    print(next_period_date)
