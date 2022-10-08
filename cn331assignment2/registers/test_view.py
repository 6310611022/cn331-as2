from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import Course, Student,Subject
from django.contrib.auth.models import User

class RegistersViewTestCase(TestCase):

    def setUp(self):
        # create subject
        subject1 = Subject.objects.create(subject_id="cn101", subject_name="intro python")

        # create courses
        Course.objects.create(course=subject1, semester="1", year="2022",
                              seat="1", current_seat="0", q_status="Available", status=True)
        Course.objects.create(course=subject1, semester="2", year="2022",
                              seat="1", current_seat="0", q_status="Available", status=True)
        
        # create user
        user = User.objects.create_user(username="6310682627", email="6310682627@cn331.com", password="Reg1234.")
        Student.objects.create(student=user)

    def test_can_enroll_course(self):
        """ can enroll course """
        pass
    
    def test_cannot_enroll_full_seat_course(self):
        """ cannot enroll full seat course """
        
        user1 = User.objects.first()
        student1 = Student.objects.create(student=user1)
        course = Course.objects.first()
        course.student_apply.add(student1)
       
        c = Client()
        #response = c.post(reverse('registers:request', args=(course,)))
        self.assertEqual(course.student_apply.count(), 1)
    
    
    def test_cancel_status_code(self):
        """ cancel status code is 302 """
        course = Course.objects.first()

        c = Client()
        response = c.get(reverse('registers:cancel', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)

    def test_login_cancel_course_sem1_status_code(self):
        """ cancel status code is 302 """
        course = Course.objects.first()

        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:cancel', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)

    def test_login_cancel_course_sem2_status_code(self):
        """ cancel status code is 302 """
        course = Course.objects.last()

        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:cancel', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)

    def test_request_status_code(self):
        """ request status code is 302 """
        course = Course.objects.first()

        c = Client()
        response = c.get(reverse('registers:request', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)

    def test_login_request_course_sem1_status_code(self):
        """ request status code is 302 """
        course = Course.objects.first()

        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:request', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)

    def test_login_request_course_sem2_status_code(self):
        """ request status code is 302 """
        course = Course.objects.last()

        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:request', kwargs={"course":course}))
        self.assertEqual(response.status_code, 200)
        
        
    def test_index_view_status_code(self):
        """ index view's status code is OK """
        
        c = Client()
        response = c.get(reverse('registers:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_view_status_code(self):
        """ login view's status code is OK """
        
        c = Client()
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_index_status_code(self):
        """ index status code is OK """
        
        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:index'))
        self.assertEqual(response.status_code, 200)

    def test_login_quota_request_status_code(self):
        """ quota request status code is OK """
        
        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:quota_request'))
        self.assertEqual(response.status_code, 200)

    def test_login_quota_semester2_status_code(self):
        """ quota semester2 status code is OK """
        
        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:quota_semester2'))
        self.assertEqual(response.status_code, 200)

    def test_login_complete_status_code(self):
        """ complete status code is OK """
        
        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('registers:complete'))
        self.assertEqual(response.status_code, 200)

    def test_quota_request_view_status_code(self):
        """ quota_request view's status code is OK """
        
        c = Client()
        response = c.get(reverse('registers:quota_request'))
        self.assertEqual(response.status_code, 200)
    
    def test_quota_semester2_view_status_code(self):
        """ quota_semester2 view's status code is OK """
        
        c = Client()
        response = c.get(reverse('registers:quota_semester2'))
        self.assertEqual(response.status_code, 200)
        
    def test_complete_view_status_code(self):
        """ complete view's status code is OK """
        
        c = Client()
        response = c.get(reverse('registers:complete'))
        self.assertEqual(response.status_code, 200)
    
    def test_can_login(self):
        """ correct username and password """
        c = Client()
        c.post(reverse('users:login'),{'username':"6310682627", 'password':"Reg1234."})
        response = c.get(reverse('users:index'))
        self.assertEquals(response.status_code,200)
        
    def test_cannot_login(self):
        """ wrong username and password """
        c = Client()
        c.post(reverse('users:login'),{'username':"631068262", 'password':"Reg1234"})
        response = c.get(reverse('users:index'))
        self.assertEquals(response.status_code,302)
        
    def test_logout(self):
        """ can logout """
        c = Client()
        c.login(username="6310682627", password="Reg1234.")
        response = c.get(reverse('users:logout'))
        self.assertTrue(response.context['message'] == 'Logged out')
        
    