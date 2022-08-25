# -*- coding: utf-8 -*-
u"""SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Version: 1.1
    Module: SecureTea
"""
# To share mouse gestures
import struct

import sys
import time
import threading

from securetea import configurations
from securetea import logger
# from securetea.lib.notifs import secureTeaTwitter
from securetea.lib.malware_analysis.malware_analysis_runner import SecureTeaMalwareAnalysis
from securetea.lib.notifs import secureTeaDiscord
from securetea.lib.notifs.secureTeaTelegram import SecureTeaTelegram
from securetea.lib.notifs import secureTeaSlack
from securetea.lib.notifs.aws import secureTeaAwsSES
from securetea.lib.firewall import secureTeaFirewall
from securetea.lib.notifs import secureTeaTwilio
from securetea.lib.notifs import secureTeaWhatsapp
from securetea.lib.notifs import secureTeaGmail
from securetea.args.arguments import get_args
from securetea.args.args_helper import ArgsHelper
from securetea.lib.firewall.utils import setup_logger
from securetea.lib.security_header import secureTeaHeaders
from securetea.lib.ids import secureTeaIDS
from securetea.lib.waf.Server import  SecureTeaWaf
from securetea.lib.log_monitor.system_log import engine
from securetea.lib.log_monitor.server_log.secureTeaServerLog import SecureTeaServerLog
from securetea.lib.auto_server_patcher.secureTeaServerPatcher import SecureTeaAutoServerPatcher
from securetea.lib.web_deface.secureTeaWebDeface import WebDeface
from securetea.lib.antivirus.secureTeaAntiVirus import SecureTeaAntiVirus
from securetea.lib.iot import iot_checker
from securetea.lib.social_engineering.socialEngineering import SecureTeaSocialEngineering
from securetea.lib.history_logger.secureTeaHistoryLogger import SecureTeaHistoryLogger
from securetea.lib.history_logger.historylogger_logger import HistoryLogger
from securetea.modes import server_mode
from securetea.modes import system_mode
from securetea.modes import iot_mode


pynput_status = True

try:
    from pynput import mouse
except Exception as e:
    pynput_status = False


class SecureTea(object):
    """SecureTea Class."""

    alert_count = 1

    def __init__(self):
        """Init SecureTea params.

        Args:
            None

        Raises:
            None

        Returns:
            None

        Working:
            Collects the arguments passed and calls the respected module accordingly
            for parsing the arguments. Further, creates object for the demanded
            notification medium and starts SecureTea.
        """
        modulename = 'Core'
        self.cred = {}
        args = get_args()
        argsHelper = ArgsHelper(args)
        try:
            args_dict = argsHelper.check_args()
        except KeyboardInterrupt:
            print('\nKeyboard Interrupt detected. \nQuitting....')
            exit(0)
        credentials = configurations.SecureTeaConf()

        self.cred = args_dict['cred']
        self.history_logger = self.cred['history_logger']
        self.cred_provided = args_dict['cred_provided']
        # self.twitter_provided = args_dict['twitter_provided']
        self.malware_analysis_provided = args_dict['malware_analysis']
        self.telegram_provided = args_dict['telegram_provided']
        self.twilio_provided = args_dict['twilio_provided']
        self.whatsapp_provided = args_dict['whatsapp_provided']
        self.social_eng_provided = args_dict['social_eng_provided']
        self.slack_provided = args_dict['slack_provided']
        self.discord_provided = args_dict['discord_provided']
        self.aws_ses_provided = args_dict['aws_ses_provided']
        self.gmail_provided = args_dict['gmail_provided']
        self.firewall_provided = args_dict['firewall_provided']
        self.insecure_headers_provided = args_dict['insecure_headers_provided']
        self.ids_provided = args_dict['ids_provided']
        self.waf_provided=args_dict["waf_provided"]
        self.system_log_provided = args_dict['system_log_provided']
        self.server_log_provided = args_dict['server_log_provided']
        self.auto_server_patcher_provided = args_dict['auto_server_patcher_provided']
        self.web_deface_provided = args_dict['web_deface_provided']
        self.antivirus_provided = args_dict['antivirus_provided']
        self.iot_checker_provided = args_dict['iot_checker_provided']
        self.server_mode = args_dict["server_mode"]
        self.system_mode = args_dict["system_mode"]
        self.iot_mode = args_dict["iot_mode"]

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            modulename,
            self.cred['debug']
        )

        # Setup logger for utils
        setup_logger(debug=self.cred['debug'])

        if self.cred_provided and not self.cred['skip_config_file']:
            credentials.save_creds(self.cred)
        elif not self.cred['skip_config_file']:
            self.cred = credentials.get_creds(args)

            try:
                if self.cred['social_eng']:
                    self.social_eng_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Social Engineering configuration parameter not set.",
                    logtype="error"
                )
            
            """
            try:
                if self.cred['twitter']:
                    self.twitter_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Twitter configuration parameter not set.",
                    logtype="error"
                )
            """

            try:
                if self.cred['malware_analysis']:
                    self.malware_analysis_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Malware analysis configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['telegram']:
                    self.telegram_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Telegram configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['twilio']:
                    self.twilio_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Twilio configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['whatsapp']:
                    self.whatsapp_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Whatsapp configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['slack']:
                    self.slack_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Slack configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['discord']:
                    self.discord_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Discord configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['aws_ses']:
                    self.aws_ses_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "AWS SES configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['gmail']:
                    self.gmail_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Gmail configuraton parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['firewall']:
                    self.firewall_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Firewall configuraton parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['insecure_headers']:
                    self.insecure_headers_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Insecure headers parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['ids']:
                    self.ids_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Intrusion Detection System (IDS) not set.",
                    logtype="error"
                )

            try:
                if self.cred['server_log']:
                    self.server_log_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Server Log configuraton parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['auto_server_patcher']:
                    self.auto_server_patcher_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Auto server patcher configuraton not set.",
                    logtype="error"
                )

            try:
                if self.cred['web-deface']:
                    self.web_deface_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "Web Deface Detection configuraton not set.",
                    logtype="eror"
                )

            try:
                if self.cred['antivirus']:
                    self.antivirus_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "AntiVirus configuraton not set.",
                    logtype="error"
                )

            try:
                if self.cred['iot-check']:
                    self.iot_checker_provided = True
                    self.cred_provided = True
            except TypeError:
                self.logger.log(
                    "IoT Checker configuraton not set.",
                    logtype="error"
                )

        if not self.cred:
            self.logger.log(
                "Configuration not found.",
                logtype="error"
            )
            sys.exit(0)

        if not self.cred_provided and not (self.cred['history_logger'] or self.cred['clamav'] or self.cred['yara']):
            self.logger.log(
                "None of the notifications configured. Exiting...",
                logtype="error"
            )
            sys.exit(0)

        self.logger.log(
            "Welcome to SecureTea..!! Initializing System",
            logtype="info"
        )

        # Initialize modes at first (Server, System, IoT)
        # Check for Server mode
        if self.server_mode:
            self.logger.log(
                "Starting SecureTea in server mode",
                logtype="info"
            )
            # Initialize Server Mode object
            self.server_mode_obj = server_mode.ServerMode(cred=self.cred, debug=self.cred["debug"])
            self.server_mode_obj.start_server_mode()
            # Avoid multiple process of the objects created by the server mode, set their credentials to False
            self.firewall_provided = False
            self.server_log_provided = False
            self.antivirus_provided = False
            self.web_deface_provided = False
            self.system_log_provided = False
            self.auto_server_patcher_provided = False
            self.waf_provided=False
            self.ids_provided = False

        # Check for System mode
        if self.system_mode:
            self.logger.log(
                "Starting SecureTea in system mode",
                logtype="info"
            )
            # Initialize System Mode object
            self.system_mode_obj = system_mode.SystemMode(cred=self.cred, debug=self.cred["debug"])
            self.system_mode_obj.start_system_mode()
            # Avoid multiple process of the objects created by the system mode, set their credentials to False
            self.firewall_provided = False
            self.antivirus_provided = False
            self.system_log_provided = False
            self.ids_provided = False

        # Check for Social Engineering
        if self.social_eng_provided:
            self.logger.log(
                "Starting SecureTea Social Engineering",
                logtype="info"
            )
            self.social_eng_obj = SecureTeaSocialEngineering(debug=self.cred["debug"], email_id=self.cred["social_eng"]["email"])
            self.social_eng_obj.start()

        # Check for History Logger
        if self.history_logger:
            self.logger.log(
                "Starting SecureTea History Logger",
                logtype="info"
            )
            self.history_logger_obj = SecureTeaHistoryLogger(debug=self.cred["debug"])
            self.history_logger_obj.start()

        if self.iot_mode:
            self.logger.log(
                "Starting SecureTea in IoT mode",
                logtype="info"
            )
            # Initialize IoT Mode object
            self.iot_mode_obj = iot_mode.IoTMode(cred=self.cred, debug=self.cred["debug"])
            self.iot_mode_obj.start_iot_mode()
            # Avoid multiple process of the objects created by the IoT mode, set their credentials to False
            self.firewall_provided = False
            self.ids_provided = False
            self.iot_checker_provided = False
        
        """
        if self.twitter_provided:
            self.twitter = secureTeaTwitter.SecureTeaTwitter(
                self.cred['twitter'],
                self.cred['debug']
            )

            if not self.twitter.enabled:
                self.logger.log(
                    "Twitter notification not configured properly.",
                    logtype="error"
                )
            else:
                self.twitter.notify("Welcome to SecureTea..!! Initializing System")
        """

        if self.malware_analysis_provided:
            self.malware_analysis_obj = SecureTeaMalwareAnalysis(self.cred['malware_analysis'])
            self.malware_analysis_obj.runner()

        if self.telegram_provided:
            self.telegram = SecureTeaTelegram(
                self.cred['telegram'],
                self.cred['debug']
            )

            if not self.telegram.enabled:
                self.logger.log(
                    "Telegram notification not configured properly.",
                    logtype="error"
                )
            else:
                self.telegram.notify("Welcome to SecureTea..!! Initializing System")

        if self.twilio_provided:
            self.twilio = secureTeaTwilio.SecureTeaTwilio(
                self.cred['twilio'],
                self.cred['debug']
            )

            if not self.twilio.enabled:
                self.logger.log(
                    "Twilio not configured properly.",
                    logtype="error"
                )
            else:
                self.twilio.notify("Welcome to SecureTea..!! Initializing System")

        if self.whatsapp_provided:
            self.whatsapp = secureTeaWhatsapp.SecureTeaWhatsapp(
                self.cred['whatsapp'],
                self.cred['debug']
            )

            if not self.whatsapp.enabled:
                self.logger.log(
                    "Whatsapp not configured properly.",
                    logtype="error"
                )
            else:
                self.whatsapp.notify("Welcome to SecureTea..!! Initializing System")

        if self.slack_provided:
            self.slack = secureTeaSlack.SecureTeaSlack(
                self.cred['slack'],
                self.cred['debug']
            )

            if not self.slack.enabled:
                self.logger.log(
                    "Slack not configured properly.",
                    logtype="error"
                )
            else:
                self.slack.notify("Welcome to SecureTea..!! Initializing System")

        if self.discord_provided:
            self.discord = secureTeaDiscord.SecureTeaDiscord(
                self.cred['discord'],
                self.cred['debug']
            )

            if not self.discord.enabled:
                self.logger.log(
                    "Discord not configured properly.",
                    logtype="error"
                )
            else:
                self.discord.notify("Welcome to SecureTea..!! Initializing System")
        
        if self.aws_ses_provided:
            self.aws_ses = secureTeaAwsSES.SecureTeaAwsSES(
                self.cred['aws_ses'],
                self.cred['debug']
            )

            if not self.aws_ses.enabled:
                self.logger.log(
                    "AWS SES not configured properly.",
                    logtype="error"
                )
            else:
                self.aws_ses.notify("Welcome to SecureTea..!! Initializing System")

        if self.gmail_provided:
            self.gmail_obj = secureTeaGmail.SecureTeaGmail(
                cred=self.cred['gmail'],
                debug=self.cred['debug']
            )

            if not self.gmail_obj.enabled:
                self.logger.log(
                    "Gmail not configured properly.",
                    logtype="error"
                )
            else:
                self.gmail_obj.notify("Welcome to SecureTea..!! Initializing System")

        if self.firewall_provided:
            try:
                if self.cred['firewall']:
                    firewallObj = secureTeaFirewall.SecureTeaFirewall(cred=self.cred,
                                                                      debug=self.cred['debug'])
                    firewallObj.start_firewall()
            except TypeError:
                self.logger.log(
                    "Firewall configuration parameter not configured.",
                    logtype="error"
                )

        if self.insecure_headers_provided:
            try:
                if self.cred['insecure_headers']:
                    url = self.cred['insecure_headers']['url']
                    insecure_headers_obj = secureTeaHeaders.SecureTeaHeaders(url=url,
                                                                             debug=self.cred['debug'])
                    insecure_headers_obj.analyze()
            except TypeError:
                self.logger.log(
                    "Insecure headers parameter not configured.",
                    logtype="error"
                )

        if self.ids_provided:
            try:
                if self.cred['ids']:
                    ids_obj = secureTeaIDS.SecureTeaIDS(cred=self.cred['ids'],
                                                        debug=self.cred['debug'])
                    ids_obj.start_ids()
            except TypeError:
                self.logger.log(
                    "Intrusion Detection System (IDS) parameter not configured.",
                    logtype="error"
                )
        if self.waf_provided:
            try:
                if self.cred['waf']:

                    waf_obj=SecureTeaWaf.SecureTeaWaf(cred=self.cred['waf'],debug=self.cred["debug"])
                    waf_obj.startWaf()
            except TypeError:
                self.logger.log(
                    "WAF parameter not configured ",
                    logtype="error"
                )

        if self.system_log_provided:
            try:
                sys_obj = engine.SystemLogEngine(debug=self.cred['debug'])
                sys_obj.run()
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.server_log_provided:
            server_cred = self.cred['server_log']
            try:
                server_obj = SecureTeaServerLog(debug=self.cred['debug'],
                                                log_type=server_cred['log-type'],
                                                log_file=server_cred['log-file'],
                                                window=server_cred['window'],
                                                ip_list=server_cred['ip-list'],
                                                status_code=server_cred['status-code'])
                server_obj.run()
            except TypeError:
                self.logger.log(
                    "Server Log parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.auto_server_patcher_provided:
            auto_server_patcher_cred = self.cred['auto_server_patcher']
            try:
                patcher_obj = SecureTeaAutoServerPatcher(debug=self.cred['debug'],
                                                         cred=auto_server_patcher_cred)
                patcher_obj.start()
            except TypeError:
                self.logger.log(
                    "Auto Server Patcher parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.web_deface_provided:
            web_deface = self.cred['web_deface']
            try:
                web_deface_obj = WebDeface(debug=self.cred['debug'],
                                           path=web_deface['path'],
                                           server_name=web_deface['server-name'])
                web_deface_obj.start()
            except TypeError:
                self.logger.log(
                    "Web Deface Detection parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.antivirus_provided or self.cred['clamav'] or self.cred['yara']:
            if self.cred.get('antivirus',0):
                antivirus = self.cred['antivirus']
            else:
                antivirus = {}
                antivirus['update'] = False
                antivirus['custom-scan'] = False
                antivirus['auto-delete'] = False
                antivirus['monitor-usb'] = False
                antivirus['monitor-file-changes'] = False
                antivirus['virustotal-api-key'] = ''

            try:
                antivirus_obj = SecureTeaAntiVirus(debug=self.cred['debug'], cred=antivirus, use_clamav=self.cred['clamav'], use_yara=self.cred['yara'])
                antivirus_obj.start()
            except TypeError:
                self.logger.log(
                    "AntiVirus parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.iot_checker_provided:
            try:
                iot_checker_obj = iot_checker.IoTChecker(debug=self.cred['debug'],
                                                         api_key=self.cred['iot-check']['shodan-api-key'],
                                                         ip=self.cred['iot-check']['ip'])
                iot_checker_obj.check_shodan_range()
            except TypeError:
                self.logger.log(
                    "IoT checker parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

    def send_notif(self, msg):
        """Send notification through
        the available mediums.

        Args:
            msg (str): Message to send

        Raises:
            None

        Returns:
            None
        """
        
        """        
        # Send a warning message via twitter account
        if self.twitter_provided:
            self.twitter.notify(msg)
        """

        # Send a warning message via telegram bot
        # Telegram works  - 12/8/2022
        if self.telegram_provided:
            self.telegram.notify(msg)

        # Send a warning message via twilio account
        # Twilio works  - 12/8/2022
        if self.twilio_provided:
            self.twilio.notify(msg)

        # Send a warning message via whatsapp account
        if self.whatsapp_provided:
            self.whatsapp.notify(msg)

        # Send a warning message via slack bot app
        if self.slack_provided:
            self.slack.notify(msg)

        # Send a warning message via Discord channel
        if self.discord_provided:
            self.discord.notify(msg)

        # Send a warning message via aws ses bot3 app
        if self.aws_ses_provided:
            self.aws_ses.notify(msg)

        # Send a warning message via Gmail
        if self.gmail_provided:
            self.gmail_obj.notify(msg)

    def on_move(self, x, y):
        """
        Log warning on terminal & send notification
        on mouse movement.

        Args:
            x (TYPE): X - mouse position
            y (TYPE): y - mouse position

        Raises:
            None

        Returns:
            bool (False): Stop the listener
        """
        self.logger.log('Pointer moved to {0}'.format((x, y)))

        msg = '(' + str(self.alert_count) + \
            ') : Someone has accessed your computer'

        # Shows the warning msg on the console
        self.logger.log(msg, logtype="warning")

        # Send message notification to available platforms
        self.send_notif(msg)

        # Update counter for the next move
        self.alert_count += 1

        self.logger.log("The program will sleep for 10 seconds")

        time.sleep(10)

        # Ready to monitor the next move
        self.logger.log("Ready to monitor further movement .. !!")

        # Stop the listener
        return False

    @staticmethod
    def get_mouse_event():
        """Get mouse event.

        Args:
            None

        Raises:
            None

        Returns:
            x (int): X - mouse position
            y (int): y - mouse position
        """
        with open("/dev/input/mice", "rb") as fh:
            buf = fh.read(3)
            x, y = struct.unpack("bb", buf[1:])
            return x, y

    def get_by_mice(self):
        """Detect intrusion by watching mouse coordinates.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        posx = 0
        posy = 0
        while(1):
            x, y = self.get_mouse_event()
            posx = posx + x
            posy = posy + y
            if (posx > 100 or posy > 100 or posx < -100 or posy < -100):
                posx = 0
                posy = 0
                self.on_move(posx, posy)

    def on_user_update(self):
        """
        Send updates regarding the users currently logged in to the system
        to various platforms.
        """
        msg = self.userLogger.log()
        if msg == "USERS UPDATES\n":
            self.logger.log("NO NEW USERS DETECTED")
            return
        # Shows the warning msg on the console
        self.logger.log(msg, logtype="warning")

        # Send message notification to available platforms
        self.send_notif(msg)
        return

    def run_mouse_notifs(self):
        """Run methods for notification using mice activity"""
        time.sleep(10)
        try:
            if not pynput_status:
                self.get_by_mice()
            else:
                while 1:
                    # Starting mouse event listner
                    with mouse.Listener(on_move=self.on_move) as listener:
                        listener.join()
        except Exception as e:
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()

    def run_user_notifs(self):
        """Run methods for notification of users added or removed"""
        try:
            from securetea import users
            self.userLogger = users.SecureTeaUserLogger(self.cred['debug'])
            if not pynput_status:
                self.get_by_mice()
            else:
                while 1:
                    # Starting user notifs
                    self.on_user_update()
                    time.sleep(10)
        except Exception as e:
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()

    def run(self):
        """
        Track mouse activity & SSH users on
        different threads.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            t1 = threading.Thread(target=self.run_mouse_notifs)
            t2 = threading.Thread(target=self.run_user_notifs)
            t2.start()
            t1.start()
        except Exception as e:
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()
