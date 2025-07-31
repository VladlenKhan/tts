from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm
from django.http import JsonResponse
from django.http import JsonResponse
from tgbot.config import bot, user_ids
from asgiref.sync import async_to_sync


async def send_message_async(message):
    async with bot:
        await bot.send_message(chat_id="-1002152314733", text=message, parse_mode='Markdown')



def home(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            # application.is_checked = False
            # application.save()
            # messages.success(request, 'Application submitted successfully.')
            comment = application.Comment if application.Comment else " - "
            message = (
                f"*Новое предложение получено*\n"
                f"*Форма:* Предложения и вопросы\n\n"
                f"*ФИО:* {application.name}\n"
                f"*Email:* {application.email}\n"
                f"*Номер телефона:* {application.phone_number}\n"
                f"*Сообщение:* {comment}"
            )

            async_to_sync(send_message_async)(message)
            return JsonResponse({'success': True})  # Ответ в формате JSON для успешной отправки формы
        else:          
            return JsonResponse({'success': False})  # Ответ в формате JSON с ошибками валидации
    else:
        form = ApplicationForm()

    context = {
        'form': form
    }

    return render(request, 'home.html', context)


def feedback_form(request):
    if request.method == 'POST':
        quality_rating = request.POST.get('quality_rating')
        competence_rating = request.POST.get('competence_rating')
        service_rating = request.POST.get('service_rating')
        suggestions = request.POST.get('suggestions', '')

        # Вывод данных в терминал
        message = (
            f"*Новая оценка услуг получена*\n"
            f"*Форма:* Оценка услуг\n\n"
            f"*Оценка качества проводимых испытаний:* {quality_rating}/10\n"
            f"*Оценка компетентности персонала:* {competence_rating}/10\n"
            f"*Оценка качества обслуживания клиентов:* {service_rating}/10\n"
            f"*Предложения и комментарии:* {suggestions}"
        )

        async_to_sync(send_message_async)(message)

        # Возвращаем успешный ответ для AJAX запроса
        return redirect("home")




def certificate(request):
    return render(request, 'certificate.html')


def complaint(request):

    return render(request, "complaint.html")


def price_list(request):
    return render(request, 'price-list.html')


def application_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        comment = request.POST.get('Comment')

        if not name or not email or not phone_number or not comment:
            return JsonResponse({'success': False, 'error': 'Все поля должны быть заполнены'}, status=400)

        # Форматирование сообщения
        message = (
            f"*Новая жалоба получена*\n"
            f"*Форма:* Жалобы и претензии\n\n"
            f"*ФИО:* {name}\n"
            f"*Email:* {email}\n"
            f"*Номер телефона:* {phone_number}\n"
            f"*Сообщение:* {comment}"
        )

        # Отправка сообщения через бота
        async_to_sync(send_message_async)(message)

        # Ответ с JSON объектом для AJAX запроса
        return JsonResponse({'success': True, 'message': 'Форма успешно отправлена!'}, status=200)

    return render(request, 'complaint.html')


def agreement(request):
    return render(request, 'agreement.html')
