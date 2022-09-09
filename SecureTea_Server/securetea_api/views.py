from urllib.parse import uses_fragment
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
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
import signal
import subprocess
import re
import json


# Create your views here.

processid = False

def is_logged_in(request):
    """
    checks if the cookie value is present in the databse. If present, User is logged in.
    """

    req_data = request.data
    users = User.objects.all()
    try:
        if not list(users.filter(cookie=req_data["cookie"])):
            return False
    except KeyError:
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

        data = {
            "cookie" : cookie_string
        }

        

        return Response(data)

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
    data = {
        "status" : "ep_working"
    }
    return Response(data)

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

@api_view(["POST"])
def stop(request):
    """Endpoint to stop running securetea app"""
    if not is_logged_in(request):
        raise Http404
    
    runserver_kill = subprocess.run(["pkill", "-f", "runserver"])
    return Response(status=204)

def get_list(list_var):
    """Returns empty string if variable is None."""
    if list_var:
        return list_var
    else:
        return ""


def get_integer(bool_var):
    """Returns string value for the bool variable."""
    if bool_var:
        return "1"
    else:
        return "0"


@api_view(["GET", "POST"])
def sleep(request):
    """Endpoint to get start running securetea app with given configuration"""  
    if not is_logged_in(request):
        raise Http404
    
    global processid
    if request.method == 'GET':
        try:
            if not processid:
                print("""processid = subprocess.Popen('python3 ../SecureTea.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)""")
                processid = subprocess.Popen(
                    'python3 ../SecureTea.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
                data = {
                    "status": 200
                }
                return Response(data)
            else:
                data = {
                    "status": 200
                }
                return Response(data)
        except Exception as e:
            print(e)
        raise Http404

    creds = request.data
    print(json.dumps(creds, indent=4, sort_keys=True))
    args_str = " --debug --skip_input --skip_config_file "

    if "hist_logger" in creds and creds["hist_logger"]:
        args_str+="--hist "
    
    """
    # Twitter parsing
    if ("twitter_api_key" in creds and
        "twitter_access_token" in creds and
        "twitter_access_token_secret" in creds and
        "twitter_api_secret_key" in creds):
        if (bool(creds['twitter_api_key']) and
            bool(creds['twitter_api_secret_key']) and
            bool(creds['twitter_access_token']) and
            bool(creds['twitter_access_token_secret'])):
            args_str += ' --twitter_api_key="' + creds['twitter_api_key'] + '"'
            args_str += ' --twitter_api_secret_key="' + creds['twitter_api_secret_key'] + '"'
            args_str += ' --twitter_access_token="' + creds['twitter_access_token'] + '"'
            args_str += ' --twitter_access_token_secret="' + creds['twitter_access_token_secret'] + '"'
    """

    # Telegram parsing
    if (creds["telegram_token"] and
        creds["telegram_userId"]):

        args_str += ' --telegram_bot_token="' + creds['telegram_token'] + '"'
        args_str += ' --telegram_user_id="' + creds['telegram_userId'] + '"'

    # Twilio SMS parsing
    if (creds["twilio_sid"] and
        creds["twilio_token"] and
        creds["twilio_from"] and
        creds["twilio_to"]):

        args_str += ' --twilio_sid="' + creds['twilio_sid'] + '"'
        args_str += ' --twilio_token="' + creds['twilio_token'] + '"'
        args_str += ' --twilio_from="' + creds['twilio_from'] + '"'
        args_str += ' --twilio_to="' + creds['twilio_to'] + '"'

    # Whatsapp parsing
    if (creds["whatsapp_sid"] and
        creds["whatsapp_token"] and
        creds["whatsapp_from"] and
        creds["whatsapp_to"]):
        
        args_str += ' --whatsapp_sid="' + creds['whatsapp_sid'] + '"'
        args_str += ' --whatsapp_token="' + creds['whatsapp_token'] + '"'
        args_str += ' --whatsapp_from="' + creds['whatsapp_from'] + '"'
        args_str += ' --whatsapp_to="' + creds['whatsapp_to'] + '"'

    # Slack parsing
    if (creds["slack_token"] and
        creds["slack_userId"]):

        args_str += ' --slack_token="' + creds['slack_token'] + '"'
        args_str += ' --slack_user_id="' + creds['slack_userId'] + '"'

    # AWS parsing
    if (creds["aws_secretKey"] and
        creds["aws_accessKey"] and
        creds["aws_email"]):

        args_str += ' --aws_secret_key="' + creds['aws_secret_key'] + '"'
        args_str += ' --aws_access_key="' + creds['aws_access_key'] + '"'
        args_str += ' --aws_email="' + creds['aws_email'] + '"'

    # Gmail parsing
    if (creds["sender_email"] and
        creds["to_email"] and
        creds["password"]):

        args_str += ' --sender_email="' + creds['sender_email'] + '"'
        args_str += ' --to_email="' + creds['to_email'] + '"'
        args_str += ' --password="' + creds['password'] + '"'

    # AntiVirus parsing
    antivirus = creds['antivirus']
    custom_scan = creds['custom_scan']
    virustotal_api_key = creds['virustotal_api_key']
    update = creds['update']
    auto_delete = creds['auto_delete']
    monitor_usb = creds['monitor_usb']
    monitor_file_changes = creds['monitor_file_changes']

    if antivirus:
        if custom_scan:
            args_str += ' --custom-scan=' + custom_scan
        if virustotal_api_key:
            args_str += ' --virustotal-api-key=' + str(virustotal_api_key)
        if update:
            args_str += ' --update=1'
        else:
            args_str += ' --update=0'
        if auto_delete:
            args_str += ' --auto-delete=1'
        else:
            args_str += ' --auto-delete=0'
        if monitor_usb:
            args_str += ' --monitor-usb=1'
        else:
            args_str += ' --monitor-usb=0'
        if monitor_file_changes:
            args_str += ' --monitor-file-changes=1'
        else:
            args_str += ' --monitor-file-changes=0'

    # Auto Server Patcher parsing
    asp = creds['asp']
    sslvuln = creds['sslvuln']
    apache = creds['apache']
    login = creds['login']
    ssh = creds['ssh']
    sysctl = creds['sysctl']
    asp_state = False

    if asp:
        if sslvuln:
            args_str += ' --ssl --url=' + sslvuln
            asp_state = True
        if apache:
            args_str += ' --apache'
            asp_state = True
        if login:
            args_str += ' --login'
            asp_state = True
        if ssh:
            args_str += ' --ssh'
            asp_state = True
        if sysctl:
            args_str += ' --sysctl'
            asp_state = True

    if asp_state:
        args_str += ' --auto-server-patcher'

    # System Log Parsing
    sys_log = creds['sys_log']
    if sys_log:
        args_str += ' --system_log'

    # Firewall parsing
    firewall = creds['firewall']
    if firewall:
        interface = creds['inter_face']
        ip_inbound = get_list(creds['ip_inbound'])
        inbound_action = get_integer(creds['inbound_action'])
        ip_outbound = get_list(creds['ip_outbound'])
        outbound_action = get_integer(creds['outbound_action'])
        protocols = get_list(creds['protocols'])
        protocol_action = get_integer(creds['protocol_action'])
        extensions = get_list(creds['extensions'])
        scan_load_action = get_integer(creds['scan_load_action'])
        sports = get_list(creds['sports'])
        sports_action = get_integer(creds['sports_action'])
        dest_ports = get_list(creds['dest_ports'])
        dest_ports_action = get_integer(creds['dest_ports_action'])
        dns = get_list(creds['dns'])
        dns_action = get_integer(creds['dns_action'])
        time_lb = creds['time_lb']
        time_ub = creds['time_ub']
        http_req = get_integer(creds['http_req'])
        http_resp = get_integer(creds['http_resp'])

        # Set default values for time
        if not time_lb:
            time_lb = "00:00"
        if not time_ub:
            time_ub = "23:59"

        if interface:
            args_str += " --interface=" + interface

        args_str += " --inbound_IP_list=" + ip_inbound
        args_str += " --inbound_IP_action=" + inbound_action
        args_str += " --outbound_IP_list=" + ip_outbound
        args_str += " --outbound_IP_action=" + outbound_action
        args_str += " --protocol_list=" + protocols
        args_str += " --protocol_action=" + protocol_action
        args_str += " --scan_list=" + extensions
        args_str += " --scan_action=" + scan_load_action
        args_str += " --source_port_list=" + sports
        args_str += " --source_port_action=" + sports_action
        args_str += " --dest_port_list=" + dest_ports
        args_str += " --dest_port_action=" + dest_ports_action
        args_str += " --dns_list=" + dns
        args_str += " --dns_action=" + dns_action
        args_str += " --time_lb=" + time_lb
        args_str += " --time_ub=" + time_ub
        args_str += " --HTTP_request_action=" + http_req
        args_str += " --HTTP_response_action=" + http_resp

    # Server Log Parsing
    server_log = creds['server_log']
    if server_log:
        log_type = get_list(creds['log_type'])
        log_file = get_list(creds['log_file'])
        window = get_list(creds['window'])
        ip_list = get_list(creds['ip_list'])
        status_code = get_list(creds['status_code'])

        args_str += " --log-type=" + log_type
        args_str += " --log-file=" + log_file
        args_str += " --window=" + window
        args_str += " --ip-list=" + ip_list
        args_str += " --status-code=" + status_code

    # Intrusion Detection System
    ids = creds['ids']
    if ids:
        interface = get_list(creds['ids_inter_face'])
        threshold = get_list(creds['threshold'])
        ethreshold = get_list(creds['ethreshold'])
        sfactor = get_list(creds['sfactor'])

        args_str += " --interface=" + interface
        args_str += " --threshold=" + threshold
        args_str += " --eligibility_threshold=" + ethreshold
        args_str += " --severity_factor=" + sfactor

    se_mail_id = get_list(creds["se_mail_id"])
    if se_mail_id:
        args_str += " --social_eng_email=" + se_mail_id

    # Local Web Deface Detection Parsing
    web_deface = creds['web_deface']
    if web_deface:
        server_name = get_list(creds["server_name"])
        path = get_list(creds["path"])

        args_str += " --web-deface"
        args_str += " --server-name=" + server_name
        args_str += " --path=" + path

    # Web Application Firewall Parsing
    waf = creds['waf'] = creds['waf']
    if waf:
        listen_ip = get_list(creds["listen_ip"])
        listen_port = get_list(creds["listen_port"])
        mode = get_list(creds["mode"])
        backend_server_config = get_list(creds["backend_server_config"])

        args_str += " --listenIp=" + listen_ip
        args_str += " --listenPort=" + listen_port
        args_str += " --mode=" + mode
        args_str += " --hostMap=" + backend_server_config

    # IoT Anonymity Checker Parsing
    iot_ano = creds['iot_ano']
    if iot_ano:
        shodan_api_key = get_list(creds["shodan_api"])
        ip_addr_iot = get_list(creds["ip_addr_iot"])

        args_str += " --iot-checker"
        args_str += " --shodan-api-key=" + shodan_api_key
        args_str += " --ip=" + ip_addr_iot

    # Insecure Headers Parsing
    insecure_headers = creds['insecure_headers']
    if insecure_headers:
        url = get_list(creds["url_ih"])

        args_str += " --insecure_headers"
        args_str += " --url=" + url


    print("\033[95m" + args_str + "\033[0m")
    try:
        if not processid:
            print("""processid = subprocess.Popen('python3 ../SecureTea.py' """ + args_str + """ ' &',
                                         stdout=subprocess.PIPE, shell=True,
                                         preexec_fn=os.setsid)""")
            print("Wih args str ------------------------------------------------------------")
            processid = subprocess.Popen('python3 ../SecureTea.py' + args_str + ' &',
                                         stdout=subprocess.PIPE, shell=True,
                                         preexec_fn=os.setsid)
            data = {
                "status": 201
            }
            return Response(data)
        else:
            data = {
                "status": 200
            }
            return Response(data)
    except Exception as e:
        print(e)
    raise Http404

def findpid():
    """Endpoint to find pid of securetea app
        Returns:
            pid of securetea app
    """
    proce = get_process()
    if proce[0] == 200:
        response = proce[1].get_data()
        for res in response:
            cmds = res['cmd']
            if 'SecureTea.py' in cmds:
                print("PID is - " + str(res["pid"]))
                return res['pid']
    return None

@api_view(["POST"])
def get_login(request):
    """Get last login details.

    Returns:
        login details of a user
    """
    if not is_logged_in(request):
        raise Http404
    try:
        data = []

        details_regex = r"([a-zA-Z]+\s[a-zA-Z]+\s+[0-9]+\s[0-9]+:[0-9]+)\s+(.*)"
        username_regex = r"^[a-zA-Z0-9]+\s"

        output = subprocess.check_output("last")
        output = output.decode("utf-8").split("\n")

        for line in output:
            username = re.findall(username_regex, line)
            if username != []:
                username = username[0].strip(" ")
                if username != "reboot":
                    details = re.findall(details_regex, line)
                    if details != []:
                        date = details[0][0]
                        status = details[0][1].strip("-")
                        status = status.strip(" ")
                        login_row = {
                            "status": 200,
                            "name": username, 
                            "date": date, 
                            "login_status": status
                        }
                        data.append(login_row)
        data_dict = {
            "status": 200,
            "data": data,
        }
        return Response(data_dict)
    except Exception as e:
        print(e)
    raise Http404
