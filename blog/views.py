from django.shortcuts import render


def home(request):
    return render(request,'blog/home.html')   

def about(request):
    return render(request,'blog/about.html')

def browse(request):
    #render a page to take an input

    return {'aagam'}

# def browse_with_details(request):
#     src=request.GET.get('src')
#     print (src)

#     return src




    



# Create your views here.
