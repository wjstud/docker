# coding: utf-8

import sys
from pymongo import MongoClient
from collections import OrderedDict
def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    a = [
            {"$group":{
                    "_id":"$user_id",
                    "count_score":{"$sum":"$score"},
                    "count_time":{"$sum":"$submit_time"}
            }},
            {"$sort":OrderedDict([("count_score",-1),("count_time",1)])}
        ]
    id_list = [x['_id'] for x in contests.aggregate(a)]
    if user_id in id_list:
        for i in enumerate(contests.aggregate(a),start=1):
            if user_id == i[1]['_id']:
                rank = i[0]
                score = i[1]['count_score']
                submit_time = i[1]['count_time']
                return rank,score,submit_time
    else:
        return "NOTFOUND"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            print(get_rank(int(sys.argv[1])))
        except:
            print("argv must be int")
    else:
        print("Usage: %s 2" % sys.argv[0]) 
