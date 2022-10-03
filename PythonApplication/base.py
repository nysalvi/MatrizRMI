import time
import numpy as np

def salvaMatriz(arquivo, matriz):    
    matrix = open(arquivo, '+w')
    
    matrix.write(str(matriz[0]).removeprefix('[').removesuffix(']').replace(',', ' '))
    for row in range(1, len(matriz)):
        matrix.write('\n')
        matrix.write(str(matriz[row]).removeprefix('[').removesuffix(']').replace(',', ' '))        
    matrix.close()

def carregaMatriz(arquivo):    
    i = 0
    j = 0
    temp = ""
    matriz = np.ndarray([4096, 4096], dtype="float")   
    for o in open(arquivo, "r"):        
        for q in o:
            if q != '\t' and q != '\n' and q != ' ' and q != '\r\n':  
                temp += q    
            else:
                matriz[i][j] = float(temp)
                temp = ""
            j += 1
        i+=1
        j = 0

    matriz[i - 1].append(float(temp))
    return matriz

def monitorarTempo(matriz1, matriz2, arquivo, funcao):

    start_timer = time.time()
    matrix = funcao(matriz1, matriz2)
    end_timer = time.time() - start_timer
    
    arquivo = open(arquivo, 'a+')
    arquivo.write("//" + str(end_timer))

    arquivo.close()
    return matrix