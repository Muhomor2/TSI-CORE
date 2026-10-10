#!/usr/bin/env python3
"""Exhaustive finite-model checks for the *specified examples* in TSI-CORE-1.0-RC2.

Pure Python 3.10+, no external dependencies.
Does NOT prove general theorems or replace a proof assistant / independent review.
Data are transcribed from the canonical spec's sections 8–10; errors in the
transcription or in this verifier remain possible.
"""
from dataclasses import dataclass
from itertools import product
import json

AXIOMS = ('AX-C01', 'AX-C02', 'AX-C04', 'AX-C05', 'AX-C06', 'AX-C07')

@dataclass(frozen=True)
class Model:
    R: tuple
    T: tuple
    E: frozenset   # subset Rep * Rep
    A: frozenset   # subset Trans * Rep * Rep
    C: frozenset   # subset Trans * Trans * Trans
    unit: str = 'e'


def mk(R, T, E, A, C):
    return Model(tuple(R), tuple(T), frozenset(E), frozenset(A), frozenset(C))


def check_signature(m):
    r, t = set(m.R), set(m.T)
    return bool(r and t and m.unit in t and
                all(x in r and y in r for x, y in m.E) and
                all(f in t and x in r and y in r for f, x, y in m.A) and
                all(f in t and g in t and h in t for f, g, h in m.C))


def check_axioms(m):
    R, T, E, A, C, e = m.R, m.T, m.E, m.A, m.C, m.unit
    c01 = (all((x,x) in E for x in R) and
           all((y,x) in E for x,y in E) and
           all((x,z) in E for x,y,z in product(R,repeat=3)
               if (x,y) in E and (y,z) in E))
    c02 = all(y == z for f,x,y,z in product(T,R,R,R)
              if (f,x,y) in A and (f,x,z) in A)
    c04 = all(((h,x,z) in A) == any((g,x,y) in A and (f,y,z) in A for y in R)
              for f,g,h in C for x,z in product(R,repeat=2))
    c05 = all((e,x,x) in A for x in R)
    c06 = all((e,f,f) in C and (f,e,f) in C for f in T)
    c07 = all(v == z for f,g,h,u,v,w,z in product(T, repeat=7)
              if (f,g,u) in C and (u,h,v) in C and
                 (g,h,w) in C and (f,w,z) in C)
    return dict(zip(AXIOMS, (c01,c02,c04,c05,c06,c07)))


def structural_all(m):
    return all((y,yp) in m.E for f,x,xp,y,yp in product(m.T,m.R,m.R,m.R,m.R)
               if (x,xp) in m.E and (f,x,y) in m.A and (f,xp,yp) in m.A)


def unit_comp(T):
    return set([('e',f,f) for f in T] + [(f,'e',f) for f in T])


IDENTITY_EQ_2 = {(0,0),(1,1)}
EXAMPLES = {
    'M0_satisfiability': mk(['r'],['e'],{('r','r')}, {('e','r','r')},{('e','e','e')}),
    'not_AX-C01': mk([0,1],['e'],set(),{('e',0,0),('e',1,1)},{('e','e','e')}),
    'not_AX-C02': mk([0,1],['e'],IDENTITY_EQ_2,
                     {('e',0,0),('e',0,1),('e',1,1)},{('e','e','e')}),
    'not_AX-C04': mk([0,1],['e','f'],IDENTITY_EQ_2,
                     {('e',0,0),('e',1,1),('f',0,1),('f',1,1)},
                     {('e','e','e'),('e','f','f'),('f','e','f'),('f','f','e')}),
    'not_AX-C05': mk([0],['e'],{(0,0)},set(),{('e','e','e')}),
    'not_AX-C06': mk([0],['e'],{(0,0)},{('e',0,0)},set()),
    'not_AX-C07': mk([0,1],['e','a','b','c','p','q','r','s'],IDENTITY_EQ_2,
                     {(f,x,x) for f in ('e','a','b','c','p','q','r','s') for x in (0,1)},
                     unit_comp(('e','a','b','c','p','q','r','s')) |
                     {('a','b','p'),('p','c','r'),('b','c','q'),('a','q','s')}),
    'not_AX-C08': mk([0,1,2],['e','a'],
                     {(0,0),(0,1),(1,0),(1,1),(2,2)},
                     {('e',0,0),('e',1,1),('e',2,2),('a',0,0),('a',1,2)},
                     {('e','e','e'),('e','a','a'),('a','e','a')}),
}


def main():
    results = {}
    ok = True
    for name, m in EXAMPLES.items():
        sig = check_signature(m)
        ax = check_axioms(m)
        c08 = structural_all(m)
        expect = {k: True for k in AXIOMS}
        if name.startswith('not_AX-C0') and name != 'not_AX-C08':
            expect[name.replace('not_', '')] = False
        expect_c08 = name == 'not_AX-C08'
        passed = bool(sig and ax == expect and (not c08 if expect_c08 else True))
        ok &= passed
        results[name] = {
            'typed': sig, 'axioms': ax, 'AX-C08_structural_all': c08,
            'expected_axioms': expect, 'case_passed': passed,
        }
    result = {
        'status': 'PASS' if ok else 'FAIL',
        'scope': 'finite-example-exhaustive-check; not a proof-assistant verification',
        'checked_examples': len(EXAMPLES), 'examples': results,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
