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
# Quitar comentario para activar la lista necesaria
#country = data['Country'].tolist()
#edlevel = data['EdLevel'].tolist()
#devtype = data['DevType'].tolist()
#yearscode = data['YearsCode'].tolist()
salary = data['ConvertedComp'].tolist()
#workhrs = data['WorkWeekHrs'].tolist()
#languages = data['LanguageWorkedWith'].tolist()
#age = data['Age'].tolist()
#gender = data['Gender'].tolist()
ethnicity = data['Ethnicity'].tolist()

# 1. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per gender.
# Genders found: Man, Woman, Non-binary
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

mean = sum(salary_m)/len(salary_m)

print('**** Resumen: Salario por anio de hombres ****')
print('Minimo:', salary_m[0])
print('Percentil 1:', percentil(salary_m, 0.25))
print('Mediana:', percentil(salary_m, 0.5))
print('Percentil 3:', percentil(salary_m, 0.75))
print('Maximo:', salary_m[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_m, mean))

mean = sum(salary_w)/len(salary_w)

print('\n**** Resumen: Salario por anio de mujeres ****')
print('Minimo:', salary_w[0])
print('Percentil 1:', percentil(salary_w, 0.25))
print('Mediana:', percentil(salary_w, 0.5))
print('Percentil 3:', percentil(salary_w, 0.75))
print('Maximo:', salary_w[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_w, mean))

mean = sum(salary_nb)/len(salary_nb)

print('\n**** Resumen: Salario por anio de personas no-binarias ****')
print('Minimo:', salary_nb[0])
print('Percentil 1:', percentil(salary_nb, 0.25))
print('Mediana:', percentil(salary_nb, 0.5))
print('Percentil 3:', percentil(salary_nb, 0.75))
print('Maximo:', salary_nb[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_nb, mean))

plt.boxplot([salary_m, salary_w, salary_nb], labels=['Man','Woman','Non-binary'])
'''
# 2. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per ethnicity.
# Found ethnicities: Biracial, multiracial, black, east asian, hispanic, middle eastern,
# native american, south asian, white
'''
salary_bi = []
salary_multi = []
salary_blk = []
salary_ea = []
salary_hisp = []
salary_me = []
salary_na = []
salary_sa = []
salary_w = []

i = 0
while(i < len(salary)):
    if not mt.isnan(salary[i]) and type(ethnicity[i]) is str:
        if ethnicity[i].lower().count('biracial') > 0:
            salary_bi.append(salary[i])
        if ethnicity[i].lower().count('multiracial') > 0:
            salary_multi.append(salary[i])
        if ethnicity[i].lower().count('black') > 0:
            salary_blk.append(salary[i])
        if ethnicity[i].lower().count('east asian') > 0:
            salary_ea.append(salary[i])
        if ethnicity[i].lower().count('hispanic') > 0:
            salary_hisp.append(salary[i])
        if ethnicity[i].lower().count('middle') > 0:
            salary_me.append(salary[i])
        if ethnicity[i].lower().count('native') > 0:
            salary_na.append(salary[i])
        if ethnicity[i].lower().count('south') > 0:
            salary_sa.append(salary[i])
        if ethnicity[i].lower().count('white') > 0:
            salary_w.append(salary[i])
    i += 1

salary_bi.sort()
salary_multi.sort()
salary_blk.sort()
salary_ea.sort()
salary_hisp.sort()
salary_me.sort()
salary_na.sort()
salary_sa.sort()
salary_w.sort()

mean = sum(salary_bi)/len(salary_bi)

print('**** Resumen: Salario por anio de personas biraciales ****')
print('Minimo:', salary_bi[0])
print('Percentil 1:', percentil(salary_bi, 0.25))
print('Mediana:', percentil(salary_bi, 0.5))
print('Percentil 3:', percentil(salary_bi, 0.75))
print('Maximo:', salary_bi[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_bi, mean))

mean = sum(salary_multi)/len(salary_multi)

print('**** Resumen: Salario por anio de personas multiraciales ****')
print('Minimo:', salary_multi[0])
print('Percentil 1:', percentil(salary_multi, 0.25))
print('Mediana:', percentil(salary_multi, 0.5))
print('Percentil 3:', percentil(salary_multi, 0.75))
print('Maximo:', salary_multi[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_multi, mean))

mean = sum(salary_blk)/len(salary_blk)

print('**** Resumen: Salario por anio de personas afroamericanas ****')
print('Minimo:', salary_blk[0])
print('Percentil 1:', percentil(salary_blk, 0.25))
print('Mediana:', percentil(salary_blk, 0.5))
print('Percentil 3:', percentil(salary_blk, 0.75))
print('Maximo:', salary_blk[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_blk, mean))

mean = sum(salary_ea)/len(salary_ea)

print('**** Resumen: Salario por anio de personas del este asiatico ****')
print('Minimo:', salary_ea[0])
print('Percentil 1:', percentil(salary_ea, 0.25))
print('Mediana:', percentil(salary_ea, 0.5))
print('Percentil 3:', percentil(salary_ea, 0.75))
print('Maximo:', salary_ea[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_ea, mean))

mean = sum(salary_hisp)/len(salary_hisp)

print('**** Resumen: Salario por anio de personas hispanas ****')
print('Minimo:', salary_hisp[0])
print('Percentil 1:', percentil(salary_hisp, 0.25))
print('Mediana:', percentil(salary_hisp, 0.5))
print('Percentil 3:', percentil(salary_hisp, 0.75))
print('Maximo:', salary_hisp[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_hisp, mean))

mean = sum(salary_me)/len(salary_me)

print('**** Resumen: Salario por anio de personas del medio este ****')
print('Minimo:', salary_me[0])
print('Percentil 1:', percentil(salary_me, 0.25))
print('Mediana:', percentil(salary_me, 0.5))
print('Percentil 3:', percentil(salary_me, 0.75))
print('Maximo:', salary_me[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_me, mean))

mean = sum(salary_na)/len(salary_na)

print('**** Resumen: Salario por anio de personas nativo-americanas ****')
print('Minimo:', salary_na[0])
print('Percentil 1:', percentil(salary_na, 0.25))
print('Mediana:', percentil(salary_na, 0.5))
print('Percentil 3:', percentil(salary_na, 0.75))
print('Maximo:', salary_na[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_na, mean))

mean = sum(salary_sa)/len(salary_sa)

print('**** Resumen: Salario por anio de personas del sur asiatico ****')
print('Minimo:', salary_sa[0])
print('Percentil 1:', percentil(salary_sa, 0.25))
print('Mediana:', percentil(salary_sa, 0.5))
print('Percentil 3:', percentil(salary_sa, 0.75))
print('Maximo:', salary_sa[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_sa, mean))

mean = sum(salary_w)/len(salary_w)

print('**** Resumen: Salario por anio de personas caucasicas ****')
print('Minimo:', salary_w[0])
print('Percentil 1:', percentil(salary_w, 0.25))
print('Mediana:', percentil(salary_w, 0.5))
print('Percentil 3:', percentil(salary_w, 0.75))
print('Maximo:', salary_w[-1])
print('Media:', mean)
print('Desviacion estandar:', std_desv(salary_w, mean))

plt.boxplot([salary_bi, salary_multi, salary_blk, salary_ea, salary_hisp, salary_me, salary_na,
salary_sa, salary_w], labels=['BiR','MR','Afros','EA','Hisp','ME','NA','SA','Caucasic'])
'''
# Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per developer type.
# Found dev-types: Academic; Business; Learning; Database Administrator; Designer; back-end; desktop;
# embedded,; full-stack; game; mobile; qa; devops; educator; engineer, data; reliability; engineering; Sales;
# Product; Scientist; VP; Student; System
