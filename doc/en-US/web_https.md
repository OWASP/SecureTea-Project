# Enable local web serving / hosting over HTTPS

## Requirements
1. Open SSL

### Installing Open SSL
Read [here to install Open SSL](https://websiteforstudents.com/manually-install-the-latest-openssl-toolkit-on-ubuntu-16-04-18-04-lts/).

## Procedure
 - **Step 1:** Creating the directory where all our certificate configurations and generated key will be stored.
 ```shell
 $ sudo mkdir cert
 $ cd cert
 ```
 
 - **Step 2:** Creating the certificate configuration file.
 ```shell
 $ sudo touch cert.cnf
 ```
 
 - **Step 3:** Editing the configuration file using gedit (following) or you can continue to use any text editor of your choice.
 ```shell
 $ sudo gedit cert.cnf
 ```
 Paste in the following configuration data:
  ```text
  [req]
  default_bits = 2048
  prompt = no
  default_md = sha256
  x509_extensions = v3_req
  distinguished_name = dn
  [dn]
  C = GB
  ST = Location
  L = Location
  O = My Organisation
  OU = My Organisational Unit
  emailAddress = email@domain.com
  CN = localhost
  [v3_req]
  subjectAltName = @alt_names
  [alt_names]
  DNS.1 = localhost
  ```
  
 - **Step 4:** Use Open SSL to generate the certificate.
 ```shell
 sudo openssl req -new -x509 -newkey rsa:2048 -sha256 -nodes -keyout localhost.key -days 3560 -out localhost.crt -config cert.cnf
 ```
 
 - **Step 5:** Copy the directory `cert` to SecureTea GUI directory, i.e. `~/secure-tea-path/SecureTea-Project/gui`
 ```shell
 $ sudo cp -r ~/cert ~/secure-tea-path/SecureTea-Project/gui
 ```
 
 - **Step 6:** Edit the `start` under `scripts` in `package.json`. Paste the following instead:
 ```javascript
 "start": "ng serve --ssl --ssl-key ./cert/localhost.key  --ssl-cert ./cert/localhost.crt"
 ```
 
 - **Step 7:** Trusting the new certificate, navigate to `cert` directory we created.
 ```shell
 $ sudo cp localhost.crt /usr/share/ca-certificates/localhost.crt
 $ sudo update-ca-certificates
 ```
 
  - **Step 8:** Start the web server.
 ```shell
 $ npm install
 $ npm run start
 ```
 
 That's it! This will enable local host web serving over HTTPS.
