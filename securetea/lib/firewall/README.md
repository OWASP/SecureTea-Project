# SecureTea-Firewall Wiki

## Working
Currently, SecureTea-Firewall uses stateless packet filtering to accept or drop packets.
Rules are applied to both the incoming and outgoing packets.

## Writing rules
Edit the `securetea.conf` file in `etc/securetea/securetea.conf`, with the following JSON data.
```{
	"twitter": {
		"api_key": "XXXX",
		"api_secret_key": "XXXX",
		"access_token": "XXXX",
		"access_token_secret": "XXXX"
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
	"slack": {
		"token": "XXXX",
		"user_id": "XXXX"
	},
	"firewall": {
		"interface": "None",
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
	"debug": false
}
```
Edit the variables accordingly.

### Notations used
`0` - Block packet<br />
`1` - Accept packet<br />
`interface` - Name of your interface, leave blank if you want to setup interactively<br />
`inbound_IPRule` - IP filter rule for incoming packets<br />
`outbound_IPRule` - IP filter rule for outgoing packets<br />
`protocolRule` - Protocol filter rule for incoming/ outgoing packets<br />
`scanLoad` - Scan HTTP load for the specified extensions, example '.exe', '.mp3' downloads<br />
`source_portRule` - Source port filter rule<br />
`dest_portRule` - Destination port filter rule<br />
`HTTPRequest` - Allow or block HTTP request<br />
`HTTPResponse` - Allow or block HTTP response<br />
`DNSRule` - DNS filter rule for incoming/ outgoing packets<br />
`time` - Time-frame (lower-bound & upper-bound) within which packet transfer is allowed<br />

### The above example rule does the following
 1. Blocks ICMP requests
 2. Limits network usage from 00:00 to 23:59.
 3. Scans for '.exe' downloads in HTTP websites, and blocks them

### Writing inbound_IPRule, outbound_IPRule
Example:
```
  	 "inbound_IPRule": {
			"action": "0",
			"ip_inbound": "127.0.0.1, 192.168.0.1-192.168.0.3"
		},
		 "outbound_IPRule": {
			"action": "1",
			"ip_outbound": "10.0.0.3-10.0.0.5"
		}
```
The above rule will block incoming packets from 127.0.0.1, 192.168.0.1, 192.168.0.2, 192.168.0.3, also outgoing packets
having destination 10.0.0.3, 10.0.0.4, 10.0.0.5 will only be allowed.

### Writing protcolRule
Example:
```
		"protocolRule": {
			"action": "0",
			"protocols": "ICMP, TCP"
		}
```
The above rule will block ICMP & TCP packets.

### Writing source_portRule, dest_portRule
Example:
```		"source_portRule": {
			"action": "0",
			"sports": "90, 91"
		},
		"dest_portRule": {
			"action": "1",
			"dports": "80"
		}
```
The above rule will block packets from source port 90, 91 and allow packets having destination port 80.

### Writing DNSRule
Example:
```
		"DNSRule": {
			"action": "0",
			"dns": "google"
		}
```
The above rule will block packets having DNS such as `api.google.com`, `mail.google.com`.

### Writing scanLoad
Example:
```
		"scanLoad": {
			"action": "0",
			"extensions": ".exe, .mp3, .png"
		}
```
The above rule will block HTTP requests having the following load, '.exe', '.mp3', '.png'

## Adding new rules (for developers)
Easy peasy! You need to worry about the various logics whether to allow or drop packets.<br />
Just write your rule by following the current structure, and use the `@utils.xnor` decorator, it will decide
whether to allow or drop the packet using the following XNOR table.
```
        XNOR Table
        ---------------------
        |action|result|final|
        ---------------------
        |   0  |  0   |  1  |
        ---------------------
        |   0  |  1   |  0  |
        ---------------------
        |   1  |  0   |  0  |
        ---------------------
        |   1  |  1   |  1  |
        ---------------------

        Where, 1 : Allow
               0 : Block

				Usage: @utils.xnor
```

## Running tests

To run all the tests at once, run the following command, `python -m unittest` in the `SecureTea` parent directory.
