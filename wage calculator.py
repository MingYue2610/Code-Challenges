# Writing a program to provide an employee's weekly wage with regular and overtime pay taken into consideration

pay_hours = float(input("Enter your hour: "))
pay_rate = float(input("Enter your rate: "))
reg_pay = pay_hours * pay_rate
if pay_hours > 40:
    max_base_pay = 40 * pay_rate
    overtime_hours = pay_hours - 40
    overtime_rate = pay_rate * 1.5
    overtime_pay = (overtime_hours * overtime_rate) + max_base_pay
    print(overtime_pay)

else:
    print(reg_pay)
