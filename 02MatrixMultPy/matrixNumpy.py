import time
import threading
import random
import numpy as np
import sys

s = int(sys.argv[1])
#print s


#Matriz A
A = np.random.rand(s,s)
#print A


#Matriz B
B = np.random.rand(s,s)
#print B


#Matriz C
C = np.zeros((s,s))
#print C

threads = []

#funcion a paralelizar

def matMult(mf, mc, size):
    temp = 0
    for j in range(size):
        temp += A[mf][j] * B[j][mc]
    C[mf][mc] = temp
    #print C[mf][mc]

def main():
    for f in range(s):
        for c in range(s):
            tr = threading.Thread(target=matMult, args=(f,c,s,))
            threads.append(tr)
            tr.start()
            tr.join()
    print C


main()
