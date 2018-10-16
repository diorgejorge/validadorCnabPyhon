# -*- coding: utf-8 -*-
from validarP import validarP
from validarQ import validarQ
def generate(fileDir):
  with open(fileDir) as f:
    global valorTitulo
    global valorAbatimento
    global dataVencimento
    global dataEmissao
    global nomePagador
    global nomeSacado
    global nomeAvalista
    global enderecoPagador
    global enderecoSacado
    global enderecoAvalista
    global numeroDeInscricaoAvalista
    global dataJuros
    global bairroPagador
    global cidadePagador
    for line_number, line in enumerate(f):
        type = line[7:8]
        if type == "0" :
          print 'ae'
        elif type == "1":
          print 'ae'
        elif type == "3":
          segmento = line[13:14]
          if segmento == "P":
            validarP(line,line_number)
          if segmento == "Q":
            validarQ(line,line_number)
        elif type == "5":
          print 'ae'
        elif type == "9":
          print 'ae'
generate("/media/totvs/OS/CNAB/GERADOS/CLI_CRB_00433_20180507_CNAB240REM.00001")
