#!/bin/bash
cd /workspace/crawling
date "+%Y/%m/%d/%H:%M" -d +9hours
echo "디버깅 업데이트를 시작하겠습니다."
echo "워프레임 업데이트 중입니다....."
sleep 5
/usr/local/bin/python3 /workspace/crawling/python/warframes_update.py
sleep 5
/usr/local/bin/python3 /workspace/crawling/python/today_recommend.py
echo "무기 업데이트 중입니다....."
sleep 5
/usr/local/bin/python3 /workspace/crawling/python/weapons_update.py
sleep 5
/usr/local/bin/python3 /workspace/crawling/python/today_recommend.py
echo "결산 중입니다....."
sleep 5
/usr/local/bin/python3 /workspace/crawling/python/today_recommend.py
date "+%Y/%m/%d/%H:%M" -d +9hours
echo "업데이트를 마쳤습니다."