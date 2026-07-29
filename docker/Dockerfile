FROM amazoncorretto:17 AS builder

RUN yum -y update
RUN yum -y groupinstall development
RUN yum -y install openssl openssl-devel
RUN yum -y install python3.11 python3.11-devel python3.11-pip

FROM builder AS apache-spark

# Install Python dependencies
RUN pip3.11 install tox flake8 mypy

# Amazon Linux 2023 keeps the default python3 at 3.9 because dnf itself runs on
# it, so PySpark is pointed at 3.11 for invocations made outside tox. Keep both
# values bare names and never absolute paths: under tox they must resolve to the
# venv interpreter that holds pyspark and langid, not to the system 3.11. Both
# tox.ini files pass them through via `passenv = *`.
ENV PYSPARK_PYTHON=python3.11
ENV PYSPARK_DRIVER_PYTHON=python3.11

ENV PATH="${PATH}:/opt/spark/apps/scripts"

CMD ["bash"]
