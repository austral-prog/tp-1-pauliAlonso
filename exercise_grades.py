def grades():

    nota1 = 8
    nota2 = 7
    nota3 = 9

    promedio = (nota1 + nota2 + nota3) / 3 
    nota_max = max(nota1,nota2,nota3)
    nota_min = min(nota1,nota2,nota3)
    promedio_10 = 10 - promedio 

    print(promedio)
    print(nota_max)
    print(nota_min)
    print(promedio_10)

