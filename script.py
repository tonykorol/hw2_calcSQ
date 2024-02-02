A =  float(input('Введите число: '))
n = float(input('Введите степень корня: '))
Xk = 0
Xk1 = 2
Xk0 = 0
counter = 0

while round(Xk, 4) != round(Xk1, 4):
  
    Xk = Xk1
    Xk1 = (1/n)*((n-1)*Xk + (A/(Xk**(n-1))))
    counter += 1
    #print(Xk, Xk1)

print('Корень {0} степени из {1} равен {2}'.format(n, A, round(Xk1, 4)))
print('Число итераций: {0}'.format(counter))
