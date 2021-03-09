import math
import numpy as np
import matplotlib.pyplot as plt

def fungsi(x):
    y = (x*x)-(7*x)-7
    return y

def turunanFungsi(x):
    y = 2*x - 7
    return y

def main():
    x = 3
    x_sebelum = 9999
    selisih = x_sebelum - x
    error = 0
    print(" x | Selisih ")
    print('------------')
    
    print(x, " | ", selisih)
    
    while(abs(selisih)>error):
        x_sebelum = x
        x = x_sebelum - (fungsi(x)/turunanFungsi(x))
        selisih = x_sebelum - x
        print(x, " | ", selisih)
        
    print("\nAkar Persamaan = ", x, "\t|\t", "Error = ", abs(selisih))
    
    x = np.linspace(3,9999,100)
    plt.plot(x, fungsi(x))
    plt.plot(x, turunanFungsi(x))
    plt.grid()
    plt.xlabel("Grafik Fungsi y(x)")
    plt.show()
    
main()
