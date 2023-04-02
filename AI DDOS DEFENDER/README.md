# DDOS AI DEFENDER

This Python code uses machine learning to detect suspicious IP addresses that may be attempting to perform network intrusion on a specified host IP address. It uses Pyshark to capture live network packets and Keras to load a pre-trained Bidirectional Recurrent Neural Network (BRNN) model that has been trained to classify network traffic as either normal or suspicious.


## Features
- [X] Detects for network anomolies.
- [X] Disconnects the suspected IP.


## Usage

1. Install the required packages using the command `pip install -r requirements.txt`.
2. Update the `interface`, `host_ip`, `capture_filter`, variables in the code according to your specific network configuration.
3. Run the code using the command `python network_intrusion_detection.py`.
4. The code will continuously capture live network packets and classify them as normal or suspicious based on the loaded BRNN model.
5. If a suspicious IP address is detected, a RST packet will be sent to the IP address to terminate the connection.


## Credits

The BRNN model used in this code was trained and provided by [santhisenan](https://github.com/santhisenan/DeepDefense)
