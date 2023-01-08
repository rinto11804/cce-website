import datetime
from random import shuffle
from django.shortcuts import render
from website.models import *
from django.http import Http404



def home_page(request):
    anouncement = HomeAnouncement.objects.all().first()
    testimonials = Testimonials.objects.all()
    updates = HomeUpdates.objects.all()
    events =  HomeEvents.objects.all().order_by('?')
    gallery_imgs = Gallery.objects.all()
    upcomingEvents = UpcomingEvents.objects.all().filter(date__lte=datetime.date.today())
    recruiters = Recruiters.objects.all()
    recruiters3 = recruiters.order_by('?')
    recruiters2 = recruiters.order_by('?')
    achivements = Achivements.objects.order_by('?')
    context = {"anouncement":anouncement,'Testimonials': testimonials, "updates":updates, "Events": events, "gallery": gallery_imgs,"upcomingEvents": upcomingEvents,"recruiters":recruiters,"recruiters2":recruiters2,"recruiters3":recruiters3,"achivements":achivements}
    return render(request, 'home.html', context=context)





def admission_page(request):
    return render(request, 'admission.html')


def nirf_page(request):
    return render(request, 'nirf.html', context={})


def gallery_page(request):
    gallery_imgs = Gallery.objects.order_by('?')
    context = {"gallery":gallery_imgs}
    return render(request, 'gallery.html', context=context)

def alumini_page(request):
    return render(request, 'Alumini.html')

def facilities_page(request):
    context = {
        "facilities": Facilities.objects.all(),
        "hero_img":Hero_Image.objects.all().filter(page="facilities").first(),
        "hero_title":"Facilities"
    }
    return render(request, 'facilities.html' ,context=context)

def research_page(request,slug):
    
    match slug:
        case "index":
            hero_img = Hero_Image.objects.all().filter(page="research").first()
            hero_title = "Research"
            context = {"hero_img":hero_img,"hero_title":hero_title,"slug":slug}
            
            return render(request, 'researchAndConsultancy/index.html',context=context)
        case 'consultancy':
            return render(request, 'researchAndConsultancy/academic_consultancy.html')
        case 'parternship':
            return render(request, 'researchAndConsultancy/academic_partnership.html')
        case 'conference':
            return render(request, 'researchAndConsultancy/conference.html')
        case 'funded_projects':
            hero_img = Hero_Image.objects.all().filter(page="research").first()
            hero_title = "Funded Projects"
            cse_projects = FundedProjects.objects.all().filter(department="CSE")
            ece_projects = FundedProjects.objects.all().filter(department="ECE")
            eee_projects = FundedProjects.objects.all().filter(department="EEE")
            me_projects = FundedProjects.objects.all().filter(department="ME")
            ce_projects = FundedProjects.objects.all().filter(department="CE")
            bsh_projects = FundedProjects.objects.all().filter(department="BSH")
            context = {"cse_projects":cse_projects,"ece_projects":ece_projects,'eee_projects':eee_projects,"me_projects":me_projects,"ce_projects":ce_projects,"bsh_projects":bsh_projects,"hero_img":hero_img,"hero_title":hero_title,"slug":slug}
            return render(request, 'researchAndConsultancy/funded_projects.html',context=context)
        case 'publications':
            return render(request, 'researchAndConsultancy/publications.html')
        case 'research_guides':
            return render(request, 'researchAndConsultancy/research_guides.html')
        case other:
            raise Http404("Page Kanumanilla")
            

    return render(request, 'research.html')

def test_page(request):
    return render(request, 'Test.html')


def server_error_page(request):
    return render(request, 'Errors/500.html')


def not_found_error_page(request, exception):
    return render(request, 'Errors/404.html')
