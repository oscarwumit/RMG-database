#!/usr/bin/env python
# encoding: utf-8

name = "CJ-frag"
shortDesc = u""
longDesc = u""""""

entry(
    index = 1,
    label = "s18 + HO2 <=> s18-rad1 + H2O2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.07227e-07, 'cm^3/(mol*s)'), n=5.51849, Ea=(15.8562, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 2,
    label = "s18 + HO2 <=> s18-rad2 + H2O2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.90798e-39, 'cm^3/(mol*s)'), n=15.3474, Ea=(6.51402, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)
