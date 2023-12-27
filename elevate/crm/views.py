from django.shortcuts import render


# Create your views here.

def home(request):

    examList = [
        {
            'id':1,
            'name':'Science',
            'grade':'12',
        },
        {
            'id':2,
            'name':'Math',
            'grade':'12',
        },
        {
            'id':3,
            'name':'English',
            'grade':'12',
        },
        {
            'id':4,
            'name':'Nepali',
            'grade':'12',
        },
        {
            'id':5,
            'name':'Social',
            'grade':'12',
        },
    ]

    context = { 'exams': examList }

    return render(request, 'crm/index.html',context)

def register(request):
    return render(request, 'crm/register.html')