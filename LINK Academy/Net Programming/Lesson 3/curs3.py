# import _thread
# import threading
# import time

# def printeaza_ceva(inainte, dupa):
#     print("Inainte de sleep...", inainte)
#     time.sleep(3)
#     print("Hello", dupa)
#     print("Identificatorul threadului din functia printeaza", threading.get_ident())

# # printeaza_ceva("AAA", "BBB")

# # _thread.start_new_thread(printeaza_ceva, ("CCC", "DDD"))
# # print("Identificatorul threadului din functia printeaza", _thread.get_ident())
# # time.sleep(10)


# t1 = threading.Thread(target=printeaza_ceva, args=("EEE", "FFF"))
# t1.start()



# t2 = threading.Thread(target=printeaza_ceva, args=("GGG", "HHH"))
# t2.start()


import threading
import time

# tuplu = (1)
# print(tuplu)

# t = threading.Thread(target=lambda x: print(x**2), args=(2, ))
# t.start()

an = 2023

def incrementeaza_anul():
    global an
    time.sleep(0.1)
    an += 1

threads = []

for i in range(3):
    threads.append(threading.Thread(target=incrementeaza_anul, args=()))

for th in threads:
    th.start()

print(an)