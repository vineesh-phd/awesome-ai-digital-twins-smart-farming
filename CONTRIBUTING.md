# Curation and Verification Rules

## Scope

Contributions should connect AI or digital twins to agricultural sensing, physical modelling, calibration, irrigation, crop response, or evaluation. General methods are acceptable when their relevance and limits are explicit.

## Adding a Scholarly Source

1. Check title, author list, year, venue, and DOI against publisher or authoritative metadata. Distinguish issue year from first-online year.
2. Read the accessible source before describing results. Record whether the check used full text, an abstract, or metadata only.
3. Identify the evidence type. Do not count a guide or preprint toward the 20 published-paper minimum.
4. Write a specific relevance note and an inference limit. Do not translate prediction accuracy into unreported water savings.
5. Add a stable ID and fields to `references/references.json`, then run `python3 scripts/build_catalog.py`.
6. Run `python3 scripts/check_repository.py` and review the Markdown diff. Update the audit if manuscript claims change.

## Data and Software

Record provider, intended use, spatial and temporal scale, access conditions, citation requirements, and limitations. For software, inspect documentation, examples, source, license terms, and maintenance evidence. Inspection is not reproduction; do not describe unexecuted code as tested.

## Research Integrity

Keep illustrative examples, proposed methods, and reported observations distinct. Preserve uncertainty and negative findings. Link to third-party papers unless redistribution rights are established. Never commit credentials, personal documents, field data with unclear permissions, or invented results.

## Student Review and Git History

AI assistance is disclosed. The student must independently review sources and take responsibility for submitted curation. Make meaningful commits for actual work; do not fabricate dates or manufacture history. The repository remains unlicensed unless its owner explicitly changes that policy.
