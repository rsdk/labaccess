from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.mail import send_mail

from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext, loader

from datetime import datetime

from labaccess.models import Verantwortlicher
from labaccess.models import Labor
from labaccess.models import Zugang


def index(request):
    verantwortliche = Verantwortlicher.objects.all()
    context = {'verantwortliche': verantwortliche}
    return render(request, 'labaccess/index.html', context)


def detail(request, labor_id):
    lab = get_object_or_404(Labor, pk=labor_id)
    vw = get_object_or_404(Verantwortlicher, pk=lab.verantwortlicher_id)
    return render(request, 'labaccess/detail.html', {'lab': lab, 'vw': vw})


def anfrage(request, labor_id):
    lab = get_object_or_404(Labor, pk=labor_id)
    vw = get_object_or_404(Verantwortlicher, pk=lab.verantwortlicher_id)
    try:
        s_lname = request.POST['s_lname']
        s_fname = request.POST['s_fname']
        s_mnr = request.POST['s_mnr']
        s_email = request.POST['s_email']
        s_begruendung = request.POST['s_begruendung']
    except (KeyError, Labor.DoesNotExist):
        # Redisplay the question voting form.
        return HttpResponse("Fehler für %s." % labor_id)
    else:
        # Speichern der neuen Anfrage
        neu_anfr = Zugang(zugang_v=vw, zugang_l=lab,
             zugang_vname=s_fname, zugang_nname=s_lname, zugang_matnr=s_mnr,
             zugang_email=s_email, zugang_begruendung=s_begruendung,
             zugang_anfrage_date=timezone.now())
        neu_anfr.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('genehmigung', args=(lab.id,)))


def genehmigung(request, labor_id):
    lab = get_object_or_404(Labor, pk=labor_id)
    return HttpResponse("Genehmigungsanfrage für %s erfolgreich gestellt." % lab.labor_text)


def approve(request):
    vw = get_object_or_404(Verantwortlicher, pk=1)
    anfragen = Zugang.objects.filter(zugang_l=vw)
    anfragen_offen = anfragen.filter(zugang_genehmigt_date__isnull=True)
    app = anfragen.exclude(zugang_genehmigt_date__isnull=True)

    context = {'vw': vw, 'anfragen': anfragen_offen, 'app': app}
    return render(request, 'labaccess/approve.html', context)


def approved(request):
    z_id = request.POST['zid']
    ap = get_object_or_404(Zugang, pk=z_id)

    # Speichern
    ap.zugang_genehmigt_date = timezone.now()
    ap.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('approve'))


def mail(request):
    mail = request.POST['mail']
    vw = get_object_or_404(Verantwortlicher, pk=mail)
    anfragen = Zugang.objects.filter(zugang_l=vw)
    app = anfragen.exclude(zugang_genehmigt_date__isnull=True)


    timestr = timezone.now().strftime(" %d. %B %Y %I:%M%p")
    verantw = vw.titel_text + " " + vw.firstname_text + " " + vw.verantwortlicher_text
    subject = "Laborzugänge " + verantw + timestr

    msg = ""
    for e in app:
        msg += e.zugang_l.labor_text + "; " + e.zugang_matnr
        msg += "; " + e.zugang_vname + "; " + e.zugang_nname
        msg += "; " + e.zugang_matnr + "; " + e.zugang_nname + "\r\n"

    send_mail(subject, msg, 'labaccess@dieneuewi.de',
    ['rnkblr@gmail.com'], fail_silently=False)

    ##TODO lösche die Anfragen aus der DB oder setzt einen Wert für gesendet

    return HttpResponseRedirect(reverse('sent'))


def sent(request):
    return HttpResponse("Mail abgeschickt.")


