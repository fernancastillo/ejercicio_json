import os
import json
import csv
empresas_csv=[]
contribuyentes=[]
os.system("cls")
with open("listadoRutEmpresa.csv",'r', newline="") as archivo:
    lector_csv = csv.reader(archivo)
    for x in lector_csv:
        empresas_csv.append(x)
for x in range(len(empresas_csv)):
    if x>0:
        contribuyente={
            "rut": empresas_csv[x][0],
            "nombre":empresas_csv[x][1],
            "empresa":int(empresas_csv[x][2]),
            "clasificacionEmpresa": ""
        }
        contribuyentes.append(contribuyente)
        if contribuyente["empresa"]<=100000000:
            contribuyente["clasificacionEmpresa"]="Pequeño Contribuyente"
        elif contribuyente["empresa"]>100000000 and contribuyente["empresa"]<=200000000:
            contribuyente["clasificacionEmpresa"]="Mediano Contribuyente"
        else:
            contribuyente["clasificacionEmpresa"]="Gran contribuyente"
with open("segmentacionEmpresas.json",'w') as arch:
    json.dump(contribuyentes,arch)