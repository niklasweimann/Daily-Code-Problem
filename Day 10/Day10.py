import time

def jobscheduler(f, n):
	time.sleep(n/1000)
	return f()

print("Before: " + time.ctime())
print(jobscheduler(lambda: "Thread", 2000))
print("After: " + time.ctime())