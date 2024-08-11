from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import FileResponse
import os
from django.conf import settings  # добавьте этот импорт
from .forms import ContactFormForm, KaufenFormForm
from django.core.mail import send_mail
from .models import ContactForm

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

#import matplotlib.pyplot as plt
import io
import urllib, base64
from django.db.models import Count
from datetime import datetime


def contact_form_view(request):

    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()

            # Отправка email
            subject = "New contact form submission"
            message = f"""
            Thema: {form.cleaned_data['thema']}
            Vorname: {form.cleaned_data['vorname']}
            Nachname: {form.cleaned_data['nachname']}
            Firma: {form.cleaned_data['firma']}
            Telephone: {form.cleaned_data['telephone']}
            E-mail: {form.cleaned_data['email']}
            Betreff: {form.cleaned_data['betreff']}
            Nachricht: {form.cleaned_data['nachricht']}
            """
            recipient_list = ["peter.baumann.sulz@bluewin.ch"]  # Замените на ваш email адрес

            send_mail(subject, message, "sender@example.com", recipient_list)

            return redirect("index")  # Перенаправить на домашнюю страницу
    else:
        form = ContactFormForm()
    return render(request, "contact_form.html", {"form": form})


def kaufen_form_view(request):
    if request.method == "POST":
        form = KaufenFormForm(request.POST)
        if form.is_valid():
            form.save()
            # Отправка email
            subject = "New contact form submission"
            message = f"""
            ---------------Rechnungsadresse---------------
            Vorname: {form.cleaned_data['vorname']}
            Nachname: {form.cleaned_data['nachname']}
            Firma: {form.cleaned_data['firma']}
            Telephone: {form.cleaned_data['telephone']}
            E-mail: {form.cleaned_data['email']}
            Betreff: {form.cleaned_data['betreff']}
            Strasse: {form.cleaned_data['strasse']}
            Hausnummer: {form.cleaned_data['hausnummer']} 
            PLZ: {form.cleaned_data['plz']}
            Ort: {form.cleaned_data['ort']} 
            Nachricht: {form.cleaned_data['nachricht']}
            ---------------Lieferadresse------------------
            Vorname: {form.cleaned_data['vorname_l']}
            Nachname: {form.cleaned_data['nachname_l']}
            Firma: {form.cleaned_data['firma_l']}
            Telephone: {form.cleaned_data['telephone_l']}
            E-mail: {form.cleaned_data['email_l']}
            Betreff: {form.cleaned_data['betreff_l']}
            Strasse: {form.cleaned_data['strasse_l']}
            Hausnummer: {form.cleaned_data['hausnummer_l']} 
            PLZ: {form.cleaned_data['plz_l']}
            Ort: {form.cleaned_data['ort_l']}
            Nachricht: {form.cleaned_data['nachricht_l']}
            """
            recipient_list = ["peter.baumann.sulz@bluewin.ch"]  # Замените на ваш email адрес

            send_mail(subject, message, "sender@example.com", recipient_list)

            print("Форма сохранена успешно")
            return redirect("index")
        else:
            print("Форма недействительна", form.errors)
    else:
        form = KaufenFormForm()
    return render(request, "utils/buttons/Bestellen.html", {"form": form})


def index(request):
    return render(request, "Home.html")


def page_Unterstutzung(request):
    return render(request, "utils/buttons/Unterstutzung.html")


def page_Referenzen(request):
    return render(request, "utils/buttons/Referenzen.html")


def page_Literatur(request):
    return render(request, "utils/buttons/Literatur.html")


def page_Kontakt(request):
    return render(request, "utils/buttons/Kontakt.html")


def page_Unser_Angebot(request):
    return render(request, "utils/buttons/Unser_Angebot.html")


def page_Bestellen(request):
    return render(request, "utils/buttons/Bestellen.html")


def page_Organisatorisches_Sicherheitskonzept(request):
    return render(request, "utils/buttons/Organisatorisches_Sicherheitskonzept.html")


def page_Technisches_Sicherheitskonzept(request):
    return render(request, "utils/buttons/Technisches_Sicherheitskonzept.html")


def page_Personal_Area(request):
    # Получаем данные из базы данных
    contacts = ContactForm.objects.all()

    # Получаем статистику (например, количество контактов)
    contacts_count = (
        contacts.count()
    )  # Это просто пример, вы можете использовать любую другую логику для получения статистики

    # Передаем контакты и статистику в контекст
    context = {
        "contacts": contacts,
        "contacts_count": contacts_count,
    }

    # Рендерим шаблон с передачей контекста
    return render(request, "utils/Personal_Area/Personal_Area.html", context)


def pdf_view(request):
    # Замените 'example.pdf' на фактический путь к вашему PDF-файлу в директории 'media'
    pdf_path = os.path.join(settings.MEDIA_ROOT, "example.pdf")

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            response = FileResponse(pdf_file, content_type="application/pdf")
            return response
    else:
        return render(request, "pdf_not_found.html")


def plot_contacts_statistics(request):
    # Получаем текущий год
    current_year = datetime.now().year

    # Получаем данные из базы данных, начиная с текущего года
    contacts = ContactForm.objects.filter(created_at__year=current_year)

    # Строим статистику количества контактов по датам
    dates = contacts.values("created_at__date").annotate(count=Count("id"))

    # Разделяем даты и количество контактов
    x = [date["created_at__date"] for date in dates]
    y = [date["count"] for date in dates]

    # Строим график
    plt.figure(figsize=(10, 6))
    plt.plot(
        x, y, marker="o", linestyle="-", color="blue"
    )  # Устанавливаем цвет графика
    plt.xlabel("Date")
    plt.ylabel("Number of Contacts")
    plt.title("Contacts Statistics for Current Year")
    plt.grid(True)
    plt.xticks(rotation=45)  # Поворачиваем подписи по оси X для лучшей читаемости

    # Добавляем стиль ggplot для более красивого дизайна
    plt.style.use("ggplot")

    # Создаем объект для хранения изображения в памяти
    buffer = io.BytesIO()

    # Сохраняем график в объекте
    plt.savefig(buffer, format="png")

    # Получаем данные из объекта
    buffer.seek(0)
    plot_data = buffer.getvalue()

    # Очищаем буфер
    buffer.close()

    # Возвращаем график как HTTP-ответ
    return HttpResponse(plot_data, content_type="image/png")
