#!/bin/bash

read VAR

echo "content-type: text/html"
echo

urldecode (){
	echo -e $(sed 's/%/\\x/g')
}

TYPE=$(echo $VAR | cut -d"&" -f1 | cut -d"=" -f2)
USER=$(echo $VAR | cut -d"&" -f2 | cut -d"=" -f2)
PASS=$(echo $VAR | cut -d"&" -f3 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
CPASS=$(echo $VAR | cut -d"&" -f4 | cut -d"=" -f2 | sha256sum | cut -d" " -f1)
EMAILA=$(echo $VAR | cut -d"&" -f5 | cut -d"=" -f2 | tr + ' ' | urldecode)
CEMAILA=$(echo $VAR | cut -d"&" -f6 | cut -d"=" -f2 | tr + ' ' | urldecode)

echo "<script lang=javascript>"
grep "^$USER;" users.csv> /dev/null
if [[ $? != "0" ]] ; then
	if [[ $TYPE != "" ]] ; then
		if [[ $USER != "" ]] ; then
			if [[ $PASS != "" ]] ; then
				if [[ $CPASS != "" ]] ; then
					if [[ $EMAILA != "" ]] ; then
						if [[ $CEMAILA != "" ]] ; then
							if [[ $PASS == $CPASS ]] ; then
								if [[ $EMAILA == $CEMAILA ]] ; then
									echo "$USER;$PASS;$EMAILA;$TYPE;IP;nlogged" >> users.csv
									echo "$(date);$USER;ADDED" >> user.log
									echo "alert('Usuário adicionado.')"
									echo "location.href='../index.html'"
								fi
							fi
						fi
					fi
				fi
			fi
		fi
	fi
else
	echo "alert('Campos não coincidem-se.')"
	echo "location.href='../index.html'"
fi
echo "</script>"
