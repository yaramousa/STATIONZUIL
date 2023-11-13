yara= int(input('voe je leeftijd'))
mm=input('heb je paspoort:')
if yara >=18 and  mm== 'ja':
    print('je kan stemmen')
else:
     print('je kan niet nu')



maand= int(input('voe je maandnummer in'))
if maand <1 or maand >= 13:
   print('ongeldig')

