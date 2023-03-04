#Given an array of integers, find the pair of adjacent elements that has the largest product
#and return that product.
def solution(inputArray):
    largestProduct = -1000000
    low = -1000
    high = 1000
    if len(inputArray) >= 2 and len(inputArray) <= 10:
        for i in range(len(inputArray)):
            if inputArray[i] >= low and inputArray[i] <= high:
                pass
            else:
                raise ValueError
        for x in range(len(inputArray)-1):
            if inputArray[x] * inputArray[x+1] > largestProduct:
                largestProduct = inputArray[x] * inputArray[x+1]    
    else:
        raise ValueError            
    return largestProduct