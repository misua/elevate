from django.shortcuts import render


# Create your views here.

def home(request):

    clientlist =[
        {
            'id': 1,
            'name': 'John wick',
            'occupation': 'electrician',

        },
         {
            'id': 2,
            'name': 'Smith wesson',
            'occupation': 'musician',

        }
    ]


    context = {
        'Mainclientlist': clientlist
    }


    return render(request, 'crm/index.html',context)

def register(request):
    return render(request, 'crm/register.html')