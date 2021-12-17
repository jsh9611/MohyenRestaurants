from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'page/main.html') # main을 요청받으면 page/main.html 으로

def eng_main(request):
    return render(request, 'page/eng_main.html') # eng_main을 요청받으면 page/eng_main.html 으로

def map(request):
    return render(request, 'page/map.html') # map을 요청받으면 page/map.html 으로
