cd /home/ec2-user/environment/warframets/python/
date "+%Y/%m/%d/%H:%M" -d +9hours
echo "업데이트를 시작하겠습니다."
echo "워프레임 업데이트 중입니다....."
sleep 5
python3 warframes_update.py
echo "무기 업데이트 중입니다....."
sleep 5
python3 weapons_update.py
echo "기타 무기 업데이트 중입니다....."
sleep 5
python3 weapons_etc_update.py
echo "모드 업데이트 중입니다....."
sleep 5
python3 mods_update.py
echo "아케인 업데이트 중입니다....."
sleep 5
python3 etcs_update.py
echo "결산 중입니다....."
sleep 5
python3 today_recommend.py
date "+%Y/%m/%d/%H:%M" -d +9hours
echo "업데이트를 마쳤습니다."