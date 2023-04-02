import pyshark
import keras
import numpy as np
import logging

# create logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

interface = "eth0"
host_ip="192.168.0.1"
capture_filter = f"host {host_ip}"
feature_names = ['ip.src', 'frame.len', 'ip.hdr_len', 'ip.len', 'ip.flags.rb', 'ip.flags.df', 'p.flags.mf', 'ip.frag_offset',       
                 'ip.ttl', 'ip.proto', 'tcp.srcport', 'tcp.dstport',       
                 'tcp.len', 'tcp.ack', 'tcp.flags.res', 'tcp.flags.ns', 'tcp.flags.cwr',       
                 'tcp.flags.ecn', 'tcp.flags.urg', 'tcp.flags.ack', 'tcp.flags.push',       
                 'tcp.flags.reset', 'tcp.flags.syn', 'tcp.flags.fin', 'tcp.window_size',       
                 'tcp.time_delta']
model_path = "brnn_model.h5"
model = keras.models.load_model(model_path)
suspicious_ips = set()

capture = pyshark.LiveCapture(interface=interface, display_filter=capture_filter)
for packet in capture.sniff_continuously():
    features = [getattr(packet, feature_name) for feature_name in feature_names]
    x = np.array(features[1:]).reshape(1, -1)  # Skip the first feature (IP address)
    prediction = model.predict(x)
    tcp_header = packet.tcp
    src_port = tcp_header.srcport
    dst_port = tcp_header.dstport
    seq_num = tcp_header.seq
    ack_num = tcp_header.ack

    if prediction[0] == 1:
        suspicious_ips.add(features[0])
        logger.info("Suspicious IP detected: %s", features[0])
        # Send RST packet to source IP
        ip_packet = IP(dst=host_ip, src=features[0])
        tcp_packet = TCP(dport=src_port, sport=dst_port, flags="R", seq=seq_num, ack=ack_num)
        rst_packet = ip_packet/tcp_packet
        send(rst_packet)
        logger.info("RST packet sent to %s", features[0])
