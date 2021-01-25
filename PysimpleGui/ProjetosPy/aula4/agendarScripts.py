import schedule
import time
import threading

def job():
    print("Estou executando a thread %s" % threading.current_thread())

def executar_thread(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(10).seconds.do(executar_thread, job)
schedule.every(10).seconds.do(executar_thread, job)


while 1:
    schedule.run_pending()
    time.sleep(1)
