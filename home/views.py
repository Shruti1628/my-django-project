from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={'name': 'Shruti','course':'Django'}
    return render(request,'home.html',context)
    #return HttpResponse("""<h1>This Is My HomePage</h1>""")
def about(request):
    return render(request,'about.html')
   # return HttpResponse("Learning Django Step Ny Step By Harry Bhai")
def projects(request):
    return render(request,'projects.html')
   # return HttpResponse("Make My First Portfolio Using Django")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        form_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        form_errors = []

        if not name:
            form_errors.append('Please enter your name.')
        if not email:
            form_errors.append('Please enter your email.')
        if not subject:
            form_errors.append('Please enter a subject.')
        if not message:
            form_errors.append('Please enter your message.')

        if not form_errors:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(
                request,
                'Your message has been submitted successfully!'
            )
            return redirect('contact')

        return render(request, 'contact.html', {
            'form_data': form_data,
            'form_errors': form_errors,
        })

    return render(request, 'contact.html', {'form_data': {}})

    
    #return HttpResponse("Contact me For Job Regarding using my linkedin ")