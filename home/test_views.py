from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Testimonial, CollaborateRequest, Inquire, Service
from home.forms import CollaborateForm

class HomeViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.staff_user = User.objects.create_user('staff', 'staff@example.com', 'password', is_staff=True)
        self.user = User.objects.create_user('user', 'user@example.com', 'password')
        self.testimonial = Testimonial.objects.create(name="Test", testimonial="Testimonial test", status=1)
        self.inquiry = CollaborateRequest.objects.create(name="Test Inquiry", email="test@example.com", message="Test Message")
        self.service = Service.objects.create(name="Test Service")
        

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, self.testimonial.testimonial)

    def test_inquiry_view_get(self):
        response = self.client.get(reverse('inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/inquiry.html')
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_inquiry_view_post(self):
        response = self.client.post(reverse('inquiry'), {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'service': '1',
            'message': 'Test Message'
        })
        self.assertEqual(response.status_code, 200)
        print(response.context['form'].errors)  # Check if there are any validation errors
        print(response.context['form'].errors)  # Check if there are any validation errors
        self.assertTrue(CollaborateRequest.objects.filter(email='testuser@example.com').exists())

    def test_inquiry_list_view(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('inquiry_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/inquiryadminlist.html')
        self.assertContains(response, self.inquiry.message)

    def test_archive_inquiry_view(self):
        self.client.login(username='staff', password='password')
        response = self.client.post(reverse('archive_inquiry', args=[self.inquiry.id]))
        self.inquiry.refresh_from_db()
        self.assertTrue(self.inquiry.read)
        self.assertRedirects(response, reverse('inquiry_list'))

    def test_un_archive_inquiry_view(self):
        self.client.login(username='staff', password='password')
        self.inquiry.read = True
        self.inquiry.save()
        response = self.client.post(reverse('un_archive_inquiry', args=[self.inquiry.id]))
        self.inquiry.refresh_from_db()
        self.assertFalse(self.inquiry.read)
        self.assertRedirects(response, reverse('inquiry_list'))
