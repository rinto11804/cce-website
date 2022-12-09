from django.shortcuts import render

from Administration.models import *
from website.models import Hero_Image

# Create your views here.
def governing_body(request):
    governing_body_data = GoverningBody.objects.all()
    context = {
        "governing_body_data": governing_body_data,
    }
    return render(request, "Administration/governing_body.html", context)

def iqac_page(request):
    IQAC_executive_commitee = IQACExecutiveCommitee.objects.all()
    formation_notice = IQACFormationNotice.objects.all()
    hero_img = Hero_Image.objects.filter(page="iqac").first()
    return render(request, 'Administration/IQAC.html',context={"IQAC_executive_commitee":IQAC_executive_commitee,"formation_notice":formation_notice,'hero_img':hero_img,'hero_title':'Internal Quality Assurance Cell (IQAC)'})
