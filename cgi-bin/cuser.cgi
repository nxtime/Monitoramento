#!/bin/bash

read VAR

echo "content-type: text/html"
echo

TYPE=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)
INF=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2)
CINF=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2)
CUSER=$(grep "^$USER;" users.csv | cut -d";" -f1)
F1=$(grep "^$USER;" users.csv | cut -d";" -f1)
F2=$(grep "^$USER;" users.csv | cut -d";" -f2)
F3=$(grep "^$USER;" users.csv | cut -d";" -f3)
F4=$(grep "^$USER;" users.csv | cut -d";" -f4)

echo "<script lang=javascript>"
if [[ $USER == $CUSER ]] ; then
	if [[ $INF != "" ]] ; then
		if [[ $INF == $CINF ]] ; then
			if [[ $TYPE == "user" ]] ; then
				grep -v "^$USER;" users.csv > users.new
				grep "^$USER;" users.csv | sed -e "s/^$F1;/$INF;/g" >> users.new
				mv users.new users.csv
				chmod 777 users.csv
				echo "$(date);$USER;CHANGED" >> user.log
				echo "alert('Usuário alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "pass" ]] ; then
				INF=$(echo "$INF" | sha256sum | cut -d" " -f1)
				grep -v "^$USER;" users.csv > users.new
				grep "^$USER;" users.csv | sed -e "s/;$F2;/;$INF;/g" >> users.new
				mv users.new users.csv
				chmod 777 users.csv
				echo "$(date);$USER;CHANGED" >> user.log
				echo "alert('Usuário alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "e-mail" ]] ; then
				grep -v "^$USER;" users.csv > users.new
				grep "^$USER;" users.csv | sed -e "s/;$F3;/;$INF;/g" >> users.new
				mv users.new users.csv
				chmod 777 users.csv
				echo "$(date);$USER;CHANGED" >> user.log
				echo "alert('Usuário alterado.');"
				echo "location.href='../index.html'"
			elif [[ $TYPE == "type" ]] ; then
				grep -v "^$USER;" users.csv > users.new
				grep "^$USER;" users.csv | sed -e "s/;$F4$/;$INF/g" >> users.new
				mv users.new users.csv
				chmod 777 users.csv
				echo "$(date);$USER;CHANGED" >> user.log
				echo "alert('Usuário alterado.');"
				echo "location.href='../index.html'"
			fi
		fi
	fi
else
	echo "alert('Campos não coincidem-se.');"
	echo "location.href='../index.html'"
fi
echo "</script>"
