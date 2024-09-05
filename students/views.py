from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from students.models import Student

# Create your views here.
class StudentView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        return render(request, 'student-view.html', {
            'student': student,
        })