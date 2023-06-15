from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm
from django.http import JsonResponse
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.is_checked = False
            application.save()
            # messages.success(request, 'Application submitted successfully.')
            return JsonResponse({'success': True})  # Ответ в формате JSON для успешной отправки формы
        else:          
            return JsonResponse({'success': False})  # Ответ в формате JSON с ошибками валидации
    else:
        form = ApplicationForm()

    context = {
        'form': form
    }

    return render(request, 'home.html', context)

def certificate(request):
    return render(request, 'certificate.html')