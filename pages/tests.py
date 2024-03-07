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
        request = HttpRequest()
        response = More(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/More.html')
        self.assertTrue('something' in response.context)
        self.assertIsNotNone(response.context['something'])
        
def test_More():
    request = type('Request', (object,), {'META': {'REQUEST_METHOD': 'GET'}})
    response = More(request)
    assert response.template_name == 'pages/More.html'
    assert response.status_code == 200
    try:
        loader.get_template(response.template_name)
    except TemplateDoesNotExist:
        assert False, 'התבנית לא קיימת'
