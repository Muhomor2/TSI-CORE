# RC2 bilingual repository — release readiness

## Completed in this preparation package

- [x] Canonical English RC2 preserved without formula changes.
- [x] Companion scientific Russian exposition prepared (normative source identified).
- [x] English and Russian general-reader explanations prepared.
- [x] Editorial claims distinguish formal satisfiability from empirical usefulness.
- [x] Historic document retained separately from RC2 source.
- [x] Finite-model test script and reproducible JSON output added.
- [x] Hashes of the canonical source and the four editions recorded.
- [x] README provides direct bilingual links.

## Required before final audited scientific release

- [ ] Independently confirm correctness of all six independence countermodels.
- [ ] Independently confirm TH-C00 instantiation and full TH-C02 proof.
- [ ] Cross-check relation to established partial-map and restriction-category mathematics, with bibliography.
- [ ] Independently review scientific Russian translation for exact correspondence to original axioms.
- [ ] Have an outside reviewer inspect the eight-model Python encoding.
- [ ] Formalize the six axiom groups and proofs in Lean 4.
- [ ] Formalize minimal model, six independence witnesses, AX-C08 nonderivability example.
- [ ] Replicate essential claims in Isabelle/HOL.
- [ ] Collect verified toolchain versions, logs, and source hashes.
- [ ] Decide an explicit licensing policy; don't assume CC BY or an OSS license.
- [ ] Validate citation metadata against actual public release date and GitHub URL.
- [ ] Create dedicated GitHub repository `Muhomor2/TSI-CORE`.
- [ ] Publish a prepublication tag if desired, clearly labeled **not machine verified**.
- [ ] Render/check scientific PDFs if required for Zenodo.
- [ ] Register an archival Zenodo record only after checking released files and metadata.
- [ ] Add actual DOI to README/CITATION if and when minted.

## Academic status language (recommended)

> TSI-CORE-1.0-RC2 is a publication candidate presenting a two-sorted first-order specification, a finite model, finite independence countermodels, and derived claims. Its supplied finite examples have also been checked with a simple Python enumerator. Independent final audit, proof-assistant verification, and empirical validation of extension modules are pending.

Avoid claims of a certified, universal, empirical, or machine-verified theory.
