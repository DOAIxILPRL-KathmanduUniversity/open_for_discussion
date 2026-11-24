"""
Experiment 11: displaCy Visualization
Explores: Entity visualization, dependency visualization, HTML export for Devanagari
"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from lang.ne import Nepali
from spacy import displacy

nlp = Nepali()

print("=" * 60)
print("EXPERIMENT 11: DISPLACY VISUALIZATION")
print("=" * 60)

# --- A. Setup: Add entity ruler for visual demo ---
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns([
    {"label": "PERSON", "pattern": "राम"},
    {"label": "PERSON", "pattern": "सीता"},
    {"label": "PERSON", "pattern": "गौतम बुद्ध"},
    {"label": "GPE", "pattern": "काठमाडौँ"},
    {"label": "GPE", "pattern": "नेपाल"},
    {"label": "GPE", "pattern": "लुम्बिनी"},
    {"label": "ORG", "pattern": "नेपाल सरकार"},
    {"label": "DATE", "pattern": [{"TEXT": "वि.सं."}, {"LIKE_NUM": True}]},
])

# --- B. Generate Entity HTML ---
print("\n--- A. Entity Visualization (HTML Export) ---")
os.makedirs(os.path.join(PROJECT_ROOT, "outputs"), exist_ok=True)

texts = [
    "रामले काठमाडौँमा भात खायो।",
    "गौतम बुद्धको जन्म लुम्बिनीमा भयो।",
    "नेपाल सरकारले वि.सं. २०८२ को बजेट ल्यायो।",
]

docs = [nlp(t) for t in texts]

# Custom options for Devanagari
ent_options = {
    "colors": {
        "PERSON": "#FF6B6B",
        "GPE": "#4ECDC4",
        "ORG": "#45B7D1",
        "DATE": "#FFA07A",
    }
}

html = displacy.render(docs, style="ent", options=ent_options, page=True)

# Inject Devanagari font into the HTML
html = html.replace(
    "<body",
    '<style>body { font-family: "Noto Sans Devanagari", "Annapurna SIL", sans-serif; font-size: 18px; }</style><body'
)

ent_path = os.path.join(PROJECT_ROOT, "outputs", "entities.html")
with open(ent_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"  Entity HTML saved to: {ent_path}")

# --- C. Generate Dependency HTML (simulated with attribute ruler) ---
print("\n--- B. Token Analysis Table (HTML) ---")
table_html = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<style>
  body { font-family: "Noto Sans Devanagari", sans-serif; padding: 40px; background: #1a1a2e; color: #eee; }
  h1 { color: #FF6B6B; }
  table { border-collapse: collapse; width: 100%; margin: 20px 0; }
  th { background: #16213e; color: #4ECDC4; padding: 12px; text-align: left; }
  td { padding: 10px; border-bottom: 1px solid #333; }
  tr:hover { background: #16213e; }
  .tag { padding: 2px 8px; border-radius: 4px; font-size: 0.85em; }
  .stop { background: #FF6B6B33; color: #FF6B6B; }
  .num { background: #4ECDC433; color: #4ECDC4; }
  .ent { background: #45B7D133; color: #45B7D1; }
</style>
</head><body>
<h1>Nepali Token Analysis</h1>
"""

for text in texts:
    doc = nlp(text)
    table_html += f"<h2>{text}</h2><table><tr><th>Token</th><th>is_stop</th><th>like_num</th><th>norm_</th><th>Entity</th></tr>"
    
    # Build entity map
    ent_map = {}
    for ent in doc.ents:
        for t in ent:
            ent_map[t.i] = ent.label_
    
    for t in doc:
        stop_cls = ' class="tag stop"' if t.is_stop else ''
        num_cls = ' class="tag num"' if t.like_num else ''
        ent_label = ent_map.get(t.i, "")
        ent_cls = f' class="tag ent"' if ent_label else ''
        table_html += f"<tr><td>{t.text}</td><td><span{stop_cls}>{t.is_stop}</span></td><td><span{num_cls}>{t.like_num}</span></td><td>{t.norm_}</td><td><span{ent_cls}>{ent_label}</span></td></tr>"
    
    table_html += "</table>"

table_html += "</body></html>"

table_path = os.path.join(PROJECT_ROOT, "outputs", "analysis.html")
with open(table_path, "w", encoding="utf-8") as f:
    f.write(table_html)
print(f"  Analysis HTML saved to: {table_path}")

# --- D. SVG export ---
print("\n--- C. SVG Entity Export ---")
svg = displacy.render(docs[0], style="ent", options=ent_options)
svg_path = os.path.join(PROJECT_ROOT, "outputs", "entities.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"  SVG saved to: {svg_path}")

print("\n--- Done! Open the HTML files in a browser to view. ---")
