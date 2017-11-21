from django.views import generic
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Hash, Virus_hash
from datetime import datetime
import os, hashlib,requests

def temp(request):
    context={
        'all_my_hash': Hash.objects.all(),
        'temp':'True'
    }
    return TemplateResponse(request, 'temp.html', context)
def profile(request):
    context={
        'profile':'True'
    }
    return TemplateResponse(request, 'temp.html', context)
def my_hash(request):
    context={
        'all_my_hash': Hash.objects.all(),
        'my_hash':'True'
    }
    return TemplateResponse(request, 'temp.html', context)

def create(request):
    os.chdir('C:\Users\Zolboo\Desktop\manage')
    a = os.listdir(os.curdir)
    hasher = hashlib.sha256()
    too = 0; m = 0
    for e in a:
        if m < e:
            m = e
            with open(m, 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
            hash = hasher.hexdigest()
            too += 1
        try :
            r = Hash.objects.create(hash_name=m, hash_value=hash, hash_type='0')
        except Exception as e:
            print e

    context ={
        'all_create': Hash.objects.all(),
        'create':'True'

    }
    return TemplateResponse(request, 'temp.html', context)
def virus_hash(request):
    print 'orlooooooooooooooooooooooooooooo'
    Hash.objects.all()
    print 'dahilaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    all = Hash.hash_type[0]
    if all == '1':
        check=Hash.objects.get_queryset()
        Virus_hash.virus_file_name= check.hash_name
        print check
        params = {'apikey': '45ba7a910c1801eb8d37b4ea981d759f80f54104356eccaaeb013516220e4e0f',
                  'resource': '7657fcb7d772448a6d8504e4b20168b8'}
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "gzip,  My Python requests library example client or username"
        }
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                params=params, headers=headers)
        json_response = response.json()
        print '------------virus---------', Hash.hash_name
    else:
        print '-----------------No viruss------------- '
        print Hash.hash_type
    try:
        r = Virus_hash.objects.create(virus_file_name=Hash.hash_name, virus_hash_value=Hash.hash_value, virus_detail='aaa')

    except Exception as e:
        print e

    context={
        'all_virus': Virus_hash.objects.all(),
        'virus_hash':'True'
    }
    return TemplateResponse(request, 'virus_hash.html', context)
def about(request):
    context={
        'about':'True'
    }
    return TemplateResponse(request, 'about.html', context)
