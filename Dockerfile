FROM python:3.8.0b3-buster
RUN apt update && \
		apt upgrade -y
RUN apt install -y nodejs
RUN python3 -m pip install --upgrade pip
RUN git clone https://github.com/OWASP/SecureTea-Project securetea
RUN wget https://github.com/cdr/code-server/releases/download/2.preview.11-vsc1.37.0/code-server2.preview.11-vsc1.37.0-linux-x86_64.tar.gz &&\
	tar --gzip -xf ./code-server2.preview.11-vsc1.37.0-linux-x86_64.tar.gz && \
	mv -f code-server2.preview.11-vsc1.37.0-linux-x86_64/* ~/ && \
	chmod +x ~/code-server
RUN apt install zsh -y
WORKDIR /root/securetea
EXPOSE 7171
CMD ~/code-server ./ --port 7171 --host 0.0.0.0
