from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from .views import aboutus
class AboutUsPageTest(TestCase):
    def test_about_us_page(self):
       
        request = HttpRequest()
        response = aboutus(request)

       
        self.assertEqual(response.status_code, 200)

        
        self.assertTemplateUsed(response, 'pages/aboutus.html')
        ##########################################################################################################################
        request = type('Request', (object,), {'META': {'REQUEST_METHOD': 'GET'}})

    
    response = aboutus(request)

    
    assert response.template_name == 'pages/aboutus.html'

    
    assert response.status_code == 200
        ###############בדיקת יחידה מAL#####################################################################################
        




class MorePageTest(TestCase):
    def test_more_page(self):
        # יצירת בקשת HTTP GET לדף "More"
        request = HttpRequest()
        response = More(request)

        # בדיקה שהפונקציה חזרה תשובת HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # בדיקה שהתבצעה הפניה לתבנית 'pages/More.html'
        self.assertTemplateUsed(response, 'pages/More.html')
