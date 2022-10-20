from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    number = 100
    name = 'Sangmin Lee'
    course = ["AI"]
    nums = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {'my_name': name, "course": course})

# model -> html을 위해서는 반드시 view를 거쳐야 함
def coffee_view(request):
    coffee_all = Coffee.objects.all() # 모든 행을 다 가져옴
    # 만약 request가 POST라면
    # POST를 바탕으로 Form을 완성하고
    # Form이 유효하면 저장
    if request.method == "POST":
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = CoffeeForm()
    return render(request, 'coffee.html', {"coffee_list": coffee_all, "coffee_form": form})

def Monthly_Project_I(request):
    learning_list = ["Python을 이용한 자료구조와 알고리즘","인공지능 수학",\
    "데이터 분석 라이브러리(Numpy, Pandas, Matplotlib)","파이썬 웹 프레임워크(Flask, Django)"]
    return render(request, 'Monthly_Project_I.html', {'l_list': learning_list})