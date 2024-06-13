# FROM python:3.9

# RUN pip install --no-cache-dir newrelic

# CMD ["newrelic", "agent", "run"]

FROM python:3.9

RUN pip install --no-cache-dir newrelic

ENTRYPOINT ["newrelic-admin", "run-program"]
