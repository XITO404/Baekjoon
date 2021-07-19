a = int(input())

for i in range(a):
    price = float(input())
    print('${:.2f}'.format(round(price*0.8, 2)))
    
