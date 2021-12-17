from django.shortcuts import render
from .models import Restaurants
import json

def showmap(request):
    qs = Restaurants.objects.all() # 테이블의 모든 row를 할당
    # ret_dict = {}
    # i = 0
    # map_dic = {}
    # orderList: Restaurants = qs.values()
    
    # for i in range(len(qs)):
    #     'id': qs[i]['id'],
    #     'name': 
    #     'kinds': 
    #     'score': 
    #     'review':  
    #     'web_link': 
    #     'address':  
    #     'lat': 
    #     'lng': 
    #     'category':
    # print("aaaaaaaaaaaaaaaaaaaa")
    # print(qs.values())
    # print("bbbbbbbaabbbb")
    # print(qs.values()[0])
    # print(len(qs))
    rows = []
    for i in range(len(qs)):
        rows.append(qs.values()[i])
    # print(rows)

    map_dict = {}
    
    for i in range(len(qs)):
        map_dict['item'+str(i)] = ( json.dumps(qs.values()[i], ensure_ascii=False) )
    # print(33333333333333)
    # print(map_dict)

    # rows = (qs)
    context = {'rows': map_dict}
    # print(context)
    # print(map_dict)
    return render(request, 'map/map.html', context)
"""
    for item in rst_data:
        'id':  
        'name': 
        'kinds': 
        'score': 
        'review':  
        'web_link': 
        'address':  
        'lat': 
        'lng': 
        'category': 
"""