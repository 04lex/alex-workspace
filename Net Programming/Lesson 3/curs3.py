import _thread
import threading
import time

def printeaza_ceva(inainte, dupa):
    print("Inainte de sleep...", inainte)
    time.sleep(3)
    print("Hello", dupa)
    print("Identificatorul threadului din functia printeaza", threading.get_ident())

# printeaza_ceva("AAA", "BBB")

# _thread.start_new_thread(printeaza_ceva, ("CCC", "DDD"))
# print("Identificatorul threadului din functia printeaza", _thread.get_ident())
# time.sleep(10)


t1 = threading.Thread(target=printeaza_ceva, args=("EEE", "FFF"))
t1.start()



t2 = threading.Thread(target=printeaza_ceva, args=("GGG", "HHH"))
t2.start()