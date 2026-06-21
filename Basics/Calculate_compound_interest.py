Principal = int(input("Enter the Principal amount: "));
rate = int(input("Enter the Rate of interest per annum: "));
time = int(input("Enter the time in years: "));

print(f"The compound interest is {Principal*(1+rate/100)**time - Principal}");