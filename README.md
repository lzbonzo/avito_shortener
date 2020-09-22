# avito_shortener
AVITO SHORTENER

Step 1. Clone repository:

$ git clone https://github.com/lzbonzo/avito_shortener avito_shortener 

$ cd avito_shortener

Step 2. Configure «settings.py»:

(Skip if ports 5000 for shortener and 5050 for client are not used)

Set SERVER_PORT, CLIENT_PORT.

Step 3. Configure SERVER_URL:

(Skip if client and shortener started from same IPs )

Set SERVER_URL in "client.py".

Step 4. App works with PostgreSQL.

Create database «avito_shortener».

Configure «DB_CONFIG» in «settings.py».


Step 5. Run scripts:

$ sh venv.sh 

$ sh shortener.sh
