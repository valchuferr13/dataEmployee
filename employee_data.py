import pandas as pd

# Carga el archivo Excel
df = pd.read_excel('Employee Data 2.xlsx')

# Acceder a las columnas relevantes para extraer la información requerida
nombres = df['Full Name']
puestos = df['Job Title']
salarios = df['Annual Salary']
paises = df['Country']

# Imprimir la información de cada empleado
for nombre, puesto, salario, pais in zip(nombres, puestos, salarios, paises):
    print("Nombre Completo:", nombre)
    print("Puesto:", puesto)
    print("Salario:", salario)
    print("País:", pais)
    print("------------------------")
