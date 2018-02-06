#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Cria o esqueleto de pastas para armazenamento de dados da aplicação Evolutto
# (base de dados, arquivos usados pela plataforma, etc)
# Cria o arquivo de configuração (envvars) para a aplicação
#

import argparse
import os

parser = argparse.ArgumentParser(description='Cria o esqueleto (estrutuda de pastas) para armazenamento dos dados da plataforma Evolutto')
parser.add_argument('-d','--datadir', help='Diretório base para a armazenamento dos dados utilizados pela plataforma Evolutto',required=True)
args = parser.parse_args()

## show values ##
datadir = args.datadir

print ("Diretório raiz para dados : %s" % datadir )

#
# ---> diretórios que devem ser criados
#
dirs = {
        'COMPOSER_CACHE_DIR': 'cache/composer',
        'EVOLUTTO_FRONTEND_BASE_DIR': 'frontend',
        'EVOLUTTO_PLATAFORMA_CONSULTORIA_CACHE_DIR': 'cache/consultoria',
        'EVOLUTTO_PLATAFORMA_PRM_CACHE_DIR': 'cache/prm',
        'EVOLUTTO_PLATAFORMA_CONSULTORIA_LOG_DIR': 'logs/consultoria',
        'EVOLUTTO_PLATAFORMA_PRM_LOG_DIR': 'logs/prm',
        'EVOLUTTO_APACHE_LOG_DIR': 'logs/apache',
        'EVOLUTTO_MONGODB_DATA_DIR': 'mongodb/data',
        'EVOLUTTO_MONGODB_SHARE_DIR': 'mongodb/share',
        'EVOLUTTO_PLATAFORMA_MYSQL_DATA_DIR': 'mysql/data',
        'EVOLUTTO_PLATAFORMA_MYSQL_SHARE_DIR': 'mysql/share',
        'EVOLUTTO_CONSULTORIA_ARQUIVOS_DIR': 'plataforma-arquivos'
      }


#
# ---> cria a estrutura de pastas
#
for dir in list(dirs.values()):
    dirVer = datadir + '/' + dir

    try:
      os.makedirs(dirVer)
    except:
      print ("Não foi possivel criar %s" % dirVer)




#
# ---> cria o arquivo com as configurações (variáveis de ambiente)
#

fileConfig = open('./envvars', 'w')

fileConfig.write("# -- NÃO EDITE ESTE ARQUIVO. Ele é criado automaticamente\n\n")

fileConfig.write("export EVOLUTTO_PLATAFORMA_HOSTNAME=evolutto.localhost\n\n")

fileConfig.write("export EVOLUTTO_PLATAFORMA_BASE_DIR=..\n\n")

for key in dirs.keys():
   cmd = 'export ' + key + '=' + datadir + '/' + dirs[key] + "\n"
   fileConfig.write(cmd)
fileConfig.close()

