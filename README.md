Temperature Monitor for Raspberry Pi. 

*For Raspbian (Jessie)*

Requirements: Python, SQLite, Apache

    sudo apt install sqlite3 apache2

    sqlite3 templog.db

    BEGIN;
    CREATE TABLE temps (timestamp DATETIME, temp NUMERIC);
    COMMIT;


    sudo mv templog.db /var/www/
    sudo chown www-data:www-data /var/www/templog.db 

    sudo chmod +x /usr/lib/cgi-bin/monitor.py 
    sudo chown www-data:www-data /usr/lib/cgi-bin/monitor.py
    
    sudo mv webgui.py /usr/lib/cgi-bin/webgui.py
    sudo chmod +x /usr/lib/cgi-bin/webgui.py
    sudo chown www-data:www-data /usr/lib/cgi-bin/webgui.py

Setup a cron job to trigger monitor.py every 15 mins

    sudo crontab -u root -e

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

Enable the w1 device tree overlay in /boot/config.txt

    dtoverlay=w1-gpio
