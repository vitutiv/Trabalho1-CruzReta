# Victor Pereira Moura
# 11836160
import pandas as pd
import numpy as np
#Carregar arquivo .csv com os dados
arquivo = pd.read_csv("cruzreta.csv")
print("TABELA: \n", arquivo)
# Colunas da tabela
xc1 = arquivo['xc1']
yc1 = arquivo['yc1']
xp1 = arquivo['xp1']
yp1 = arquivo['yp1']
xc2 = arquivo['xc2']
yc2 = arquivo['yc2']
xp2 = arquivo['xp2']
yp2 = arquivo['yp2']
# Número de linhas na tabela
numeroLinhas = len(arquivo)
#Câmeras 1 e 2: 
#   Coluna mr1:
mr1 = []
#   Coluna mr2: 
mr2 = []
#   Coluna br1: 
br1 = []
#   Coluna br2:
br2 = []

# X:
x = []
# Y:
y = []
for linha in range (numeroLinhas):
    mr1.append((yp1[linha] - yc1[linha]) / (xp1[linha] - xc1[linha]))
    mr2.append((yp2[linha] - yc2[linha]) / (xp2[linha] - xc2[linha]))
    br1.append((mr1[linha] * xc1[linha] - yc1[linha]) * -1)
    br2.append((mr2[linha] * xc2[linha] - yc2[linha]) * -1)
    x.append( ((mr2[linha] *  xc2[linha] * -1) + yc2[linha] + (mr1[linha] * xc1[linha] - yc1[linha])) / (mr1[linha] - mr2[linha]))
    y.append( mr1[linha] * x[linha] - mr1[linha] * xc1[linha] + yc1[linha])
print("mr1: ", mr1)
print("mr2: ", mr2)
print("br1: ", br1)
print("br2: ", br2)
print("X:", x)
print("Y:", y)
xRec3D = np.mean([x[0], x[1]])
print("Rec3D - X:", xRec3D)
yRec3D = np.mean([y[0], y[2]])
print("Rec3D - Y:", yRec3D)
zRec3D = np.mean([y[1], x[2]])
print("Rec3D - Z:", zRec3D)
xErroAbsoluto = abs(xRec3D - 159.3)
print("Erro absoluto - X: ", xErroAbsoluto)
yErroAbsouto = abs(yRec3D - 168.2)
print("Erro absoluto - Y: ", yErroAbsouto)
zErroAbsoluto = abs(zRec3D - 74.9)
print("Erro absoluto - Z: ", zErroAbsoluto)
erroAbsoluto = [xErroAbsoluto, yErroAbsouto, zErroAbsoluto]
erroTotal = np.mean(erroAbsoluto)
print("Erro total: ", erroTotal)
