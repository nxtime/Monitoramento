#!/bin/bash

read X
DIRET="/usr/lib/cgi-bin"

urldecode(){
	echo -e $(sed 's/%/\\x/g')
}

chmod 777 sendemail.log
chmod 777 email.log

chown www-data:www-data sendemail.log
chown www-data:www-data email.log

echo "content-type: text/html"
echo

email=$(echo $X | cut -d"&" -f1 | cut -d"=" -f2)
email=$(echo $email | urldecode)

msg=$(echo $X | cut -d"&" -f2 | cut -d"=" -f2)
msg=$(echo $msg | urldecode | tr + ' ')

sendemail -l sendemail.log	\
-f "senaimonitoramento@gmail.com " 	\
-u "[CONTATO]" 		\
-t "pedroreiki03080@gmail.com"		\		
-m "$email\n$msg"			\	
-cc "$email"				\
-s "smtp.gmail.com:587"			\
-o tls=yes				\
-xu "senaimonitoramento@gmail.com"	\
-xp "sen@i132" >> email.log

val=$?
	if [[ $val == "0" ]]
then
echo "<script>"
	echo 'alert("Email enviado com sucesso")'
	echo 'window.location="../index.html";'
	echo "</script>"
else
echo "<script>"
	echo 'alert("Ocorreu um erro, Email não enviado")'
	echo 'window.location="../index.html";'
	echo "</script>"
fi
