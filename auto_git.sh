#!/bin/bash
cd /workspace/crawling
echo "자동 백업을 시작합니다"
git status
git add -A
git commit -m "update files"
git push origin master
echo "백업이 완료 되었습니다"