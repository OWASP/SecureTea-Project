"""Docstring."""
import cpuinfo
import os
import psutil
import signal
import subprocess
import time

from datetime import datetime
from datetime import timedelta
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

diskReadNew = 0
diskReadOld = 0
diskWriteNew = 0
diskWriteOld = 0
processid = False


@app.route('/', methods=['GET'])
def test_api():
    """Docstring.

    Returns:
        TYPE: Description
    """
    return '', 200


@app.route('/uptime', methods=['GET'])
def get_uptime():
    """Docstring.

    Returns:
        TYPE: Description
    """
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
    """Docstring.

    Args:
        data (TYPE): Description
        key (TYPE): Description

    Returns:
        TYPE: Description
    """
    try:
        return data[key]
    except Exception:
        return None


@app.route('/processor', methods=['GET'])
def get_processor():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/cpu', methods=['GET'])
def get_cpu():
    """Docstring.

    Returns:
        TYPE: Description

    Raises:
        e: Description
    """
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
    """Docstring.

    Returns:
        TYPE: Description
    """
    try:
        username = os.getlogin()
        data = {
            "username": username
        }
        return jsonify(data), 200
    except Exception as e:
        print(e)
    return "404", 404


@app.route('/ram', methods=['GET'])
def get_ram():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/swap', methods=['GET'])
def get_swap():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/hdd', methods=['GET'])
def get_hdd():
    """Docstring.

    Returns:
        TYPE: Description
    """
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
    """Docstring.

    Returns:
        TYPE: Description
    """
    try:
        pids = psutil.pids()
        data = get_process_details(pids)
        if data:
            return jsonify(data=data), 200

    except Exception:
        return "404", 404


def get_process_details(pids):
    """Docstring.

    Args:
        pids (TYPE): Description

    Returns:
        TYPE: Description
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


@app.route('/diskio', methods=['GET'])
def getdiskio():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/netio', methods=['GET'])
def getnetworks():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/status', methods=['GET'])
def checkstatus():
    """Docstring.

    Returns:
        TYPE: Description
    """
    global processid
    if processid:
        return '200', 200
    return "204", 204


@app.route('/stop', methods=['GET'])
def stop():
    """Docstring.

    Returns:
        TYPE: Description
    """
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


@app.route('/sleep', methods=['POST', 'GET'])
def sleep():
    """Docstring."""
    global processid
    if request.method == 'GET':
        try:
            if not processid:
                processid = subprocess.Popen(
                    'python SecureTea.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
                return '201', 201
            else:
                return '200', 200
        except Exception as e:
            print(e)
        return "404", 404

    creds = request.get_json()
    # print(creds)
    args_str = ""
    try:
        if len(creds['twitter_api_key']) and len(creds['twitter_api_secret_key']) and len(creds['twitter_access_token']) and len(creds['twitter_access_token_secret']):
            args_str += ' --twitter_api_key="' + creds['twitter_api_key'] + '"'
            args_str += ' --twitter_api_secret_key="' + creds['twitter_api_secret_key'] + '"'
            args_str += ' --twitter_access_token="' + creds['twitter_access_token'] + '"'
            args_str += ' --twitter_access_token_secret="' + creds['twitter_access_token_secret'] + '"'
    except:
        pass
    try:
        if len(creds['telegram_token']) and len(creds['telegram_user_id']):
            args_str += ' --telegram_bot_token="' + creds['telegram_token'] + '"'
            args_str += ' --telegram_user_id="' + creds['telegram_user_id'] + '"'
    except:
        pass
    try:
        if len(creds['twilio_sid']) and len(creds['twilio_token']) and len(creds['twilio_from']) and len(creds['twilio_to']):
            args_str += ' --twilio_sid="' + creds['twilio_sid'] + '"'
            args_str += ' --twilio_token="' + creds['twilio_token'] + '"'
            args_str += ' --twilio_from="' + creds['twilio_from'] + '"'
            args_str += ' --twilio_to="' + creds['twilio_to'] + '"'
    except:
        pass
    try:
        if len(creds['slack_token']) and len(creds['slack_user_id']):
            args_str += ' --slack_token="' + creds['slack_token'] + '"'
            args_str += ' --slack_user_id="' + creds['slack_user_id'] + '"'
    except:
        pass
    try:
        if len(creds['aws_email']) and len(creds['aws_access_key']) and len(creds['aws_secret_key']):
            args_str += ' --aws_secret_key="' + creds['aws_secret_key'] + '"'
            args_str += ' --aws_access_key="' + creds['aws_access_key'] + '"'
            args_str += ' --aws_email="' + creds['aws_email'] + '"'
    except:
        pass
    print(args_str)
    try:
        if not processid:
            processid = subprocess.Popen('python SecureTea.py' + args_str + ' &',
                                         stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
            return '201', 201
        else:
            return '200', 200
    except Exception as e:
        print(e)
    return "404", 404


def findpid():
    """Docstring.

    Returns:
        TYPE: Description
    """
    proce = process()
    if proce[0] == 200:
        response = proce[1].get_data()
        for res in response:
            cmds = res['cmd']
            if 'SecureTea.py' in cmds:
                return res['pid']
    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
