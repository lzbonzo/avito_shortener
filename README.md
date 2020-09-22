# avito_shortener
AVITO SHORTENER
(localhost)

Step 1.
Clone repository:

$ git clone https://github.com/lzbonzo/avito_shortener avito_shortener 
$ cd avito_shortener

Step 2.
Configure «settings.py»:

(Skip if localhost: 127.0.0.1 and ports 5000, 5050 ports are not used)

- Set SERVER_IP, SERVER_PORT, CLIENT_IP, CLIENT_PORT 

Step 3.
App works with PostgreSQL.
- Create database «avito_shortener»
- Configure «DB_CONFIG» in «settings.py»

Step 4.
Run scripts:

$ sh venv.sh
$ sh shortener.sh 
