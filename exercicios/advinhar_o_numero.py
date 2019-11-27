import random

x = random.randint(1,5)

count = True

while count == True:

    Numero01 = input('Adivinhe o numero ')

    if int(Numero01) < x:
        print('Voce errou, o numero e maior')

    elif int(Numero01) > x:
        print('Voce errou o numeor e menor')


    elif int(Numero01) == x:
        print('Voce acertou')
        count = False

#s = n1 + n2

#print('A some {} e {} é igual a {}'.format(n1,n2, s ))
