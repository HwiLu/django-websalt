from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from .models import Os

@require_http_methods(["GET"])
def add_os(request):
    response = {}
    try:
        os = Os(os_version=request.GET.get('os_version'))
        os.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_os(request):
    response = {}
    try:
        all_os = Os.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",all_os))
        response['msg'] = 'success'
        response['error_num'] =0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)