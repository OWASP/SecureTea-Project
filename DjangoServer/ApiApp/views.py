from django.conf.urls import url
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json, requests, subprocess, os

from ApiApp.core.meta_info import MetaInfo
from ApiApp.core.cmdrunner import Runner

# Create your views here.

@csrf_exempt
def get_meta(request):
    print('in get_meta')
    if request.method == 'GET':
        meta_obj = MetaInfo()
        meta = meta_obj.get_meta()
        return JsonResponse(meta, safe=False)

@csrf_exempt
def get_module_meta(request):
    print('in get_module_meta')
    if request.method == 'GET':
        meta_obj = MetaInfo()
        cmd_command = request.GET["module"].strip()
        module_info = meta_obj.get_module_meta(modulename=cmd_command)
        return JsonResponse(module_info, safe=False)

@csrf_exempt
def run_cmd(request):
    print('in run_cmd')
    if request.method == 'GET':
        runner_obj = Runner()
        cmd_recv = request.GET["cmd_list"].strip()
        module_name = request.GET["modulename"].strip()
        res = runner_obj.run_command(cmd_list=cmd_recv, modulename=module_name)
        return JsonResponse(res, safe=False)
        