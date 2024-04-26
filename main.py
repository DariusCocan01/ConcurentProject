from Downloadthread import DownloadThread
from DecryptThread import DecryptThread
from Combiner import Combiner
import threading
download_thread1 = DownloadThread('https://advancedpython.000webhostapp.com/s1.txt', 's1_enc.txt')
download_thread2 = DownloadThread('https://advancedpython.000webhostapp.com/s2.txt', 's2_enc.txt')
download_thread3 = DownloadThread('https://advancedpython.000webhostapp.com/s3.txt', 's3_enc.txt')

download_thread1.start()
download_thread2.start()
download_thread3.start()

download_thread1.join()
download_thread2.join()
download_thread3.join()


decrypt_thread1 = DecryptThread('s1_enc.txt','s1.txt')
decrypt_thread2 = DecryptThread('s2_enc.txt','s2.txt')
decrypt_thread3 = DecryptThread('s3_enc.txt','s3.txt')
decrypt_thread1.start()
decrypt_thread2.start()
decrypt_thread3.start()
decrypt_thread1.join()  
decrypt_thread2.join()  
decrypt_thread3.join()

combiner = Combiner('s1.txt', 's2.txt', 's3.txt')
combiner.combine_files()

with open('s_final.txt', 'r') as file:
    content = file.read()

print(content)