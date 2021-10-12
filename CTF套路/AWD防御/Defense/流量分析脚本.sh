#!/bin/bash
#
TX=0;
RX=0;
MAX_TX=0;
MAX_RX=0;
while read line
do
        a=`echo $line | grep "em1" |awk '{print $3}'`
if [ $a -ge 0 ]
then
        TX=$a
        if [ $TX -ge $MAX_TX ]
        then
                MAX_TX=$TX
        fi
fi
        b=`echo $line | grep "em1" |awk '{print $7}'`
if [ $b -ge 0 ]
then
        RX=$b
        if [ $RX -ge $MAX_RX ]
        then
                MAX_RX=$RX
        fi
fi
done < /usr/monitor/network/network_$(date +%Y%m%d).log 
echo "The top of Upload $MAX_TX kb/s at $(date +%Y%m%d)">>/usr/monitor/network/tongji.log
echo "The top of download $MAX_RX kb/s at $(date +%Y%m%d)">>/usr/monitor/network/tongji.log