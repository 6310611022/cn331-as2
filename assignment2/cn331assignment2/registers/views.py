from django.shortcuts import render
from .models import Course, Student, Apply, Complete
# Create your views here.

def index(request):
    subjects = Course.objects.all()
    return render(request, 'registers/index.html',{
        'subjects' : subjects 
    })

def quota_request(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
        # return HttpResponseRedirect(reverse('users:login'))
    else:
        student_info = Student.objects.get(pk=request.user)
        course_apply = student_info.student_apply.all()
        other_course = Course.objects.exclude(pk__in=course_apply.values_list('course', flat=True))

        return render(request, 'registers/quota_request.html',{
            'student_info' : student_info,
            'course_apply': course_apply,
            'other_course' : other_course,
        })

def quota_semester2(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
        # return HttpResponseRedirect(reverse('users:login'))
    else:
        student_info = Student.objects.get(pk=request.user)
        course_apply = student_info.student_apply.all()
        other_course = Course.objects.exclude(pk__in=course_apply.values_list('course', flat=True))

        return render(request, 'registers/quota_semester2.html',{
            'student_info' : student_info,
            'course_apply': course_apply,
            'other_course' : other_course,
        })

def complete(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        student_info = Student.objects.get(pk=request.user)
        course_apply = student_info.student_apply.all()
            
        return render(request, 'registers/complete.html',{
            'student_info' : student_info,
            'course_apply': course_apply,
        })

def cancel(request,course):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else: 
        student_info = Student.objects.get(pk=request.user)
        cancel_course = Course.objects.get(pk=course) 

        cancel_course.current_seat -= 1
        cancel_course.q_status = 'Available'
        cancel_course.save()

        Apply.objects.filter(student=student_info,course=cancel_course).delete()
        return quota_request(request)

def request(request,course):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else: 
        student_info = Student.objects.get(pk=request.user)
        request_course = Course.objects.get(pk=course)

        if request_course.q_status == 'Available':
            request_course.current_seat += 1
            if request_course.current_seat == request_course.seat:
                request_course.q_status = 'Full'
            request_course.save()
            Apply.objects.create(student=student_info,course=request_course)
       
        return quota_request(request)