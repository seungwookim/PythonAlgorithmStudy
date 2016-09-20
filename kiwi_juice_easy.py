"""
Taro has prepared deliciois kiwi fruit juice he porured it into N bottles numberd form 0 to N-1.
The capacity of the i-th bottle is capaacities[i] liters, and he poured bottles[i] liters of kiwi
juice into this bottle .
New he wants to redistribute juice in the bottles. In order to do this, he will perform M operations
numbered form 0 to M-1 in the order in which he will perform them. For the i-th operation,
he will pour kiwi juice form bottle from ID[i] to bottle toId[i].
He will stop pouring when bottle fromId[i] becomes empty or bottle toId[i] becomes ull,whichever
happens earlier.
Return an Int[] that contains exactly N elements and whose i-th element is the amout of kiwi juice
in the i-th bottle after all pouring operations are finished
"""

import datetime as dt


class KiwiJuiceEasy:
    def pour_v1(self, capacities, bottles, fromIds, toIds):
        start_time = dt.datetime.now()
        for x in range(0, len(fromIds)):
            fromId = fromIds[x]
            toId = toIds[x]
            space = capacities[toId] - bottles[toId]

            if(space >= bottles[fromId]):
                vol = bottles[fromId]
                bottles[toId] += vol
                bottles[fromId] = 0

            else:
                bottles[toId] += space
                bottles[fromId] -= space

        end_time = dt.datetime.now()

        print("time cost : {0}".format(end_time - start_time))
        return bottles


result = KiwiJuiceEasy().pour_v1([7,6,7,5,3,5,6,4,2,2,6], [3,3,5,2,1,3,2,1,0,0,2], [1,5,7,9], [8,2,3,4])

print("remained amount : {0}".format(result))