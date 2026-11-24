# Nepali Visualization Guide (Matplotlib & Seaborn)

> [!IMPORTANT] Gist
> Rendering Devanagari in standard Python plotting libraries often results in "tofu" blocks or broken clusters. This module provides a "monkeypatch" protocol to force Matplotlib and Seaborn to use Devanagari-compatible fonts (e.g., Noto Sans Devanagari).

## 1. The Devanagari Monkeypatch
Standard `plt.title()` or `ax.set_xlabel()` calls don't automatically use Unicode-aware fonts. We wrap these methods to inject `FontProperties` globally.

```python
import os, matplotlib, matplotlib.pyplot as plt, matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
from functools import wraps
import matplotlib.axes as maxes

# 1. Path to Noto Sans Devanagari (Common in Colab/Linux)
P = "/usr/local/share/fonts/NotoSansDevanagari-Regular.ttf"
FP = FontProperties(fname=P)

# 2. Wrapper function
def _wrap(fn, kind="text"):
    @wraps(fn)
    def w(*a, **kw):
        if kind=="legend": kw.setdefault("prop", FP)
        else: kw.setdefault("fontproperties", FP)
        return fn(*a, **kw)
    return w

# 3. Patching global plt methods
for name in ["title", "suptitle", "xlabel", "ylabel", "text", "annotate"]:
    setattr(plt, name, _wrap(getattr(plt, name)))

# 4. Patching Axes methods (for Seaborn/Subplots)
for m in ["set_title", "set_xlabel", "set_ylabel"]:
    setattr(maxes.Axes, m, _wrap(getattr(maxes.Axes, m)))
```

## 2. Handling Ticks (Seaborn Countplots)
Seaborn often sets tick labels directly, which bypasses global font settings. We must patch `set_xticklabels` and `set_yticklabels`.

```python
def _apply_fp_to_ticks(ax, which="x"):
    labels = ax.get_xticklabels() if which=="x" else ax.get_yticklabels()
    for t in labels:
        try: t.set_fontproperties(FP)
        except: pass

def _wrap_set_ticks(fn, which):
    @wraps(fn)
    def _w(self, labels, *a, **kw):
        out = fn(self, labels, *a, **kw)
        _apply_fp_to_ticks(self, which)
        return out
    return _w

setattr(maxes.Axes, "set_xticklabels", _wrap_set_ticks(maxes.Axes.set_xticklabels, "x"))
```

## 3. Nepali Word Clouds
WordCloud requires an explicit `font_path` to render Devanagari glyphs correctly.
```python
wordcloud = WordCloud(width=800, height=400, font_path=P).generate_from_frequencies(freqs)
```

---

**Notebook**: [nepali_viz_monkeypatch.py](notebooks/nepali_viz_monkeypatch.py)

#nepali-nlp #visualization #matplotlib #seaborn #wordcloud #font-patching
