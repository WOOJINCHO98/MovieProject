from urllib import response
from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = '7a0d0069a04f55529285b6584831368c'

def home(request):
    if request.method == 'POST':
        #입력된 내용으로
        #https://api.themoviedb.org/3/search/movie?api_key=7a0d0069a04f55529285b6584831368c&language=en-US&page=1&include_adult=false
        #이 형태의 url 로 get 요청을 보내게 된다.
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query='+ searchword
            resposne = requests.get(url)
            resdata = resposne.text
            
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request,'search.html',{'obj' : obj})
    
    else : 
        form = SearchForm
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        resposne = requests.get(url)
        resdata = resposne.text
        obj = json.loads(resdata)
        obj = obj['results']
    
    return render(request, 'index.html', { 'obj' : obj, 'form' : form })



def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {'resdata' : resdata})