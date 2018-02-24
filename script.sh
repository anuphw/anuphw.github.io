apt-get update && apt-get upgrade
www_home=/home/pi/www

# If you don't have apache installed install it
if ! [ -x $(which apache2)  ] ; then 
	apt-get install apache2
fi

# If you don't have php installed install it
if ! [ -x $(which php) ] ; then 
	apt-get install php
fi

# Check apache installation
if [ -x $(which apache2)  ] ; then 
	wget "https://anuphw.github.io/apache2.conf" -O /tmp/apache2.conf
	wget "https://anuphw.github.io/000-default.conf" -O /tmp/000-default.conf
	wget "https://anuphw.github.io/index.php"  -O /tmp/index.php
	cp  /tmp/apache2.conf /etc/apache2/apache2.conf
	cp /tmp/000-default.conf /etc/apache2/sites-available/000-default.conf
	mkdir -p "$www_home"
	cp /tmp/index.php "$www_home"
	chmod -R 777 "$www_home"
	service apache2 restart
else 
	echo "Apache is not installed. Run 'sudo apt-get install apache2'"
	exit 1
fi

# Check php installation
if ! [ -x $(which php) ] ; then 
	print "Php is not installed. Run 'sudo apt-get install php'"
	exit 1
fi

# Download website contents 

wget "https://www.dropbox.com/s/03544uihvjr0a26/VideoCoding.zip?dl=0" -O /tmp/VideoCoding.zip
unzip /tmp/VideoCoding.zip -d "$www_home"
chmod -R 777 "$www_home"

# Find IP addess

echo "Your IP" $(ifconfig | grep inet | grep broadcast | sed 's/netmask.*//;s/inet //g')

