#!/bin/bash  
#   
#  Decription:   
#       A Shell script used to set the txts in one file.  
#  Author:  
#       kuritan  
#  Date:  
#       2016-07-04 17:37:00  

#  
STRING="Beginning TXT mix..."  
  
#print var on screen   
echo $STRING  
  
sleep 1  
echo "...."  

for ((i=1;i<431;i++)); do
	cat "${i}.txt" >> RE_all.txt
#RE_all.txt is a filename
	sleep 1

done
