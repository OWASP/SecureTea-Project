# -*- coding: utf-8 -*-

def get_config():
    """Get default configuration credentials."""
    return {
        "twitter": {
            "api_key": "XXXX",
            "api_secret_key": "XXXX",
            "access_token": "XXXX",
            "access_token_secret": "XXXX"
        },
        "malware_analysis": {
            "mode": "XXXX",
            'filename':"XXXX",
            'virustotal_api_key':"XXXX"
        },
        "telegram": {
            "token": "XXXX",
            "user_id": "XXXX"
        },
        "twilio": {
            "twilio_sid": "XXXX",
            "twilio_token": "XXXX",
            "twilio_from": "XXXX",
            "twilio_to": "XXXX"
        },
        "whatsapp": {
            "whatsapp_sid": "XXXX",
            "whatsapp_token": "XXXX",
            "whatsapp_from": "XXXX",
            "whatsapp_to": "XXXX"
        },
        "slack": {
            "token": "XXXX",
            "user_id": "XXXX"
        },
        "aws_ses": {
            "aws_email": "XXXX",
            "aws_access_key": "XXXX",
            "aws_secret_key": "XXXX"
        },
        "gmail": {
            "sender_email": "XXXX",
            "to_email": "XXXX",
            "password": "XXXX"
        },
        "firewall": {
            "interface": "",
            "inbound_IPRule": {
                "action": "0",
                "ip_inbound": ""
            },
            "outbound_IPRule": {
                "action": "0",
                "ip_outbound": ""
            },
            "protocolRule": {
                "action": "0",
                "protocols": "ICMP"
            },
            "scanLoad": {
                "action": "0",
                "extensions": ".exe"
            },
            "source_portRule": {
                "action": "0",
                "sports": ""
            },
            "dest_portRule": {
                "action": "0",
                "dports": ""
            },
            "HTTPRequest": {
                "action": "0"
            },
            "HTTPResponse": {
                "action": "0"
            },
            "DNSRule": {
                "action": "0",
                "dns": ""
            },
            "time": {
                "time_lb": "00:00",
                "time_ub": "23:59"
            }
        },
        "insecure_headers": {
                "url": ""
        },
        "waf": {
            "listen_ip": "127.0.0.1",
            "listen_port": 8865,
            "mode": 0,
            "backend_server_config": "{}"
        },
        "ids": {
            "threshold": 10,
            "eligibility_threshold": 0.5,
            "severity_factor": 0.9,
            "interface": "XXXX"
        },
        "server-log": {
            "log-type": "",
            "log-file": "",
            "window": "30",
            "ip-list": "",
            "status-code": ""
        },
        "auto-server-patcher": {
            "url": "XXXX",
            "apache": "1",
            "sysctl": "1",
            "login": "1",
            "ssh": "1"
        },
        "web-deface": {
            "path": "",
            "server-name": ""
        },
        "antivirus": {
            "update": "1",
            "custom-scan": "",
            "auto-delete": "0",
            "monitor-usb": "1",
            "monitor-file-changes": "1",
            "virustotal-api-key": "XXXX"
        },
        "iot-check": {
            "shodan-api-key": "XXXX",
            "ip": ""
        },
        "social_eng": {
            "email": "XXXX"
        },
        "history_logger": 0,
        "clamav": 0,
        "yara": 0,
        "debug": 0
    }
