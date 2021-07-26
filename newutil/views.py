from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def navigator(request):
    navigatortext= request.POST.get('navigator','off')
    if navigatortext == "on":
        return render(request, 'navigator.html')
    else:
        return HttpResponse("error")


def analyse(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    capitalise = request.POST.get('capitalise', 'off')

    if removepunc == "on":
        print("removepunc")
        analysed=""
        punctuations = '''!@#$%^&*(){}:"<>?/.,;'[]~-+_'''
        for char in djtext:
             if char not in punctuations:
                  analysed = analysed + char
        mydict={'purpose':'removed punctuations','analysed_text':analysed}
        djtext=analysed

    if fullcaps == "on":
        print("fullcaps")
        analysed=""
        for char in djtext:
            analysed = analysed + char.upper()
        mydict={'purpose':'changed to uppercase','analysed_text':analysed}
        djtext = analysed

    if newlineremover == "on":
        print("newlineremover")
        analysed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analysed = analysed + char
        mydict = {'purpose': 'removed new lines', 'analysed_text': analysed}
        djtext = analysed

    if extraspaceremover == "on":
        print("extraspaceremover")
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1]== " ":
                pass
            else :
                analysed = analysed + char
        mydict = {'purpose': 'removed extra space', 'analysed_text': analysed}
        djtext = analysed

    if capitalise == "on":
        print("capitalise")
        analysed = djtext.capitalize()
        mydict = {'purpose': 'removed extra space', 'analysed_text': analysed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and capitalise != "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyse.html', mydict)