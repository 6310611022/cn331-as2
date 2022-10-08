from django.test import TestCase
from .models import Course, Student, Subject
from django.contrib.auth.models import User

# Create your tests here.

class RegistersTestCase(TestCase):

    def setUp(self):
        # create subject
        subject1 = Subject.objects.create(subject_id="cn101", subject_name="intro python")

        # create courses
        Course.objects.create(course=subject1, semester="1", year="2022",
                              seat="1", current_seat="0", q_status="Available", status=True)
        
        
    def test_seat_available(self):
        """ is_seat_available should be True """

        course = Course.objects.filter(status=True).first()
        self.assertTrue(course.is_seat_available())
    
    
    def test_seat_not_available(self):
        """ is_seat_available should be False """

        user1 = User.objects.create(id="6310682627", password="Reg1234.")
        student1 = Student.objects.create(student=user1)

        course = Course.objects.first()
        course.student_apply.add(student1)

        self.assertFalse(course.is_seat_available())
    
    
    def test_no_duplicate_course(self):
        """ duplicate_course should be False """

        subject = Subject.objects.first()
        Course.objects.create(course=subject, semester="2", year="2022",
                              seat="1", current_seat="0", q_status="Available", status=True)
        
        duplicate_course = False


        self.assertFalse(duplicate_course)
        
    
    def test_no_duplicate_student(self):
        """" count_student should be 1 """
        
        user1 = User.objects.create(id="6310682627", password="Reg1234.")
        student1 = Student.objects.create(student=user1)
        subject = Subject.objects.first()
        course = Course.objects.create(course=subject, semester="2", year="2023", seat="2", current_seat="0", q_status="Available", status=True)
        
        course.student_apply.add(student1)
        course.student_apply.add(student1)
        
        count_student = 0
        for student in course.student_apply.all():
            if student.id ==student.id:
                count_student += 1
                
        self.assertEqual(count_student, 1)