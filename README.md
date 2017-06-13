# esp8266-micropython-101
* all most command we demo on mac OS *

## Prerequisite
  - python 3
  - [virtualenvwrappe](http://virtualenvwrapper.readthedocs.io)
  - [CP210x USB to UART Bridge VCP Drivers](http://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
  - firmware [MicroPython downloads page](http://micropython.org/download#esp8266)
## How to Flash firmware micropython to esp8266
1. create virtualenv and activate

    ```
    # mkvirtualenv -p $(which python3) micropython-101
    Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.4/bin/python3
    Using base prefix '/Library/Frameworks/Python.framework/Versions/3.4'
    New python executable in /Users/montri.s/.virtualenvs/micropython-101/bin/python3
    Also creating executable in /Users/montri.s/.virtualenvs/micropython-101/bin/python
    Installing setuptools, pip, wheel...done.

    # setvirtualenvproject $VIRTUAL_ENV $(pwd)
    ```
2. Deploying the firmware

   ```  
   # pip install esptool
   ```

3. git clone

    ```
    # git clone https://github.com/montri2025/esp8266-micropython-101.git
    ```    
4. connect esp8266 with USB Port And then deploy the new firmware using:
    ```
    # esptool.py --port /dev/tty.wchusbserial1420 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20170612-v1.9.1.bin
    ```
