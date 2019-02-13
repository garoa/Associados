#!/usr/bin/env python
# coding: utf-8
#
# (c) 2019 Felipe Correa da Silva Sanches <juca@members.fsf.org>
# Licensed under the terms of the GNU General Public License, version 2 (or later)
import os

PEDANTE = False

class Pessoa():
  def __init__(self, nome, wiki=None, apelido=None):
    self.nome = nome
    self.apelido = apelido
    self.wiki = wiki
    self.cmc = None
    self.associacao = []
    self.padawans = []
    self.cofundador = False
    self.endosso = None

  def __repr__(self):
    return self.nome

  def apresenta_padawans(self, padawans):
    for p in padawans:
      self.apresenta_padawan(p)

  def apresenta_padawan(self, p):
    if p in self.cmc.padawans:
      if self not in p.jedi:
        p.jedi.append(self)
      print(("{} já havia sido apresentado"
             " como padawan no dia {}!").format(p.nome,
                                                p.apresentacao))
    else:
      p.jedi = [self]
      p.apresentacao = self.cmc.data_da_reuniao
      self.padawans.append(p)
      self.cmc.padawans.append(p)


def menos_de_6_meses(data):
  import datetime
  ano, mes, dia = data.split('-')
  data = datetime.datetime(int(ano), int(mes), int(dia))
  hoje = datetime.datetime.today()
  return (hoje - data).days <= 6*30


class ConselhoMandaChuva():
  def __init__(self, fundadores):
    self.data_da_reuniao = "????-??-??"
    self.num_fundadores = len(fundadores)
    self.associados = fundadores
    self.padawans = []
    self.ex_associados = []

    for f in fundadores:
      f.cmc = self
      f.cofundador = True

  def pergunta(self, pergunta):
    print("[{}] Pergunta: '{}'".format(self.data_da_reuniao, pergunta))

  def data(self, d):
    self.data_da_reuniao = d
    print("CMC de {}:".format(d))

  def readmite_associado(self, pessoa):
    pessoa.cmc = self

    if pessoa in self.ex_associados:
      self.ex_associados.remove(pessoa)

    if pessoa not in self.associados:
      self.associados.append(pessoa)

    pessoa.associacao.append({"admissao": self.data_da_reuniao})

  def aprova_associado_honorario(self, pessoa):
    """FIXME: Implementar esse método."""

  def aprova_associado(self, pessoa, endosso=None, fundador=False):
    pessoa.cmc = self
    pessoa.associacao.append({"admissao": self.data_da_reuniao})
    pessoa.endosso = endosso

    if pessoa in self.padawans:
      self.padawans.remove(pessoa)
    else:
      if not fundador and endosso != "HACK":
        print("ERRO: Aprovando associado '{}' que não é padawan de ninguém!".format(pessoa.nome))
    if pessoa not in self.associados:
      self.associados.append(pessoa)

  def nao_documentou_desligamento(self, pessoa, motivo=None):
    """Para todos efeitos, esse método é equivalente ao
       observa_desligamento. Mas ele é usado para que não
       haja confusão, diferenciando os desligamentos que constam
       em atas, daqueles que foram inferidos por outros meios como,
       por exemplo, pela planilha de associados mantida pelo tesoureiro."""
    self.observa_desligamento(pessoa, motivo)

  def observa_desligamento(self, pessoa, motivo=None):
    pessoa.cmc = None

    if pessoa not in self.ex_associados:
      self.ex_associados.append(pessoa)

    if pessoa in self.associados:
      self.associados.remove(pessoa)
      try:
        pessoa.associacao[-1]["desligamento"] = self.data_da_reuniao
        pessoa.associacao[-1]["motivo"] = motivo
      except IndexError:
        if PEDANTE:
          print("ERRO: não achei registro de associação para '{}'".format(pessoa.nome))
    else:
      print("ERRO: Desligando '{}' que nem era associado!".format(pessoa.nome))


  def print_padawans(self):
    def jedis_str(x):
      return ', '.join(map(lambda m: m.nome, x.jedi))

    print("Padawans órfãos:\n\t{}".format('\n\t'.join(map(lambda x: "{}: {}\t\t(indicação: {})".format(x.apresentacao, x.nome, jedis_str(x)), self.padawans))))

  def print_associados(self):
    self.associados = sorted(self.associados, key=lambda x: len(x.padawans), reverse=True)
    print("Associados:\n\t{}".format('\n\t'.join(map(lambda x: "{} ({})".format(x.nome, len(x.padawans)), self.associados))))

  def output_graph(self):
    from graphviz import Digraph
    dot = Digraph(comment='Associados e Padawans do Garoa Hacker Clube')
    dot.engine = "neato"
    dot.attr('graph', overlap="false")
#    dot.attr('node', shape='circle')
    dot.attr('node', labelloc='c')
    dot.attr('node', fontsize='12')
    dot.attr('node', style='filled')
    dot.attr('node', fontcolor="#eeffee")

    pessoas = self.associados + self.padawans + self.ex_associados
    dot.attr('node', color='black')
    dot.node("Pre_sistema_de_padawanice", "Primeiros associados\nantes da criação\ndo sistema\nde padawanice")

    for p in pessoas:
      if p.cofundador:
        dot.attr('node', color='black')
      elif p in self.ex_associados:
        dot.attr('node', color='gray')
      elif p.associacao == []: # é padawan
        if menos_de_6_meses(p.apresentacao):
          # é padawan recente
          dot.attr('node', color='#cccc00')
        else:
          # provavelmente é um padawan abandonado
          # ou com muito pouca chance de se efetivar associado
          dot.attr('node', color='#cc7777')
      else: # atualmente é associado
        dot.attr('node', color='#559955')

      nome = '\n'.join(p.nome.split())
      if p.apelido:
        nome += '\n({})'.format(p.apelido)
      dot.node("Pessoa_{}".format(pessoas.index(p)), nome)


    for p in pessoas:
      if p.endosso == "HACK":
        dot.edge("Pre_sistema_de_padawanice",
                 "Pessoa_{}".format(pessoas.index(p)))

      for padawan in p.padawans:
        dot.edge("Pessoa_{}".format(pessoas.index(p)),
                 "Pessoa_{}".format(pessoas.index(padawan)))

    dot.render('garoa-associados', view=True)
    os.rename('garoa-associados', 'garoa-associados.gv')
