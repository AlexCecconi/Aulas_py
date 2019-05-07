from pymongo import MongoClient, DESCENDING
import time

try:
	client = MongoClient("mongodb://admin:aPSFpvXDLWfHtEX7@cluster0-shard-00-00-nstlp.mongodb.net:27017,cluster0-shard-00-01-nstlp.mongodb.net:27017,cluster0-shard-00-02-nstlp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
	db = client['chat']
except Exception as e:
	print('ERRO: {}'.format(e))
	exit()

def cadastrar(name,mensagem):
	db.chat.insert({
		'name':name,
		'mensagem':mensagem,
		'hora':time.strftime('%d-%m-%Y %H:%M:%S')
		})

def select():
	ultimo = [x for x in db.chat.find().sort('_id', DESCENDING)]
	while True:
		atual = [x for x in db.chat.find().sort('_id', DESCENDING)]
		if atual != ultimo:
			print('[{}] {} : {} \n'.format(
				atual[0]['hora'], atual[0]['name'], atual[0]['mensagem']
			))
			ultimo = atual 
		time.sleep(2.0)