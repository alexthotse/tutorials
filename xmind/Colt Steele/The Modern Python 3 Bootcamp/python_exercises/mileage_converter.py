#kilometers = input("How many Kilometers did you run?:  ")
miles = input("How many miles did you cycle today?: ")
kilometers = float(miles) * 1.609269392
kilometers = round(kilometers,2)

miles = float(kilometers) / 1.609269392
miles = round(miles,2)
#print(f"Your {kilometers}km run was {miles}mi")
print(f"Your {miles}mi run was {kilometers}km")
