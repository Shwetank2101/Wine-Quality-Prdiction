from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# Create your views here.
import joblib

reloadModel=joblib.load('./models/RFModelforMPG.pkl')

def index(request):
    return render(request,'index.html',)

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


