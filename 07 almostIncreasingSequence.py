#Encontrar el par incorrecto
def find_bad_pair(sequence):

    #Con el ciclo recorremos todo el array
    for i in range(0,len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            #Regresamos el valor de i
            return i
    return -1

def solution(sequence):
    #Si nuestra función nos retorna -1, el resultado de esta es True
    #Por otro lado si nos retorna un valor distinto debemos evaluar de otra manera
    j = find_bad_pair(sequence)
    print(j)
    if j == -1:
        return True
    #Elemento anterior con el siguiente
    if find_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    #Elemento siguiente
    if find_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False

if __name__ == '__main__':
    solution([1, 3, 2])