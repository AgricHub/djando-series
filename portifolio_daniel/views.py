from django.shortcuts import render
from .models import Service, CaseStudy, Testimonial
from .forms import ContactForm

def daniel_home(request):
    services = Service.objects.all()
    case_studies = CaseStudy.objects.all()
    testimonials = Testimonial.objects.all()
    contact_form = ContactForm()
    return render(request, 'index.html', {'services': services, 'case_studies': case_studies, 'testimonials': testimonials, 'contact_form': contact_form})
