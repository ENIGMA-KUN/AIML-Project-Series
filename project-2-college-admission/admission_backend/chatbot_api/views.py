from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def get_admission_info(request):
    # Simulated admission information
    admission_info = {
        'requirements': 'High school transcripts, SAT/ACT scores, personal statement',
        'deadlines': {
            'regular': 'January 15',
            'early_action': 'November 1'
        },
        'majors': ['Computer Science', 'Engineering', 'Business', 'Psychology']
    }
    return JsonResponse(admission_info)