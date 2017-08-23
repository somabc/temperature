Temperature Monitor for Raspberry Pi. 

*For Raspbian (Jessie)*

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

Setup a cron job to trigger monitor.py every 15 mins

    sudo crontab -u www-data -e

    */15 * * * * /usr/lib/cgi-bin/monitor.py

Configure Apache to run Python files

    sudo vim /etc/apache2/sites-enabled/000-default.conf

      ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
        <Directory "/usr/lib/cgi-bin">
         Options +ExecCGI
         AddHandler cgi-script .cgi .pl .py
         Options FollowSymLinks
         Require all granted
        </Directory>

Enable cgi-bin

    sudo a2enmod cgi
    sudo service apache2 restart

You will also need to enable the gpio pins on boot by adding dtoverlay=w1-gpio to /boot/config.txt
