"""
Mr. White is very versatile person - abosolutely everything is interesting to him. Perhaps
this is why he has many friends. Quite unfortunately, however, noe of hus friends are
verstile at all. Each of them is interested only in two topics and refuses to talk about
anything else Therefore, each time Mr. White organizers a party, it's big problem for
him to decide whom to invite so that the party is interes Not that Mr.
White has a lot of expereience i organizing parties, he knows for sure that a party will be
interesting if and only if there's topic interesing to each of the invited friends.
you will be given String[] first and second. The i-thh frien of Mr White is interested in
topics first[i] and second[i]. Return the largest numver of friends that Mr . White can
invaite to his pary so that the party will be ineresting.
"""
import math
import datetime as dt

class IntrestParty :
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def max_invite_num_v1(self):
        """
        my own answer - not no the book
        let's see.. who's answer is faster...
        :return:
        """
        start_time = dt.datetime.now()
        first_key_set = set(self.first)
        second_key_set = set(self.second)
        dict = {}

        for idx, key in enumerate(first_key_set):
            if(key in dict):
                dict[key] += (len(filter(lambda x:x==key, self.first)))
            else :
                dict[key] = int((len(filter(lambda x: x == key, self.first))))

        for idx, key in enumerate(second_key_set):
            if(key in dict):
                dict[key] = (len(filter(lambda x:x==key, self.second)))
            else :
                dict[key] = int((len(filter(lambda x: x == key, self.second))))

        result = max(dict.iterkeys(), key=(lambda key : dict[key]))
        print("inviting {0} people interest in {1}".format(dict[result] , result))

        end_time = dt.datetime.now()
        print("time cost : {0}".format(end_time - start_time))




ip = IntrestParty([1,3,2,1,3,1,2,3,2,2,3,3,4,1,2,3], [2,1,3,2,1,2,3,2,1,3,2,1,2,2,3,1])
ip.max_invite_num_v1()