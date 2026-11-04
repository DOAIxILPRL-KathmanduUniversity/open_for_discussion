# Experiment template

Use one folder per experiment.  Every experiment:

* states a hypothesis,
* lists `uses:` (nepali_utils modules it imports),
* records `status:` (proposed | running | verified | dropped),
* writes small fixtures only into its own `data/` (no corpora!),
* ends with `OUT.md` (what could graduate to `nepali_utils`).

Do not put corpora here — task datasets belong in `assignments/`.
