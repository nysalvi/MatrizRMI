import base
import numpy as np

def calculaMatriz(matrix1, matrix2):
    linha = len(matrix1)
    coluna = len(matrix2[0])
    
    matrizFinal = np.ndarray([4096, 4096], dtype='float')
    
    for i in range(linha):
        for r in range(linha):
            mult = 0    
            for j in range(coluna):
                mult += matrix1[i][j] * matrix2[j][r]  
            matrizFinal[i][r] = mult
    return matrizFinal
       
if __name__ == "__main__":
    matriz1 = base.carregaMatriz("matA.txt")
    matriz2 = base.carregaMatriz("matB.txt")    

    matrix = base.monitorarTempo(matriz1, matriz2, 'matA_B_C.txt', calculaMatriz)
    
    base.salvaMatriz("matC.txt", matrix)    