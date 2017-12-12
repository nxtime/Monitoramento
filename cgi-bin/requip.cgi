#!/bin/bash

read VAR

echo "content-type: text/html"
echo

IP=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
CIP=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)

echo "<!DOCTYPE html>"
echo "<head>"
echo "</head>"
echo "<body>"
echo "<script lang='javascript'>"
if [[ $IP == $CIP ]] ; then
	grep -v ";$IP$" equips.csv > equips.new
	mv equips.new equips.csv
	echo "$(date);$IP;REMOVED" >> equip.log
	echo "alert ('Equipamento removido.');"
	echo "location.href='../index.html'"
else
	echo "alert ('Campos não coincidem-se.');"
	echo "location.href='../index.html'"
fi
echo "</script>"
echo "</body>"
echo "</html>"
