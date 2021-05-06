import speedtest

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
#s.get_servers(servers)

fid = open('data.txt','w')
for i in range(100):
	try:
		s.get_best_server()
		d = float(s.download(threads=threads))/1000000
		u = float(s.upload(pre_allocate=False,threads=threads))/1000000
		p = s.results.ping
		print("%.2f\t%.2f\t%.2f"%(d,u,p))
		fid.write("%.2f\t%.2f\t%.2f"%(d,u,p))
	except KeyboardInterrupt:
		break

print("Test closed\n")
fid.close()

#s.results.share()

results_dict = s.results.dict()
