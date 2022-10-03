from __future__ import nested_scopes
from multiprocessing import Array, Pool
import multiprocessing
from multiprocessing import shared_memory
from multiprocessing.shared_memory import SharedMemory
import time
import base
import sys
import array
import numpy as np

shm = SharedMemory("Array Compartilhado", True, 4096 * 4096 * 32)
matrizFinal = np.ndarray([4096, 4096], dtype="float", buffer=shm.buf)

shm_matriz1 = SharedMemory("Matriz1", True, 4096 * 4096 * 32)
matriz1 = np.ndarray([4096, 4096], dtype="float", buffer=shm_matriz1.buf)
matriz1[:] = base.carregaMatriz("matA.txt")

def calculaSubMatriz(x, matriz1, matriz2):  
    linha = int(len(matriz1) / 8)
    coluna = int(len(matriz2[0]))    
    for i in range(linha):
        for r in range(linha):
            mult = 0    
            for j in range(coluna):
                mult += matriz1[i + x * linha][j] * matriz2[j][r + x * linha]  
            matrizFinal[i + x * linha][r + x * linha] = mult            

def calculaMatriz(matrix1, matrix2):                
    with Pool(8) as pool:
        pool.starmap(calculaSubMatriz, [(x, matrix1, matrix2) for x in range (8)])        
        pool.close()
        pool.join()    
    shm.unlink()
    
if __name__ == "__main__":    
        
    matriz2 = base.carregaMatriz("matB.txt")      
    
    #start_timer = time.time()
    matrix = base.monitorarTempo(matriz1, matriz2, 'matA_B_C.txt', calculaMatriz)
    #end_timer = time.time() - start_timer            
    base.salvaMatriz("matC.txt", matrizFinal)