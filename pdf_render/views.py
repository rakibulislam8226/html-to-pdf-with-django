from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import View
from xhtml2pdf import pisa
import datetime



# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    'today': datetime.date.today(), 
    'amount': 39.99,
    'customer_name': 'amra amrai',
    'order_id': 1233434,
}


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        data['user'] = user
        pdf = render_to_pdf('pdf/cirtificate.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf/cirtificate.html', data)
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "cirtificate%s.pdf" %("12341231")
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response


def home(request):
    return render(request, 'pdf/home.html')























