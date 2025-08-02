# Compound Interest Calculator

# Take inputs for principal, rate, and time
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (in %): "))
time = float(input("Enter the time period in years:"))

# Calculate compound interest
compound_interest = principal * (1 + rate / 100) ** time - principal

# Calculate the total amount after interest
total_amount = principal + compound_interest

# Display the results
print(f"Total amount after {time} years: {total_amount:.2f}")
print(f"Compound Interest earned: {compound_interest:.2f}")
