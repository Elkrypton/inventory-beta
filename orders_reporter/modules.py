import traceback

try:
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
    from django.shortcuts import render, get_object_or_404
    from .models import Manufacturer
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg') 

except ImportError as err:
    print("----IMPORT ERROR --->\n---> {}".format(err))
    traceback.print_exc()