from django.shortcuts import render

def post_list(request):
    return render(request, 'Myapp/post_list.html', {})
