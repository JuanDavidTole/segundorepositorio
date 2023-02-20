# Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
def ortografia(c):
    if(c[-1]==chr(225) or c[-1]==chr(233) or c[-1]==chr(237) or c[-1]==chr(243) or c[-1]==chr(250)):
        print('Aguda')
    elif (c[-2]==chr(225) or c[-2]==chr(233) or c[-2]==chr(237) or c[-2]==chr(243) or c[-2]==chr(250)):
        print('Grave')
    elif (c[-3]==chr(225) or c[-3]==chr(233) or c[-3]==chr(237) or c[-3]==chr(243) or c[-3]==chr(250)):
        print('Esdrujula')
    elif (c[-4]==chr(225) or c[-4]==chr(233) or c[-4]==chr(237) or c[-4]==chr(243) or c[-4]==chr(250)):
        print('sobreesdrujula')
    else:
        print('No es ningun tipo de palabra')

ortografia('brujáfdf')