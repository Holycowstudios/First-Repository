
x=input('Enter hours of work=')
hour=int(x)
print(hour)
y=input('Enter wage rate=')
rate=float(y)
print(rate)
if hour>40 :
    pay=(40*rate)+(hour-40)*(1.5*rate)
    print('pay of the employee is= ')
    print(pay)          
else:
    pay=hour*rate
    print('pay of the employee is= ')
    print(pay)
