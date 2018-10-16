# -*- coding: utf-8 -*-
from datetime import datetime

def validarAbatimento(line,line_number):
  valorTitulo = line[85:100]
  valorAbatimento = line[180:195]
  if(valorTitulo<valorAbatimento):
      print "segmento P linha:",line_number,"181:195 86:100-> o valor do abatimento deve ser menor que o valor do titulo"

def validarDesconto(line,line_number):
  tipoDesconto = line[141:142]
  valorDesconto = line[150:165]
  if(tipoDesconto == 1):
    if(valorDesconto>valorTitulo):
      print "segmento P linha:",line_number,"151:165 86:100-> o valor do desconto 1 deve ser menor que o valor do titulo"
  if(tipoDesconto==2):
    if(valorDesconto>9999):
        print "segmento P linha:",line_number,"151:165 86:100-> o valor do desconto 1 deve ser menor que o valor do titulo"

def validarDatas(line,line_number):
  dataVencimento = datetime.strptime(line[77:85],'%d%m%Y')
  dataEmissao = datetime.strptime(line[109:117],'%d%m%Y')
  dataJuros = datetime.strptime(line[118:126],'%d%m%Y')
  if (dataVencimento>dataEmissao):
   print "segmento P linha:",line_number,"78:85 110:117-> a data de vencimento não pode ser inferior a data de emissão"
  if (dataJuros>dataEmissao):
   print "segmento P linha:",line_number,"119:126 78:85-> a data de juros não pode ser inferior a data de emissao"
  if (dataJuros<dataVencimento):
   print "segmento P linha:",line_number,"119:126 78:85-> a data de juros não pode ser inferior a data de vencimento"

def validarP(line,line_number):
  validarDesconto(line,line_number)
  validarDatas(line,line_number)
  validarAbatimento(line,line_number)
