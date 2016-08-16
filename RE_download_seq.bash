#!/bin/sh
#   
#  Decription:   
#       A Shell script used to download txts from Internet.  
#  Author:  
#       kuritan  
#  Date:  
#       2016-08-16 29:51:00  
#  

# declare STIRNG variable  
STRING="Beginning TXT download..."  
  
#print var on screen   
echo $STRING
sleep 1  

echo "Input the beginning chapter :\c" 
read my_begin
echo "OK. We will begin at $my_begin."
sleep 1

echo "Input the End chapter :\c"
read my_end
echo "Alright. We will begin at $my_end."
sleep 1

#if you have a Syntax error: Bad for loop variable.
#do not worry.
#sudo dpkg-reconfigure dash
#then select 'NO'.
#it will help you there.
for i in `seq -w $my_begin $my_end`;
do          
    curl "http://ncode.syosetu.com/txtdownload/dlstart/ncode/302237/?no=$i&hankaku=0&code=utf-8&kaigyo=crlf" -o re_download/${i}.txt  
    sleep 1  
done