FROM python:3.9-slim-bullseye


RUN apt-get update
RUN apt-get install -y wget && apt-get clean

# wkhtmltopdf dependencies
RUN apt-get install -y fontconfig \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
    && apt-get clean
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.bullseye_amd64.deb && \
    dpkg -i wkhtmltox_0.12.6.1-2.bullseye_amd64.deb && \
    rm wkhtmltox_0.12.6.1-2.bullseye_amd64.deb

WORKDIR /app

# directory for request temp files
RUN mkdir temp

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY views.py .

EXPOSE 5000
CMD ["sh", "-c", "flask run --host ${HOST:-0.0.0.0}"]
