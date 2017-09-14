from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm
from .models import Join


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # print
        # "returning FORWARDED_FOR"
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        # print
        # "returning REAL_IP"
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        # print
        # "returning REMOTE_ADDR"
        ip = request.META.get('REMOTE_ADDR')
    return ip


import uuid


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').upper()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id


def share(request, ref_id):
    try:
        join_obj = Join.objects.get(ref_id=ref_id)
        friends_refferd = Join.objects.filter(friend=join_obj)# don't needa
        count = join_obj.referral.all().count()
        ref_url = 'http://' + str(join_obj.ref_id)
        context = {'ref_id': ref_id, 'count':count, 'ref_url': ref_url}
        template = "share.html"
        return render(request, template, context)
    except Join.DoesNotExist:
        raise Http404


def home(request):
    try:
        join_id = request.session['join_id_ref']
        obj = Join.objects.get(id=join_id)
    except:
        obj = None
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_form = form.save(commit=False)
        # in case we want to something do here
        # new_form.save()
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            if not obj == None:
                new_join_old.friend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
        return HttpResponseRedirect(new_join_old .ref_id)
    context = {'form': form}
    template = 'home.html'
    return render(request, template, context)
