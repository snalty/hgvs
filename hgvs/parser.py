import os

import parsley

import hgvs.edit
import hgvs.location
import hgvs.posedit
import hgvs.variant

from hgvs.exceptions import *

class Parser(object):
    default_grammar_fn = os.path.join(os.path.dirname(__file__),'grammar.txt')

    def __init__(self,grammar_fn=default_grammar_fn):
        self._grammar_fn = grammar_fn
        self._grammar = parsley.makeGrammar(open(grammar_fn,'r').read(),{
            'CDSPosition': hgvs.location.CDSPosition,
            'Interval': hgvs.location.Interval,
            'Position': hgvs.location.Position,

            'DelIns': hgvs.edit.DelIns,
            'Dup': hgvs.edit.Dup,
            'Repeat': hgvs.edit.Repeat,
            
            'PosEdit': hgvs.posedit.PosEdit,

            'Variant': hgvs.variant.Variant,
            })
        
    def parse(self,variant):
        return self._grammar(variant).hgvs_variant()
        #try:
        #except Exception as e:
        #    raise HGVSParseError('{variant}: parsing raised {type} ({e.message})'.format(
        #        variant = variant, type = type(e), e = e))
