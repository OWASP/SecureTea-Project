import React from "react";

// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Container,
  Row,
  Col,
} from "react-bootstrap";


import Cookies from 'universal-cookie';

const cookies = new Cookies();

class Security extends React.Component {

  // Constructor 
  constructor(props) {
    super(props);

    this.state = {
      return_data: [],

      twitter_apikey: "",
      twitter_apiSecret: "",
      twitter_token: "",
      twitter_tokenSecret: "",
      telegram_token: "",
      telegram_userId: "",
      twilio_sid: "",
      twilio_token: "",
      twilio_from: "",
      twilio_to: "",
      whatsapp_sid: "",
      whatsapp_token: "",
      whatsapp_from: "",
      whatsapp_to: "",
      slack_token: "",
      slack_userId: "",
      aws_email: "",
      aws_secretKey: "",
      aws_accessKey: "",
      sender_email: "",
      to_email: "",
      password: "",
      antivirus: "",
      custom_scan: "",
      virustotal_api_key: "",
      update: "",
      auto_delete: "",
      monitor_usb: "",
      monitor_file_changes: "",
      asp: "",
      apache: "",
      sysctl: "",
      login: "",
      ssh: "",
      sslvuln: "",
      sys_log: "",
      inter_face: "",
      firewall: "",
      ip_inbound: "",
      inbound_action: "",
      ip_outbound: "",
      outbound_action: "",
      protocols: "",
      protocol_action: "",
      extensions: "",
      scan_load_action: "",
      sports: "",
      sports_action: "",
      dest_ports: "",
      dest_ports_action: "",
      dns: "",
      dns_action: "",
      time_ub: "",
      time_lb: "",
      http_req: "",
      http_resp: "",
      server_log: "",
      log_type: "",
      log_file: "",
      window: "",
      ip_list: "",
      status_code: "",
      ids: "",
      ids_inter_face: "",
      threshold: "",
      ethreshold: "",
      sfactor: "",
      web_deface: "",
      server_name: "",
      path: "",
      waf: "",
      listen_ip: "",
      listen_port: "",
      mode: "",
      backend_server_config: "",
      iot_ano: "",
      shodan_api: "",
      ip_addr_iot: "",
      insecure_headers: "",
      url_ih: "",
      hist_logger: "",
      se_mail_id: "",
    };


    this.handletwitter_apikeyChange;
    this.handletwitter_apiSecretChange;
    this.handletwitter_tokenChange;
    this.handletwitter_tokenSecretChange;
    this.handletelegram_tokenChange;
    this.handletelegram_userIdChange;
    this.handletwilio_sidChange;
    this.handletwilio_tokenChange;
    this.handletwilio_fromChange;
    this.handletwilio_toChange;
    this.handlewhatsapp_sidChange;
    this.handlewhatsapp_tokenChange;
    this.handlewhatsapp_fromChange;
    this.handlewhatsapp_toChange;
    this.handleslack_tokenChange;
    this.handleslack_userIdChange;
    this.handleaws_emailChange;
    this.handleaws_secretKeyChange;
    this.handleaws_accessKeyChange;
    this.handlesender_emailChange;
    this.handleto_emailChange;
    this.handlepasswordChange;
    this.handleantivirusChange;
    this.handlecustom_scanChange;
    this.handlevirustotal_api_keyChange;
    this.handleupdateChange;
    this.handleauto_deleteChange;
    this.handlemonitor_usbChange;
    this.handlemonitor_file_changesChange;
    this.handleaspChange;
    this.handleapacheChange;
    this.handlesysctlChange;
    this.handleloginChange;
    this.handlesshChange;
    this.handlesslvulnChange;
    this.handlesys_logChange;
    this.handleinter_faceChange;
    this.handlefirewallChange;
    this.handleip_inboundChange;
    this.handleinbound_actionChange;
    this.handleip_outboundChange;
    this.handleoutbound_actionChange;
    this.handleprotocolsChange;
    this.handleprotocol_actionChange;
    this.handleextensionsChange;
    this.handlescan_load_actionChange;
    this.handlesportsChange;
    this.handlesports_actionChange;
    this.handledest_portsChange;
    this.handledest_ports_actionChange;
    this.handlednsChange;
    this.handledns_actionChange;
    this.handletime_ubChange;
    this.handletime_lbChange;
    this.handlehttp_reqChange;
    this.handlehttp_respChange;
    this.handleserver_logChange;
    this.handlelog_typeChange;
    this.handlelog_fileChange;
    this.handlewindowChange;
    this.handleip_listChange;
    this.handlestatus_codeChange;
    this.handleidsChange;
    this.handleids_inter_faceChange;
    this.handlethresholdChange;
    this.handleethresholdChange;
    this.handlesfactorChange;
    this.handleweb_defaceChange;
    this.handleserver_nameChange;
    this.handlepathChange;
    this.handlewafChange;
    this.handlelisten_ipChange;
    this.handlelisten_portChange;
    this.handlemodeChange;
    this.handlebackend_server_configChange;
    this.handleiot_anoChange;
    this.handleshodan_apiChange;
    this.handleip_addr_iotChange;
    this.handleinsecure_headersChange;
    this.handleurl_ihChange;
    this.handlehist_loggerChange;
    this.handlese_mail_idChange;


    this.handleSubmit = this.handleSubmit.bind(this);
  }


  handletwitter_apikeyChange = (event) => {this.setState({twitter_apikey: event.target.value});}
  handletwitter_apiSecretChange = (event) => {this.setState({twitter_apiSecret: event.target.value});}
  handletwitter_tokenChange = (event) => {this.setState({twitter_token: event.target.value});}
  handletwitter_tokenSecretChange = (event) => {this.setState({twitter_tokenSecret: event.target.value});}
  handletelegram_tokenChange = (event) => {this.setState({telegram_token: event.target.value});}
  handletelegram_userIdChange = (event) => {this.setState({telegram_userId: event.target.value});}
  handletwilio_sidChange = (event) => {this.setState({twilio_sid: event.target.value});}
  handletwilio_tokenChange = (event) => {this.setState({twilio_token: event.target.value});}
  handletwilio_fromChange = (event) => {this.setState({twilio_from: event.target.value});}
  handletwilio_toChange = (event) => {this.setState({twilio_to: event.target.value});}
  handlewhatsapp_sidChange = (event) => {this.setState({whatsapp_sid: event.target.value});}
  handlewhatsapp_tokenChange = (event) => {this.setState({whatsapp_token: event.target.value});}
  handlewhatsapp_fromChange = (event) => {this.setState({whatsapp_from: event.target.value});}
  handlewhatsapp_toChange = (event) => {this.setState({whatsapp_to: event.target.value});}
  handleslack_tokenChange = (event) => {this.setState({slack_token: event.target.value});}
  handleslack_userIdChange = (event) => {this.setState({slack_userId: event.target.value});}
  handleaws_emailChange = (event) => {this.setState({aws_email: event.target.value});}
  handleaws_secretKeyChange = (event) => {this.setState({aws_secretKey: event.target.value});}
  handleaws_accessKeyChange = (event) => {this.setState({aws_accessKey: event.target.value});}
  handlesender_emailChange = (event) => {this.setState({sender_email: event.target.value});}
  handleto_emailChange = (event) => {this.setState({to_email: event.target.value});}
  handlepasswordChange = (event) => {this.setState({password: event.target.value});}
  handleantivirusChange = (event) => {this.setState({antivirus: event.target.value});}
  handlecustom_scanChange = (event) => {this.setState({custom_scan: event.target.value});}
  handlevirustotal_api_keyChange = (event) => {this.setState({virustotal_api_key: event.target.value});}
  handleupdateChange = (event) => {this.setState({update: event.target.value});}
  handleauto_deleteChange = (event) => {this.setState({auto_delete: event.target.value});}
  handlemonitor_usbChange = (event) => {this.setState({monitor_usb: event.target.value});}
  handlemonitor_file_changesChange = (event) => {this.setState({monitor_file_changes: event.target.value});}
  handleaspChange = (event) => {this.setState({asp: event.target.value});}
  handleapacheChange = (event) => {this.setState({apache: event.target.value});}
  handlesysctlChange = (event) => {this.setState({sysctl: event.target.value});}
  handleloginChange = (event) => {this.setState({login: event.target.value});}
  handlesshChange = (event) => {this.setState({ssh: event.target.value});}
  handlesslvulnChange = (event) => {this.setState({sslvuln: event.target.value});}
  handlesys_logChange = (event) => {this.setState({sys_log: event.target.value});}
  handleinter_faceChange = (event) => {this.setState({inter_face: event.target.value});}
  handlefirewallChange = (event) => {this.setState({firewall: event.target.value});}
  handleip_inboundChange = (event) => {this.setState({ip_inbound: event.target.value});}
  handleinbound_actionChange = (event) => {this.setState({inbound_action: event.target.value});}
  handleip_outboundChange = (event) => {this.setState({ip_outbound: event.target.value});}
  handleoutbound_actionChange = (event) => {this.setState({outbound_action: event.target.value});}
  handleprotocolsChange = (event) => {this.setState({protocols: event.target.value});}
  handleprotocol_actionChange = (event) => {this.setState({protocol_action: event.target.value});}
  handleextensionsChange = (event) => {this.setState({extensions: event.target.value});}
  handlescan_load_actionChange = (event) => {this.setState({scan_load_action: event.target.value});}
  handlesportsChange = (event) => {this.setState({sports: event.target.value});}
  handlesports_actionChange = (event) => {this.setState({sports_action: event.target.value});}
  handledest_portsChange = (event) => {this.setState({dest_ports: event.target.value});}
  handledest_ports_actionChange = (event) => {this.setState({dest_ports_action: event.target.value});}
  handlednsChange = (event) => {this.setState({dns: event.target.value});}
  handledns_actionChange = (event) => {this.setState({dns_action: event.target.value});}
  handletime_ubChange = (event) => {this.setState({time_ub: event.target.value});}
  handletime_lbChange = (event) => {this.setState({time_lb: event.target.value});}
  handlehttp_reqChange = (event) => {this.setState({http_req: event.target.value});}
  handlehttp_respChange = (event) => {this.setState({http_resp: event.target.value});}
  handleserver_logChange = (event) => {this.setState({server_log: event.target.value});}
  handlelog_typeChange = (event) => {this.setState({log_type: event.target.value});}
  handlelog_fileChange = (event) => {this.setState({log_file: event.target.value});}
  handlewindowChange = (event) => {this.setState({window: event.target.value});}
  handleip_listChange = (event) => {this.setState({ip_list: event.target.value});}
  handlestatus_codeChange = (event) => {this.setState({status_code: event.target.value});}
  handleidsChange = (event) => {this.setState({ids: event.target.value});}
  handleids_inter_faceChange = (event) => {this.setState({ids_inter_face: event.target.value});}
  handlethresholdChange = (event) => {this.setState({threshold: event.target.value});}
  handleethresholdChange = (event) => {this.setState({ethreshold: event.target.value});}
  handlesfactorChange = (event) => {this.setState({sfactor: event.target.value});}
  handleweb_defaceChange = (event) => {this.setState({web_deface: event.target.value});}
  handleserver_nameChange = (event) => {this.setState({server_name: event.target.value});}
  handlepathChange = (event) => {this.setState({path: event.target.value});}
  handlewafChange = (event) => {this.setState({waf: event.target.value});}
  handlelisten_ipChange = (event) => {this.setState({listen_ip: event.target.value});}
  handlelisten_portChange = (event) => {this.setState({listen_port: event.target.value});}
  handlemodeChange = (event) => {this.setState({mode: event.target.value});}
  handlebackend_server_configChange = (event) => {this.setState({backend_server_config: event.target.value});}
  handleiot_anoChange = (event) => {this.setState({iot_ano: event.target.value});}
  handleshodan_apiChange = (event) => {this.setState({shodan_api: event.target.value});}
  handleip_addr_iotChange = (event) => {this.setState({ip_addr_iot: event.target.value});}
  handleinsecure_headersChange = (event) => {this.setState({insecure_headers: event.target.value});}
  handleurl_ihChange = (event) => {this.setState({url_ih: event.target.value});}
  handlehist_loggerChange = (event) => {this.setState({hist_logger: event.target.value});}
  handlese_mail_idChange = (event) => {this.setState({se_mail_id: event.target.value});}




  handleSubmit(event) {

    console.log(this.state.twitter_apikey);
    console.log(this.state.twitter_apiSecret);
    console.log(this.state.twitter_token);
    console.log(this.state.twitter_tokenSecret);
    console.log(this.state.telegram_token);
    console.log(this.state.telegram_userId);
    console.log(this.state.twilio_sid);
    console.log(this.state.twilio_token);
    console.log(this.state.twilio_from);
    console.log(this.state.twilio_to);
    console.log(this.state.whatsapp_sid);
    console.log(this.state.whatsapp_token);
    console.log(this.state.whatsapp_from);
    console.log(this.state.whatsapp_to);
    console.log(this.state.slack_token);
    console.log(this.state.slack_userId);
    console.log(this.state.aws_email);
    console.log(this.state.aws_secretKey);
    console.log(this.state.aws_accessKey);
    console.log(this.state.sender_email);
    console.log(this.state.to_email);
    console.log(this.state.password);
    console.log(this.state.antivirus);
    console.log(this.state.custom_scan);
    console.log(this.state.virustotal_api_key);
    console.log(this.state.update);
    console.log(this.state.auto_delete);
    console.log(this.state.monitor_usb);
    console.log(this.state.monitor_file_changes);
    console.log(this.state.asp);
    console.log(this.state.apache);
    console.log(this.state.sysctl);
    console.log(this.state.login);
    console.log(this.state.ssh);
    console.log(this.state.sslvuln);
    console.log(this.state.sys_log);
    console.log(this.state.inter_face);
    console.log(this.state.firewall);
    console.log(this.state.ip_inbound);
    console.log(this.state.inbound_action);
    console.log(this.state.ip_outbound);
    console.log(this.state.outbound_action);
    console.log(this.state.protocols);
    console.log(this.state.protocol_action);
    console.log(this.state.extensions);
    console.log(this.state.scan_load_action);
    console.log(this.state.sports);
    console.log(this.state.sports_action);
    console.log(this.state.dest_ports);
    console.log(this.state.dest_ports_action);
    console.log(this.state.dns);
    console.log(this.state.dns_action);
    console.log(this.state.time_ub);
    console.log(this.state.time_lb);
    console.log(this.state.http_req);
    console.log(this.state.http_resp);
    console.log(this.state.server_log);
    console.log(this.state.log_type);
    console.log(this.state.log_file);
    console.log(this.state.window);
    console.log(this.state.ip_list);
    console.log(this.state.status_code);
    console.log(this.state.ids);
    console.log(this.state.ids_inter_face);
    console.log(this.state.threshold);
    console.log(this.state.ethreshold);
    console.log(this.state.sfactor);
    console.log(this.state.web_deface);
    console.log(this.state.server_name);
    console.log(this.state.path);
    console.log(this.state.waf);
    console.log(this.state.listen_ip);
    console.log(this.state.listen_port);
    console.log(this.state.mode);
    console.log(this.state.backend_server_config);
    console.log(this.state.iot_ano);
    console.log(this.state.shodan_api);
    console.log(this.state.ip_addr_iot);
    console.log(this.state.insecure_headers);
    console.log(this.state.url_ih);
    console.log(this.state.hist_logger);
    console.log(this.state.se_mail_id);
        
    const cookie_val = cookies.get('cookie');
    const url = cookies.get('url');
    console.log(cookie_val);

    const data = {

      "cookie" : cookie_val,
      "twitter_apikey" : this.state.twitter_apikey,
      "twitter_apiSecret" : this.state.twitter_apiSecret,
      "twitter_token" : this.state.twitter_token,
      "twitter_tokenSecret" : this.state.twitter_tokenSecret,
      "telegram_token" : this.state.telegram_token,
      "telegram_userId" : this.state.telegram_userId,
      "twilio_sid" : this.state.twilio_sid,
      "twilio_token" : this.state.twilio_token,
      "twilio_from" : this.state.twilio_from,
      "twilio_to" : this.state.twilio_to,
      "whatsapp_sid" : this.state.whatsapp_sid,
      "whatsapp_token" : this.state.whatsapp_token,
      "whatsapp_from" : this.state.whatsapp_from,
      "whatsapp_to" : this.state.whatsapp_to,
      "slack_token" : this.state.slack_token,
      "slack_userId" : this.state.slack_userId,
      "aws_email" : this.state.aws_email,
      "aws_secretKey" : this.state.aws_secretKey,
      "aws_accessKey" : this.state.aws_accessKey,
      "sender_email" : this.state.sender_email,
      "to_email" : this.state.to_email,
      "password" : this.state.password,
      "antivirus" : this.state.antivirus,
      "custom_scan" : this.state.custom_scan,
      "virustotal_api_key" : this.state.virustotal_api_key,
      "update" : this.state.update,
      "auto_delete" : this.state.auto_delete,
      "monitor_usb" : this.state.monitor_usb,
      "monitor_file_changes" : this.state.monitor_file_changes,
      "asp" : this.state.asp,
      "apache" : this.state.apache,
      "sysctl" : this.state.sysctl,
      "login" : this.state.login,
      "ssh" : this.state.ssh,
      "sslvuln" : this.state.sslvuln,
      "sys_log" : this.state.sys_log,
      "inter_face" : this.state.inter_face,
      "firewall" : this.state.firewall,
      "ip_inbound" : this.state.ip_inbound,
      "inbound_action" : this.state.inbound_action,
      "ip_outbound" : this.state.ip_outbound,
      "outbound_action" : this.state.outbound_action,
      "protocols" : this.state.protocols,
      "protocol_action" : this.state.protocol_action,
      "extensions" : this.state.extensions,
      "scan_load_action" : this.state.scan_load_action,
      "sports" : this.state.sports,
      "sports_action" : this.state.sports_action,
      "dest_ports" : this.state.dest_ports,
      "dest_ports_action" : this.state.dest_ports_action,
      "dns" : this.state.dns,
      "dns_action" : this.state.dns_action,
      "time_ub" : this.state.time_ub,
      "time_lb" : this.state.time_lb,
      "http_req" : this.state.http_req,
      "http_resp" : this.state.http_resp,
      "server_log" : this.state.server_log,
      "log_type" : this.state.log_type,
      "log_file" : this.state.log_file,
      "window" : this.state.window,
      "ip_list" : this.state.ip_list,
      "status_code" : this.state.status_code,
      "ids" : this.state.ids,
      "ids_inter_face" : this.state.ids_inter_face,
      "threshold" : this.state.threshold,
      "ethreshold" : this.state.ethreshold,
      "sfactor" : this.state.sfactor,
      "web_deface" : this.state.web_deface,
      "server_name" : this.state.server_name,
      "path" : this.state.path,
      "waf" : this.state.waf,
      "listen_ip" : this.state.listen_ip,
      "listen_port" : this.state.listen_port,
      "mode" : this.state.mode,
      "backend_server_config" : this.state.backend_server_config,
      "iot_ano" : this.state.iot_ano,
      "shodan_api" : this.state.shodan_api,
      "ip_addr_iot" : this.state.ip_addr_iot,
      "insecure_headers" : this.state.insecure_headers,
      "url_ih" : this.state.url_ih,
      "hist_logger" : this.state.hist_logger,
      "se_mail_id" : this.state.se_mail_id,
      
    }

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({


        "cookie" : cookie_val,
        "twitter_apikey" : this.state.twitter_apikey,
        "twitter_apiSecret" : this.state.twitter_apiSecret,
        "twitter_token" : this.state.twitter_token,
        "twitter_tokenSecret" : this.state.twitter_tokenSecret,
        "telegram_token" : this.state.telegram_token,
        "telegram_userId" : this.state.telegram_userId,
        "twilio_sid" : this.state.twilio_sid,
        "twilio_token" : this.state.twilio_token,
        "twilio_from" : this.state.twilio_from,
        "twilio_to" : this.state.twilio_to,
        "whatsapp_sid" : this.state.whatsapp_sid,
        "whatsapp_token" : this.state.whatsapp_token,
        "whatsapp_from" : this.state.whatsapp_from,
        "whatsapp_to" : this.state.whatsapp_to,
        "slack_token" : this.state.slack_token,
        "slack_userId" : this.state.slack_userId,
        "aws_email" : this.state.aws_email,
        "aws_secretKey" : this.state.aws_secretKey,
        "aws_accessKey" : this.state.aws_accessKey,
        "sender_email" : this.state.sender_email,
        "to_email" : this.state.to_email,
        "password" : this.state.password,
        "antivirus" : this.state.antivirus,
        "custom_scan" : this.state.custom_scan,
        "virustotal_api_key" : this.state.virustotal_api_key,
        "update" : this.state.update,
        "auto_delete" : this.state.auto_delete,
        "monitor_usb" : this.state.monitor_usb,
        "monitor_file_changes" : this.state.monitor_file_changes,
        "asp" : this.state.asp,
        "apache" : this.state.apache,
        "sysctl" : this.state.sysctl,
        "login" : this.state.login,
        "ssh" : this.state.ssh,
        "sslvuln" : this.state.sslvuln,
        "sys_log" : this.state.sys_log,
        "inter_face" : this.state.inter_face,
        "firewall" : this.state.firewall,
        "ip_inbound" : this.state.ip_inbound,
        "inbound_action" : this.state.inbound_action,
        "ip_outbound" : this.state.ip_outbound,
        "outbound_action" : this.state.outbound_action,
        "protocols" : this.state.protocols,
        "protocol_action" : this.state.protocol_action,
        "extensions" : this.state.extensions,
        "scan_load_action" : this.state.scan_load_action,
        "sports" : this.state.sports,
        "sports_action" : this.state.sports_action,
        "dest_ports" : this.state.dest_ports,
        "dest_ports_action" : this.state.dest_ports_action,
        "dns" : this.state.dns,
        "dns_action" : this.state.dns_action,
        "time_ub" : this.state.time_ub,
        "time_lb" : this.state.time_lb,
        "http_req" : this.state.http_req,
        "http_resp" : this.state.http_resp,
        "server_log" : this.state.server_log,
        "log_type" : this.state.log_type,
        "log_file" : this.state.log_file,
        "window" : this.state.window,
        "ip_list" : this.state.ip_list,
        "status_code" : this.state.status_code,
        "ids" : this.state.ids,
        "ids_inter_face" : this.state.ids_inter_face,
        "threshold" : this.state.threshold,
        "ethreshold" : this.state.ethreshold,
        "sfactor" : this.state.sfactor,
        "web_deface" : this.state.web_deface,
        "server_name" : this.state.server_name,
        "path" : this.state.path,
        "waf" : this.state.waf,
        "listen_ip" : this.state.listen_ip,
        "listen_port" : this.state.listen_port,
        "mode" : this.state.mode,
        "backend_server_config" : this.state.backend_server_config,
        "iot_ano" : this.state.iot_ano,
        "shodan_api" : this.state.shodan_api,
        "ip_addr_iot" : this.state.ip_addr_iot,
        "insecure_headers" : this.state.insecure_headers,
        "url_ih" : this.state.url_ih,
        "hist_logger" : this.state.hist_logger,
        "se_mail_id" : this.state.se_mail_id,
        
  

      })
    };

    fetch(
      url + "sleep/", requestOptions
      )
        .then((res) => res.json())
        .then((json) => {
            this.setState({
              return_data: json,
              DataisLoaded: true
            });
        })

    alert("New Monitoring set up. System will go to sleep")
    event.preventDefault();


  }

   

  render () {


    return (
      <>
        <Container fluid>
          <Row>
            <Col md="12" className="page-data">
              <Card>
                <Card.Header className="box-header">
                  <Card.Title as="h4" className="text-white text-bold pb-3 pt-1">Security</Card.Title>
                </Card.Header>
                <Card.Body>
  
  
                <div class="container my-auto pt-5">

                  <form role="form" class="text-start" onSubmit={this.handleSubmit}>


                    <div class="row">


                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Twitter</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twitter_apikey" value={this.state.twitter_apikey} onChange={this.handletwitter_apikeyChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twitter_apikey" value={this.state.twitter_apiSecret} onChange={this.handletwitter_apiSecretChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twitter_apikey" value={this.state.twitter_token} onChange={this.handletwitter_tokenChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twitter_apikey" value={this.state.twitter_tokenSecret} onChange={this.handletwitter_tokenSecretChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>
                    

                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Telegram</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="telegram_token" value={this.state.telegram_token} onChange={this.handletelegram_tokenChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="telegram_userId" value={this.state.telegram_userId} onChange={this.handletelegram_userIdChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>


                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Twilio</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twilio_sid" value={this.state.twilio_sid} onChange={this.handletwilio_sidChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twilio_token" value={this.state.twilio_token} onChange={this.handletwilio_tokenChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twilio_from" value={this.state.twilio_from} onChange={this.handletwilio_fromChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="twilio_to" value={this.state.twilio_to} onChange={this.handletwilio_toChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>

                      
                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Whatsapp</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="whatsapp_sid" value={this.state.whatsapp_sid} onChange={this.handlewhatsapp_sidChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="whatsapp_token" value={this.state.whatsapp_token} onChange={this.handlewhatsapp_tokenChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="whatsapp_from" value={this.state.whatsapp_from} onChange={this.handlewhatsapp_fromChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="whatsapp_to" value={this.state.whatsapp_to} onChange={this.handlewhatsapp_toChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>
                      

                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Slack</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="slack_token" value={this.state.slack_token} onChange={this.handleslack_tokenChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="slack_userId" value={this.state.slack_userId} onChange={this.handleslack_userIdChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>


                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">AWS</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="aws_email" value={this.state.aws_email} onChange={this.handleaws_emailChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="aws_secretKey" value={this.state.aws_secretKey} onChange={this.handleaws_secretKeyChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="aws_accessKey" value={this.state.aws_accessKey} onChange={this.handleaws_accessKeyChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>


                      <div class="col-lg-4 col-md-6 col-12 mx-auto">
                        <div class="card z-index-0 fadeIn3 fadeInBottom">
                          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                            <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                              <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">GMail</h4>
                            </div>
                          </div>
                          <div class="card-body">
                            
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="sender_email" value={this.state.sender_email} onChange={this.handlesender_emailChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="to_email" value={this.state.to_email} onChange={this.handleto_emailChange} />
                              </div>
                              <div class="input-group input-group-outline my-2">
                                <input type="text" class="form-control" placeholder="password" value={this.state.password} onChange={this.handlepasswordChange} />
                              </div>
                            
                          </div>
                        </div>
                      </div>


                    </div>

                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SECURITY</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="antivirus" value={this.state.antivirus} onChange={this.handleantivirusChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="custom_scan" value={this.state.custom_scan} onChange={this.handlecustom_scanChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="virustotal_api_key" value={this.state.virustotal_api_key} onChange={this.handlevirustotal_api_keyChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="update" value={this.state.update} onChange={this.handleupdateChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="auto_delete" value={this.state.auto_delete} onChange={this.handleauto_deleteChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="monitor_usb" value={this.state.monitor_usb} onChange={this.handlemonitor_usbChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="monitor_file_changes" value={this.state.monitor_file_changes} onChange={this.handlemonitor_file_changesChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Auto Server Patcher</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="asp" value={this.state.asp} onChange={this.handleaspChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="apache" value={this.state.apache} onChange={this.handleapacheChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sysctl" value={this.state.sysctl} onChange={this.handlesysctlChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="login" value={this.state.login} onChange={this.handleloginChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ssh" value={this.state.ssh} onChange={this.handlesshChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sslvuln" value={this.state.sslvuln} onChange={this.handlesslvulnChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">System Logs</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sys_log" value={this.state.sys_log} onChange={this.handlesys_logChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">FireWall</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="inter_face" value={this.state.inter_face} onChange={this.handleinter_faceChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="firewall" value={this.state.firewall} onChange={this.handlefirewallChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ip_inbound" value={this.state.ip_inbound} onChange={this.handleip_inboundChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="inbound_action" value={this.state.inbound_action} onChange={this.handleinbound_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ip_outbound" value={this.state.ip_outbound} onChange={this.handleip_outboundChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="outbound_action" value={this.state.outbound_action} onChange={this.handleoutbound_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="protocols" value={this.state.protocols} onChange={this.handleprotocolsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="protocol_action" value={this.state.protocol_action} onChange={this.handleprotocol_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="extensions" value={this.state.extensions} onChange={this.handleextensionsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="scan_load_action" value={this.state.scan_load_action} onChange={this.handlescan_load_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sports" value={this.state.sports} onChange={this.handlesportsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sports_action" value={this.state.sports_action} onChange={this.handlesports_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="dest_ports" value={this.state.dest_ports} onChange={this.handledest_portsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="dest_ports_action" value={this.state.dest_ports_action} onChange={this.handledest_ports_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="dns" value={this.state.dns} onChange={this.handlednsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="dns_action" value={this.state.dns_action} onChange={this.handledns_actionChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="time_ub" value={this.state.time_ub} onChange={this.handletime_ubChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="time_lb" value={this.state.time_lb} onChange={this.handletime_lbChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="http_req" value={this.state.http_req} onChange={this.handlehttp_reqChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="http_resp" value={this.state.http_resp} onChange={this.handlehttp_respChange}  />
                                </div>

                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Server Logs</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="server_log" value={this.state.server_log} onChange={this.handleserver_logChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="log_type" value={this.state.log_type} onChange={this.handlelog_typeChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="log_file" value={this.state.log_file} onChange={this.handlelog_fileChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="window" value={this.state.window} onChange={this.handlewindowChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ip_list" value={this.state.ip_list} onChange={this.handleip_listChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="status_code" value={this.state.status_code} onChange={this.handlestatus_codeChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Intrusion Detection System</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ids" value={this.state.ids} onChange={this.handleidsChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ids_inter_face" value={this.state.ids_inter_face} onChange={this.handleids_inter_faceChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="threshold" value={this.state.threshold} onChange={this.handlethresholdChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ethreshold" value={this.state.ethreshold} onChange={this.handleethresholdChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="sfactor" value={this.state.sfactor} onChange={this.handlesfactorChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Social Engineering</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="se_mail_id" value={this.state.se_mail_id} onChange={this.handlese_mail_idChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Web Deface</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="web_deface" value={this.state.web_deface} onChange={this.handleweb_defaceChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="server_name" value={this.state.server_name} onChange={this.handleserver_nameChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="path" value={this.state.path} onChange={this.handlepathChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Web Application FireWall</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="waf" value={this.state.waf} onChange={this.handlewafChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="listen_ip" value={this.state.listen_ip} onChange={this.handlelisten_ipChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="listen_port" value={this.state.listen_port   } onChange={this.handlelisten_portChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="mode" value={this.state.mode} onChange={this.handlemodeChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="backend_server_config" value={this.state.backend_server_config} onChange={this.handlebackend_server_configChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Web Deface</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="iot_ano" value={this.state.iot_ano} onChange={this.handleiot_anoChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="shodan_api" value={this.state.shodan_api} onChange={this.handleshodan_apiChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="ip_addr_iot" value={this.state.ip_addr_iot} onChange={this.handleip_addr_iotChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Insecure Headers</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="insecure_headers" value={this.state.insecure_headers} onChange={this.handleinsecure_headersChange}  />
                                </div>
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="url_ih" value={this.state.url_ih} onChange={this.handleurl_ihChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>


                      <div className="row mt-3">
                        <div class="col-lg-12 col-md-12 col-12 mx-auto">
                          <div class="card z-index-0 fadeIn3 fadeInBottom">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                              <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                                <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">Hist Logger</h4>
                              </div>
                            </div>
                            <div class="card-body container-fluid">
                              
                                <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                                  <input type="text" class="form-control" placeholder="hist_logger" value={this.state.hist_logger} onChange={this.handlehist_loggerChange}  />
                                </div>
                              
                            </div>
                          </div>
                        </div>
                      </div>
                      

                      <div class="text-center signin-btn">
                        <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit All Data</button>
                      </div>


                  </form>
                </div>
  
  
                  
                  
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </Container>
      </>
    );



  }
}

export default Security;




/*

function Security() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12" className="page-data">
            <Card>
              <Card.Header className="box-header">
                <Card.Title as="h4" className="text-white text-bold pb-3 pt-1">Security</Card.Title>
              </Card.Header>
              <Card.Body>


              <div class="container my-auto pt-5">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SECURITY</h4>
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start">
                  <div class="input-group input-group-outline my-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                 
                  <div class="text-center signin-btn">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SSL</h4>
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start">
                  <div class="input-group input-group-outline my-2">
                    <input type="text" class="form-control" placeholder="Some text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="Some text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="text"/>
                  </div>
                 
                  <div class="text-center signin-btn">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SSH</h4>
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start">
                  <div class="input-group input-group-outline my-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="some text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="text"/>
                  </div>
                  <div class="text-center signin-btn">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <div className="row mt-3">
        <div class="col-lg-6 col-md-6 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SECURITY</h4>
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start">
                  <div class="input-group input-group-outline my-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                 
                  <div class="text-center signin-btn">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-6 col-md-6 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SECURITY</h4>
                </div>
              </div>
              <div class="card-body">
                <form role="form" class="text-start">
                  <div class="input-group input-group-outline my-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                  <div class="input-group input-group-outline mb-2">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                 
                  <div class="text-center signin-btn">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

  <div className="row mt-3">
        <div class="col-lg-12 col-md-12 col-12 mx-auto">
            <div class="card z-index-0 fadeIn3 fadeInBottom">
              <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2 bg-transparent">
                <div class="bg-gradient-info shadow-info border-radius-lg py-2 pe-1">
                  <h4 class="text-white font-weight-bolder text-center mt-2 mb-1">SECURITY</h4>
                </div>
              </div>
              <div class="card-body container-fluid">
                <form role="form" class="text-start row">
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="Some Text"/>
                  </div>
                  <div class="input-group input-group-outline mb-2 col-lg-6 col-md-6 col-12">
                    <input type="text" class="form-control" placeholder="sometext"/>
                  </div>
                
                 
                  <div class="text-center signin-btn col-lg-6 col-md-4 col-6 mx-auto">
                    <button type="submit" class="text-white btn bg-gradient-info w-100 my-4 mb-2">Submit</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>


                
                
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}


export default Security;














/*
twitter_apikey
twitter_apiSecret
twitter_token
twitter_tokenSecret
telegram_token
telegram_userId
twilio_sid
twilio_token
twilio_from
twilio_to
whatsapp_sid
whatsapp_token
whatsapp_from
whatsapp_to
slack_token
slack_userId
aws_email
aws_secretKey
aws_accessKey
sender_email
to_email
password
antivirus
custom_scan
virustotal_api_key
update
auto_delete
monitor_usb
monitor_file_changes
asp
apache
sysctl
login
ssh
sslvuln
sys_log
inter_face
firewall
ip_inbound
inbound_action
ip_outbound
outbound_action
protocols
protocol_action
extensions
scan_load_action
sports
sports_action
dest_ports
dest_ports_action
dns
dns_action
time_ub
time_lb
http_req
http_resp
server_log
log_type
log_file
window
ip_list
status_code
ids
ids_inter_face
threshold
ethreshold
sfactor
web_deface
server_name
path
waf
listen_ip
listen_port
mode
backend_server_config
iot_ano
shodan_api
ip_addr_iot
insecure_headers
url_ih
hist_logger
se_mail_id
*/