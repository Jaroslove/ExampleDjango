from django.shortcuts import render


def testhome(request):
    context = {}
    template = 'doNotUse.html'
    return render(request, template, context)
