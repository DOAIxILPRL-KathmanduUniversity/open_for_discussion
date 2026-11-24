import matplotlib.pyplot as plt
import matplotlib.axes as maxes
from matplotlib.font_manager import FontProperties
from functools import wraps

# --- 1. CONFIG ---
FONT_PATH = "/usr/local/share/fonts/NotoSansDevanagari-Regular.ttf"
FP = FontProperties(fname=FONT_PATH)

# --- 2. MONKEYPATCH ---
def _wrap(fn, kind="text"):
    @wraps(fn)
    def w(*a, **kw):
        if kind=="legend": kw.setdefault("prop", FP)
        else: kw.setdefault("fontproperties", FP)
        return fn(*a, **kw)
    return w

for name in ["title", "suptitle", "xlabel", "ylabel", "text", "annotate"]:
    if hasattr(plt, name): setattr(plt, name, _wrap(getattr(plt, name)))

for m in ["set_title", "set_xlabel", "set_ylabel"]:
    if hasattr(maxes.Axes, m): setattr(maxes.Axes, m, _wrap(getattr(maxes.Axes, m)))

if __name__ == "__main__":
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("नेपाली शीर्षक")
    plt.xlabel("एक्स अक्ष")
    plt.show()
