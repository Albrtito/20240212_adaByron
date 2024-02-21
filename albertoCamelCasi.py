# Get the one entrie with the most number of upper case and then change every other entrie so that it is like tha one. 

# Evaluate wich entries are actually the same by: 
"""
    1. Difference in lenght
    2. Go letter by letter comparing (mayus and minus are not important in this case.)

"""

def main():
    # String list to contain all variables
    variables = ["something", "someThing", "anotherThing", "someOtherthing", "someOtherThing"]
    for i in range(1000):
        variables.append("SomeThing")
    n = len(variables)
    output = []
    worDic = {}
    print(n)
    # Corner cases: 
    """
        + If n = 0: Output an empty list o directamente los tres guiones
        + If n = 2: Solo hay uno que está bien: El que tenga más uppercase
        + If n = 1: Do nothing. 
    """
    if n == 0: 
        return output
    
    if n == 2: 
        print("n = 2")
        maxcount = 0
        for string in variables:
            count = 0 
            for letter in string:
                if letter.isupper():
                    count += 1

            if count > maxcount: 
                maxcount = count
                goodstring = string
        output = [goodstring,goodstring]
        return output
            
    if n == 1: 
        output = variables
        return output
    
    # General cases: 

    for string in variables:
        mayusCounter = 0
        print(string)

        # If the dictionary no esta vacio podemos comprobar sobre el
        if len(worDic) != 0: 
            # Para cada una de las entradas del diccionario comprobamos si es la misma que la string que tenemos
            for dicString in worDic:
                # Comprobar si son la misma, en el caso de que la sean comprobar cuantas mayusculas tiene la string
                if string.lower() == dicString.lower(): 
                    for  letter in string: 
                        if letter.isupper():
                            mayusCounter +=1
                    # Si las mayusculas que tiene la string son más que las que tiene su parecida guardad en el diccionario, guardar
                    # la nueva string y eliminar la anterior. 
                    if mayusCounter > worDic[dicString]:
                        del worDic[dicString]
                        worDic[string] = mayusCounter
                        # Una vez esta guardad romper el for, reseteando el mayuscounter(en realidad no se pq se resetea pero funciona)
                        mayusCounter = 0
                        break
            # Si no encontramos ninguna string parecida en el diccionario entonces habra que añadir la string con su número de mayusculas
            for  letter in string: 
                if letter.isupper():
                    mayusCounter +=1
            worDic[string] = mayusCounter
            #Tampoco se pq resetear pero funciona
            mayusCounter = 0

        # First time going through the dictionary, add the first element. 
        else:
            for letter in string: 
                if letter.isupper():
                    mayusCounter +=1
            worDic[string] = mayusCounter
    
    # Change the strings in the variables list to their camelCase form stored in the dict
    
    for string in variables:
        for key in worDic: 
            if key.lower() == string.lower():
                output.append(key)



    return output


print(main())