from django.shortcuts import render_to_response
from django.shortcuts import render

from demo.models import Sites
from demo.models import SiteProperties
from django.db import connection

def home(request):
    content = Sites.objects.all()
    return render_to_response('sites.html', {'contents': content})
    
def sites(request):
    content = Sites.objects.all()
    return render_to_response('sites.html', {'contents': content})
    
def sites_details(request, pk):
    siteObject = Sites.objects.get(pk=pk)
    post = SiteProperties.objects.filter(relatedSite=siteObject)
    return render(request, 'sites_details.html', {'post': post})
    
def sum_summary(request):
    content= []
    uniq = []
    sitePropertyObjects = SiteProperties.objects.all()
    for sitePropertyObject in sitePropertyObjects:
        siteNameRef = sitePropertyObject.relatedSite.siteName
        aValueRef = sitePropertyObject.aValue
        bValueRef = sitePropertyObject.bValue
        if siteNameRef not in uniq:
            uniq.append(siteNameRef)
            content.append([siteNameRef, aValueRef, bValueRef])
        else:
            for item in content:
                if item[0]==siteNameRef:
                    item[1]=item[1]+aValueRef
                    item[2]=item[2]+bValueRef
 
    return render(request, 'sum_summary.html', {'post': content})
    
def average_summary(request):
    content = []
    sitesInfo = []
    cursor = connection.cursor()
    for q in cursor.execute('''SELECT * FROM demo_sites'''):
        sitesInfo.append(q)
        
    for p in cursor.execute('''SELECT relatedSite_id, Avg(aValue), Avg(bValue) FROM demo_siteproperties GROUP BY relatedSite_id'''):
        for s in sitesInfo:
            if p[0]==s[0]:
                b = s[1]
        p=p+(b,)
        content.append(p)

    return render(request, 'average_summary.html', {'post': content})