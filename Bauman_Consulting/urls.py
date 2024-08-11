from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    page_Referenzen,
    page_Unterstutzung,
    page_Literatur,
    page_Kontakt,
    page_Unser_Angebot,
    page_Bestellen,
    contact_form_view,
    kaufen_form_view,
    page_Personal_Area,
    plot_contacts_statistics,
    page_Organisatorisches_Sicherheitskonzept,
    page_Technisches_Sicherheitskonzept,
)

urlpatterns = [
    path("", views.index, name="index"),
    path("Unterstutzung/", page_Unterstutzung, name="Unterstutzung"),
    path("Referenzen/", page_Referenzen, name="Referenzen"),
    path("Literatur/", page_Literatur, name="Literatur"),
    path("Kontakt/", page_Kontakt, name="Kontakt"),
    path("Unser_Angebot/", page_Unser_Angebot, name="Unser_Angebot"),
    path("contact/", contact_form_view, name="contact_form"),
    path("kaufen/", kaufen_form_view, name="kaufen_form"),
    path("Bestellen/", page_Bestellen, name="Bestellen"),
    path("Personal_Area/", page_Personal_Area, name="Personal_Area"),
    path("plot/", views.plot_contacts_statistics, name="plot_contacts_statistics"),
    path(
        "Organisatorisches_Sicherheitskonzept/",
        page_Organisatorisches_Sicherheitskonzept,
        name="Organisatorisches_Sicherheitskonzept",
    ),
    path(
        "Technisches_Sicherheitskonzept/",
        page_Technisches_Sicherheitskonzept,
        name="Technisches_Sicherheitskonzept",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
