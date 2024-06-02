import re
import datetime
sekarang = datetime.datetime.now()
kal = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."
a = re.sub("-","/",kal)
b = re.findall("\d+/\d+/\d+",a)
from datetime import datetime
for tanggal in b:
    tanggal = datetime.strptime(tanggal, "%Y/%m/%d")
    hasil = sekarang - tanggal
    print(f"{tanggal} selisih {hasil.days} hari")
