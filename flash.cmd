esptool.py --chip esp32 -p COM3 erase_flash
esptool.py --chip esp32 -p COM3 --baud 460800 write_flash -z 0x1000 esp32-idf3-20190529-v1.11.bin