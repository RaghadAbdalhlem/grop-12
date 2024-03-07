from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from .views import aboutus
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import addapartment
from .forms import addApartmentform
from django.contrib import messages  
from django.core.exceptions import ValidationError  
from django.urls import reverse  

from .models import Apartment  
from .forms import AddApartmentForm  





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
################################################################################
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
    self.assertTrue(soup.find('h1'))
    self.assertEqual(response.status_code, 150)
######################################################



class AddApartmentPageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_apartment_page_GET(self):
      
        request = self.factory.get('/addapartment/')
        response = addapartment(request)

       
        self.assertEqual(response.status_code, 200)

       
        self.assertTemplateUsed(response, 'pages/addapartment.html')

    def test_add_apartment_page_POST_valid_form(self):
     
        form_data = {
            'field1': 'value1',
            'field2': 'value2',
            
        }
        request = self.factory.post('/addapartment/', data=form_data)
        response = addapartment(request)

        
        self.assertRedirects(response, reverse('addclasses'))

    def test_add_apartment_page_POST_invalid_form(self):
        
        form_data = {
            
        }
        request = self.factory.post('/addapartment/', data=form_data)
        response = addapartment(request)

        
        self.assertEqual(response.status_code, 200)

        
        self.assertTemplateUsed(response, 'pages/addapartment.html')
        self.assertTrue('form' in response.context)
        self.assertFalse(response.context['form'].is_valid())











@pytest.mark.django_db
def test_addapartment_get(client):
    """Tests the GET request behavior of addapartment."""

    response = client.get(reverse('addapartment'))

   
    assert response.template_name == 'pages/addapartment.html'

    
    form = response.context_data['form']
    assert isinstance(form, AddApartmentForm)
    assert not form.has_bound_data()  

def test_addapartment_post_valid(client):
    """Tests the POST request behavior with valid data."""

    
    valid_data = {
        'title': 'Test Apartment',
        'description': 'This is a test apartment.',
        'price': 1000,
        
    }

    response = client.post(reverse('addapartment'), valid_data)

    
    assert response.status_code == 302
    assert response.url == reverse('addclasses')

   
    apartment = Apartment.objects.get(title=valid_data['title'])
    assert apartment.description == valid_data['description']
    assert apartment.price == valid_data['price']

def test_addapartment_post_invalid(client):
    """Tests the POST request behavior with invalid data."""

   
    invalid_data = {
        'title': 'Test Apartment',
        
    }

    with pytest.raises(ValidationError):  
        response = client.post(reverse('addapartment'), invalid_data)

   
    assert response.status_code == 200
    assert response.template_name == 'pages/addapartment.html'
    form = response.context_data['form']
    assert form.is_bound  
    assert form.errors  

