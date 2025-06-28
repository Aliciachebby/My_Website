from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you can add logic to save to database or send email
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('contact')
    
    return render(request, 'contact/contact.html')
