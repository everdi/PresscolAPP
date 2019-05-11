from django.shortcuts import render

# Create your views here.
def login(request):
    if  request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            # Show an error page
            return render(request, 'log/in.html')
    else:
        return render(request, 'log/in.html')