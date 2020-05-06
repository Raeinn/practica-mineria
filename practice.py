import math as mt
import numpy as np
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

# Funcion para mostrar el resumen de los 5 numeros, media y desviacion estandar
# Se asume que la lista que se da como argumento esta ordenada
def five_num_summary(lista):
    mean = sum(lista) / len(lista)
    print('Minimo:', lista[0])
    print('Percentil 1:', percentil(lista, 0.25))
    print('Mediana:', percentil(lista, 0.5))
    print('Percentil 3:', percentil(lista, 0.75))
    print('Maximo:', lista[-1])
    print('Media:', mean)
    print('Desviacion estandar:', std_desv(lista, mean))

# Funcion que muestra media, mediana y desviacion estandar
def centre_summary(lista):
    mean = sum(lista) / len(lista)
    print('Media:', mean)
    print('Mediana:', percentil(lista, 0.5))
    print('Desviacion estandar:', std_desv(lista, mean))

# Funcion para conseguir una lista de strings individuales
# Necesaria para encontrar tipos de desarrolladores, o lenguajes de programacion
def str_splitter(lista):
    output = []
    for elem in lista:
        if type(elem) is str:
            aux_str = elem.split(sep=';')
            for string in aux_str:
                if string not in output:
                    output.append(string)
    return output


# Importar archivo de datos, modificar directorio de datos de ser necesario
w_d = 'D:\\last_\\Documents\\Uni\\Octavo\\Mineria\\Python\\practica-mineria\\data\\'
i_f = w_d+'survey_results_public.csv'
data = pd.read_csv(i_f, encoding='utf-8')

# Importar los datos como listas
# Quitar comentarios para activar las listas necesarias
#country = data['Country'].tolist()
#edlevel = data['EdLevel'].tolist()
#devtype = data['DevType'].tolist()
#yearscode = data['YearsCode'].tolist()
#salary = data['ConvertedComp'].tolist()
#workhrs = data['WorkWeekHrs'].tolist()
#languages = data['LanguageWorkedWith'].tolist()
#age = data['Age'].tolist()
#gender = data['Gender'].tolist()
#ethnicity = data['Ethnicity'].tolist()

# A continuacion estan los ejercicios
# Retire el grupo de comentarios necesario para probar la seccion especifica

# 1. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per gender.
# Genders found: Man, Woman, Non-binary
'''
all_genders = ['Man', 'Woman', 'Non-binary']

for genders in all_genders:
    i = 0
    salary_gender = []
    while(i < len(salary)):
        if type(gender[i]) is str and not mt.isnan(salary[i]):
            if gender[i].count(genders) > 0:
                salary_gender.append(salary[i])
        i += 1
    salary_gender.sort()
    print('**** Resumen de estadistica para {} ****'.format(genders))
    five_num_summary(salary_gender)
    plt.boxplot(salary_gender, labels=[genders])
    plt.show()
'''
# 2. Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per ethnicity.
# First, list all ethnicities
'''
ethnicities = str_splitter(ethnicity)

for ethn in ethnicities:
    i = 0
    salary_ethn = []
    while(i < len(salary)):
        if type(ethnicity[i]) is str and not mt.isnan(salary[i]):
            if ethnicity[i].count(ethn) > 0:
                salary_ethn.append(salary[i])
        i += 1
    salary_ethn.sort()
    print('**** Resumen de estadistica para {} ****'.format(ethn))
    five_num_summary(salary_ethn)
    plt.boxplot(salary_ethn, labels=[ethn])
    plt.show()
'''
# 3. Compute the five-number summary, the boxplot, the mean, and the standard deviation
# for the annual salary per developer type.
# A list of all dev-types is needed
'''
dev_types = str_splitter(devtype)

for dvtype in dev_types:
    i = 0
    salary_devs = []
    while(i < len(salary)):
        if type(devtype[i]) is str and not mt.isnan(salary[i]):
            if devtype[i].count(dvtype) > 0:
                salary_devs.append(salary[i])
        i += 1
    salary_devs.sort()
    print('**** Resumen de estadistica para {} ****'.format(dvtype))
    five_num_summary(salary_devs)
    plt.boxplot(salary_devs, labels=[dvtype])
    plt.show()
'''
# 4. Compute the median, mean and standard deviation of the annual salary per country.
# Find all possible countries on the column
'''
all_countries = []
for c in country:
    if c not in all_countries and type(c) is str:
        all_countries.append(c)

for c in all_countries:
    i = 0
    salary_country = []
    while(i < len(salary)):
        if country[i] == c and not mt.isnan(salary[i]):
            salary_country.append(salary[i])
        i += 1
    print('**** Resumen de estadistica para {} ****'.format(c))
    if len(salary_country) > 1: centre_summary(salary_country)
    else: print('No se cuenta con datos suficientes de este pais para su analisis.')
'''
# 5. Obtain a bar plot with the frequencies of responses for each developer type.
# Place all dev types in a list
'''
dev_types = str_splitter(devtype)

freqs = []
for types in dev_types:
    cnt = 0
    for elem in devtype:
        if type(elem) is str:
            cnt += elem.count(types)
    freqs.append(cnt)

x_ticks = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X')
y_pos = np.arange(len(dev_types))
plt.bar(y_pos, freqs)
plt.xticks(y_pos, x_ticks)
plt.show()
'''
# 6. Plot histograms with 10 bins for the years of experience with coding per gender.
# Make a list with all genders (3)
# For simple coding, "less than 1 year" will be "0", and "more than 50 years" shall be "51"
'''
all_genders = ['Man', 'Woman', 'Non-binary']

for genders in all_genders:
    years_gender = []
    i = 0
    while(i < len(yearscode)):
        if type(gender[i]) is str and type(yearscode[i]) is str:
            if gender[i].count(genders) > 0:
                if yearscode[i] == 'Less than 1 year':
                    years_gender.append(0)
                elif yearscode[i] == 'More than 50 years':
                    years_gender.append(51)
                else:
                    years_gender.append(int(yearscode[i]))
        i += 1
    years_gender.sort()
    print('**** Histograma para {} ****'.format(genders))
    plt.hist(years_gender, bins=10)
    plt.show()
'''
# 7. Plot histograms with 10 bins for the average number
# of working hours per week, per developer type.
# For simple coding, any worker over 500 hours shall be treated as if they worked only 500 hrs
'''
dev_types = str_splitter(devtype)

for types in dev_types:
    workhrs_devtype = []
    i = 0
    while(i < len(workhrs)):
        if type(devtype[i]) is str and not mt.isnan(workhrs[i]):
            if workhrs[i] < 500:
                workhrs_devtype.append(workhrs[i])
            else:
                workhrs_devtype.append(500)
        i += 1
    workhrs_devtype.sort()
    print('**** Histograma para {} ****'.format(types))
    plt.hist(workhrs_devtype, bins=10)
    plt.show()
'''
# 8. Plot histograms with 10 bins for the age per gender.
'''
all_genders = ['Man', 'Woman', 'Non-binary']

for genders in all_genders:
    age_gender = []
    i = 0
    while(i < len(age)):
        if type(gender[i]) is str and not mt.isnan(age[i]):
            if gender[i].count(genders) > 0:
                age_gender.append(age[i])
        i += 1
    age_gender.sort()
    print('**** Histograma para {} ****'.format(genders))
    plt.hist(age_gender, bins=10)
    plt.show()
'''
# 9. Compute the median, mean and standard deviation of the age per programming language.
# First, list all dev languages
'''
dev_lang = str_splitter(languages)

for lang in dev_lang:
    i = 0
    age_lang = []
    while(i < len(age)):
        if type(languages[i]) is str and not mt.isnan(age[i]):
            if languages[i].count(lang) > 0:
                age_lang.append(age[i])
        i += 1
    print('**** Resumen de estadistica para {} ****'.format(lang))
    if len(age_lang) > 1: centre_summary(age_lang)
    else: print('No se cuenta con datos suficientes de este lenguaje para su analisis.')
'''