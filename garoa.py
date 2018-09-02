#!/usr/bin/env python
# coding: utf-8

class Pessoa():
  def __init__(self, nome):
    self.nome = nome
    self.cmc = None
    self.associacao = []
    self.padawans = []

  def __repr__(self):
    return self.nome

  def apresenta_padawans(self, pessoas):
    for p in pessoas:
      self.apresenta_padawan(p)

  def apresenta_padawan(self, pessoa):
    self.padawans.append(pessoa)
    self.cmc.padawans.append(pessoa)

class ConselhoMandaChuva():
  def __init__(self, fundadores=[]):
    self.associados = fundadores
    self.padawans = []
    self.ex_associados = []

    for f in fundadores:
      f.cmc = self

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

  def aprova_associado(self, pessoa, endosso=None):
    pessoa.cmc = self
    pessoa.associacao.append([self.dia, None])

    if pessoa in self.padawans:
      self.padawans.remove(pessoa)
    else:
      print("ERRO: Aprovando associado '{}' que não é padawan de ninguém!".format(pessoa.nome))
    if pessoa not in self.associados:
      self.associados.append(pessoa)

  def observa_desligamento(self, pessoa, motivo=None):
    pessoa.cmc = None
    try:
      pessoa.associacao[-1][1] = self.dia
    except:
      print("ERRO: Desligando '{}' que nem era associado!".format(pessoa.nome))


    if pessoa not in self.ex_associados:
      self.ex_associados.append(pessoa)

    if pessoa in self.associados:
      self.associados.remove(pessoa)
