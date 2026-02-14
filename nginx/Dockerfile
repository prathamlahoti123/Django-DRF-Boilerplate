FROM nginxinc/nginx-unprivileged:1-alpine

WORKDIR /etc/nginx

COPY ./default.conf.tpl ./run.sh ./

ARG USER=nginx

USER root

RUN touch ./conf.d/default.conf && \
    chown $USER:$USER ./conf.d/default.conf && \
    chmod +x ./run.sh

USER $USER

CMD ["./run.sh"]
