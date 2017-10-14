FROM python:3.5
MAINTAINER youchen <youchen.du@gmail.com>
USER root

RUN git clone https://github.com/Time1ess/SRPA
VOLUME ["/SRPA/static", "/SRPA/media"]

RUN chmod a+x /SRPA/web/entrypoint.sh

EXPOSE 8000

ENV SRPA_SETTINGS production
ENTRYPOINT ["/SRPA/web/entrypoint.sh"]
