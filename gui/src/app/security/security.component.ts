import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { HttpParams } from '@angular/common/http';
import { Router} from '@angular/router';
import $ from 'jquery';
declare var require: any;
const swal = require('sweetalert');

@Component({
  selector: 'app-security',
  templateUrl: './security.component.html',
  styleUrls: ['./security.component.css']
})
export class SecurityComponent implements OnInit {

  apiRoot = '';
  error: String;
  status = '';
  notificationsForm = new FormGroup({
    twitter_apikey: new FormControl(''),
    twitter_apiSecret: new FormControl(''),
    twitter_token: new FormControl(''),
    twitter_tokenSecret: new FormControl(''),
    telegram_token: new FormControl(''),
    telegram_userId: new FormControl(''),
    twilio_sid: new FormControl(''),
    twilio_token: new FormControl(''),
    twilio_from: new FormControl(''),
    twilio_to: new FormControl(''),
    whatsapp_sid: new FormControl(''),
    whatsapp_token: new FormControl(''),
    whatsapp_from: new FormControl(''),
    whatsapp_to: new FormControl(''),
    slack_token: new FormControl(''),
    slack_userId: new FormControl(''),
    aws_email: new FormControl(''),
    aws_secretKey: new FormControl(''),
    aws_accessKey: new FormControl(''),
    sender_email: new FormControl(''),
    to_email: new FormControl(''),
    password: new FormControl(''),
    antivirus: new FormControl(''),
    custom_scan: new FormControl(''),
    virustotal_api_key: new FormControl(''),
    update: new FormControl(''),
    auto_delete: new FormControl(''),
    monitor_usb: new FormControl(''),
    monitor_file_changes: new FormControl(''),
    asp: new FormControl(''),
    apache: new FormControl(''),
    sysctl: new FormControl(''),
    login: new FormControl(''),
    ssh: new FormControl(''),
    sslvuln: new FormControl(''),
    sys_log: new FormControl(''),
    interface: new FormControl(''),
    firewall: new FormControl(''),
    ip_inbound: new FormControl(''),
    inbound_action: new FormControl(''),
    ip_outbound: new FormControl(''),
    outbound_action: new FormControl(''),
    protocols: new FormControl(''),
    protocol_action: new FormControl(''),
    extensions: new FormControl(''),
    scan_load_action: new FormControl(''),
    sports: new FormControl(''),
    sports_action: new FormControl(''),
    dest_ports: new FormControl(''),
    dest_ports_action: new FormControl(''),
    dns: new FormControl(''),
    dns_action: new FormControl(''),
    time_ub: new FormControl(''),
    time_lb: new FormControl(''),
    http_req: new FormControl(''),
    http_resp: new FormControl(''),
    server_log: new FormControl(''),
    log_type: new FormControl(''),
    log_file: new FormControl(''),
    window: new FormControl(''),
    ip_list: new FormControl(''),
    status_code: new FormControl(''),
    ids: new FormControl(''),
    ids_interface: new FormControl(''),
    threshold: new FormControl(''),
    ethreshold: new FormControl(''),
    sfactor: new FormControl(''),
    web_deface: new FormControl(''),
    server_name: new FormControl(''),
    path: new FormControl(''),
    waf: new FormControl(''),
    listen_ip: new FormControl(''),
    listen_port: new FormControl(''),
    mode: new FormControl(''),
    backend_server_config: new FormControl(''),
    iot_ano: new FormControl(''),
    shodan_api: new FormControl(''),
    ip_addr_iot: new FormControl(''),
    insecure_headers: new FormControl(''),
    url_ih: new FormControl(''),
    hist_logger: new FormControl(''),
    se_mail_id: new FormControl('')
  });

  constructor(
    private http: HttpClient, 
    private router: Router
  ) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.checkStatus();

    var twitter_api_key = localStorage.getItem('twitter_api_key')
    if(twitter_api_key)
    {
      this.notificationsForm.value.twitter_apikey = twitter_api_key;
    }
    var twitter_api_secret_key = localStorage.getItem('twitter_api_secret_key')
    if(twitter_api_secret_key)
    {
      this.notificationsForm.value.twitter_apiSecret = twitter_api_secret_key;
    }
    var twitter_access_token = localStorage.getItem('twitter_access_token')
    if(twitter_access_token)
    {
      this.notificationsForm.value.twitter_token = twitter_access_token;
    }
    var twitter_access_token_secret = localStorage.getItem('twitter_access_token_secret')
    if(twitter_access_token_secret)
    {
      this.notificationsForm.value.twitter_tokenSecret = twitter_access_token_secret;
    }
    var telegram_token = localStorage.getItem('telegram_token')
    if(telegram_token)
    {
      this.notificationsForm.value.telegram_token = telegram_token;
    }
    var telegram_user_id = localStorage.getItem('telegram_user_id')
    if(telegram_user_id)
    {
      this.notificationsForm.value.telegram_userId = telegram_user_id;
    }
    var twilio_sid = localStorage.getItem('twilio_sid')
    if(twilio_sid)
    {
      this.notificationsForm.value.twilio_sid = twilio_sid;
    }
    var twilio_token = localStorage.getItem('twilio_token')
    if(twilio_token)
    {
      this.notificationsForm.value.twilio_token = twilio_token;
    }
    var twilio_from = localStorage.getItem('twilio_from')
    if(twilio_from)
    {
      this.notificationsForm.value.twilio_from = twilio_from;
    }
    var twilio_to = localStorage.getItem('twilio_to')
    if(twilio_to)
    {
      this.notificationsForm.value.twilio_to = twilio_to;
    }
    var whatsapp_sid = localStorage.getItem('whatsapp_sid')
    if(whatsapp_sid)
    {
      this.notificationsForm.value.whatsapp_sid = whatsapp_sid;
    }
    var whatsapp_token = localStorage.getItem('whatsapp_token')
    if(whatsapp_token)
    {
      this.notificationsForm.value.whatsapp_token = whatsapp_token;
    }
    var whatsapp_from = localStorage.getItem('whatsapp_from')
    if(whatsapp_from)
    {
      this.notificationsForm.value.whatsapp_from = whatsapp_from;
    }
    var whatsapp_to = localStorage.getItem('whatsapp_to')
    if(whatsapp_to)
    {
      this.notificationsForm.value.whatsapp_to = whatsapp_to;
    }
    var slack_token = localStorage.getItem('slack_token')
    if(slack_token)
    {
      this.notificationsForm.value.slack_token = slack_token;
    }
    var slack_user_id = localStorage.getItem('slack_user_id')
    if(slack_user_id)
    {
      this.notificationsForm.value.slack_userId = slack_user_id;
    }
    var aws_email = localStorage.getItem('aws_email')
    if(aws_email)
    {
      this.notificationsForm.value.aws_email = aws_email;
    }
    var aws_access_key = localStorage.getItem('aws_access_key')
    if(aws_access_key)
    {
      this.notificationsForm.value.aws_accessKey = aws_access_key;
    }
    var aws_secret_key = localStorage.getItem('aws_secret_key')
    if(aws_secret_key)
    {
      this.notificationsForm.value.aws_secretKey = aws_secret_key;
    }
    var sender_email = localStorage.getItem('sender_email')
    if(sender_email)
    {
      this.notificationsForm.value.sender_email = sender_email;
    }
    var to_email = localStorage.getItem('to_email')
    if(to_email)
    {
      this.notificationsForm.value.to_email = to_email;
    }
    var password = localStorage.getItem('password')
    if(password)
    {
      this.notificationsForm.value.password = password;
    }
    var custom_scan = localStorage.getItem('custom_scan')
    if(custom_scan)
    {
      this.notificationsForm.value.custom_scan = custom_scan;
    }
    var virustotal_api_key = localStorage.getItem('virustotal_api_key')
    if(virustotal_api_key)
    {
      this.notificationsForm.value.virustotal_api_key = virustotal_api_key;
    }
    var update = localStorage.getItem('update')
    if(update)
    {
      this.notificationsForm.value.update = update;
    }
    var auto_delete = localStorage.getItem('auto_delete')
    if(auto_delete)
    {
      this.notificationsForm.value.auto_delete = auto_delete;
    }
    var monitor_usb = localStorage.getItem('monitor_usb')
    if(monitor_usb)
    {
      this.notificationsForm.value.monitor_usb = monitor_usb;
    }
    var monitor_file_changes = localStorage.getItem('monitor_file_changes')
    if(monitor_file_changes)
    {
      this.notificationsForm.value.monitor_file_changes = monitor_file_changes;
    }
    var antivirus = localStorage.getItem('antivirus')
    if(antivirus)
    {
      this.notificationsForm.value.antivirus = antivirus;
    }
    var asp = localStorage.getItem('asp')
    if(asp)
    {
      this.notificationsForm.value.asp = asp;
    }
    var apache = localStorage.getItem('apache')
    if(apache)
    {
      this.notificationsForm.value.apache = apache;
    }
    var login = localStorage.getItem('login')
    if(login)
    {
      this.notificationsForm.value.login = login;
    }
    var sysctl = localStorage.getItem('sysctl')
    if(sysctl)
    {
      this.notificationsForm.value.sysctl = sysctl;
    }
    var ssh = localStorage.getItem('ssh')
    if(ssh)
    {
      this.notificationsForm.value.ssh = ssh;
    }
    var sslvuln = localStorage.getItem('sslvuln')
    if(sslvuln)
    {
      this.notificationsForm.value.sslvuln = sslvuln;
    }
    var sys_log = localStorage.getItem('sys_log')
    if(sys_log)
    {
      this.notificationsForm.value.sys_log = sys_log;
    }
    var firewall = localStorage.getItem('firewall')
    if(firewall)
    {
      this.notificationsForm.value.firewall = firewall;
    }
    var interface_var = localStorage.getItem('interface')
    if(interface_var)
    {
      this.notificationsForm.value.interface = interface_var;
    }
    var ip_inbound = localStorage.getItem('ip_inbound')
    if(ip_inbound)
    {
      this.notificationsForm.value.ip_inbound = ip_inbound;
    }
    var inbound_action = localStorage.getItem('inbound_action')
    if(inbound_action)
    {
      this.notificationsForm.value.inbound_action = inbound_action;
    }
    var ip_outbound = localStorage.getItem('ip_outbound')
    if(ip_outbound)
    {
      this.notificationsForm.value.ip_outbound = ip_outbound;
    }
    var outbound_action = localStorage.getItem('outbound_action')
    if(outbound_action)
    {
      this.notificationsForm.value.outbound_action = outbound_action;
    }
    var protocols = localStorage.getItem('protocols')
    if(protocols)
    {
      this.notificationsForm.value.protocols = protocols;
    }
    var protocol_action = localStorage.getItem('protocol_action')
    if(protocol_action)
    {
      this.notificationsForm.value.protocol_action = protocol_action;
    }
    var extensions = localStorage.getItem('extensions')
    if(extensions)
    {
      this.notificationsForm.value.extensions = extensions;
    }
    var scan_load_action = localStorage.getItem('scan_load_action')
    if(scan_load_action)
    {
      this.notificationsForm.value.scan_load_action = scan_load_action;
    }
    var sports = localStorage.getItem('sports')
    if(sports)
    {
      this.notificationsForm.value.sports = sports;
    }
    var sports_action = localStorage.getItem('sports_action')
    if(sports_action)
    {
      this.notificationsForm.value.sports_action = sports_action;
    }
    var dest_ports = localStorage.getItem('dest_ports')
    if(dest_ports)
    {
      this.notificationsForm.value.dest_ports = dest_ports;
    }
    var dest_ports_action = localStorage.getItem('dest_ports_action')
    if(dest_ports_action)
    {
      this.notificationsForm.value.dest_ports_action = dest_ports_action;
    }
    var dns = localStorage.getItem('dns')
    if(dns)
    {
      this.notificationsForm.value.dns = dns;
    }
    var dns_action = localStorage.getItem('dns_action')
    if(dns_action)
    {
      this.notificationsForm.value.dns_action = dns_action;
    }
    var time_ub = localStorage.getItem('time_ub')
    if(time_ub)
    {
      this.notificationsForm.value.time_ub = time_ub;
    }
    var time_lb = localStorage.getItem('time_lb')
    if(time_lb)
    {
      this.notificationsForm.value.time_lb = time_lb;
    }
    var http_req = localStorage.getItem('http_req')
    if(http_req)
    {
      this.notificationsForm.value.http_req = http_req;
    }
    var http_resp = localStorage.getItem('http_resp')
    if(http_resp)
    {
      this.notificationsForm.value.http_resp = http_resp;
    }
    var server_log = localStorage.getItem('server_log')
    if(server_log)
    {
      this.notificationsForm.value.server_log = server_log;
    }
    var log_type = localStorage.getItem('log_type')
    if(log_type)
    {
      this.notificationsForm.value.log_type = log_type;
    }
    var log_file = localStorage.getItem('log_file')
    if(log_file)
    {
      this.notificationsForm.value.log_file = log_file;
    }
    var window = localStorage.getItem('window')
    if(window)
    {
      this.notificationsForm.value.window = window;
    }
    var ip_list = localStorage.getItem('ip_list')
    if(ip_list)
    {
      this.notificationsForm.value.ip_list = ip_list;
    }
    var status_code = localStorage.getItem('status_code')
    if(status_code)
    {
      this.notificationsForm.value.status_code = status_code;
    }
    var ids = localStorage.getItem('ids')
    if(ids)
    {
      this.notificationsForm.value.ids = ids;
    }
    var ids_interface = localStorage.getItem('ids_interface')
    if(ids_interface)
    {
      this.notificationsForm.value.ids_interface = ids_interface;
    }
    var threshold = localStorage.getItem('threshold')
    if(threshold)
    {
      this.notificationsForm.value.threshold = threshold;
    }
    var ethreshold = localStorage.getItem('ethreshold')
    if(ethreshold)
    {
      this.notificationsForm.value.ethreshold = ethreshold;
    }
    var sfactor = localStorage.getItem('sfactor')
    if(sfactor)
    {
      this.notificationsForm.value.sfactor = sfactor;
    }
    var web_deface = localStorage.getItem('web_deface')
    if(web_deface)
    {
      this.notificationsForm.value.web_deface = web_deface;
    }
    var server_name = localStorage.getItem('server_name')
    if(server_name)
    {
      this.notificationsForm.value.server_name = server_name;
    }
    var path = localStorage.getItem('path')
    if(path)
    {
      this.notificationsForm.value.path = path;
    }
    var waf = localStorage.getItem('waf')
    if(waf)
    {
      this.notificationsForm.value.waf = waf;
    }
    var listen_ip = localStorage.getItem('listen_ip')
    if(listen_ip)
    {
      this.notificationsForm.value.listen_ip = listen_ip;
    }
    var listen_port = localStorage.getItem('listen_port')
    if(listen_port)
    {
      this.notificationsForm.value.listen_port = listen_port;
    }
    var mode = localStorage.getItem('mode')
    if(mode)
    {
      this.notificationsForm.value.mode = mode;
    }
    var backend_server_config = localStorage.getItem('backend_server_config')
    if(backend_server_config)
    {
      this.notificationsForm.value.backend_server_config = backend_server_config;
    }
    var iot_ano = localStorage.getItem('iot_ano')
    if(iot_ano)
    {
      this.notificationsForm.value.iot_ano = iot_ano;
    }
    var shodan_api = localStorage.getItem('shodan_api')
    if(shodan_api)
    {
      this.notificationsForm.value.shodan_api = shodan_api;
    }
    var ip_addr_iot = localStorage.getItem('ip_addr_iot')
    if(ip_addr_iot)
    {
      this.notificationsForm.value.ip_addr_iot = ip_addr_iot;
    }
    var insecure_headers = localStorage.getItem('insecure_headers')
    if(insecure_headers)
    {
      this.notificationsForm.value.insecure_headers = insecure_headers;
    }
    var url_ih = localStorage.getItem('url_ih')
    if(url_ih)
    {
      this.notificationsForm.value.url_ih = url_ih;
    }
    var hist_logger = localStorage.getItem('hist_logger')
    if(hist_logger)
    {
      this.notificationsForm.value.hist_logger = hist_logger;
    }
    var se_mail_id = localStorage.getItem('se_mail_id')
    if(se_mail_id)
    {
      this.notificationsForm.value.se_mail_id = se_mail_id;
    }
  }
  isValid()
  {
    return (
              (this.notificationsForm.value.twitter_apikey!="" && this.notificationsForm.value.twitter_apiSecret!=""  && this.notificationsForm.value.twitter_token!="" && this.notificationsForm.value.twitter_tokenSecret!="" ) ||
              (this.notificationsForm.value.telegram_token!=""  && this.notificationsForm.value.telegram_userId!="" ) ||
              (this.notificationsForm.value.twilio_sid!=""  && this.notificationsForm.value.twilio_token!=""  && this.notificationsForm.value.twilio_to!=""  && this.notificationsForm.value.twilio_from!="" ) ||
              (this.notificationsForm.value.whatsapp_sid!=""  && this.notificationsForm.value.whatsapp_token!=""  && this.notificationsForm.value.whatsapp_to!=""  && this.notificationsForm.value.whatsapp_from!="" ) ||
              (this.notificationsForm.value.slack_token!=""  && this.notificationsForm.value.slack_userId!="" ) ||
              (this.notificationsForm.value.aws_email!=""  && this.notificationsForm.value.aws_accessKey!="" && this.notificationsForm.value.aws_secretKey!="" ) ||
              (this.notificationsForm.value.sender_email != "" && this.notificationsForm.value.to_email != "" && this.notificationsForm.value.password != "")
           )
  }
  Submit() {
    const posturl = `${this.apiRoot}sleep`;
    if (this.notificationsForm.valid) {
      this.error = '';
      const data = {
        'username': localStorage.getItem('user_name'),
        'twitter_api_key': this.notificationsForm.value.twitter_apikey,
        'twitter_api_secret_key': this.notificationsForm.value.twitter_apiSecret,
        'twitter_access_token': this.notificationsForm.value.twitter_token,
        'twitter_access_token_secret': this.notificationsForm.value.twitter_tokenSecret,
        'telegram_token': this.notificationsForm.value.telegram_token,
        'telegram_user_id': this.notificationsForm.value.telegram_userId,
        'twilio_sid': this.notificationsForm.value.twilio_sid,
        'twilio_token': this.notificationsForm.value.twilio_token,
        'twilio_from': this.notificationsForm.value.twilio_from,
        'twilio_to': this.notificationsForm.value.twilio_to,
        'whatsapp_sid': this.notificationsForm.value.whatsapp_sid,
        'whatsapp_token': this.notificationsForm.value.whatsapp_token,
        'whatsapp_from': this.notificationsForm.value.whatsapp_from,
        'whatsapp_to': this.notificationsForm.value.whatsapp_to,
        'slack_token': this.notificationsForm.value.slack_token,
        'slack_user_id': this.notificationsForm.value.slack_userId,
        'aws_email': this.notificationsForm.value.aws_email,
        'aws_access_key': this.notificationsForm.value.aws_accessKey,
        'aws_secret_key': this.notificationsForm.value.aws_secretKey,
        'sender_email': this.notificationsForm.value.sender_email,
        'to_email': this.notificationsForm.value.to_email,
        'password': this.notificationsForm.value.password,
        'custom_scan': this.notificationsForm.value.custom_scan,
        'virustotal_api_key': this.notificationsForm.value.virustotal_api_key,
        'update': this.notificationsForm.value.update,
        'auto_delete': this.notificationsForm.value.auto_delete,
        'monitor_usb': this.notificationsForm.value.monitor_usb,
        'monitor_file_changes': this.notificationsForm.value.monitor_file_changes,
        'antivirus': this.notificationsForm.value.antivirus,
        'asp': this.notificationsForm.value.asp,
        'apache': this.notificationsForm.value.apache,
        'login': this.notificationsForm.value.login,
        'sysctl': this.notificationsForm.value.sysctl,
        'ssh': this.notificationsForm.value.ssh,
        'sslvuln': this.notificationsForm.value.sslvuln,
        'sys_log': this.notificationsForm.value.sys_log,
        'firewall': this.notificationsForm.value.firewall,
        'interface': this.notificationsForm.value.interface,
        'ip_inbound': this.notificationsForm.value.ip_inbound,
        'inbound_action': this.notificationsForm.value.inbound_action,
        'ip_outbound': this.notificationsForm.value.ip_outbound,
        'outbound_action': this.notificationsForm.value.outbound_action,
        'protocols': this.notificationsForm.value.protocols,
        'protocol_action': this.notificationsForm.value.protocol_action,
        'extensions': this.notificationsForm.value.extensions,
        'scan_load_action': this.notificationsForm.value.scan_load_action,
        'sports': this.notificationsForm.value.sports,
        'sports_action': this.notificationsForm.value.sports_action,
        'dest_ports': this.notificationsForm.value.dest_ports,
        'dest_ports_action': this.notificationsForm.value.dest_ports_action,
        'dns': this.notificationsForm.value.dns,
        'dns_action': this.notificationsForm.value.dns_action,
        'time_ub': this.notificationsForm.value.time_ub,
        'time_lb': this.notificationsForm.value.time_lb,
        'http_req': this.notificationsForm.value.http_req,
        'http_resp': this.notificationsForm.value.http_resp,
        'server_log': this.notificationsForm.value.server_log,
        'log_type': this.notificationsForm.value.log_type,
        'log_file': this.notificationsForm.value.log_file,
        'window': this.notificationsForm.value.window,
        'ip_list': this.notificationsForm.value.ip_list,
        'status_code': this.notificationsForm.value.status_code,
        'ids': this.notificationsForm.value.ids,
        'ids_interface': this.notificationsForm.value.ids_interface,
        'threshold': this.notificationsForm.value.threshold,
        'ethreshold': this.notificationsForm.value.ethreshold,
        'sfactor': this.notificationsForm.value.sfactor,
        'web_deface': this.notificationsForm.value.web_deface,
        'server_name': this.notificationsForm.value.server_name,
        'path': this.notificationsForm.value.path,
        'waf': this.notificationsForm.value.waf,
        'listen_ip': this.notificationsForm.value.listen_ip,
        'listen_port': this.notificationsForm.value.listen_port,
        'mode': this.notificationsForm.value.mode,
        'backend_server_config': this.notificationsForm.value.backend_server_config,
        'iot_ano': this.notificationsForm.value.iot_ano,
        'shodan_api': this.notificationsForm.value.shodan_api,
        'ip_addr_iot': this.notificationsForm.value.ip_addr_iot,
        'insecure_headers': this.notificationsForm.value.insecure_headers,
        'url_ih': this.notificationsForm.value.url_ih,
        'hist_logger' : this.notificationsForm.value.hist_logger,
        'se_mail_id' : this.notificationsForm.value.se_mail_id
      };
      swal({
        title: 'Are you sure?',
        text: 'This will monitor your system with new configuration.',
        icon: 'warning',
        buttons: ['No', 'Yes'],
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.http.post(
            posturl, 
            data
          ).subscribe((res) => {
            if (res === 201) {
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
              localStorage.setItem('twitter_api_key', this.notificationsForm.value.twitter_apikey);
              localStorage.setItem('twitter_api_secret_key', this.notificationsForm.value.twitter_apiSecret);
              localStorage.setItem('twitter_access_token', this.notificationsForm.value.twitter_token);
              localStorage.setItem('twitter_access_token_secret', this.notificationsForm.value.twitter_tokenSecret);
              localStorage.setItem('telegram_token', this.notificationsForm.value.telegram_token);
              localStorage.setItem('telegram_user_id', this.notificationsForm.value.telegram_userId);
              localStorage.setItem('twilio_sid', this.notificationsForm.value.twilio_sid);
              localStorage.setItem('twilio_token', this.notificationsForm.value.twilio_token);
              localStorage.setItem('twilio_from', this.notificationsForm.value.twilio_from);
              localStorage.setItem('twilio_to', this.notificationsForm.value.twilio_to);
              localStorage.setItem('whatsapp_sid', this.notificationsForm.value.whatsapp_sid);
              localStorage.setItem('whatsapp_token', this.notificationsForm.value.whatsapp_token);
              localStorage.setItem('whatsapp_from', this.notificationsForm.value.whatsapp_from);
              localStorage.setItem('whatsapp_to', this.notificationsForm.value.whatsapp_to);
              localStorage.setItem('slack_token', this.notificationsForm.value.slack_token);
              localStorage.setItem('slack_user_id', this.notificationsForm.value.slack_userId);
              localStorage.setItem('aws_email', this.notificationsForm.value.aws_email);
              localStorage.setItem('aws_access_key', this.notificationsForm.value.aws_accessKey);
              localStorage.setItem('aws_secret_key', this.notificationsForm.value.aws_secretKey);
              localStorage.setItem('sender_email', this.notificationsForm.value.sender_email);
              localStorage.setItem('to_email', this.notificationsForm.value.to_email);
              localStorage.setItem('password', this.notificationsForm.value.password);
              localStorage.setItem('custom_scan', this.notificationsForm.value.custom_scan);
              localStorage.setItem('virustotal_api_key', this.notificationsForm.value.virustotal_api_key);
              localStorage.setItem('update', this.notificationsForm.value.update);
              localStorage.setItem('auto_delete', this.notificationsForm.value.auto_delete);
              localStorage.setItem('monitor_usb', this.notificationsForm.value.monitor_usb);
              localStorage.setItem('monitor_file_changes', this.notificationsForm.value.monitor_file_changes);
              localStorage.setItem('antivirus', this.notificationsForm.value.antivirus);
              localStorage.setItem('asp', this.notificationsForm.value.asp);
              localStorage.setItem('apache', this.notificationsForm.value.apache);
              localStorage.setItem('login', this.notificationsForm.value.login);
              localStorage.setItem('sysctl', this.notificationsForm.value.sysctl);
              localStorage.setItem('ssh', this.notificationsForm.value.ssh);
              localStorage.setItem('sslvuln', this.notificationsForm.value.sslvuln);
              localStorage.setItem('sys_log', this.notificationsForm.value.sys_log);
              localStorage.setItem('firewall', this.notificationsForm.value.firewall);
              localStorage.setItem('interface', this.notificationsForm.value.interface);
              localStorage.setItem('ip_inbound', this.notificationsForm.value.ip_inbound);
              localStorage.setItem('inbound_action', this.notificationsForm.value.inbound_action);
              localStorage.setItem('ip_outbound', this.notificationsForm.value.ip_outbound);
              localStorage.setItem('outbound_action', this.notificationsForm.value.outbound_action);
              localStorage.setItem('protocols', this.notificationsForm.value.protocols);
              localStorage.setItem('protocol_action', this.notificationsForm.value.protocol_action);
              localStorage.setItem('extensions', this.notificationsForm.value.extensions);
              localStorage.setItem('scan_load_action', this.notificationsForm.value.scan_load_action);
              localStorage.setItem('sports', this.notificationsForm.value.sports);
              localStorage.setItem('sports_action', this.notificationsForm.value.sports_action);
              localStorage.setItem('dest_ports', this.notificationsForm.value.dest_ports);
              localStorage.setItem('dest_ports_action', this.notificationsForm.value.dest_ports_action);
              localStorage.setItem('dns', this.notificationsForm.value.dns);
              localStorage.setItem('dns_action', this.notificationsForm.value.dns_action);
              localStorage.setItem('time_ub', this.notificationsForm.value.time_ub);
              localStorage.setItem('time_lb', this.notificationsForm.value.time_lb);
              localStorage.setItem('http_req', this.notificationsForm.value.http_req);
              localStorage.setItem('http_resp', this.notificationsForm.value.http_resp);
              localStorage.setItem('server_log', this.notificationsForm.value.server_log);
              localStorage.setItem('log_type', this.notificationsForm.value.log_type);
              localStorage.setItem('log_file', this.notificationsForm.value.log_file);
              localStorage.setItem('window', this.notificationsForm.value.window);
              localStorage.setItem('ip_list', this.notificationsForm.value.ip_list);
              localStorage.setItem('status_code', this.notificationsForm.value.status_code);
              localStorage.setItem('ids', this.notificationsForm.value.ids);
              localStorage.setItem('ids_interface', this.notificationsForm.value.ids_interface);
              localStorage.setItem('threshold', this.notificationsForm.value.threshold);
              localStorage.setItem('ethreshold', this.notificationsForm.value.ethreshold);
              localStorage.setItem('sfactor', this.notificationsForm.value.sfactor);
              localStorage.setItem('web_deface', this.notificationsForm.value.web_deface);
              localStorage.setItem('server_name', this.notificationsForm.value.server_name);
              localStorage.setItem('path', this.notificationsForm.value.path);
              localStorage.setItem('waf', this.notificationsForm.value.path);
              localStorage.setItem('listen_ip', this.notificationsForm.value.listen_ip);
              localStorage.setItem('listen_port', this.notificationsForm.value.listen_port);
              localStorage.setItem('mode', this.notificationsForm.value.mode);
              localStorage.setItem('backend_server_config', this.notificationsForm.value.backend_server_config);
              localStorage.setItem('iot_ano', this.notificationsForm.value.iot_ano);
              localStorage.setItem('shodan_api', this.notificationsForm.value.shodan_api);
              localStorage.setItem('ip_addr_iot', this.notificationsForm.value.ip_addr_iot);
              localStorage.setItem('insecure_headers', this.notificationsForm.value.insecure_headers);
              localStorage.setItem('url_ih', this.notificationsForm.value.url_ih);
              localStorage.setItem('hist_logger', this.notificationsForm.value.hist_logger);
              localStorage.setItem('se_mail_id', this.notificationsForm.value.se_mail_id);
            } else if (res === 200) {
              $('#startForm').hide();
              $('#stopForm').show();
              swal('Already monitoring', {
                icon: 'success',
              });
              this.error = '';
            }
          }, (err) => {
            this.error = 'Something went wrong';
          });
        }
      });
    } else {
      swal({
        title: 'Are you sure?',
        text: 'This will monitor your system with existsting configuration.',
        icon: 'warning',
        buttons: ['No', 'Yes'],
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.http.get(posturl).subscribe((res) => {
            if (res === 201) {
              this.notificationsForm.reset();
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
            } else if (res === 200) {
              $('#startForm').hide();
              $('#stopForm').show();
              swal('Already monitoring', {
                icon: 'success',
              });
              this.error = '';
            }
          }, (err) => {
            this.error = 'Something went wrong';
          });
        }
      });
    }
  }

  Stop() {
    const posturl = `${this.apiRoot}stop`;
    this.http.post(
      posturl,
      { 
        "username":localStorage.getItem('user_name')
      }
    ).subscribe((res) => {
      if (res === 200) {
        $('#stopForm').hide();
        $('#startForm').show();
        this.error = '';
      }
    }, (err) => {
      console.log(err);
    });
  }

  checkStatus() {
    const geturl = `${this.apiRoot}status`;
    this.http.post(
      geturl,
      { 
        "username":localStorage.getItem('user_name')
      }
    ).subscribe((res) => {
      if (res === 200) {
        $('#startForm').hide();
        $('#stopForm').show();
        this.error = '';
      } else if (res === 204) {
        $('#startForm').show();
        $('#stopForm').hide();
        this.error = '';
      }
    }, (err) => {
      $('#startForm').show();
      $('#stopForm').hide();
      this.error = '';
    });
  }
  toggleCheckbox(event) {
       if ( event.target.checked ) {
           event.target.value = " ";
        }
        else
        {
          event.target.value = " ";
        }
  }
}
