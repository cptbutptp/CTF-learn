#coding:utf-8
import base64

text=raw_input('miwen:')


for i in range(0,10):
	try:
		text1=base64.b16decode(text)
		text=text1
	except Exception,e:
		pass
		try:
			text1=base64.b32decode(text)
			text=text1
		except Exception,e:
			pass
			try:
				text1=base64.b64decode(text)
				text=text1
			except Exception,e:
				pass
print text


