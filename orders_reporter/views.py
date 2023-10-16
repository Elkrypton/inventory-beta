#importing all modules from one file
from .modules import *

class TotalNumoProducts():
    """Total number of products"""

    def __init__(self):
        self.manufacturer = Manufacturer.objects.all().values()

    def total_number_of_products(self):
        items_list = [value['item'] for value in self.manufacturer]
        return dict(Counter(items_list))
    
    def __str__(self):
        return "Class includes all products counts and quantity for each"

class GeneratePDF(View):
    """Class to generate PDF from web page"""

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

def QRCodeScanner(request):

    return render(request, 'qrcode.html')

def product_search(request):

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():

            query = form.cleaned_data.get('query')
            results = Manufacturer.objects.filter(item=query) | Manufacturer.objects.filter(sku=query)
        else:

            results = []

    else:

        form = SearchForm()
        results = []
        
    return render(request, 'search.html', {'form': form, 'results': results})


def GraphView(request):
    item_counts = TotalNumoProducts().total_number_of_products()
    manufacturer = TotalNumoProducts().manufacturer

    products =[values['item'] for values in manufacturer]
    quantities = [values['quantity'] for values in manufacturer]

    
    items = list(item_counts.keys())
    counts = list(item_counts.values())

    context = {'items': items, 'counts': counts, 'products':products, 'quantities':quantities}
    return render(request, 'graph.html', context)


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
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, "PNG")
    return base64.b64encode(buffer.getvalue()).decode()


@permission_required('manufacturer_edit', raise_exception=True)
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
@permission_required('my_form_view',raise_exception=True)
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


@permission_required('delete_manufacturer', raise_exception=True)
def delete_manufacturer(request, pk):

    manufacturer = Manufacturer.objects.get(pk=pk)
    manufacturer.delete()
    return redirect(reverse('manufacturer_list'))



@login_required
def manufacturer_detail(request, pk):

    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    qr_codes = generate_qr_code("http://127.0.0.1:8000/manufacturer/{}".format(pk))
    return render(request, "manufacturer_detail.html", {"manufacturer": manufacturer, "qr_code": qr_codes})
