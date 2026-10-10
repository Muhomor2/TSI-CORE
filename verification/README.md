# Finite-model test scope / О чём говорят автоматические проверки

Run from repository root:

```bash
python3 verification/check_finite_models.py
```

The script checks all relevant finite assignments for **eight explicitly written structures** from sections 8–10 of the English normative specification:

1. Minimal model M0 (all six mandatory axiom groups hold).
2. Six witness structures, with exactly one designated mandatory axiom group failing each time.
3. One structure in which the six mandatory groups hold and optional structural preservation AX-C08 fails.

The result JSON has `status=PASS` when all finite examples match their claimed satisfaction pattern. The assertions are fully quantified **over each listed finite domain**, but this test does **not** prove any universally quantified theorem about all structures or prove the formulas encoded in Python faithfully reproduce the specification.

**Not claimed:** formal proof assistant verification, an independent implementation, all-model validity of derived theorems, peer review, empirical validation, or scientific novelty.

Русский: программа проверяет восемь конечных *примеров*, а не доказывает общее утверждение о всех моделях. Для полноценной формальной верификации требуются Lean/Isabelle и независимая сверка кодировки с исходными математическими формулами.
