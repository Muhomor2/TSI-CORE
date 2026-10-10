# Independent Audit Challenge — TSI-CORE → UTS / Независимый аудит применимости TSI к UTS

**Document class:** Public audit challenge and acceptance protocol (proposal)  
**Status:** Invitation to independent review; NO proof of UTS correctness is claimed.  
**Normative target:** TSI-CORE-1.0-RC2, `docs/TSI-CORE-1.0-RC2.md` in this repository.  
**UTS target:** An explicitly frozen and cited UTS specification + implementation revision, to be recorded by the auditor before testing.  
**Version / DOI:** Record the exact TSI version DOI and commit SHA when available. Until then use the RC2 filename and canonical SHA-256 from `PROVENANCE_SHA256.txt`.

## I. Questions to answer (English)

Can an independently defined UTS subsystem be represented as a conservative, internally consistent extension or interpretation of TSI-CORE without smuggling in assumptions not present in the kernel? If yes, which specific UTS properties can be justified by which *additional* assumptions and which proof obligations remain open?

The audit must distinguish four layers:
1. **Logical kernel:** only two sorts, three primitive relations, one unit constant, six axiom groups.
2. **Interpretation map:** meaning assigned to the kernel's representations, transformations, equivalence, application, composition, and unit in each UTS domain.
3. **UTS-specific axioms and semantics:** authenticated events, storage, adversarial scheduling, concurrency, consensus, finality, rollback/reorganization, privileges, policy, and temporal behavior.
4. **Implemented system and evidence:** exact repository revision, executable traces, models, counterexamples, test logs, and deployment assumptions.

No result about layer 1 automatically establishes security or operational correctness at layer 4.

### Candidate mapping (hypotheses, NOT assumed correct)

| TSI concept | Potential UTS candidate | Audit question |
| --- | --- | --- |
| Representation | State commitment, verified record or policy snapshot | Can identity, domain, epoch and provenance be distinguished? |
| Transformation | Typed UTS state transition | Does application model failed/rejected transitions as partial? |
| Structural equivalence | An explicitly selected UTS observation relation | Is it really an equivalence relation, and which observers can distinguish states? |
| Declared composition | Sequentially admissible transition composition | What about concurrency, races, reorgs, and non-atomic reads? |
| Unit transformation | A genuine identity/no-op transition | Is it neutral under UTS signatures, gas, fees, audit logs, and event time? |
| Optional structural preservation | Extra UTS theorem/axiom with side conditions | Can valid operations preserve the chosen relation, or provide counterexamples? |

### Required independent audit tracks

**A. Mathematical integrity.** Independently reconstruct the RC2 signature, quantify every axiom correctly, validate finite witnesses, test independence claims, and review derivations and hidden domain assumptions. Search for equivalent formalisms and prior work; report genuine novelty only with citations.

**B. Conservative-extension contract.** Provide explicit added sorts, symbols, axioms and interpretation maps. Demonstrate that the extension does not rewrite core symbols or produce a contradiction with the base system; otherwise supply a minimal countermodel or classify the result as unproven.

**C. UTS safety/liveness.** State assumptions on cryptography, nodes, finality, network timing, quorum behavior and faults. Separate invariants and progress properties; do not derive bridge safety, nullifier soundness, DAG ancestry soundness, token or wallet conservation from TSI axioms alone.

**D. Adversarial schedule & PRE-F.** Reproduce concurrency and non-atomic verification hazards (reservation races, nullifier replay/double spend, partial visibility windows, delayed DAG roots, reorg overlap) from a frozen UTS artifact. Record concrete traces, red-before-fix and green-after-fix evidence. Treat monotone accumulator arguments as UTS extensions that require separate verification.

**E. Multi-domain policies.** For elections, legislation, lotteries, social allocation and ratings: specify roles, verifiable eligibility, identity scope and privacy boundary. Distinguish anonymous ballots from attributed rule-authoring. Analyse Sybil, coercion, censorship, biased randomness, auditability and governance conflicts. TSI is not itself a source of fair or legitimate policy.

**F. Independent review.** Require at least one adversarial reviewer who did not construct the model, machine-readable examples, signed exact revision hashes, reproduction instructions, and classification of each property as PASS / FAIL / UNPROVEN / OUT OF SCOPE.

### Mandatory falsification tasks / STOP gates

- Show one explicit partial transition that should not be considered composable; reject the mapping if the TSI relation asserts it is.
- Try to construct two UTS states that map to the same TSI representation/equivalence class but differ on a security-critical property. If possible, narrow the claim or FAIL the interpretation.
- Run concurrent conflicting UTS transitions against identical pre-state commitments and demonstrate exactly what enforces single consumption.
- Check that historical provenance is not falsely inferred from a current accumulator root.
- Reject any claim that AX-C08 is mandatory or already follows from the six core groups.
- STOP whenever a necessary UTS source, version, security assumption or witness is missing. Do not invent it.

### Report format

1. Source manifest: URLs, repository IDs, commit hashes, TSI DOI, UTS release.
2. Assumption ledger: axioms vs implementation assumptions vs empirical inputs.
3. Mapping table: total/partial, injective/noninjective, counterexamples.
4. Property matrix: requirement, formalization, evidence, reviewer, PASS/FAIL/UNPROVEN/OUT OF SCOPE.
5. Minimal failing traces with exact reproducibility steps.
6. Open proof obligations and recommended revisions.
7. Reproducibility appendix (tools/versions, commands, logs, seeds where relevant).

**Interpretation of verdict:** PASS for finite-model examples does not imply PASS for any UTS security property. A valid model embedding may still be operationally useless.

---

## II. Русская версия: обязательное задание аудиторам

**Основной вопрос:** можно ли корректно интерпретировать конкретные механизмы UTS в TSI-CORE-1.0-RC2 без добавления скрытых допущений? Если для UTS требуются новые аксиомы, должны быть отдельно изложены их смысл, необходимость, совместимость, доказательства и контрпримеры.

Строго разделять **(1)** математическое ядро TSI, **(2)** отображение понятий UTS на ядро, **(3)** дополнительные модели криптографии, сети, времени, конкуренции и управления, **(4)** работающий код и реальные измерения. Подмена этих уровней запрещена.

**Проверить следующие направления:**
- независимую реконструкцию шести групп аксиом, выполнимости, независимости и доказательств;
- точность отображения состояний, преобразований, эквивалентности, частичной композиции и единичного действия;
- сохранение или потерю существенных свойств при отображении (особенно права, авторство, эпохи, домены, финальность);
- безопасность и прогресс UTS при асинхронных событиях, сбоях, реорганизациях, конкурентных вызовах и вредоносных участниках;
- PRE-F: проверку повторного использования nullifier, гонок резервирования, неатомарных чтений, DAG-root/ancestry, видимости старого состояния;
- независимость политик различных доменов: выборов, голосований по законам, социальных лотерей, рейтингов и финансов;
- невыводимость анонимности, справедливости, атомарности и консенсуса из одних аксиом TSI.

**Критерии остановки:** отсутствует точный источник UTS; нет замороженного коммита; критическая гипотеза не определена; контрпример ломает заявленное соответствие; тест не воспроизводится; положительный вывод строится только на доверии к прежнему аудиту. В этих случаях статус — UNPROVEN или FAIL, а не условный PASS.

**Итог аудита:** перечень исходников и хешей; матрица формальных обязательств; исполняемые контрпримеры и следы атак; минимальные изменения, действительно необходимые UTS; неустранённые проблемы и независимые рецензенты.

### Scope limitation / Ограничение области

This file initiates an audit topic and does **not** itself demonstrate that TSI improves or verifies UTS. / Этот документ ставит задачи аудита и **не доказывает**, что TSI усиливает UTS.
