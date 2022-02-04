from django.shortcuts import render

def main(request):
    return render(request, "base.html") # 나중에 users/main.html 로 수정