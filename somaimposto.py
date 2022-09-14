def soma_imposto(custo,taxa):
    soma=custo*taxa +custo
    return 'O valor do imposto é ' + str(soma)

c = input('Digite o custo: ')
c = float(c)

t = input('Digite a taxa: ')
t = float(t)

print(soma_imposto(c,t))