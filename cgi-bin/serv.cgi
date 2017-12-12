#!/bin/bash

read VAR

echo "content-type: text/html"
echo

VAR=$(echo $VAR | cut -d"=" -f2)

iniciar(){
	source pingd.cgi
	echo $! > serv.pid
}

echo "<html>"
echo "<head>"
echo "</head>"
echo "<body>"
echo "<script lang='javascript'>"
case $VAR in
	Iniciar)
		iniciar &> /dev/null
		echo "alert('Monitoramento iniciado.');"
		echo "location.href='../index.html'"
		;;
	Encerrar)
		kill -9 $(cat serv.pid)
		rm -rf serv.pid
		echo "alert('Monitoramento encerrado.');"
		echo "location.href='../index.html'"
		;;
	Status)
		if [ -e serv.pid ] ; then
			echo "alert ('Monitoramento está em funcionamento. PID=$(cat serv.pid)');"
			echo "location.href='../index.html'"
		else
			echo "alert ('Monitoramento está desligado.');"
			echo "location.href='../index.html'"
		fi
		;;
esac
echo "</script>"
echo "</body>"
echo "</html>"
