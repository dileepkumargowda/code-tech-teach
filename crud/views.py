from django.shortcuts import render, redirect
from .models import Member

# Create your views here.
'''' Views for home button or sitelogo click or index page at starting point of site '''

def index(request):
    return render(request, 'crud/core/home.html', {})

def homepage(request):
    return redirect('/')
    

#============================JAVA MENU==================================
'''' Views for &Group::JAVA '''


'''' Views for &Group::JAVA->JAVAHOME '''
def javahome(request):
    return render(request,'crud/java/home/javahome.html',{})


                #============================JAVA PART-1 ===========================#
'''' Views for &Group::JAVA->JAVAPARTS '''
def javapartone(request):
    return render(request, 'crud/java/parts/part-one/part-one.html', {})


'''' Views for &Group::JAVA->JAVAPARTS->JAVASUBHEADS '''
def javaPartOneSubOne(request):
    return render(request, 'crud/java/parts/part-one/sub-one/part-one-sub-one.html', {})



def javaPartOneSubOne_11(request):
    return render(request, 'crud/java/parts/part-one/sub-one/11.html', {})

def javaPartOneSubOne_12(request):
    return render(request, 'crud/java/parts/part-one/sub-one/12.html', {})

def javaPartOneSubOne_13(request):
    return render(request, 'crud/java/parts/part-one/sub-one/13.html', {})

def javaPartOneSubOne_14(request):
    return render(request, 'crud/java/parts/part-one/sub-one/14.html', {})



def javaPartOneSubOne_21(request):
    return render(request, 'crud/java/parts/part-one/sub-one/21.html', {})

def javaPartOneSubOne_22(request):
    return render(request, 'crud/java/parts/part-one/sub-one/22.html', {})

def javaPartOneSubOne_23(request):
    return render(request, 'crud/java/parts/part-one/sub-one/23.html', {})

def javaPartOneSubOne_24(request):
    return render(request, 'crud/java/parts/part-one/sub-one/24.html', {})


def javaPartOneSubOne_31(request):
    return render(request, 'crud/java/parts/part-one/sub-one/31.html', {})

def javaPartOneSubOne_32(request):
    return render(request, 'crud/java/parts/part-one/sub-one/32.html', {})

def javaPartOneSubOne_33(request):
    return render(request, 'crud/java/parts/part-one/sub-one/34.html', {})

def javaPartOneSubOne_34(request):
    return render(request, 'crud/java/parts/part-one/sub-one/35.html', {})


def javaPartOneSubOne_41(request):
    return render(request, 'crud/java/parts/part-one/sub-one/41.html', {})

def javaPartOneSubOne_42(request):
    return render(request, 'crud/java/parts/part-one/sub-one/42.html', {})

def javaPartOneSubOne_43(request):
    return render(request, 'crud/java/parts/part-one/sub-one/43.html', {})

def javaPartOneSubOne_44(request):
    return render(request, 'crud/java/parts/part-one/sub-one/44.html', {})










def javaPartOneSubTwo(request):
    return render(request, 'crud/java/parts/part-one/sub-two/part-one-sub-two.html', {})

def javaPartOneSubThree(request):
    return render(request, 'crud/java/parts/part-one/sub-three/part-one-sub-three.html', {})




                #============================JAVA PART-2 ===========================#
'''' Views for &Group::JAVA->JAVAPARTS '''
def javaparttwo(request):
    return render(request, 'crud/java/parts/part-two/part-two.html', {})


'''' Views for &Group::JAVA->JAVAPARTS->JAVASUBHEADS '''
def javaPartTwoSubOne(request):
    return render(request, 'crud/java/parts/part-two/sub-one/part-two-sub-one.html', {})

def javaPartTwoSubTwo(request):
    return render(request, 'crud/java/parts/part-two/sub-two/part-two-sub-two.html', {})

def javaPartTwoSubThree(request):
    return render(request, 'crud/java/parts/part-two/sub-three/part-two-sub-three.html', {})

def javaPartTwoSubFour(request):
    return render(request, 'crud/java/parts/part-two/sub-four/part-two-sub-three.html', {})

   


                  #============================JAVA PART-3 ===========================#
'''' Views for &Group::JAVA->JAVAPARTS '''
def javapartthree(request):
    return render(request, 'crud/java/parts/part-three/part-three.html', {})


'''' Views for &Group::JAVA->JAVAPARTS->JAVASUBHEADS '''
def javaPartThreeSubOne(request):
    return render(request, 'crud/java/parts/part-three/sub-one/part-three-sub-one.html', {})

def javaPartThreeSubTwo(request):
    return render(request, 'crud/java/parts/part-three/sub-two/part-three-sub-two.html', {})

def javaPartThreeSubThree(request):
    return render(request, 'crud/java/parts/part-three/sub-three/part-three-sub-three.html', {})

def javaPartThreeSubFour(request):
    return render(request, 'crud/java/parts/part-three/sub-four/part-three-sub-three.html', {})



               #============================JAVA PART-4 ===========================#
'''' Views for &Group::JAVA->JAVAPARTS '''

def javapartfour(request):
    return render(request, 'crud/java/parts/part-four/part-four.html', {})


'''' Views for &Group::JAVA->JAVAPARTS->JAVASUBHEADS '''
def javaPartFourSubOne(request):
    return render(request, 'crud/java/parts/part-four/sub-one/part-four-sub-one.html', {})

def javaPartFourSubTwo(request):
    return render(request, 'crud/java/parts/part-four/sub-two/part-four-sub-two.html', {})

def javaPartFourSubThree(request):
    return render(request, 'crud/java/parts/part-four/sub-three/part-four-sub-three.html', {})

def javaPartFourSubFour(request):
    return render(request, 'crud/java/parts/part-four/sub-four/part-four-sub-four.html', {})




