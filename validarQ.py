# -*- coding: utf-8 -*-
import re
def validarQ(line,line_number):
  nomePagador = line[33:73]
  enderecoPagador = line[73:113]
  bairroPagador = line[113:128]
  cidadePagador = line[136:151]
  nomeAvalista = line[169:209]
  numeroDeInscricaoAvalista = line[154:169]
  if(re.compile('\s').match(nomePagador)):
    print "segmento Q linha:",line_number,"34:73-> nome de pagador não pode estar em branco"
  if(re.compile('\s').match(enderecoPagador)):
    print "segmento Q linha:",line_number,"74:113-> endereço do pagador não pode estar em branco"
  if(re.compile('\s').match(nomeAvalista)):
    print "segmento Q linha:",line_number,"170:209-> nome do avalista não pode estar em branco"
  if(re.compile('[0]{15}').match(numeroDeInscricaoAvalista)):
    print "segmento Q linha:",line_number,"155:169-> numero inscricao avalista não pode estar em branco"
  if(re.compile('\s').match(bairroPagador)):
    print "segmento Q linha:",line_number,"113:128-> bairro do pagador não pode estar em branco"
  if(re.compile('\s').match(cidadePagador)):
    print "segmento Q linha:",line_number,"136:151-> cidade do pagador não pode estar em branco"
