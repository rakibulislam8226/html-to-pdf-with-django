
from django.contrib import admin
from django.urls import path
from pdf_render.views import GeneratePdf, home, DownloadPDF

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('generate_pdf/', GeneratePdf.as_view(),name='generate_pdf'),
    path('pdf_download/', DownloadPDF.as_view(), name="pdf_download"),

]
