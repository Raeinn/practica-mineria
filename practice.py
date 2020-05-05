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

# Funcion para mostrar el resumen de los 5 numeros, media y desviacion estandar
# Se asume que la lista que se da como argumento esta ordenada
# TODO: Ajustar funcion a dos funciones: Una mostrara minimo, maximo y los percentiles;
# otra mostrara la media, mediana y desviacion estandar
def five_num_summary(lista):
    mean = sum(lista) / len(lista)
    print('Minimo:', lista[0])
    print('Percentil 1:', percentil(lista, 0.25))
    print('Mediana:', percentil(lista, 0.5))
    print('Percentil 3:', percentil(lista, 0.75))
    print('Maximo:', lista[-1])
    print('Media:', mean)
    print('Desviacion estandar:', std_desv(lista, mean))

# Importar archivo de datos, modificar directorio de datos de ser necesario
w_d = 'D:\\last_\\Documents\\Uni\\Octavo\\Mineria\\Python\\practica-mineria\\data\\'
i_f = w_d+'survey_results_public.csv'
data = pd.read_csv(i_f, encoding='utf-8')

# Importar los datos como listas
# Quitar comentario para activar la lista necesaria
#country = data['Country'].tolist()
#edlevel = data['EdLevel'].tolist()
devtype = data['DevType'].tolist()
#yearscode = data['YearsCode'].tolist()
salary = data['ConvertedComp'].tolist()
#workhrs = data['WorkWeekHrs'].tolist()
#languages = data['LanguageWorkedWith'].tolist()
#age = data['Age'].tolist()
#gender = data['Gender'].tolist()
#ethnicity = data['Ethnicity'].tolist()

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

print('**** Resumen: Salario por anio de hombres ****')
five_num_summary(salary_m)

print('\n**** Resumen: Salario por anio de mujeres ****')
five_num_summary(salary_w)

print('\n**** Resumen: Salario por anio de personas no-binarias ****')
five_num_summary(salary_nb)

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

print('**** Resumen: Salario por anio de personas biraciales ****')
five_num_summary(salary_bi)

print('**** Resumen: Salario por anio de personas multiraciales ****')
five_num_summary(salary_multi)

print('**** Resumen: Salario por anio de personas afroamericanas ****')
five_num_summary(salary_blk)

print('**** Resumen: Salario por anio de personas del este asiatico ****')
five_num_summary(salary_ea)

print('**** Resumen: Salario por anio de personas hispanas ****')
five_num_summary(salary_hisp)

print('**** Resumen: Salario por anio de personas del medio este ****')
five_num_summary(salary_me)

print('**** Resumen: Salario por anio de personas nativo-americanas ****')
five_num_summary(salary_na)

print('**** Resumen: Salario por anio de personas del sur asiatico ****')
five_num_summary(salary_sa)

print('**** Resumen: Salario por anio de personas caucasicas ****')
five_num_summary(salary_w)

plt.boxplot([salary_bi, salary_multi, salary_blk, salary_ea, salary_hisp, salary_me, salary_na,
salary_sa, salary_w], labels=['BiR','MR','Afros','EA','Hisp','ME','NA','SA','Caucasic'])
'''
# Compute the five-number summary, the boxplot, the mean,
# and the standard deviation for the annual salary per developer type.
# Found dev-types: Academic; Business; Learning; Database Administrator; Designer; back-end; desktop; front-end
# embedded; full-stack; game; mobile; qa; devops; educator; engineer, data; reliability; engineering; Sales;
# Product; Scientist; VP; Student; System

salary_ar = []
salary_ba = []
salary_mls = []
salary_dba = []
salary_dsgn = []
salary_dbe = []
salary_ddk = []
salary_dfe = []
salary_demb = []
salary_dfs = []
salary_dg = []
salary_dm = []
salary_dqa = []
salary_dvop = []
salary_edu = []
salary_engdt = []
salary_engra = []
salary_engman = []
salary_sales = []
salary_pdm = []
salary_scien = []
salary_vp = []
salary_stud = []
salary_sysadm = []

i = 0
while(i < len(salary)):
    if not mt.isnan(salary[i]) and type(devtype[i]) is str:
        if devtype[i].lower().count('academic') > 0:
            salary_ar.append(salary[i])
        if devtype[i].lower().count('business') > 0:
            salary_ba.append(salary[i])
        if devtype[i].lower().count('learning') > 0:
            salary_mls.append(salary[i])
        if devtype[i].lower().count('database administrator') > 0:
            salary_dba.append(salary[i])
        if devtype[i].lower().count('designer') > 0:
            salary_dsgn.append(salary[i])
        if devtype[i].lower().count('back-end') > 0:
            salary_dbe.append(salary[i])
        if devtype[i].lower().count('desktop') > 0:
            salary_ddk.append(salary[i])
        if devtype[i].lower().count('front-end') > 0:
            salary_dfe.append(salary[i])
        if devtype[i].lower().count('embedded') > 0:
            salary_demb.append(salary[i])
        if devtype[i].lower().count('full-stack') > 0:
            salary_dfs.append(salary[i])
        if devtype[i].lower().count('game') > 0:
            salary_dg.append(salary[i])
        if devtype[i].lower().count('mobile') > 0:
            salary_dm.append(salary[i])
        if devtype[i].lower().count('qa') > 0:
            salary_dqa.append(salary[i])
        if devtype[i].lower().count('devops') > 0:
            salary_dvop.append(salary[i])
        if devtype[i].lower().count('educator') > 0:
            salary_edu.append(salary[i])
        if devtype[i].lower().count('engineer, data') > 0:
            salary_engdt.append(salary[i])
        if devtype[i].lower().count('reliability') > 0:
            salary_engra.append(salary[i])
        if devtype[i].lower().count('engineering') > 0:
            salary_engman.append(salary[i])
        if devtype[i].lower().count('sales') > 0:
            salary_sales.append(salary[i])
        if devtype[i].lower().count('product') > 0:
            salary_pdm.append(salary[i])
        if devtype[i].lower().count('scientist') > 0:
            salary_scien.append(salary[i])
        if devtype[i].lower().count('vp') > 0:
            salary_vp.append(salary[i])
        if devtype[i].lower().count('student') > 0:
            salary_stud.append(salary[i])
        if devtype[i].lower().count('system') > 0:
            salary_sysadm.append(salary[i])
    i += 1

salary_ar.sort()
salary_ba.sort()
salary_mls.sort()
salary_dba.sort()
salary_dsgn.sort()
salary_dbe.sort()
salary_ddk.sort()
salary_dfe.sort()
salary_demb.sort()
salary_dfs.sort()
salary_dg.sort()
salary_dm.sort()
salary_dqa.sort()
salary_dvop.sort()
salary_edu.sort()
salary_engdt.sort()
salary_engra.sort()
salary_engman.sort()
salary_sales.sort()
salary_pdm.sort()
salary_scien.sort()
salary_vp.sort()
salary_stud.sort()
salary_sysadm.sort()

print('**** Resumen: Salario por anio de investigadores academicos ****')
five_num_summary(salary_ar)

print('**** Resumen: Salario por anio de analistas de negocios ****')
five_num_summary(salary_ba)

print('**** Resumen: Salario por anio de cientificos de machine learning ****')
five_num_summary(salary_mls)

print('**** Resumen: Salario por anio de administradores de database ****')
five_num_summary(salary_dba)

print('**** Resumen: Salario por anio de diseniadores ****')
five_num_summary(salary_dsgn)

print('**** Resumen: Salario por anio de desarrolladores back-end ****')
five_num_summary(salary_dbe)

print('**** Resumen: Salario por anio de desarrolladores de escritorio ****')
five_num_summary(salary_ddk)

print('**** Resumen: Salario por anio de desarrolladores front-end ****')
five_num_summary(salary_dfe)

print('**** Resumen: Salario por anio de desarrolladores de aplicaciones integradas ****')
five_num_summary(salary_demb)

print('**** Resumen: Salario por anio de desarrolladores full-stack ****')
five_num_summary(salary_dfs)

print('**** Resumen: Salario por anio de desarrolladores de juegos ****')
five_num_summary(salary_dg)

print('**** Resumen: Salario por anio de desarrolladores de apps moviles ****')
five_num_summary(salary_dm)

print('**** Resumen: Salario por anio de desarrolladores QA ****')
five_num_summary(salary_dqa)

print('**** Resumen: Salario por anio de DevOps ****')
five_num_summary(salary_dvop)

print('**** Resumen: Salario por anio de educadores ****')
five_num_summary(salary_edu)

print('**** Resumen: Salario por anio de ingenieros en datos ****')
five_num_summary(salary_engdt)

print('**** Resumen: Salario por anio de ingenieros en fiabilidad ****')
five_num_summary(salary_engra)

print('**** Resumen: Salario por anio de gerentes de ingenieria ****')
five_num_summary(salary_engman)

print('**** Resumen: Salario por anio de encargados de ventas ****')
five_num_summary(salary_sales)

print('**** Resumen: Salario por anio de gerentes de productos ****')
five_num_summary(salary_pdm)

print('**** Resumen: Salario por anio de cientificos ****')
five_num_summary(salary_scien)

print('**** Resumen: Salario por anio de cientificos ****')
five_num_summary(salary_scien)

print('**** Resumen: Salario por anio de VP ****')
five_num_summary(salary_vp)

print('**** Resumen: Salario por anio de estudiantes ****')
five_num_summary(salary_stud)

print('**** Resumen: Salario por anio de administradores de sistemas ****')
five_num_summary(salary_sysadm)

plt.boxplot([salary_ar,salary_ba,salary_mls,salary_dba,salary_dsgn,salary_dbe,salary_ddk,salary_dfe,
salary_demb,salary_dfs,salary_dg,salary_dm,salary_dqa,salary_dvop,salary_edu,salary_engdt,salary_engra,
salary_engman,salary_sales,salary_pdm,salary_scien,salary_vp,salary_stud,salary_sysadm])