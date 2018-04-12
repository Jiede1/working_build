#coding:utf-8
# join()：在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
 
# setDaemon(True)：
'''
         将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
 
         当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程 就分兵两路，分别运行，那么当主线程完成
 
         想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是只要主线程
 
         完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以 用setDaemon方法啦
'''
 
 
import threading
from time import ctime,sleep
import time
 
def Music(name):
 
        print ("Begin listening to {name}. {time}".format(name=name,time=ctime()))
        sleep(3)
        print("end listening {time}".format(time=ctime()))
 
def Blog(title):
 
        print ("Begin recording the {title}. {time}".format(title=title,time=ctime()))
        sleep(5)
        print('end recording {time}'.format(time=ctime()))
 
 
threads = []
 
 
t1 = threading.Thread(target=Music,args=('FILL ME',))
t2 = threading.Thread(target=Blog,args=('',))
 
threads.append(t1)
threads.append(t2)
 
if __name__ == '__main__':
 
    #t2.setDaemon(True)
 
    for t in threads:
 
        t.setDaemon(True) #注意:一定在start之前设置
        t.start()
 
        #t.join()
 
    t1.join()
    t2.join()    #  考虑这三种join位置下的结果？
 
    print ("all over %s" %ctime())
