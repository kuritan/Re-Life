#!/bin/bash
#   
#  Decription:   
#       A Shell script used to download the txts from Internet.  
#  Author:  
#       kuritan  
#  Date:  
#       2016-07-04 16:41:00  
#  

#add base URL
BASE_URL="http://ncode.syosetu.com/txtdownload/dlstart/ncode/302237/?no="  
  
# declare STIRNG variable  
STRING="Beginning TXT download..."  
  
#print var on screen   
echo $STRING  
  
sleep 1  
echo "...."  
 
#def last URL and filename extension
TXT_FORMAT="&hankaku=0&code=utf-8&kaigyo=CRLF"  
TXT=".txt"  

#430 parts txt files
#if you have a Syntax error: Bad for loop variable.
#do not worry.
#sudo dpkg-reconfigure dash
#then select 'NO'.
#it will help you there.
for((i=1;i<431;i++));
do
    echo TXT_URL=${BASE_URL}${i}${TXT_FORMAT}  
    echo "final url="${TXT_URL}  
  
    curl ${BASE_URL}${i}${TXT_FORMAT} -o re_download/${i}${TXT}  
#re_download is a directory which can be change
    sleep 1  
done

