"""
The digits 3 and 9 share an interesting property. if you tak any muliple of 3 and sum its
digitis, you get another multiple of 3. For example, 118*3=354 and 3 + 5+ 4 =12, which is
multiple of 3.  out goal is find this kind of interesting number on given base number.
(Don't have to consider numbers greater than 999)

"""
import math
import datetime as dt


def find_intrest_v1(base):
    """
    full search , cause we have clue that number are smaller than 999
    :return:
    """
    start_time = dt.datetime.now()
    answer = []

    for n in range(2, base):
        flag = True
        for n1 in range(0, base):
            for n2 in range(0, base):
                for n3 in range(0, base):
                    if((n1+(n2*base)+(n3*base*base)%n) == 0 and ((n1 + n2+ n3) % n !=0)):
                        flag = False
                        break
                if(flag == False):
                    break
            if(flag == False):
                break
        if(flag == True):
            answer.append(n)

    print(answer)


    end_time = dt.datetime.now()
    print("time cost : {0}".format(end_time - start_time))


result = find_intrest_v1(10)

print(result)