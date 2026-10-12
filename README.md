# TSI-CORE-1.0-RC2 · Four reading editions / Четыре редакции

**Author / Автор:** Igor Chechelnitsky (Игорь Чечельницкий) · [ORCID 0009-0007-4607-1946](https://orcid.org/0009-0007-4607-1946)  
**Canonical mathematical version / Версия исходного ядра:** `1.0-RC2`, 2026-07-30  
**Package prepared / Пакет подготовлен:** 2026-10-10  
**Publication status / Статус:** **Public pre-release candidate — independent final audit and proof-assistant verification pending / Публичный предварительный релиз — независимый заключительный аудит и машинная верификация доказательств ещё не завершены.**

## Choose your edition / Выберите версию

| Audience / Аудитория | Русский 🇷🇺 | English 🇬🇧 |
|---|---|---|
| **Scientific / Научная** | [Научная версия RU](science/TSI-CORE-1.0-RC2-SCIENTIFIC-RU.md) | [Scientific version EN](science/TSI-CORE-1.0-RC2-SCIENTIFIC-EN.md) |
| **Popular / Для неспециалистов** | [Простое объяснение RU](popular/TSI-CORE-1.0-RC2-EXPLAINED-RU.md) | [Plain-language explanation EN](popular/TSI-CORE-1.0-RC2-EXPLAINED-EN.md) |

### Normative source / Нормативный первоисточник

- **[Canonical TSI-CORE-1.0-RC2 manuscript (English)](docs/TSI-CORE-1.0-RC2.md)** — unchanged original mathematical text. Its primitive signature, formulas, model data, numbering, and stated proof dependencies take precedence over companion editions.
- [Historical audited edition](history/TSI-CORE-1.0_FORMALLY_AUDITED-HISTORICAL.md) — historical, *not* current normative RC2.

## English overview

TSI-CORE is a small two-sorted first-order formal specification for representations and partial transformations. It has two primitive sorts (`Rep`, `Trans`), three relations (structural equivalence, `Apply`, `Comp`), one constant (`e`), and exactly six mandatory axiom groups (AX-C01, AX-C02, AX-C04, AX-C05, AX-C06, AX-C07). The document includes a finite satisfiability model, proposed independence countermodels, derived results, and a countermodel showing that universal structural preservation (AX-C08) is *not* entailed. AX-C08 remains optional.

The specification is **not a theory of reality, physics, consciousness, or an empirically proven method for FCO**. Independent final review, machine-checked proofs, and application tests remain future work. The popular editions are educational companion texts, not axiomatic supplements. The Russian scientific edition is a companion scientific exposition; the English source remains normative if terminology conflicts arise.

**Finite examples:** The pure-Python script [`verification/check_finite_models.py`](verification/check_finite_models.py) exhaustively checks the eight *specified finite structures* against the formulas encoded in the script. Its output is [`verification/finite_model_check_results.json`](verification/finite_model_check_results.json). This reproducible computational check **does not** constitute machine verification of the general theorems or independent validation of the code/transcription.

## Обзор на русском

TSI-CORE — компактная многосортная формальная спецификация представлений и частичных преобразований. В языке два сорта, три отношения, одна выделенная константа и шесть обязательных групп аксиом. Представлены конечная модель выполнимости, кандидаты-контрмодели независимости и обоснование необязательности AX-C08.

Это **не доказанная теория реальности и не подтверждённый метод распознавания для FCO**. Популярные тексты не вводят новых математических посылок. Русский научный текст содержит самостоятельное строгое изложение, однако при расхождениях с ним математический приоритет остаётся за неизменённой англоязычной спецификацией RC2.

**Проверяемость:** запустите `python3 verification/check_finite_models.py`. Скрипт перебирает конечные структуры из исходной спецификации и проверяет кодированные аксиомы. Успех этой проверки не означает, что доказательства в Lean/Isabelle уже получены.

## Audit and reproducibility / Аудит и воспроизводимость

- [Release checklist / Список незакрытых проверок](RELEASE_CHECKLIST.md)
- [Verification scope / Объём автоматической проверки](verification/README.md)
- [SHA-256 hashes of the editions and source](EDITION_HASHES_SHA256.txt)
- [Version history](CHANGELOG.md)
- [Authorship](AUTHORS.md)
- [Citation metadata](CITATION.cff)
- [Publication guide (RU)](PUBLICATION_GUIDE_RU.md)

**License / Лицензия:** not selected / не выбрана. See [`LICENSE_DECISION.md`](LICENSE_DECISION.md). This package does not presume CC BY, MIT, or any other open license.

**GitHub release / Публикация GitHub:** [v1.0-RC2](https://github.com/Muhomor2/TSI-CORE/releases/tag/v1.0-RC2) — public pre-release; release source commit `96c45564dfe14e232836e5a9a15fb1598ccbfd84`. / Публичный предварительный релиз; исходный коммит закреплён тегом.

**Zenodo DOI / DOI Zenodo:** [10.5281/zenodo.23322303](https://doi.org/10.5281/zenodo.23322303) — DOI supplied by the author / DOI предоставлен автором. *Zenodo record contents, license, and metadata remain to be independently checked / Содержимое, лицензия и метаданные Zenodo ещё требуют независимой сверки.*

**Audit / Аудит UTS:** [Bilingual independent audit protocol](publication/UTS_TSI_INDEPENDENT_AUDIT_RU_EN.md) / [Двуязычное задание независимым аудиторам](publication/UTS_TSI_INDEPENDENT_AUDIT_RU_EN.md).

## Feedback / Как сообщить об ошибке

Please quote the exact axiom, theorem, or model ID, give a reproducible counterexample, and explain whether the problem is mathematical, terminological, or editorial. / Укажите конкретный идентификатор формулы, теоремы или модели и воспроизводимый контрпример. Изменение формул требует новой математической версии; RC2 нельзя незаметно переписать после замечаний.
