from django.http import request
from django.shortcuts import render


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


# def name(request):
#     view_name = '变量'
#     return render(request, 'runoob.html', {'name': view_name})


# def name(request):
#     view_list=['列表1','元素2','元素3']
#     return render(request,'runoob.html',{'view_list':view_list})

# def name(request):
#     views_dict={'name':'字典'}
#     return render(request,'runoob.html', {'view_dict':views_dict})

def name(request):
    name=1
    return render(request,'runoob.html',{'name':name})