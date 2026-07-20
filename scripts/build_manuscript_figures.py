"""
Task #12: build the 4 planned manuscript figures (protocol v0.1, "Planned Figures").

1. Native corneal layer requirements mapped to engineering targets
   - Reference physiological values (thickness, AFM elastic modulus, bulk tensile
     modulus, endothelial cell density, transmittance) pulled via WebSearch
     2026-07-20 from: Spectral Transmission of the Human Corneal Layers (MDPI
     J Clin Med 2021, PMC8509317); AFM layer-by-layer elastic modulus study
     (PMC4280096, rabbit cornea epithelium-to-endothelium); native corneal
     stroma ultimate tensile strength / tensile modulus (Frontiers Bioeng
     Biotechnol 2022, PMC / ScienceDirect SMILE-lenticule tensile studies);
     endothelial cell density and decompensation threshold (multiple reviews,
     Cornea/IOVS literature, cross-checked against 2-3 sources). These are
     NOT from our own extraction corpus -- they are established physiological
     reference values, cited as such, used only to give Figure 1 real anchor
     numbers instead of a schematic with invented values.
2. Biomaterial class benchmarking matrix (from our 100 Tier 1 records)
3. Layer-specific translational pathway (from our 100 Tier 1 records)
4. Manufacturing and regulatory bottleneck map (corpus gap-analysis stats +
   established regulatory pathway framing, ATMP/HCT-P terminology)

Outputs: figures/figure1_...png+pdf ... figures/figure4_...png+pdf (300 dpi)
"""
import csv
import re
from pathlib import Path
from collections import Counter, defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path("figures")
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": "#333333",
    "figure.dpi": 150,
})

# ---------------------------------------------------------------------------
# Load corpus data (Tier 1, 100 valid primary studies)
# ---------------------------------------------------------------------------
with open("extraction/pubmed_balanced_core_data_extraction_template.csv", newline="", encoding="utf-8-sig") as f:
    rows = [r for r in csv.DictReader(f) if r["extraction_status"] == "completed" and r["screening_id"] != "PUBMED_0672"]

LAYER_ORDER = ["endothelium", "epithelium_limbus", "stroma", "multiple_layers"]
LAYER_LABELS = {"endothelium": "Endothelium", "epithelium_limbus": "Epithelium/Limbus",
                "stroma": "Stroma", "multiple_layers": "Multiple layers"}

def normalize_layer_raw(raw):
    """Exact same prefix-matching logic as scripts/build_benchmarking_tables.py
    (Task #8), reused here so the two figures stay consistent with Table 1's
    layer distribution (endothelium 33 / epithelium_limbus 33 / stroma 23 /
    multiple_layers 11) rather than drifting via a different heuristic."""
    raw = (raw or "").strip()
    for prefix in LAYER_ORDER:
        if raw == prefix or raw.startswith(prefix + " ("):
            return prefix
    if raw.startswith("epithelium"):
        return "epithelium_limbus"
    return raw or "unclassified"

for r in rows:
    key = normalize_layer_raw(r.get("target_layer_final") or r.get("corneal_layer") or "")
    r["_layer"] = LAYER_LABELS.get(key, "Multiple layers")

# ---------------------------------------------------------------------------
# FIGURE 1: Native corneal layer requirements mapped to engineering targets
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 8.2))
ax.axis("off")

layers = [
    ("Epithelium\n(+ Bowman's layer)", "#FDE9C8", "40-50 µm\n(+ Bowman 8-15 µm)", "0.57 ± 0.29 kPa\n(AFM, local)", "Multilayer squamous;\ntight junctions; barrier fn."),
    ("Stroma", "#D8ECD4", "470-500 µm\n(~90% of total)", "Anterior 1.1±0.6 kPa\nPosterior 0.38±0.22 kPa (AFM)\nBulk tensile modulus\n~13.2-13.5 MPa; UTS ~10.6±0.7 MPa", "Lamellar collagen\norganization; lowest single-\nlayer transmittance of the 5"),
    ("Descemet's membrane\n+ Endothelium", "#CFE3F5", "DM 10-12 µm\nEndo 4-6 µm", "DM 11.7±7.4 kPa\nEndo 4.1±1.7 kPa (AFM)", "Native ECD 2000-3000\n(up to 3500) cells/mm²;\ndecompensation risk\nbelow ~500-700 cells/mm²"),
]

x0 = 0.03
w = 0.30
gap = 0.015
for i, (name, color, thick, mod, bio) in enumerate(layers):
    x = x0 + i * (w + gap)
    box = FancyBboxPatch((x, 0.68), w, 0.24, boxstyle="round,pad=0.01,rounding_size=0.02",
                          linewidth=1.3, edgecolor="#333333", facecolor=color, transform=ax.transAxes)
    ax.add_patch(box)
    ax.text(x + w / 2, 0.905, name, transform=ax.transAxes, ha="center", va="top", fontsize=10.5, fontweight="bold")
    ax.text(x + w / 2, 0.85, "Thickness", transform=ax.transAxes, ha="center", va="top", fontsize=8, fontweight="bold", color="#555")
    ax.text(x + w / 2, 0.815, thick, transform=ax.transAxes, ha="center", va="top", fontsize=8)
    ax.text(x + w / 2, 0.755, "Mechanical", transform=ax.transAxes, ha="center", va="top", fontsize=8, fontweight="bold", color="#555")
    ax.text(x + w / 2, 0.72, mod, transform=ax.transAxes, ha="center", va="top", fontsize=7.3)

    box2 = FancyBboxPatch((x, 0.30), w, 0.35, boxstyle="round,pad=0.01,rounding_size=0.02",
                           linewidth=1.0, edgecolor="#888888", facecolor="#FAFAFA", transform=ax.transAxes)
    ax.add_patch(box2)
    ax.text(x + w / 2, 0.625, "Native requirement", transform=ax.transAxes, ha="center", va="top", fontsize=8, fontweight="bold", color="#333")
    ax.text(x + w / 2, 0.575, bio, transform=ax.transAxes, ha="center", va="top", fontsize=7.3)
    ax.text(x + w / 2, 0.40, "Engineering target: match\nthickness within ~20%,\ntransmit >90% visible\nlight, and reach the\nmodulus/ECD range at left\nwithin the relevant scale", transform=ax.transAxes, ha="center", va="top", fontsize=6.6, style="italic", color="#444")

ax.text(0.5, 0.975, "Figure 1. Native corneal layer requirements mapped to engineering targets", transform=ax.transAxes,
        ha="center", fontsize=11.5, fontweight="bold")
ax.text(0.5, 0.14, "Whole-cornea light transmittance is near-unity (>90%) across the visible/IR range; the stroma is the single layer with lowest transmittance.\n"
                    "AFM values are local nano-indentation moduli (kPa scale); bulk tensile testing of whole stroma yields MPa-scale values -- the two are not interchangeable.\n"
                    "Sources: Spectral Transmission of the Human Corneal Layers (J Clin Med 2021, PMC8509317); layer-by-layer AFM elastic modulus (PMC4280096);\n"
                    "corneal stroma tensile testing (Front Bioeng Biotechnol 2022); endothelial cell density / decompensation threshold (cross-checked, Cornea/IOVS literature).",
        transform=ax.transAxes, ha="center", va="top", fontsize=6.3, color="#555")

fig.savefig(OUT / "figure1_native_layer_requirements.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "figure1_native_layer_requirements.pdf", bbox_inches="tight")
plt.close(fig)
print("Figure 1 done.")

# ---------------------------------------------------------------------------
# FIGURE 2: Biomaterial class benchmarking matrix (from our 100 Tier 1 records)
# ---------------------------------------------------------------------------
def classify_biomaterial(raw):
    t = raw.lower()
    if "cell sheet" in t or "cell-sheet" in t or "carrier-free" in t or "support-free" in t or "scaffold-free" in t:
        return "Cell-sheet /\nscaffold-free"
    if "decellularized" in t or "acellular" in t or "amniotic membrane" in t:
        return "Decellularized /\nnatural ECM"
    if ("synthetic" in t and ("natural" in t or "composite" in t or "hybrid" in t or "blend" in t)) or "composite" in t or "hybrid" in t or "interpenetrating" in t:
        return "Hybrid /\ncomposite"
    if re.search(r"\bpcl\b|\bpeg\b|\bpega|\bpva\b|\bplga\b|polylactic|polycaprolactone|polyethylene glycol|synthetic polymer", t) and "natural" not in t:
        return "Synthetic\npolymer"
    if any(k in t for k in ["collagen", "gelatin", "silk", "chitosan", "fibrin", "hyaluronic", "alginate", "cellulose", "keratin"]):
        return "Natural\npolymer"
    return "Other / not\nclearly classified"

def tri_score(val):
    v = (val or "").lower()
    if v == "yes":
        return 1.0
    if v == "partial":
        return 0.5
    return 0.0

classes = defaultdict(list)
for r in rows:
    c = classify_biomaterial(r.get("biomaterial_category", ""))
    classes[c].append(r)

class_order = ["Decellularized /\nnatural ECM", "Natural\npolymer", "Synthetic\npolymer",
               "Hybrid /\ncomposite", "Cell-sheet /\nscaffold-free", "Other / not\nclearly classified"]
class_order = [c for c in class_order if c in classes]
domains = ["Optical\n(transparency)", "Mechanical\n(tensile/modulus)", "Biological\n(cell/phenotype)", "Translational\n(in vivo/clinical)"]

matrix = []
counts = []
for c in class_order:
    recs = classes[c]
    n = len(recs)
    counts.append(n)
    optical = np.mean([tri_score(r["optical_transparency_reported"]) for r in recs])
    mech = np.mean([tri_score(r["mechanical_testing_reported"]) for r in recs])
    bio = np.mean([1.0 if r["biological_testing_reported"].lower() == "yes" else 0.0 for r in recs])
    transl = np.mean([1.0 if (r["clinical_evidence"] or "").lower().startswith("yes")
                       else (0.5 if (r["animal_model"] or "").lower().startswith("yes") else 0.0) for r in recs])
    matrix.append([optical, mech, bio, transl])

matrix = np.array(matrix)

fig, ax = plt.subplots(figsize=(8.5, 5.2))
im = ax.imshow(matrix, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(len(domains)))
ax.set_xticklabels(domains, fontsize=9)
ax.set_yticks(range(len(class_order)))
ax.set_yticklabels([f"{c}\n(n={n})" for c, n in zip(class_order, counts)], fontsize=8.5)
for i in range(len(class_order)):
    for j in range(len(domains)):
        val = matrix[i, j]
        txt_color = "white" if val < 0.35 or val > 0.75 else "black"
        ax.text(j, i, f"{val*100:.0f}%", ha="center", va="center", fontsize=9, color=txt_color, fontweight="bold")
cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.03)
cbar.set_label("Fraction of records reporting/meeting domain\n(1.0 = yes, 0.5 = partial, 0 = not reported)", fontsize=7.5)
ax.set_title("Figure 2. Biomaterial class benchmarking matrix\n(100 Tier 1 primary studies, this review's corpus)", fontsize=11, fontweight="bold", pad=12)
fig.text(0.5, -0.02, "Cell values = mean domain-reporting score within each biomaterial class (see Methods for tri-state scoring). Translational column credits\n"
                     "full weight for clinical evidence, half weight for an animal-model component with no clinical evidence yet.", ha="center", fontsize=6.8, color="#555")
fig.savefig(OUT / "figure2_biomaterial_class_matrix.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "figure2_biomaterial_class_matrix.pdf", bbox_inches="tight")
plt.close(fig)
print("Figure 2 done.", dict(zip(class_order, counts)))

# ---------------------------------------------------------------------------
# FIGURE 3: Layer-specific translational pathway (from our 100 Tier 1 records)
# ---------------------------------------------------------------------------
layer_order = ["Endothelium", "Epithelium/Limbus", "Stroma", "Multiple layers"]
stage_order = ["In vitro only", "Ex vivo", "Animal model", "Human clinical"]

def evidence_stage(r):
    ce = (r["clinical_evidence"] or "").lower().strip()
    if ce.startswith("yes"):
        return "Human clinical"
    if (r["animal_model"] or "").lower().startswith("yes"):
        return "Animal model"
    if (r["ex_vivo_model"] or "").lower().startswith("yes"):
        return "Ex vivo"
    return "In vitro only"

stage_counts = {layer: Counter() for layer in layer_order}
for r in rows:
    layer = r["_layer"]
    if layer not in stage_counts:
        continue
    stage_counts[layer][evidence_stage(r)] += 1

fig, ax = plt.subplots(figsize=(9, 5.5))
colors = {"In vitro only": "#B0BEC5", "Ex vivo": "#90CAF9", "Animal model": "#FFB74D", "Human clinical": "#66BB6A"}
bottoms = np.zeros(len(layer_order))
for stage in stage_order:
    vals = np.array([stage_counts[layer].get(stage, 0) for layer in layer_order])
    ax.bar(layer_order, vals, bottom=bottoms, label=stage, color=colors[stage], edgecolor="white", linewidth=0.8)
    for i, v in enumerate(vals):
        if v > 0:
            ax.text(i, bottoms[i] + v / 2, str(v), ha="center", va="center", fontsize=8.5, fontweight="bold")
    bottoms += vals

totals = [sum(stage_counts[layer].values()) for layer in layer_order]
ax.set_ylim(0, max(totals) * 1.18)
for i, t in enumerate(totals):
    ax.text(i, t + max(totals) * 0.025, f"n={t}", ha="center", fontsize=8.5, color="#333")

ax.set_ylabel("Number of Tier 1 records (highest evidence stage reached)")
ax.set_title("Figure 3. Layer-specific translational pathway\n(100 Tier 1 primary studies, by highest evidence stage reached)", fontsize=11, fontweight="bold")
ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
ax.spines[["top", "right"]].set_visible(False)
fig.savefig(OUT / "figure3_translational_pathway.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "figure3_translational_pathway.pdf", bbox_inches="tight")
plt.close(fig)
print("Figure 3 done.", {l: dict(stage_counts[l]) for l in layer_order})

# ---------------------------------------------------------------------------
# FIGURE 4: Manufacturing and regulatory bottleneck map
# ---------------------------------------------------------------------------
n_total = len(rows)
n_xenogeneic = sum(1 for r in rows if re.search(r"animal|xenogen|porcine|bovine|rabbit(?!.{0,20}human)", r.get("cell_source", "").lower()))
n_mech_gap = sum(1 for r in rows if (r["mechanical_testing_reported"] or "").lower() in ("unclear / not reported in abstract", "unclear / not reported in full text", "no_not_tested", ""))
n_optical_gap = sum(1 for r in rows if (r["optical_transparency_reported"] or "").lower() in ("unclear / not reported in abstract", "unclear / not reported in full text", "no_not_tested", ""))
n_clinical = sum(1 for r in rows if (r["clinical_evidence"] or "").lower().startswith("yes"))
n_animal_only = sum(1 for r in rows if (r["animal_model"] or "").lower().startswith("yes") and not (r["clinical_evidence"] or "").lower().startswith("yes"))
n_invitro_only = n_total - n_clinical - n_animal_only - sum(1 for r in rows if (r["ex_vivo_model"] or "").lower().startswith("yes") and not (r["animal_model"] or "").lower().startswith("yes") and not (r["clinical_evidence"] or "").lower().startswith("yes"))

fig, ax = plt.subplots(figsize=(12.5, 6.3))
ax.axis("off")
ax.set_xlim(0, 12.5)
ax.set_ylim(0, 5.6)

stages = [
    ("Cell\nsourcing", 0.95, f"{n_xenogeneic}/{n_total} records\n({n_xenogeneic/n_total*100:.0f}%) use\nxenogeneic/animal-\nderived cells", "#EF9A9A"),
    ("Scaffold\nfabrication &\ncharacterization", 3.55, f"{n_mech_gap}/{n_total} ({n_mech_gap/n_total*100:.0f}%) lack\nclear mechanical data;\n{n_optical_gap}/{n_total} ({n_optical_gap/n_total*100:.0f}%) lack\nclear optical data", "#FFCC80"),
    ("Preclinical\nvalidation", 6.15, f"In vitro/ex vivo only:\n~{n_invitro_only} records\nAnimal model: {n_animal_only}\nrecords (no clinical\nfollow-through yet)", "#FFF59D"),
    ("GMP / regulatory\nclassification\n(ATMP, HCT/P)", 8.75, "Regulatory pathway not\nreported for the large\nmajority of records in\nthis corpus (a structural\nreporting gap, not\nnecessarily a real absence)", "#C5E1A5"),
    ("Human\nclinical use", 11.35, f"Only {n_clinical}/{n_total}\n({n_clinical/n_total*100:.0f}%) records reach\nhuman clinical evidence\nof any kind", "#80CBC4"),
]

y_box = 3.35
box_h = 1.35
box_w = 2.15
for i, (name, x, detail, color) in enumerate(stages):
    box = FancyBboxPatch((x - box_w/2, y_box), box_w, box_h, boxstyle="round,pad=0.02,rounding_size=0.06",
                          linewidth=1.2, edgecolor="#333333", facecolor=color)
    ax.add_patch(box)
    ax.text(x, y_box + box_h - 0.15, name, ha="center", va="top", fontsize=8.6, fontweight="bold")
    ax.text(x, 2.55, detail, ha="center", va="top", fontsize=7.2)
    if i < len(stages) - 1:
        nx = stages[i + 1][1]
        arrow = FancyArrowPatch((x + box_w/2 + 0.08, y_box + box_h/2), (nx - box_w/2 - 0.08, y_box + box_h/2),
                                 arrowstyle="-|>", mutation_scale=15, color="#555555", linewidth=1.5)
        ax.add_patch(arrow)

ax.text(6.25, 5.45, "Figure 4. Manufacturing and regulatory bottleneck map", ha="center", fontsize=12, fontweight="bold")
ax.text(6.25, 5.1, "Where translation from bench to clinic stalls across the 100 Tier 1 corpus records, left (earliest) to right (clinical)", ha="center", fontsize=8.3, style="italic", color="#444")
ax.text(6.25, 0.55, "Percentages computed from this review's own extraction data (extraction/pubmed_balanced_core_data_extraction_template.csv); regulatory-pathway framing\n"
                 "(ATMP = Advanced Therapy Medicinal Product [EU]; HCT/P = Human Cells, Tissues, and Cellular and Tissue-Based Products [US FDA]) uses standard terminology,\n"
                 "not a corpus-derived statistic -- regulatory pathway itself was not a systematically extracted field and is flagged here as a reporting gap, not a claim about actual approval status.",
        ha="center", fontsize=6.4, color="#555")

fig.savefig(OUT / "figure4_manufacturing_regulatory_bottleneck.png", dpi=300, bbox_inches="tight")
fig.savefig(OUT / "figure4_manufacturing_regulatory_bottleneck.pdf", bbox_inches="tight")
plt.close(fig)
print("Figure 4 done.")
print(f"n_total={n_total} n_xenogeneic={n_xenogeneic} n_mech_gap={n_mech_gap} n_optical_gap={n_optical_gap} n_clinical={n_clinical} n_animal_only={n_animal_only}")
