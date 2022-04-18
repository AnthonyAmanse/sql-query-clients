FROM continuumio/miniconda3:4.10.3-alpine

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

COPY app.py .
COPY opsscale_filter.py .
COPY Python Python

CMD ["conda", "run", "--no-capture-output", "-n", "cloudsql_cos_ts", "python", "-u", "app.py"]