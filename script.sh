#!/bin/bash  
# دانلود و استخراج تصویر RouterOS  
wget https://download.mikrotik.com/routeros/7.5/chr-7.5.img.zip -O chr.img.zip && \
gunzip -c chr.img.zip > chr.img && \
mount -o loop,offset=512 chr.img /mnt && \

# تعیین آدرس IP و دروازه (Gateway)  
ADDRESS="46.8.232.88" && \
GATEWAY=$(ip route list | grep default | awk '{print $3}') && \

# تنظیمات RouterOS  
echo "/ip address add address=$ADDRESS interface=[/interface ethernet find where name=eth0]  
/ip route add gateway=$GATEWAY  
/ip service disable telnet  
/user set 0 name=root password=mahyar" > /mnt/config.rsc  

# پیاده‌سازی تصویر بر روی دیسک  
echo u > /proc/sysrq-trigger && \
dd if=chr.img bs=1024 of=/dev/sda && \
echo "sync disk" && \
echo s > /proc/sysrq-trigger && \
echo "Sleep 5 seconds" && \
sleep 5 && \
echo "Ok, reboot" && \
echo b > /proc/sysrq-trigger
