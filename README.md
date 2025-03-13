Instructions:
1. In the Arduino IDE under "Boards Manager", install "esp32" by Espressif Systems.
2. Select Tools -> Board -> esp32 -> AI Thinker ESP32-CAM.
3. Create a 2.4 GHz WiFi network and add the SSID and password to "ESP_Cam_Project.ino"
4. Ensure the baud rate is set to 115200 in the Serial Monitor.
5. Upload sketch to the ESP32-CAM via USB. If errors occur, consider updating the board's drivers using "CH431 SER Driver.exe".
6. Once connected, go to the URL displayed in the Serial Monitor.
7. In "YOLO11 Model.py", set the source equal to the URL including the video stream port number.
