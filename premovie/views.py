# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import os
from django.shortcuts import render_to_response

def showDiagramSeri(request):

    picname = 0

    if not 'datelist' in request.session:
        filesPath = os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/')
        filePath = str(filesPath) + "/filtDate.txt"
        dateFile = open(filePath, 'r')
        datelist = []
        for date in dateFile.readlines():
            datelist.append(date.strip('\n'))
        request.session['datelist'] = datelist

    datelist = request.session['datelist']

    print datelist

    try:
        dateTime = request.GET['date']

        picname = dateTime.replace('/', '')
    except:
        pass

    print picname

    t = get_template('bigdiagram.html')
    html = t.render(Context({
        'datelist': datelist,
        'totalnum': len(datelist),
        'picname': picname
    }))

    return HttpResponse(html)