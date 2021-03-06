import speedtest
import datetime
from time import sleep

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)

fid = open('data.txt','w')

print('Starting Test')
for i in range(100):
	try:
		s.get_best_server()
		sleep(10) # time for settling the best server
		d = float(s.download(threads=threads))/1000000
		u = float(s.upload(pre_allocate=False,threads=threads))/1000000
		ct = datetime.datetime.now()
		p = s.results.ping
		print("%.2f\t%.2f\t%.2f\t%s"%(d,u,p,ct))
		fid.write("%.2f\t%.2f\t%.2f\t%s\n"%(d,u,p,ct))
		sleep(10) # wait interval
	except KeyboardInterrupt:
		break

print("Test closed\n")
fid.close()

#s.results.share()

results_dict = s.results.dict()
