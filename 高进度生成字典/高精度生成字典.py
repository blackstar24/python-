# coding=utf-8
import exrex
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
传入host 例如：http://demo.webdic.com
'''
web_white = ['com','cn','gov','edu','org','www']

def host_para(host):
	#对host进行分析，处理成我们想要的格式
	if '://' in host:
		host = host.split('://')[1].replace('/','')
	if '/' in host:
		host = host.replace('/','')
	return host

def dic_create(hosts):
	web_dics = hosts.split('.')
	#取出有用的东西，如demo,webdic,放入字典生成的地方，生成字典。
	f_rule = open('rule.ini','r')
	for i in f_rule:
		if '#' != i[0]:
			rule = i
	f_pass_out = open('pass1.txt','w')
	for web_dic in web_dics:
		if web_dic not in web_white:
			f_pass = open('pass.txt','r')
			for dic_pass in f_pass:
				dics = list(exrex.generate(rule.format(web_dic=web_dic,dic_pass=dic_pass.strip('\n'))))
				for dic in dics:
					f_pass_out.write(dic+'\n')
					print dic
	f_pass_out.close()

dic_create(host_para('demo.webdic.com'))

