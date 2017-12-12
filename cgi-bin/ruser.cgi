#!/bin/bash

read VAR

echo "content-type: text/html"
echo

USER=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CUSER=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<script lang='javascript'>"
if [[ $USER == $CUSER ]] ; then
	grep -v "^$USER;" users.csv > users.new
	mv users.new users.csv
	echo "$(date);$USER;REMOVED" >> user.log
	echo "alert('Usuário removido.');"
	echo "location.href='../index.html'"
else
	echo "alert('Campos não coincidem-se.');"
	echo "location.href='../index.html'"
fi
echo "</script>"
