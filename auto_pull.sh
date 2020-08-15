#!/bin/bash
cd /workspace/crawling
echo "파일을 불러오기 시작합니다"
git stash
git pull
git stash pop
echo "정상적으로 불러왔습니다"