Temperature Monitor for Raspberry Pi.

Used to monitor datacentre temperature.

For Raspbian (Jessie)

Requirements: Python, SQLite, Apache

    sudo apt install sqlite3 apache2

    sqlite3 templog.db

    BEGIN;
    CREATE TABLE temps (timestamp DATETIME, temp NUMERIC);
    COMMIT;


    sudo cp templog.db /var/www/
    sudo chown www-data:www-data /var/www/templog.db 

    sudo chmod +x /usr/lib/cgi-bin/monitor.py 
    sudo chown www-data:www-data /usr/lib/cgi-bin/monitor.py 

Setup a cron job ro trigger monitor.py every 15 mins

    sudo crontab -u www-data -e

    */15 * * * * /usr/lib/cgi-bin/monitor.py

Configure Apache to run Python files

    sudo vim /etc/apache2/sites-enabled/000-default

    <Directory "/usr/lib/cgi-bin">
    ...
    AddHandler cgi-script .py
    </Directory>

    sudo service apache2 reload
