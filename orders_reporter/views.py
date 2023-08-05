from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
import base64
from django.template.loader import get_template
from django.views import View
from django.http import FileResponse
import xhtml2pdf.pisa as pisa
from .forms import ManufacturerForm
from .models import Manufacturer
from .forms import NoteForm

# Create your views here.{% for manufacturer in manufacturers %}



# def submitted_reports(request):
#     submitted_report = SubmittedReport.objects.all()
#     return render(request, 'submitted_list.html', {'submitted_report':submitted_report})
def feedback(request):
    if request.method == 'POST':
        feedback = NoteForm(request.POST)
        if feedback.is_valid():
            print(">> THE FORM IS VALID")
            new_feedback = feedback.save(commit=True)
            # add some extra fields or do some operations
            new_feedback.save()
            return HttpResponseRedirect(reverse('success_page'))
        else:
            print("!!!! THE FORM ISN'T VALID!")
    else:
        feedback = NoteForm()
    return render(request, 'note.html',{'feedback':feedback})


def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=7,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, "PNG")
    return base64.b64encode(buffer.getvalue()).decode()


def manufacturer_edit(request, pk):
    manufacturer = Manufacturer.objects.get(pk=pk)
    if request.method != 'POST':
        form = ManufacturerForm(instance=manufacturer)

    else:
        form = ManufacturerForm(instance=manufacturer,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manufacturer_list'))

    context = {'manufacturer':manufacturer, 'form':form}
    return render(request,'manufacturer_edit.html', context)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('manufacturer_detail.html')
        manufacturer = get_object_or_404(Manufacturer, pk=kwargs['pk'])
        context = {
            'manufacturer':manufacturer
        }

        pdf = render_to_pdf('manufacturer_detail.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Manufacturer_{}.pdf".format(manufacturer.id)
            content = "inline; filename={}".format(filename)
            download= request.GET.get("download")
            if download:
                content = "attachment; filename={}".format(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")

@login_required
def index(request):
    return render(request,'home.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

@login_required
def my_form_view(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            print(">> THE FORM IS VALID")
            new_manufacturer = form.save(commit=False)
            # add some extra fields or do some operations
            new_manufacturer.owner = request.user
            new_manufacturer.save()
            return HttpResponseRedirect(reverse('manufacturer_list'))
        else:
            print("!!!! THE FORM ISN'T VALID!")
    else:
        form = ManufacturerForm()
    return render(request, 'forms.html', {'form':form})

def success_page(request):
    return render(request, 'submitted.html')

@login_required
def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})


def delete_manufacturer(request, pk):
    manufacturer = Manufacturer.objects.get(pk=pk)
    #if manufacturer.owner != request.user:
        #raise Http404
    manufacturer.delete()
    return redirect(reverse('manufacturer_list'))


from django.shortcuts import render, get_object_or_404
from .models import Manufacturer

@login_required
def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    qr_codes = generate_qr_code("http://cryptoon.pythonanywhere.com/manufacturer/{}".format(pk))

    #if manufacturer.owner != request.user:
        #raise Http404
    #qr_code = generate_qr_code(f"Manufacturer {pk}")
    return render(request, "manufacturer_detail.html", {"manufacturer": manufacturer, "qr_code": qr_codes})



# def report_detail(request,pk):

#     report = get_object_or_404(SubmittedReport, pk=pk)
#     qr_code = generate_qr_code("http://cryptoon.pythonanywhere.com/order_detail/{}".format(pk))
#     return render(request, 'submitted_report.html',{'report':report,"qr_code":qr_code})
