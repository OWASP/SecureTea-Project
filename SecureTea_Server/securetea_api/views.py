from urllib.parse import uses_fragment
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from numpy import empty
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import User
from .serializers import UserSerializer

from datetime import datetime
from datetime import timedelta

import hashlib
import psutil
import cpuinfo
import os
import time

# Create your views here.

processid = False

"""

{
"username": "fox",
"password": "1234"
}



{
"cookie": "e0a67ce65c6c94bffd7e2f97ed30fa85cdfbed82f87f2913332efd81126af8b0"
}


"""

def is_logged_in(request):
    """
    checks if the cookie value is present in the databse. If present, User is logged in.
    """
    req_data = request.data
    users = User.objects.all()
    if not list(users.filter(cookie=req_data["cookie"])):
        return False
    user = list(users.filter(cookie=req_data["cookie"]))[0]
    print("USER" + str(user))
    if user:
        return True
    else:
        return False

@api_view(['POST'])
def login(request):
    """
    If user exists, Set a cookie to log in
    """
    req_data = request.data

    users = User.objects.all()
    user = list(users.filter(username=req_data["username"], password=req_data["password"]))
    if user:
        user = user[0]
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        user_data = UserSerializer(user).data
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        cookie_string = bytes(user_data["username"] + date_time, 'utf-8')
        cookie_string = hashlib.sha256(cookie_string).hexdigest()
        user.cookie = cookie_string
        user.save()

        return Response(cookie_string)

    else:
        print("Incorrect Credentials")
        return Response(False)

@api_view(['POST'])
def register(request):
    """
    Register new user
    """
    req_data = request.data

    users = User.objects.all()
    user = list(users.filter(username=req_data["username"]))
    if user:
        return Response(False) #if username exists, return False
    else:
        store_corporate = User(username=req_data["username"], password=req_data["password"])
        store_corporate.save()
        return Response(True)

@api_view(["GET"])
def test_api(request):
    """Endpoint to check if the endpoint works or not"""
    return Response('ep_working')

@api_view(["POST"])
def get_uptime(request):
    """Endpoint to get the uptime of the system
        Returns:
            json object of "uptime" mapped to uptime in seconds
    """
    if not is_logged_in(request):
        raise Http404
    try:
        uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        uptime = str(timedelta(seconds=uptime.seconds))
        data = {
            "status": 200,
            "uptime": uptime
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404

@api_view(["POST"])
def get_processor(request):
    """Endpoint to get the uptime of the system
        Returns:
            json object of information containing bits,count, brand, frequency, l3 cache size, l2 cache size, l1 cache size, l1 instruction cache size and vendor
    """
    if not is_logged_in(request):
        raise Http404
    try:
        info = cpuinfo.get_cpu_info()
        data = {
            "status": 200,
            "bits": info["bits"],
            "count": info["count"],
            "brand": info["brand_raw"],
            "hz_advertised": info["hz_advertised"][0],
            "l3_cache_size": info["l3_cache_size"],
            "l2_cache_size": info["l2_cache_size"],
            "l1_data_cache_size": info["l1_data_cache_size"],
            "l1_instruction_cache_size": info["l1_instruction_cache_size"],
            "vendor_id": info["vendor_id_raw"]
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_cpu(request):
    """Endpoint to get information regarding cpu
        Returns:
            json object of information containing percentage usage, number of cpus, percentage usage per cpu
    """
    if not is_logged_in(request):
        raise Http404
    try:
        percent = psutil.cpu_percent()
        count = psutil.cpu_count()
        percpu = psutil.cpu_percent(interval=1, percpu=True)
        data = {
            "status": 200,
            "percentage": percent,
            "count": count,
            "per_cpu": percpu
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_username(request):
    """Endpoint to get information of user logged in
        Returns:
            username of logged in user
    """
    if not is_logged_in(request):
        raise Http404
    try:
        username = os.getlogin()
        data = {
            "status": 200,
            "username": username
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_ram(request):
    """Endpoint to get information regarding ram
        Returns:
            json object of information containing total ram of the system, percentage used, amount used and amount free
    """
    if not is_logged_in(request):
        raise Http404
    try:
        ram = psutil.virtual_memory()
        total = float(ram.total / 1073741824)
        percent = ram.percent
        used = float(ram.used / 1073741824)
        free = float(ram.available / 1073741824)
        data = {
            "status": 200,
            "total": float("{0: .2f}".format(total)),
            "percent": percent,
            "used": float("{0: .2f}".format(used)),
            "free": float("{0: .2f}".format(free))
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_swap(request):
    """Endpoint to get information regarding swap
        Returns:
            json object of information containing total swap memory of the system, percentage used, amount used and amount free
    """
    if not is_logged_in(request):
        raise Http404
    try:
        swap = psutil.swap_memory()
        total = float(swap.total / 1073741824)
        percent = swap.percent
        used = float(swap.used / 1073741824)
        free = float(swap.free / 1073741824)
        data = {
            "status": 200,
            "total": float("{0: .2f}".format(total)),
            "percent": percent,
            "used": float("{0: .2f}".format(used)),
            "free": float("{0: .2f}".format(free))
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_hdd(request):
    """Endpoint to get information regarding ram
        Returns:
            json object of information containing hdd device, path, type of formatting, total hdd available, percentage used, amount used and amount free
    """
    if not is_logged_in(request):
        raise Http404
    try:
        hdd = psutil.disk_partitions()
        data = []
        for each in hdd:
            device = each.device
            path = each.mountpoint
            fstype = each.fstype

            drive = psutil.disk_usage(path)
            total = drive.total
            total = total / 1000000000
            used = drive.used
            used = used / 1000000000
            free = drive.free
            free = free / 1000000000
            percent = drive.percent
            drives = {
                "device": device,
                "path": path,
                "fstype": fstype,
                "total": float("{0: .2f}".format(total)),
                "used": float("{0: .2f}".format(used)),
                "free": float("{0: .2f}".format(free)),
                "percent": percent
            }
            data.append(drives)
        if data:
            data_dict = {
                "status": 200,
                "data": data,
            }
            return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_process(request):
    """Endpoint to get information regarding processes running in the system
        Returns:
            json object of information containing pids and details of the processes runnung in the system
    """
    try:
        pids = psutil.pids()
        data = get_process_details(pids)
        if data:
            data_dict = {
                "status": 200,
                "data": data,
            }
            return Response(data)

    except Exception:
        raise Http404


def get_process_details(pids):
    """Get information regarding a process

    Parameters:
        pid (list) : list of pid of the process
    Returns:
        Dictionary containing pid, command, cpu, name, start time, status, user running it and memory consumed for each process
    """
    processes = []
    for pid in pids:
        pro = {}
        try:
            process = psutil.Process(pid=pid)
            pinfo = process.as_dict(attrs=['pid', 'name', 'username', 'cmdline',
                                           'cpu_percent', 'create_time', 'status', 'memory_percent'])
            pro = {
                "pid": pinfo['pid'],
                "cmd": pinfo['cmdline'],
                "cpu": float("{0: .2f}".format(float(pinfo['cpu_percent']))),
                "name": pinfo['name'],
                "createTime": datetime.fromtimestamp(pinfo['create_time']).strftime("%Y-%m-%d %H:%M:%S"),
                "status": pinfo['status'],
                "username": pinfo['username'],
                "memory": float("{0: .2f}".format(pinfo['memory_percent']))
            }
            processes.append(pro)
        except psutil.NoSuchProcess as e:
            print(e)
        except Exception as e:
            print(e)
    processes = sorted(processes, key=lambda k: (k['cpu'], k['memory']), reverse=True)
    return processes


@api_view(["POST"])
def get_diskio(request):
    """Endpoint to get information regarding diskios
        Returns:
            json object of information containing reads and writes happening
    """
    if not is_logged_in(request):
        raise Http404
    try:
        diskiocounters = psutil.disk_io_counters()
        diskreadold = diskiocounters.read_bytes
        diskwriteold = diskiocounters.write_bytes
        time.sleep(1)
        diskiocounters = psutil.disk_io_counters()
        diskreadnew = diskiocounters.read_bytes
        diskwritenew = diskiocounters.write_bytes
        reads = diskreadnew - diskreadold
        writes = diskwritenew - diskwriteold
        data = {
            "status": 200,
            "read": reads / 1024,
            "write": writes / 1024
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def get_networks(request):
    """Endpoint to get information regarding netios
        Returns:
            json object of information containing packet transfers happening over the network
    """
    if not is_logged_in(request):
        raise Http404
    try:
        data = []
        oldnetio = psutil.net_io_counters(pernic=True)
        time.sleep(1)
        newnetio = psutil.net_io_counters(pernic=True)
        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        for key in oldnetio:
            ipv4 = '_'
            ipv6 = '_'
            try:
                for ad in addrs[key]:
                    if str(ad.family) == 'AddressFamily.AF_INET':
                        ipv4 = ad.address
                    if str(ad.family) == 'AddressFamily.AF_INET6':
                        ipv6 = ad.address
                isup = "yes" if stats[key].isup else "no"
                oldnetwork = oldnetio[key]
                newnetwork = newnetio[key]
                sent = (newnetwork.bytes_sent - oldnetwork.bytes_sent) / 1024
                receive = (newnetwork.bytes_recv - oldnetwork.bytes_recv) / 1024
                net = {
                    "name": key,
                    "sent": sent, 
                    "receive": receive,
                    "isup": isup, 
                    "ipv4": ipv4, 
                    "ipv6": ipv6
                }
                data.append(net)
            except Exception as e:
                print('key' + str(e))
        data_dict = {
            "status": 200,
            "data": data,
        }
        return Response(data)
    except Exception as e:
        print(e)
    raise Http404


@api_view(["POST"])
def check_status(request):
    """Endpoint to get information regarding securetea app running
        Returns:
            get status of securetea app running
    """
    if not is_logged_in(request):
        raise Http404
    global processid
    if processid:
        data = {
            "status": 200
        }
        return Response(data)
    return HttpResponse(status=204)

