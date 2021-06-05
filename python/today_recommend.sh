#!/bin/bash
cd /home/ec2-user/environment/warframets
sleep 5
/usr/local/bin/python3 /home/ec2-user/environment/warframets/python/today_recommend.py
echo "정산 하였습니다."