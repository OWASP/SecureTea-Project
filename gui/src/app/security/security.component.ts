import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Http } from '@angular/http';
import { Router} from '@angular/router';
import $ from 'jquery';
import swal from 'sweetalert';

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
    slack_token: new FormControl(''),
    slack_userId: new FormControl(''),
    aws_email: new FormControl(''),
    aws_secretKey: new FormControl(''),
    aws_accessKey: new FormControl(''),
    sender_email: new FormControl(' '),
    to_email: new FormControl(' '),
    password: new FormControl(' '),
    antivirus: new FormControl(''),
    custom_scan: new FormControl(''),
    virustotal_api_key: new FormControl(''),
    update: new FormControl(''),
    auto_delete: new FormControl(''),
    monitor_usb: new FormControl(''),
    monitor_file_changes: new FormControl(''),
    asp: new FormControl(' '),
    apache: new FormControl(' '),
    sysctl: new FormControl(' '),
    login: new FormControl(' '),
    ssh: new FormControl(' '),
    sslvuln: new FormControl(' '),
    sys_log: new FormControl(' '),
    interface: new FormControl(' '),
    firewall: new FormControl(' '),
    ip_inbound: new FormControl(' '),
    inbound_action: new FormControl(' '),
    ip_outbound: new FormControl(' '),
    outbound_action: new FormControl(' '),
    protocols: new FormControl(' '),
    protocol_action: new FormControl(' '),
    extensions: new FormControl(' '),
    scan_load_action: new FormControl(' '),
    sports: new FormControl(' '),
    sports_action: new FormControl(' '),
    dest_ports: new FormControl(' '),
    dest_ports_action: new FormControl(' '),
    dns: new FormControl(' '),
    dns_action: new FormControl(' '),
    time_ub: new FormControl(' '),
    time_lb: new FormControl(' '),
    http_req: new FormControl(' '),
    http_resp: new FormControl(' '),
    server_log: new FormControl(' '),
    log_type: new FormControl(' '),
    log_file: new FormControl(' '),
    window: new FormControl(' '),
    ip_list: new FormControl(' '),
    status_code: new FormControl(' ')
  });

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.checkStatus();
  }
  isValid()
  {
    return (
              (this.notificationsForm.value.twitter_apikey!="" && this.notificationsForm.value.twitter_apiSecret!=""  && this.notificationsForm.value.twitter_token!="" && this.notificationsForm.value.twitter_tokenSecret!="" ) ||
              (this.notificationsForm.value.telegram_token!=""  && this.notificationsForm.value.telegram_userId!="" ) ||
              (this.notificationsForm.value.twilio_sid!=""  && this.notificationsForm.value.twilio_token!=""  && this.notificationsForm.value.twilio_to!=""  && this.notificationsForm.value.twilio_from!="" ) ||
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
        'status_code': this.notificationsForm.value.status_code
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
          this.http.post(posturl, data).subscribe((res) => {
            if (res.status === 201) {
              this.notificationsForm.reset();
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
            } else if (res.status === 200) {
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
            if (res.status === 201) {
              this.notificationsForm.reset();
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
            } else if (res.status === 200) {
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
    this.http.get(posturl).subscribe((res) => {
      if (res.status === 200) {
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
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        $('#startForm').hide();
        $('#stopForm').show();
        this.error = '';
      } else if (res.status === 204) {
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
}
