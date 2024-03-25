a=int(input("Enter the ticket rice:"))
if a>=250 and a<300:
    print("Recliners")
elif a>=150 and a<200:
    print("Gold")
elif a>=100 and a<150:
    print("Silver")
elif a>=200 and a<250:
    print("Platinum")
else:
    print("Balcony")