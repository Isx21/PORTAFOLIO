def solution(statues):
    if len(statues) >=1 and len(statues) <= 10:
        try:
            maxNum=0
            minNum=20
            for x in statues:
                if x >=0 and x <=20:
                    if maxNum<x:
                        maxNum = x
                    if minNum>x:
                        minNum = x
                    if statues.count(x)!=1:
                        raise ValueError
                else:
                    raise ValueError
            print(maxNum,minNum)
            listComprh = [i for i in range(minNum, maxNum+1)]
            #print(listComprh)
            #print(len(listComprh), len(statues))
            numDiff = len(listComprh)-len(statues)
            print("The number of missing statues is: ", numDiff)
            result = list(filter(lambda x: x not in statues, listComprh))
            print(result)
            return numDiff

        except:
            raise ValueError
    else:
        raise ValueError

if __name__ == '__main__':
    solution([2,4,6,8,10,12,14,16])