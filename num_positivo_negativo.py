def num(n):
    if n <0:
        print('Negativo')
    elif n>0:
        print('Positivo')
    else:
        print('Neutro')

x=input('Descubra se um número é positivo ou negatico: ')
x=float(x)

print(num(x))