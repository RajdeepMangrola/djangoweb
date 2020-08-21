from django.shortcuts import render,HttpResponse
from home.models import Contact


import pickle


file = open('model.pkl','rb')
clf = pickle.load(file)
file.close()



# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mess=request.POST.get('mess')
        contact = Contact(name=name,email=email,mess=mess)
        contact.save()
    return render(request,'index.html')

def covid(request):
    if request.method =="POST":
        mydict = request.POST.get
        fever = int(mydict("fever"))
        bodypain  = int(mydict("bodypain"))
        age = int(mydict("age"))
        runnynose = int(mydict("runnynose"))
        diffbreath = int(mydict("diffbreath"))
        p = clf.predict_proba([[fever,bodypain,age,runnynose,diffbreath]])[0][1]
        p=int(p*100)
        inf={'p':p}
        return render(request,'show.html',inf)

    return render(request,'covid.html')
