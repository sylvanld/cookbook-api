FROM python:3.10-alpine AS BUILDER

COPY requirements/lock.txt /tmp/requirements
RUN pip install --no-cache-dir virtualenv               \
    && virtualenv -p python3 /opt/venv                  \
    && /opt/venv/bin/pip install                        \
        --no-cache-dir -r /tmp/requirements


FROM python:3.10-alpine

WORKDIR /app

ENV PATH /opt/venv/bin:$PATH

COPY --from=BUILDER /opt/venv /opt/venv
COPY cookbook /app/cookbook
COPY docker-entrypoint.sh /usr/bin/cookbook

HEALTHCHECK --interval=10s --timeout=5s \
    CMD [ "/usr/bin/cookbook", "healthcheck" ]

ENTRYPOINT [ "/usr/bin/cookbook" ]
CMD [ "start" ]
