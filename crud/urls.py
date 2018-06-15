from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
   
    url(r'^javahome$', views.javahome, name='javahome'),

    url(r'^javapartone$', views.javapartone, name='javapartone'),
    url(r'^javaparttwo$', views.javaparttwo, name='javaparttwo'),
    url(r'^javapartthree$', views.javapartthree, name='javapartthree'),
    url(r'^javapartfour$', views.javapartfour, name='javapartfour'),

    url(r'^javaPartOneSubOne$', views.javaPartOneSubOne, name='javaPartOneSubOne'),
    url(r'^javaPartOneSubTwo$', views.javaPartOneSubTwo, name='javaPartOneSubTwo'),
    url(r'^javaPartOneSubThree$', views.javaPartOneSubThree, name='javaPartOneSubThree'),

    url(r'^javaPartTwoSubOne$', views.javaPartTwoSubOne, name='javaPartTwoSubOne'),
    url(r'^javaPartTwoSubTwo$', views.javaPartTwoSubTwo, name='javaPartTwoSubTwo'),
    url(r'^javaPartTwoSubThree$', views.javaPartTwoSubThree, name='javaPartTwoSubThree'),
    url(r'^javaPartTwoSubFour$', views.javaPartTwoSubFour, name='javaPartTwoSubFour'),

    url(r'^javaPartThreeSubOne$', views.javaPartThreeSubOne, name='javaPartThreeSubOne'),
    url(r'^javaPartThreeSubTwo$', views.javaPartThreeSubTwo, name='javaPartThreeSubTwo'),
    url(r'^javaPartThreeSubThree$', views.javaPartThreeSubThree, name='javaPartThreeSubThree'),
    url(r'^javaPartThreeSubFour$', views.javaPartThreeSubFour, name='javaPartThreeSubFour'),

    url(r'^javaPartFourSubOne$', views.javaPartFourSubOne, name='javaPartFourSubOne'),
    url(r'^javaPartFourSubTwo$', views.javaPartFourSubTwo, name='javaPartFourSubTwo'),
    url(r'^javaPartFourSubThree$', views.javaPartFourSubThree, name='javaPartFourSubThree'),
    url(r'^javaPartFourSubFour$', views.javaPartFourSubFour, name='javaPartFourSubFour'),
    

    # deep leve of html final calls
    url(r'^javaPartOneSubOne_11$', views.javaPartOneSubOne_11, name='javaPartOneSubOne_11'),
    url(r'^javaPartOneSubOne_12$', views.javaPartOneSubOne_12, name='javaPartOneSubOne_12'),
    url(r'^javaPartOneSubOne_13$', views.javaPartOneSubOne_13, name='javaPartOneSubOne_13'),
    url(r'^javaPartOneSubOne_14$', views.javaPartOneSubOne_14, name='javaPartOneSubOne_14'),

    url(r'^javaPartOneSubOne_21$', views.javaPartOneSubOne_21, name='javaPartOneSubOne_21'),
    url(r'^javaPartOneSubOne_22$', views.javaPartOneSubOne_22, name='javaPartOneSubOne_22'),
    url(r'^javaPartOneSubOne_23$', views.javaPartOneSubOne_23, name='javaPartOneSubOne_23'),
    url(r'^javaPartOneSubOne_24$', views.javaPartOneSubOne_24, name='javaPartOneSubOne_24'),

    url(r'^javaPartOneSubOne_31$', views.javaPartOneSubOne_31, name='javaPartOneSubOne_31'),
    url(r'^javaPartOneSubOne_32$', views.javaPartOneSubOne_32, name='javaPartOneSubOne_32'),
    url(r'^javaPartOneSubOne_33$', views.javaPartOneSubOne_33, name='javaPartOneSubOne_33'),
    url(r'^javaPartOneSubOne_34$', views.javaPartOneSubOne_34, name='javaPartOneSubOne_34'),

    url(r'^javaPartOneSubOne_41$', views.javaPartOneSubOne_41, name='javaPartOneSubOne_41'),
    url(r'^javaPartOneSubOne_42$', views.javaPartOneSubOne_42, name='javaPartOneSubOne_42'),
    url(r'^javaPartOneSubOne_43$', views.javaPartOneSubOne_43, name='javaPartOneSubOne_43'),
    url(r'^javaPartOneSubOne_44$', views.javaPartOneSubOne_44, name='javaPartOneSubOne_44'),

]