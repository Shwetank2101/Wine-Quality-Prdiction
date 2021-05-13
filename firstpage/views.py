from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import smtplib
import joblib
import pandas as pd
# Create your views here.



reloadModel=joblib.load('./models/RFModelforMPG.pkl')


SMTP_HOST = settings.EMAIL_HOST
SMTP_PORT = settings.EMAIL_PORT

def send_email(from_addr, to_addr, subject, message , name):
    msg = f'Sender Mail- {from_addr} \nSubject- {subject} \nFrom- {name}\n\n\n{message}'
    with smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT) as server:
        server.starttls()
        server.login(settings.EMAIL_HOST_USER2, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(from_addr, to_addr, msg)


def index(request):
    if request.method== 'POST':
        message = request.POST.get('message')
        mail = request.POST.get('email')
        name = request.POST.get('name')
        send_email(mail ,settings.EMAIL_HOST_USER,settings.EMAIL_SUBJECT ,message , name)


    return render(request,'index.html')



def Prediction(request):
    context={'a':'Prediction'}
    print(request)
    if request.method== 'POST':
        temp={}
        temp['alcohol'] = request.POST.get('alcohol')
        temp['chlorides'] = request.POST.get('chlorides')
        temp['citric acid'] = request.POST.get('citric_acid')
        temp['density'] = request.POST.get('density')
        temp['fixed acidity'] = request.POST.get('fixed_acidity')
        temp['free sulfur dioxide'] = request.POST.get('free_sulfur_dioxide')
        temp['pH'] = request.POST.get('pH')
        temp['residual sugar'] = request.POST.get('residual_sugar')
        temp['sulphates'] = request.POST.get('sulphates')
        temp['total sulfur dioxide'] = request.POST.get('total_sulfur_dioxide')
        temp['volatile acidity'] = request.POST.get('volatile_acidity')
    testDtaa = pd.DataFrame({'x': temp}).transpose()
    scoreval=reloadModel.predict(testDtaa)[0]
    if scoreval==1:
        scoreval="High"
    elif scoreval==0:
        scoreval="Low"
    else:
        scoreval="Average"
    context={'scoreval':scoreval}
    return render(request,'index.html',context)



def handler404(request,*args,**argv):
    return render(request,'404.html')


