#!/usr/bin/env python
# coding: utf-8
#
# (c) 2019 Felipe Correa da Silva Sanches <juca@members.fsf.org>
# Licensed under the terms of the GNU General Public License, version 2 (or later)
import os

PEDANTE = False

class Pessoa():
  def __init__(self, nome, wiki=None):
    self.nome = nome
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
      p.apresentacao = self.cmc.dia
      self.padawans.append(p)
      self.cmc.padawans.append(p)


def menos_de_6_meses(data):
  import datetime
  ano, mes, dia = data.split('-')
  data = datetime.datetime(int(ano), int(mes), int(dia))
  hoje = datetime.datetime.today()
  return (hoje - data).days <= 6*30


class ConselhoMandaChuva():
  def __init__(self, fundadores=[]):
    self.num_fundadores = len(fundadores)
    self.associados = fundadores
    self.padawans = []
    self.ex_associados = []

    for f in fundadores:
      f.cmc = self
      f.cofundador = True

  def pergunta(self, p):
    print("Pergunta: '{}'".format(p))

  def data(self, d):
    self.dia = d
    print("CMC de {}:".format(d))

  def readmite_associado(self, pessoa):
    pessoa.cmc = self

    if pessoa in self.ex_associados:
      self.ex_associados.remove(pessoa)

    if pessoa not in self.associados:
      self.associados.append(pessoa)

    pessoa.associacao.append([self.dia, None])

  def aprova_associado(self, pessoa, endosso=None, fundador=False):
    pessoa.cmc = self
    pessoa.associacao.append([self.dia, None])
    pessoa.endosso = endosso

    if pessoa in self.padawans:
      self.padawans.remove(pessoa)
    else:
      if not fundador and endosso != "HACK":
        print("ERRO: Aprovando associado '{}' que não é padawan de ninguém!".format(pessoa.nome))
    if pessoa not in self.associados:
      self.associados.append(pessoa)

  def observa_desligamento(self, pessoa, motivo=None):
    pessoa.cmc = None

    if pessoa not in self.ex_associados:
      self.ex_associados.append(pessoa)

    if pessoa in self.associados:
      self.associados.remove(pessoa)
      try:
        pessoa.associacao[-1][1] = self.dia
      except:
        if PEDANTE:
          print("ERRO: nao achei registro de associacao para '{}'".format(pessoa.nome))
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
      dot.node("Pessoa_{}".format(pessoas.index(p)), '\n'.join(p.nome.split()))

    for p in pessoas:
      if p.endosso == "HACK":
        dot.edge("Pre_sistema_de_padawanice",
                 "Pessoa_{}".format(pessoas.index(p)))

      for padawan in p.padawans:
        dot.edge("Pessoa_{}".format(pessoas.index(p)),
                 "Pessoa_{}".format(pessoas.index(padawan)))

    dot.render('garoa-associados', view=True)
    os.rename('garoa-associados', 'garoa-associados.gv')
