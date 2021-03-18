#!/bin/bash
if [ ${RANDOMTIME} ];
then
  #尝试让GitHub显式显示区间长度
  time=${RANDOMTIME}
  echo "你设定的打卡时间区间为: ${time}分钟"
fi
exit
