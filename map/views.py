from django.shortcuts import render
from .models import Restaurants
import json

def showmap(request):
    qs = Restaurants.objects.all() # 테이블의 모든 row를 할당
    rows = []
    for i in range(len(qs)):
        rows.append(qs.values()[i])
    map_dict = {}
    # 데이터의 키값을 추가해준다.
    for i in range(len(qs)):
        map_dict['item'+str(i)] = ( json.dumps(qs.values()[i], ensure_ascii=False) )
    context = {'rows': map_dict}
    # json으로 포멧한 데이터를 map.html에 보내준다.
    return render(request, 'map/map.html', context)