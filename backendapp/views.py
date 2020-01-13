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
    # check checkbox values
    removepunc=(request.GET.get('removepunc','Off' ))
    fullcaps=(request.GET.get('fullcaps','Off' ))
    newlineremover=(request.GET.get('newlineremover','Off' ))
    extraspaceremover=(request.GET.get('extraspaceremover','Off' ))
    #print(djtxt)
    #print((removepunc))
    #check with which checkbox is on

    if removepunc=='on':
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        punc_marks = " "
        for char in djtxt:
            if char not in punctuation:
                analyzed = analyzed + char
            elif char in punctuation:
                punc_marks = punc_marks + char

        params = {'purpose':"removed punc is\n"+ punc_marks, 'analyze_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtxt:
            analyzed=analyzed + char.upper()
        params = {'purpose':"changed to Uppercase", 'analyze_text': analyzed}
    # analyze the text
        return render(request, 'analyze.html', params)
    elif (newlineremover == 'on'):
        analyzed = ""
        for char in djtxt:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': "new line removed", 'analyze_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover == 'on'):
         analyzed = ""
         for index,char in enumerate(djtxt):
                if not(djtxt[index] ==" " and djtxt[index+1]==" "):
                    analyzed = analyzed + char

         params = {'purpose': "Extra Space removed ", 'analyze_text': analyzed}
    # analyze the text
         return render(request, 'analyze.html', params)
    else:

        return HttpResponse('Error')


