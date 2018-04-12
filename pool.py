from  multiprocessing import Process,Pool
import time
  
def Foo(i):
    time.sleep(2)
    print('Foo: ',i)
    return i+100
  
def Bar(arg):
    print('-->exec done:',arg)
  
pool = Pool(5)
  
for i in range(10):
    pool.apply_async(func=Foo, args=(i,),callback=Bar)
    #pool.apply(func=Foo, args=(i,))
  
print('end')
pool.close()
pool.join()
