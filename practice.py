y=2016
population = 80000
for i in range(y,2021):

    if y%2==0:
        population+= population*(10/100)
        y+=1
    else:
        population-= population*(10/100)
        y+=1
print(population)