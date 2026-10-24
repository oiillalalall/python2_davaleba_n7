from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def info(request):
    context = {"name": "ilia", "surname": "zabakhidze", "age": 15, "height": 189}
    return render(request, 'info.html', context)

def hobbies(request):
    hobbies = ["basketball", "gaming", "art", "workout", "coding",  "photography",]
    grade = 10
    context = {"hobbies": hobbies, "grade": grade}
    return render(request, 'hobbies.html', context)
