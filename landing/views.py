def landing(request):

    from django.shortcuts import render
    from landing.models import Person



    return render(request, 'landing.html', locals())