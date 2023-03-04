#Given a year, return the century it is in. The first century spans from the year 1 up to 
#and including the year 100, the second - from the year 101 up to and including the year 200, etc

def solution(year):
    try:
        assert year >= 1 and year <=2005, "Error, the number is no longer available"
        if year%100 == 0:
            century = (year/100)
            print(int(century))
            return century
        else:
            century = int(year/100)
            print(century+1)
            return century+1
    except:
        raise ValueError