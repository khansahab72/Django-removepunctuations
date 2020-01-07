from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def fun1(request):
    #to get text

    #to request text
    return render(request,'text.html')

def analyze(request):
    #get the text
    djtxt = (request.GET.get('text','default'))
    removepunc=(request.GET.get('removepunc','Off' ))
    #print(djtxt)
    #print((removepunc))
    if removepunc=='on':
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        punc_marks = " "
        for char in djtxt:
            if char not in punctuation:
                analyzed = analyzed + char
            elif char in punctuation:
                punc_marks = punc_marks + char

        params = {'purpose': punc_marks, 'analyze_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')


