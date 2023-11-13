maand= int(input('voe je maandnummer in'))
if maand <1 or maand >= 13:
   print('ongeldig')
if maand >= 3 and maand <=5:
     print('lente')
elif maand >= 9 and maand <12:
     print('herfst')

lijst =[ 'maandag','dinsdag','donderdag']
for x in lijst:
    if x in lijst:
       print(x[0:3])

lst=[1,2,3,4,5,6,7,8]
for x in lst:
    if x % 2==0:
        print(x)

s = "Guido van Rossum heeft programmeertaal Python bedacht."

for letter in s:
    if letter in 'aeiou':
        print(letter)

def f(x):
    res = x**2 + 10
    print (res)

def hello(name):
    y='welkom'+ name
    print(y)


