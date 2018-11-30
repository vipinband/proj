from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def openFeedback(request):
    try:
        val = request.session["status"]
        if val:
            return render(request,"index.html",{"mess":"You Can Give feedback for One Time"})
        else:
            return render(request,"feedback.html")
    except KeyError:
        return render(request, "feedback.html")

def saveFeedback(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    mess = request.POST.get("t3")

    from .models import Feebback
    f = Feebback(name=name,cno=cno,message=mess)
    f.save()

    request.session["status"] = True

    return render(request,"index.html",{"mess":"Feedback Given"})