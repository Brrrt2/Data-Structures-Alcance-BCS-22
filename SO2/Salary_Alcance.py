# 1.write a python program that will compute for the bonus using the specifications stated

# T&M Group of Companies gives longevity bonus to its employed based on their number of year of service and their salary using the following conditions
# year of service               Bounus
# 5                              5%
# 10                             100%
# 15                             150%
# 20                             200%

# 2.
salary = int(input("Enter Salary: "))
year = int(input("Year of Service: "))
n = 0

if 5 <= year < 9:
    n = 1
    cons = 1
    bonus = salary * 0.05
    final = bonus + salary
    print("Salary with 5% Bonus :" + str(final))
elif 10 <= year < 14:
    n = 2
    bonus = salary * 0.10
    final = bonus + salary
    print("Salary with 100% Bonus :" + str(final))
elif 15 <= year < 19:
    n = 3
    bonus = salary * 1.5
    final = bonus + salary
    print("Salary with 150% Bonus :" + str(final))
elif year >= 20:
    n = 4
    bonus = salary * 2.0
    final = bonus + salary
    print("Salary with 200% Bonus :" + str(final))
else:
    print("No salary Bonus")

print(f"Runtime: {n}(n)")



