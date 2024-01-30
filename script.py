A =  float(input('Введите число: '))
n = float(input('Введите степень корня: '))
Xk = A
Xk1 = 1

while round(Xk, 4) != round(Xk1, 4):
    Xk = Xk1
    Xk1 = (1/n)*((n-1)*Xk + (A/(Xk**(n-1))))

print('Корень {0} степени из {1} равен {2}'.format(n, A, round(Xk1, 4)))
