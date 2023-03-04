#Write a code to calculate the area of the polygon.
#if the polygon n is equal to 1, the area of the polygon is 1
#If the polygon n is equal to 2, the area of the polygon is 5
#If the polygon n is equal to 3, the area of the polygon is 13
#If the polygon n is equal to 4, the area of the polygon is 25
#Range of polygon n is 1<= and >= 10**4
def solution(n):
    from functools import reduce
    try:
        #Check if the polygon range is correct
        if n > 1 and n <= 10**4:
            #Make a comprehension list to calculate the negative area of the polygon
            #The negative area of the polygon is equal the add of all numbers between 1 to n 
            #This only works if the polygon range is higher than 1   
            noArea = [x+1 for x in range(n-1)]
            print(noArea)

            #Now, we sumate all the numbers in the list
            reducedArea = reduce(lambda a,b: a+b, noArea)
            print(reducedArea) 

            #The area total is equal to the 2*n less 1 and elevate to square
            #And the negative area is equal to reduceArea by every corner, in this case we have 4
            area = (((2*n)-1)**2) - (reducedArea*4)
            print(area)
        elif n == 1:
            print(1)
            return 1
        else:
            raise ValueError
    except:
        raise ValueError
    return area
if __name__ == '__main__':
    solution(100)