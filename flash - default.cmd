esptool.py --chip esp32 -p COM3 erase_flash
esptool.py --chip esp32 -p COM3 write_flash --flash_mode dio --flash_size 2MB 0x0 factory_default.bin