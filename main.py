import requests, os, time

os.system('cls & mode 70, 32 & title github profile views booster | by lozza (github.com/qro)')
user = "https://camo.githubusercontent.com/673e0d6022ecef69601e1c5cf4ec6e271570b43797867108d9dcc74f504fa6b6/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d71726f26636f6c6f723d6c6967687467726579" # put profile here
p = ("proxies.txt")
pfile = open(p, 'r')

for txt in pfile:
	prox = {'http': txt}
	r = requests.get(user, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63'}, proxies=prox)
	print(time.strftime(" [>] (%H:%M:%S) Request sent"))