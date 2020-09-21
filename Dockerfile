FROM python:3.6
WORKDIR /avito_shortener
ADD . /avito_shortener
RUN pip install -r requirements.txt
EXPOSE 5000
ENV NAME avito_shortener
CMD ["sh", "shortener.sh"]