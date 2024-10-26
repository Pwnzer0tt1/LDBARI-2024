FROM debian:12

RUN apt-get update && apt-get install -y \
    socat 

WORKDIR /var/app/

RUN useradd -m ctf

USER ctf

COPY challenge flag.txt . 

EXPOSE 8003

CMD ["socat", "TCP-LISTEN:8003,reuseaddr,fork", "EXEC:./challenge,stderr"]
