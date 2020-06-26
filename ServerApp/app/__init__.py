"""Docstring."""
import cpuinfo
import os
import psutil
import signal
import subprocess
import time
import re
import json
import pickle

from datetime import datetime
from datetime import timedelta
from flask import Flask, Blueprint, jsonify, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

diskReadNew = 0
diskReadOld = 0
diskWriteNew = 0
diskWriteOld = 0
processid = False

from app.user.controllers import mod_user, is_logged_in
app.register_blueprint(mod_user)

def check_auth(request):
    """Check if the request is an authorized request

    Parameters:
        request : request to check
    Returns:
        Boolean variable whether the request was authorized or not
    """
    try:
        uname = json.loads(request.args['updates'])['value']
    except:
        try:
            uname = request.json['username']
        except:
            return False
    try:
        return is_logged_in(uname)
    except:
        return False

@app.route('/', methods=['GET'])
def test_api():
    """Endpoint to check if the endpoint works or not"""
    return '', 200


@app.route('/uptime', methods=['POST'])
def get_uptime():
    """Endpoint to get the uptime of the system
        Returns:
            json object of "uptime" mapped to uptime in seconds
    """
    if not check_auth(request):
        return "404", 404
    try:
        uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        uptime = str(timedelta(seconds=uptime.seconds))
        data = {
            "uptime": uptime
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


def get_value(data, key):
    """Get value of data

    Args:
        data : Description
        key : Description

    Returns:
        value mapped to key in the data
    """
    try:
        return data[key]
    except Exception:
        return None


@app.route('/processor', methods=['POST'])
def get_processor():
    """Endpoint to get the uptime of the system
        Returns:
            json object of information containing bits,count, brand, frequency, l3 cache size, l2 cache size, l1 cache size, l1 instruction cache size and vendor
    """
    if not check_auth(request):
        return "404", 404
    try:
        info = cpuinfo.get_cpu_info()
        data = {
            "bits": get_value(info, 'bits'),
            "count": get_value(info, 'count'),
            "brand": get_value(info, 'brand'),
            "hz_advertised": get_value(info, 'hz_advertised'),
            "l3_cache_size": get_value(info, 'l3_cache_size'),
            "l2_cache_size": get_value(info, 'l2_cache_size'),
            "l1_data_cache_size": get_value(info, 'l1_data_cache_size'),
            "l1_instruction_cache_size": get_value(info, 'l1_instruction_cache_size'),
            "vendor_id": get_value(info, 'vendor_id')
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/cpu', methods=['POST'])
def get_cpu():
    """Endpoint to get information regarding cpu
        Returns:
            json object of information containing percentage usage, number of cpus, percentage usage per cpu
    """
    if not check_auth(request):
        return "404", 404
    try:
        percent = psutil.cpu_percent()
        count = psutil.cpu_count()
        percpu = psutil.cpu_percent(interval=1, percpu=True)
        data = {
            "percentage": percent,
            "count": count,
            "per_cpu": percpu
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/username', methods=['GET'])
def get_username():
    """Endpoint to get information of user logged in
        Returns:
            username of logged in user
    """
    if not check_auth(request):
        return "404", 404
    try:
        username = os.getlogin()
        data = {
            "username": username
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/ram', methods=['POST'])
def get_ram():
    """Endpoint to get information regarding ram
        Returns:
            json object of information containing total ram of the system, percentage used, amount used and amount free
    """
    if not check_auth(request):
        return "404", 404
    try:
        ram = psutil.virtual_memory()
        total = float(ram.total / 1073741824)
        percent = ram.percent
        used = float(ram.used / 1073741824)
        free = float(ram.available / 1073741824)
        data = {
            "total": float("{0: .2f}".format(total)),
            "percent": percent,
            "used": float("{0: .2f}".format(used)),
            "free": float("{0: .2f}".format(free))
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/swap', methods=['POST'])
def get_swap():
    """Endpoint to get information regarding swap
        Returns:
            json object of information containing total swap memory of the system, percentage used, amount used and amount free
    """
    if not check_auth(request):
        return "404", 404
    try:
        swap = psutil.swap_memory()
        total = float(swap.total / 1073741824)
        percent = swap.percent
        used = float(swap.used / 1073741824)
        free = float(swap.free / 1073741824)
        data = {
            "total": float("{0: .2f}".format(total)),
            "percent": percent,
            "used": float("{0: .2f}".format(used)),
            "free": float("{0: .2f}".format(free))
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/hdd', methods=['POST'])
def get_hdd():
    """Endpoint to get information regarding ram
        Returns:
            json object of information containing hdd device, path, type of formatting, total hdd available, percentage used, amount used and amount free
    """
    if not check_auth(request):
        return "404", 404
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
            return jsonify(data=data), 200

    except Exception as e:
        print(e)
    return "404", 404


@app.route('/process', methods=['GET'])
def process():
    """Endpoint to get information regarding processes running in the system
        Returns:
            json object of information containing pids and details of the processes runnung in the system
    """
    try:
        pids = psutil.pids()
        data = get_process_details(pids)
        if data:
            return jsonify(data=data), 200

    except Exception:
        return "404", 404


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


@app.route('/diskio', methods=['POST'])
def getdiskio():
    """Endpoint to get information regarding diskios
        Returns:
            json object of information containing reads and writes happening
    """
    if not check_auth(request):
        return "404", 404
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
            "read": reads / 1024,
            "write": writes / 1024
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/netio', methods=['POST'])
def getnetworks():
    """Endpoint to get information regarding netios
        Returns:
            json object of information containing packet transfers happening over the network
    """
    if not check_auth(request):
        return "404", 404
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
                net = {"name": key, "sent": sent, "receive": receive,
                       "isup": isup, "ipv4": ipv4, "ipv6": ipv6}
                data.append(net)
            except Exception as e:
                print('key' + str(e))
        return jsonify(data=data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/status', methods=['POST'])
def checkstatus():
    """Endpoint to get information regarding securetea app running
        Returns:
            get status of securetea app running
    """
    if not check_auth(request):
        return "404", 404
    global processid
    if processid:
        return '200', 200
    return "204", 204


@app.route('/stop', methods=['POST'])
def stop():
    """Endpoint to stop running securetea app"""
    if not check_auth(request):
        return "404", 404
    global processid
    try:
        if processid:
            pid = findpid()
            if pid:
                os.killpg(os.getpgid(pid), signal.SIGTERM)
            processid = None
        return '200', 200
    except Exception as e:
        print(e)

    return "404", 404


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


@app.route('/sleep', methods=['GET', 'POST'])
def sleep():
    """Endpoint to get start running securetea app with given configuration"""
    if not check_auth(request):
        return "404", 404
    global processid
    if request.method == 'GET':
        try:
            if not processid:
                processid = subprocess.Popen(
                    'python3 ../SecureTea.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
                return '201', 201
            else:
                return '200', 200
        except Exception as e:
            print(e)
        return "404", 404

    creds = request.get_json()
    args_str = " --debug --skip_input --skip_config_file "

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

    # Telegram parsing
    if ("telegram_token" in creds and
        "telegram_user_id" in creds):
        if (bool(creds['telegram_token']) and
            bool(creds['telegram_user_id'])):
            args_str += ' --telegram_bot_token="' + creds['telegram_token'] + '"'
            args_str += ' --telegram_user_id="' + creds['telegram_user_id'] + '"'

    # Twilio SMS parsing
    if ("twilio_sid" in creds and
        "twilio_token" in creds and
        "twilio_from" in creds and
        "twilio_to" in creds):
        if (bool(creds['twilio_sid']) and
            bool(creds['twilio_token']) and
            bool(creds['twilio_from']) and
            bool(creds['twilio_to'])):
            args_str += ' --twilio_sid="' + creds['twilio_sid'] + '"'
            args_str += ' --twilio_token="' + creds['twilio_token'] + '"'
            args_str += ' --twilio_from="' + creds['twilio_from'] + '"'
            args_str += ' --twilio_to="' + creds['twilio_to'] + '"'

    # Slack parsing
    if ("slack_token" in creds and
        "slack_user_id" in creds):
        if (bool(creds['slack_token']) and
            bool(creds['slack_user_id'])):
            args_str += ' --slack_token="' + creds['slack_token'] + '"'
            args_str += ' --slack_user_id="' + creds['slack_user_id'] + '"'

    # AWS parsing
    if ("aws_access_key" in creds and
        "aws_email" in creds and
        "aws_secret_key" in creds):
        if (bool(creds['aws_email']) and
            bool(creds['aws_access_key']) and
            bool(creds['aws_secret_key'])):
            args_str += ' --aws_secret_key="' + creds['aws_secret_key'] + '"'
            args_str += ' --aws_access_key="' + creds['aws_access_key'] + '"'
            args_str += ' --aws_email="' + creds['aws_email'] + '"'

    # Gmail parsing
    if ("sender_email" in creds and
        "to_email" in creds and
        "password" in creds):
        if (bool(creds["sender_email"] and
            bool(creds["to_email"]) and
            bool(creds["password"]))):
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
            args_str += ' --virustotal_api_key=' + virustotal_api_key
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
        interface = creds['interface']
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
        interface = get_list(creds['ids_interface'])
        threshold = get_list(creds['threshold'])

        args_str += " --interface=" + interface
        args_str += " --threshold=" + threshold

    # Local Web Deface Detection Parsing
    web_deface = creds['web_deface']
    if web_deface:
        server_name = get_list(creds["server_name"])
        path = get_list(creds["path"])

        args_str += " --web-deface"
        args_str += " --server-name=" + server_name
        args_str += " --path=" + path

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
    print(args_str)
    try:
        if not processid:
            processid = subprocess.Popen('python3 ../SecureTea.py' + args_str + ' &',
                                         stdout=subprocess.PIPE, shell=True,
                                         preexec_fn=os.setsid)
            return '201', 201
        else:
            return '200', 200
    except Exception as e:
        print(e)
    return "404", 404


def findpid():
    """Endpoint to find pid of securetea app
        Returns:
            pid of securetea app
    """
    proce = process()
    if proce[0] == 200:
        response = proce[1].get_data()
        for res in response:
            cmds = res['cmd']
            if 'SecureTea.py' in cmds:
                return res['pid']
    return None

@app.route('/login', methods=['POST'])
def get_login():
    """Get last login details.

    Returns:
        login details of a user
    """
    if not check_auth(request):
        return "404", 404
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
                        login_row = {"name": username, "date": date, "status": status}
                        data.append(login_row)
        return jsonify(data=data), 200
    except Exception as e:
        print(e)
    return "404", 404

db.create_all()
