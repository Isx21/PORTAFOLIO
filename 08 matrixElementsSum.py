import numpy as np
def solution(matrix):
    suma = 0
    blackList = []
    shape = np.shape(matrix)
    print("El tamaño de la matriz es: ",shape)
    for i in range(0, (shape[0])):
        #print("Este es i: ",i)
        for j in range(0, (shape[1])):
            #print("Este es j: ",j)
            if j not in blackList:
                suma += matrix[i][j]
            else:
                print("no sumamos este numero", matrix[i][j])
            if (matrix[i][j]) == 0:
                blackList.append(j)

    print(suma)
if __name__ == "__main__":
    solution([
        [0,1,1,2], 
        [0,5,0,0], 
        [2,0,3,3]
])