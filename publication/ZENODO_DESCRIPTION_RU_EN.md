# TSI-CORE-1.0-RC2 — Zenodo record description / Описание записи для Zenodo

**Intended resource type:** Publication → Preprint (research specification; not a peer-reviewed article).  
**Title:** TSI-CORE-1.0-RC2: Minimal Formal Kernel for Representations and Partial Transformations  
**Author / Автор:** Igor Chechelnitsky / Игорь Чечельницкий  
**ORCID:** https://orcid.org/0009-0007-4607-1946  
**Affiliation:** Independent Researcher, Ashkelon, Israel  
**Version:** 1.0-RC2 (specification dated 2026-07-30; do not confuse source date with public deposit date).  
**Publication status:** Public release candidate intended for independent scientific review; not machine-verified or peer-reviewed.  
**Source:** https://github.com/Muhomor2/TSI-CORE  
**Tagged source release:** https://github.com/Muhomor2/TSI-CORE/releases/tag/v1.0-RC2 (commit `96c45564dfe14e232836e5a9a15fb1598ccbfd84`)  
**DOI supplied by the author:** [10.5281/zenodo.23322303](https://doi.org/10.5281/zenodo.23322303); verify the record metadata, resource type, version and file list directly on Zenodo before citing it as an independently checked publication.  
**License:** Author's choice required before release. Do not guess or auto-assert a license.

## Abstract — English

TSI-CORE-1.0-RC2 specifies a deliberately minimal formal kernel for representations and partial transformations using classical many-sorted first-order logic with equality. The core has two sorts, three primitive relations, one distinguished transformation constant, and six mandatory axiom groups. It concerns representations, structural equivalence, partial action, declared composition, and a unit transformation. Notions of time, dynamics, probability, memory, geometry, observation, computation, and physical meaning are intentionally absent from the mandatory kernel.

The submitted specification states its signature and axioms, provides explicit finite satisfiability and axiom-independence examples, describes an optional structural-preservation principle that is not derivable from the mandatory core, and outlines requirements for conservative extensions. A reproducible Python checker enumerates the relevant assignments for eight finite examples and checks their expected satisfaction patterns. This is evidence concerning the stated finite examples, not a proof of all theorems, not proof-assistant verification, and not empirical validation. Translation and general-reader editions are supplied in Russian and English, with the English mathematical manuscript serving as the normative source.

The intended research contribution is a small, auditable interface for formulating and testing future extensions rather than a completed theory of cognition, physics, social governance, or distributed systems. Possible future connections to the FCO and UTS research programs are research hypotheses requiring explicit translation maps, independent security and correctness specifications, adversarial models, and separate evidence. In particular, the present core does not establish consensus safety, data confidentiality, election anonymity, bridge atomicity, or any empirical performance claim.

The release candidate is distributed to invite independent analysis of axiom consistency and independence claims, derivations, semantic limitations, connections to prior mathematical literature, and machine formalization. All corrections to the normative formulas must be versioned rather than silently replacing an archived release.

## Аннотация — русский

TSI-CORE-1.0-RC2 представляет минимальное формальное ядро для рассуждений о представлениях и частичных преобразованиях в классической многосортной логике первого порядка с равенством. Ядро содержит два сорта, три примитивных отношения, одну выделенную константу преобразования и шесть обязательных групп аксиом. Формализуются представления, структурная эквивалентность, частичное применение преобразований, объявленная композиция и единичное преобразование. В обязательном ядре намеренно отсутствуют время, динамика, вероятность, память, геометрия, наблюдение, вычисление и физическая интерпретация.

Спецификация включает сигнатуру и аксиомы, явные конечные примеры выполнимости и независимости аксиом, а также обсуждение дополнительного принципа сохранения структуры, который не выводится из обязательных аксиом. Приложенный Python-скрипт перебирает соответствующие конечные наборы значений для восьми моделей и проверяет заявленные схемы выполнения аксиом. Это проверка конкретных примеров, а не общее машинное доказательство теорем и не экспериментальное подтверждение. В составе публикации предоставлены научные и популярные редакции на русском и английском языках. Нормативным математическим текстом является английская редакция.

Назначение TSI-CORE — предоставить небольшую, проверяемую и расширяемую формальную основу для последующих модулей, а не объявить завершённую теорию познания, физики или распределённых систем. Возможное применение в проектах FCO и UTS остаётся отдельной исследовательской гипотезой: необходимы точные отображения объектов и операций, формальные требования безопасности, модели атак и независимые доказательства. Текущее ядро само по себе не доказывает безопасность консенсуса, конфиденциальность, анонимность выборов, атомарность мостов и эффективность практических систем.

Версия RC2 предоставляется для независимой критики аксиом, доказательств, контрмоделей, связи с существующей математикой и проверки в Lean/Isabelle. Изменение нормативных формул требует выпуска новой версии, а не незаметного исправления архивной публикации.

## Keywords / Ключевые слова

formal methods; many-sorted first-order logic; partial transformations; structural equivalence; declared composition; axiom independence; finite models; conservative extension; proof obligations; formal verification; TSI-CORE; математическая логика; частичные преобразования; независимость аксиом.

## Files and intended relationship

- `docs/TSI-CORE-1.0-RC2.md` — canonical normative English specification.
- `science/` — English/Russian scientific reading editions.
- `popular/` — English/Russian nontechnical explanations (not normative).
- `verification/` — reproducible finite-example script and reference results.
- `history/` — historical earlier audited version, not the normative RC2.
- `publication/UTS_TSI_INDEPENDENT_AUDIT_RU_EN.md` — proposed future compatibility audit, not a claim that UTS is verified.

### Publication ethics / Добросовестность

Do not describe this as peer-reviewed, formally machine-proved, experimentally confirmed, or universally valid. No Zenodo DOI, site publication, GitHub public visibility, or third-party endorsement may be claimed before each event actually occurs. Use the true Zenodo deposit date for the publication date. Confirm final license and file list before pressing Publish.
