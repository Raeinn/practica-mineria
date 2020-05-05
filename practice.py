import math as mt
import pandas as pd
import matplotlib.pyplot as plt

# Funcion para calcular percentiles
def percentil(lista, perc):
    p = (len(lista)-1)*perc
    pl = mt.floor(p)
    pu = mt.ceil(p)
    return lista[pl] + (lista[pu] - lista[pl]) * perc

# Funcion para calcular desviacion estandar
def std_desv(lista, mean):
    aux1 = 0
    for item in lista:
        aux2 = mt.pow(item - mean, 2)
        aux1 += aux2
    varianza = aux1 / (len(lista) - 1)
    return mt.sqrt(varianza)

# Importar archivo de datos, modificar directorio de datos de ser necesario
w_d = 'D:\\last_\\Documents\\Uni\\Octavo\\Mineria\\Python\\practica-mineria\\data\\'
i_f = w_d+'survey_results_public.csv'
data = pd.read_csv(i_f, encoding='utf-8')

# Importar los datos como listas
country = data['Country'].tolist()
edlevel = data['EdLevel'].tolist()
devtype = data['DevType'].tolist()
yearscode = data['YearsCode'].tolist()
salary = data['ConvertedComp'].tolist()
workhrs = data['WorkWeekHrs'].tolist()
languages = data['LanguageWorkedWith'].tolist()
age = data['Age'].tolist()
gender = data['Gender'].tolist()
ethnicity = data['Ethnicity'].tolist()

# 1. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per gender.
'''
salary_m = []
salary_w = []
salary_nb = []

i = 0
while(i < len(salary)):
    if not mt.isnan(salary[i]) and type(gender[i]) is str:
        if gender[i].lower().count('man') > 0:
            salary_m.append(salary[i])
        if gender[i].lower().count('woman') > 0:
            salary_w.append(salary[i])
        if gender[i].lower().count('non-binary') > 0:
            salary_nb.append(salary[i])
    i += 1

salary_m.sort()
salary_w.sort()
salary_nb.sort()

minimo = salary_m[0]
maximo = salary_m[-1]
mediana = percentil(salary_m, 0.5)
perc_1 = percentil(salary_m, 0.25)
perc_3 = percentil(salary_m, 0.75)
mean = sum(salary_m)/len(salary_m)
std_d = std_desv(salary_m, mean)

print('**** Resumen: Salario por anio de hombres ****')
print('Minimo:', minimo)
print('Percentil 1:', perc_1)
print('Mediana:', mediana)
print('Percentil 3:', perc_3)
print('Maximo:', maximo)
print('Media:', mean)
print('Desviacion estandar:', std_d)
plt.boxplot(salary_m)

minimo = salary_w[0]
maximo = salary_w[-1]
mediana = percentil(salary_w, 0.5)
perc_1 = percentil(salary_w, 0.25)
perc_3 = percentil(salary_w, 0.75)
mean = sum(salary_w)/len(salary_w)
std_d = std_desv(salary_w, mean)

print('\n**** Resumen: Salario por anio de mujeres ****')
print('Minimo:', minimo)
print('Percentil 1:', perc_1)
print('Mediana:', mediana)
print('Percentil 3:', perc_3)
print('Maximo:', maximo)
print('Media:', mean)
print('Desviacion estandar:', std_d)
plt.boxplot(salary_w)

minimo = salary_nb[0]
maximo = salary_nb[-1]
mediana = percentil(salary_nb, 0.5)
perc_1 = percentil(salary_nb, 0.25)
perc_3 = percentil(salary_nb, 0.75)
mean = sum(salary_nb)/len(salary_nb)
std_d = std_desv(salary_nb, mean)

print('\n**** Resumen: Salario por anio de personas no-binarias ****')
print('Minimo:', minimo)
print('Percentil 1:', perc_1)
print('Mediana:', mediana)
print('Percentil 3:', perc_3)
print('Maximo:', maximo)
print('Media:', mean)
print('Desviacion estandar:', std_d)

plt.boxplot([salary_m, salary_w, salary_nb], labels=['Man','Woman','Non-binary'])
'''
# 2. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per ethnicity.
