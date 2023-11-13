def hello(name):
    line = 'Welcome, ' +name + ', to the world of Python.'


    print(line)
hello('yara')

lst = ['Alan Turing', 'Ken Thompson', 'Vint Cerf']
for name in lst:
    if  name in lst:
     print(name)


def som(getal1,getal2,getal3):
    y= getal1+getal2+getal3
    return (y)

def som(getallen):


    return sum( getallen)

def lang_genoeg(lengte):
    if lengte>=120 :
        return 'je bent lange genoer'
    else:
        return 'helaas niet'
print(lang_genoeg(120))


def new_password(old,new):
    if new != old and len(new)>= 6:
       return True
    else:
        return False
def kwadraten_som(grondgetallen):
    totaal = 0
    for x in grondgetallen:
        if x > 0:
            totaal+= getal ** 2
            return totaal

def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')


def  gemiddelde():
    y=input('voer je zin ')
    h=y.split()
    g=h.count()
    f=len(h)-g
    return f




def hoogvliegers(dict_studenten_cijfers):
    y=[]
    for naam in dict_studenten_cijfers.keys():
        if dict_studenten_cijfers > 0.9:
            y=dict_studenten_cijfers[naam]
            return y


schrijf= int(input('geef je nummer'))




