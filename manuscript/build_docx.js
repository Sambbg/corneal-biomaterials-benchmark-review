// Build the final manuscript .docx from manuscript_draft.md + build_data/*.json + figures/*.png
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  ImageRun, PageBreak, Header, Footer, PageNumber, VerticalAlign,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const DATA = path.join(__dirname, "build_data");

const citekeys = JSON.parse(fs.readFileSync(path.join(DATA, "citekeys.json")));
const table2 = JSON.parse(fs.readFileSync(path.join(DATA, "table2_data.json")));
const table3 = JSON.parse(fs.readFileSync(path.join(DATA, "table3_data.json")));
const table4 = JSON.parse(fs.readFileSync(path.join(DATA, "table4_data.json")));
const refs = JSON.parse(fs.readFileSync(path.join(DATA, "references_data.json")));
const md = fs.readFileSync(path.join(__dirname, "manuscript_draft.md"), "utf-8");

// ---------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------
const FONT = "Calibri";
const PAGE = { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } }; // US Letter, 1in margins

function inlineRuns(text) {
  // parse **bold** segments
  const runs = [];
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  for (const part of parts) {
    if (!part) continue;
    if (part.startsWith("**") && part.endsWith("**")) {
      runs.push(new TextRun({ text: part.slice(2, -2), bold: true, font: FONT }));
    } else {
      runs.push(new TextRun({ text: part, font: FONT }));
    }
  }
  return runs.length ? runs : [new TextRun({ text: "", font: FONT })];
}

function bodyPara(text, opts = {}) {
  return new Paragraph({
    children: inlineRuns(text),
    spacing: { after: 200, line: 276 },
    alignment: AlignmentType.JUSTIFIED,
    ...opts,
  });
}

function h1(text) {
  return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 200 } });
}
function h2(text) {
  return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 300, after: 150 } });
}

function cellText(text, opts = {}) {
  return new TableCell({
    children: [new Paragraph({ children: inlineRuns(String(text)), alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT })],
    width: { size: opts.width || 1000, type: WidthType.DXA },
    shading: opts.shade ? { type: ShadingType.CLEAR, fill: opts.shade } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 40, bottom: 40, left: 80, right: 80 },
  });
}

function headerRow(cells, widths) {
  return new TableRow({
    tableHeader: true,
    children: cells.map((c, i) => cellText(c, { width: widths[i], shade: "D9D9D9", center: true })),
  });
}

// ---------------------------------------------------------------------
// Parse manuscript_draft.md body sections (## headings) into paragraphs
// ---------------------------------------------------------------------
function paragraphsFromMdBlock(blockText) {
  const paras = [];
  const lines = blockText.split("\n");
  let buffer = [];
  const flush = () => {
    if (buffer.length) {
      const text = buffer.join(" ").trim();
      if (text) paras.push(bodyPara(text));
      buffer = [];
    }
  };
  for (let raw of lines) {
    const line = raw.trim();
    if (line === "") { flush(); continue; }
    if (line === "---") { flush(); continue; }
    if (line.startsWith("### ")) { flush(); paras.push(h2(line.replace(/^### /, ""))); continue; }
    if (line.startsWith("## ")) { flush(); continue; } // handled by caller split
    buffer.push(line);
  }
  flush();
  return paras;
}

function extractSection(md, startMarker, endMarker) {
  const s = md.indexOf(startMarker);
  const e = endMarker ? md.indexOf(endMarker) : md.length;
  return md.slice(s, e === -1 ? md.length : e);
}

const introBlock = extractSection(md, "## 1. Introduction", "## 2. Methods");
const methodsBlock = extractSection(md, "## 2. Methods", "## 3. Results");
const resultsBlock = extractSection(md, "## 3. Results", "## 4. Discussion");
const discussionBlock = extractSection(md, "## 4. Discussion", "## 5. Conclusions");
const conclusionsBlock = extractSection(md, "## 5. Conclusions", "## Acknowledgments");

// ---------------------------------------------------------------------
// Title page
// ---------------------------------------------------------------------
const titlePage = [
  new Paragraph({ spacing: { before: 800 }, children: [] }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 400 },
    children: [new TextRun({ text: "From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering", bold: true, size: 32, font: FONT })],
  }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Samuel Bertrand Bernard Gonzalves*", size: 26, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400 }, children: [new TextRun({ text: "Faculty of Electrical Engineering, Master of Science (Biomedical Engineering), Universiti Teknologi Malaysia (UTM), Skudai, Johor, Malaysia", size: 22, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "*Corresponding author: bertrandbernard@graduate.utm.my  |  Matric Number MKE251020", italics: true, size: 20, font: FONT })] }),
  new Paragraph({ spacing: { before: 600, after: 100 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Prepared for MEBC1163-01 Kejuruteraan Tisu (Tissue Engineering)", size: 20, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Academic Session/Semester 2025/2026-2  •  Course lecturer: Dr Norhana Jusoh", size: 20, font: FONT })] }),
  new Paragraph({ spacing: { before: 500 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Word count (Introduction–Conclusions): 4,956 words  •  Abstract: 335 words", size: 18, font: FONT, color: "555555" })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300 }, children: [new TextRun({ text: "Conflict of interest: the author declares no conflict of interest.  Funding: this work received no external funding.", size: 18, font: FONT, color: "555555" })] }),
  new Paragraph({ children: [new PageBreak()] }),
];

// ---------------------------------------------------------------------
// ToC entry + Abstract
// ---------------------------------------------------------------------
const tocAndAbstract = [
  h1("Table of Contents Entry"),
  bodyPara("This review benchmarks 100 primary studies (2018-2026) of biomaterials for corneal endothelium, stroma, and epithelium/limbus reconstruction against each layer's native optical, mechanical, and cellular requirements, rather than judging them by novelty alone. Decellularized/natural-ECM scaffolds dominate the landscape (34/100), but only 26/100 studies report both optical transparency and mechanical testing together, and just 6/100 have reached genuine human clinical evidence. Figure 2 (biomaterial-class benchmarking matrix) is the representative figure."),
  h1("Abstract"),
  bodyPara("Corneal tissue engineering has produced a large and fast-growing literature of biomaterials intended to replace or repair the epithelium/limbus, stroma, or endothelium, but individual studies are usually judged by the novelty of their material or fabrication method rather than by how well they reproduce the specific optical, mechanical, and biological requirements of the corneal layer they target. This review asks a different question: how well do currently reported biomaterials and biofabrication approaches actually meet layer-specific benchmarks, and how far have they progressed toward clinical use? A PubMed search (four layer-specific blocks, 1,318 records, 1,082 unique after deduplication) plus a targeted supplementary snowball check yielded a balanced core of 248 records, of which 100 primary studies (33 endothelium, 33 epithelium/limbus, 23 stroma, 11 multiple-layer/full-thickness) received full structured extraction across optical, mechanical, biological, and translational domains. Decellularized/natural-extracellular-matrix scaffolds were the most common strategy (34/100), followed by natural polymers (19/100) and hybrid/composite materials (17/100); purely synthetic-polymer approaches were rare (3/100). Optical transparency was reported in 58/100 studies and mechanical testing in 37/100 (with a further 30/100 partially reported), but only 26/100 studies reported both together, and this rate varied sharply by layer (stroma 10/23, endothelium 8/33, multiple-layer 5/11, epithelium/limbus 3/33). Biological/cell-phenotype outcomes were reported in nearly every study (98/100), reflecting near-universal cell-culture validation but far less consistent physical characterization. Only 6/100 studies presented genuine human clinical evidence, all in epithelium/limbus or full-thickness constructs; a further 42/100 reached an animal model without clinical follow-up. Cross-referencing an independent 2025 systematic review (Anitua, Zalduendo & Alkhraisat) that used stricter animal-comparator inclusion criteria (21 studies total) confirmed that this review's broader, layer-benchmarked approach captures substantially more of the field, including quantitative mechanical data that the comparator review does not extract at all. These findings support the central argument that corneal biomaterials should be benchmarked against explicit, layer-specific optical/mechanical/biological/translational targets rather than compared only on material novelty, and identify mechanical characterization — particularly in epithelium/limbus constructs — and the near-total absence of clinical-stage mechanical data as the field's most consistent reporting gap."),
  new Paragraph({ spacing: { after: 300 }, children: [
    new TextRun({ text: "Keywords: ", bold: true, font: FONT }),
    new TextRun({ text: "corneal tissue engineering; biomaterials; corneal endothelium; corneal stroma; limbal epithelial stem cells; benchmarking; translational readiness; decellularized extracellular matrix", italics: true, font: FONT }),
  ]}),
  new Paragraph({ children: [new PageBreak()] }),
];

// ---------------------------------------------------------------------
// Table 1
// ---------------------------------------------------------------------
const t1rows = [
  ["PubMed records identified (4 layer-specific search blocks)", "1,318", "A3 epithelium/limbus, B3 stroma, C4 endothelium, D3 full-thickness/multilayer"],
  ["Duplicate records removed (PMID)", "236", ""],
  ["Unique records screened (title/abstract)", "1,082", ""],
  ["Excluded at title/abstract stage", "354", ""],
  ["Included / uncertain, carried forward", "728", ""],
  ["Balanced final core (PubMed)", "246", "Layer-balanced after endothelium/epithelium correction"],
  ["Additional records via reference-list snowball check", "2", "Adipose-stem-cell stromal bioink; lens-capsule endothelial carrier"],
  ["Total core", "248", ""],
  ["Tier 1 — selected for full extraction", "101", "Score-based prioritization"],
  ["Tier 1 records reclassified as non-primary (review article)", "1", "See Section 2.3"],
  ["Tier 1 valid primary studies (this review's evidence base)", "100", ""],
  ["Tier 2 — light-touch / cited for context", "147", "Not deep-extracted"],
];
const table1Doc = new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: [5200, 1400, 2760],
  rows: [
    headerRow(["Stage", "Count", "Notes"], [5200, 1400, 2760]),
    ...t1rows.map(r => new TableRow({ children: [cellText(r[0], { width: 5200 }), cellText(r[1], { width: 1400, center: true }), cellText(r[2], { width: 2760 })] })),
  ],
});

// ---------------------------------------------------------------------
// Table 2 builder (by layer)
// ---------------------------------------------------------------------
function buildTable2ForLayer(layerName, rows) {
  const widths = [1750, 4900, 900, 900, 1600, 500];
  const total = widths.reduce((a,b)=>a+b,0);
  return [
    h2(`${layerName} (n=${rows.length})`),
    new Table({
      width: { size: total, type: WidthType.DXA },
      columnWidths: widths,
      rows: [
        headerRow(["Citation", "Material", "Optical", "Mech.", "Model", "Ev."], widths),
        ...rows.map(r => new TableRow({ children: [
          cellText(r.citekey, { width: widths[0] }),
          cellText(r.material, { width: widths[1] }),
          cellText(r.optical, { width: widths[2], center: true }),
          cellText(r.mechanical, { width: widths[3], center: true }),
          cellText(r.model, { width: widths[4] }),
          cellText(r.ev, { width: widths[5], center: true }),
        ]})),
      ],
    }),
    new Paragraph({ spacing: { before: 150, after: 250 }, children: [] }),
  ];
}

// ---------------------------------------------------------------------
// Table 3 builder
// ---------------------------------------------------------------------
function buildTable3ForLayer(layerName, rows) {
  const widths = [5800, 1500, 2060];
  const total = widths.reduce((a,b)=>a+b,0);
  return [
    h2(layerName),
    new Table({
      width: { size: total, type: WidthType.DXA },
      columnWidths: widths,
      rows: [
        headerRow(["Cell source category", "Count", "% of layer"], widths),
        ...rows.map(r => new TableRow({ children: [
          cellText(r.category, { width: widths[0] }),
          cellText(r.count, { width: widths[1], center: true }),
          cellText(r.pct + "%", { width: widths[2], center: true }),
        ]})),
      ],
    }),
    new Paragraph({ spacing: { before: 150, after: 250 }, children: [] }),
  ];
}

// ---------------------------------------------------------------------
// Table 4 builders
// ---------------------------------------------------------------------
function buildTable4Clinical(rows) {
  const widths = [1750, 1800, 3700, 1900];
  const total = widths.reduce((a,b)=>a+b,0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      headerRow(["Citation", "Layer", "Material / study type", "Follow-up"], widths),
      ...rows.map(r => new TableRow({ children: [
        cellText(r.citekey, { width: widths[0] }),
        cellText(r.layer, { width: widths[1] }),
        cellText(`${r.material} — ${r.readiness}`, { width: widths[2] }),
        cellText(r.followup, { width: widths[3] }),
      ]})),
    ],
  });
}
function buildTable4Animal(rows) {
  const widths = [1750, 1800, 3900, 1700];
  const total = widths.reduce((a,b)=>a+b,0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      headerRow(["Citation", "Layer", "Material", "Follow-up"], widths),
      ...rows.map(r => new TableRow({ children: [
        cellText(r.citekey, { width: widths[0] }),
        cellText(r.layer, { width: widths[1] }),
        cellText(r.material, { width: widths[2] }),
        cellText(r.followup, { width: widths[3] }),
      ]})),
    ],
  });
}

// ---------------------------------------------------------------------
// Figures
// ---------------------------------------------------------------------
function figureBlock(filename, caption, num) {
  const imgPath = path.join(ROOT, "figures", filename);
  const buf = fs.readFileSync(imgPath);
  // Read actual pixel dimensions is not trivial without a lib; use a fixed safe width and proportional height via sharp-less heuristic
  const dims = imageSizeOf(buf);
  const maxWidth = 620; // points-ish (docx uses EMU via width/height in px at 96dpi conceptually through docx.js "transformation")
  const scale = Math.min(1, maxWidth / dims.width);
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200 },
      children: [new ImageRun({
        type: "png",
        data: buf,
        transformation: { width: Math.round(dims.width * scale), height: Math.round(dims.height * scale) },
      })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 300 },
      children: [new TextRun({ text: `Figure ${num}. ${caption}`, italics: true, size: 20, font: FONT })],
    }),
  ];
}

// minimal PNG dimension reader (no deps)
function imageSizeOf(buf) {
  // PNG: width/height are big-endian uint32 at bytes 16-23
  if (buf[0]===0x89 && buf[1]===0x50) {
    const width = buf.readUInt32BE(16);
    const height = buf.readUInt32BE(20);
    return { width, height };
  }
  return { width: 800, height: 600 };
}

// ---------------------------------------------------------------------
// References
// ---------------------------------------------------------------------
function refParas(list) {
  return list.map(r => new Paragraph({ children: inlineRuns(r), spacing: { after: 120 }, indent: { left: 360, hanging: 360 } }));
}

// ---------------------------------------------------------------------
// Assemble document
// ---------------------------------------------------------------------
const children = [];
children.push(...titlePage);
children.push(...tocAndAbstract);

children.push(h1("1. Introduction"));
children.push(...paragraphsFromMdBlock(introBlock.replace("## 1. Introduction", "")));

children.push(h1("2. Methods"));
children.push(...paragraphsFromMdBlock(methodsBlock.replace("## 2. Methods", "")));
children.push(h2("Table 1. Search Strategy and Study Selection Summary"));
children.push(table1Doc);
children.push(new Paragraph({ spacing: { before: 150, after: 300 }, children: [] }));

children.push(h1("3. Results"));
children.push(...paragraphsFromMdBlock(resultsBlock.replace("## 3. Results", "")));

children.push(h1("4. Discussion"));
children.push(...paragraphsFromMdBlock(discussionBlock.replace("## 4. Discussion", "")));

children.push(h1("5. Conclusions"));
children.push(...paragraphsFromMdBlock(conclusionsBlock.replace("## 5. Conclusions", "")));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("Figures"));
children.push(...figureBlock("figure1_native_layer_requirements.png",
  "Native corneal layer requirements mapped to engineering targets. AFM values are local nano-indentation moduli (kPa scale); bulk tensile testing yields MPa-scale values — not interchangeable. Sources: Peris-Martínez et al. (2021); Thomasy et al. (2014); Formisano et al. (2021).", 1));
children.push(...figureBlock("figure2_biomaterial_class_matrix.png",
  "Biomaterial-class benchmarking matrix across the four benchmark domains (optical, mechanical, biological, translational), 100 Tier 1 records.", 2));
children.push(...figureBlock("figure3_translational_pathway.png",
  "Layer-specific translational pathway: distribution of evidence stage (in vitro/ex vivo, animal, clinical) by corneal layer.", 3));
children.push(...figureBlock("figure4_manufacturing_regulatory_bottleneck.png",
  "Manufacturing and regulatory bottleneck map, combining corpus-derived translational-stage percentages with standard ATMP/HCT-P regulatory terminology.", 4));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("Tables"));
children.push(h2("Table 2. Comparative Biomaterials Extraction Table (by corneal layer)"));
children.push(bodyPara("Evidence key: FT = full-text verified, AF = abstract + figures reviewed, AO = abstract only. Optical/Mechanical: Y = yes, P = partial, ? = unclear/not reported, N = not tested/not applicable."));
for (const layer of Object.keys(table2)) {
  children.push(...buildTable2ForLayer(layer, table2[layer]));
}

children.push(h2("Table 3. Cell-Source Comparison by Corneal Layer"));
for (const layer of Object.keys(table3)) {
  children.push(...buildTable3ForLayer(layer, table3[layer]));
}

children.push(h2("Table 4. Clinical-Stage and Regulatory-Readiness Table"));
children.push(bodyPara(`Records with genuine human clinical evidence: ${table4.clinical.length}. Additional records with an animal-model component (no clinical evidence): ${table4.animal.length}.`));
children.push(new Paragraph({ text: "Human Clinical Evidence", heading: HeadingLevel.HEADING_3, spacing: { before: 200, after: 100 } }));
children.push(buildTable4Clinical(table4.clinical));
children.push(new Paragraph({ spacing: { before: 200 }, children: [] }));
children.push(new Paragraph({ text: "Animal-Model Evidence (no clinical evidence yet)", heading: HeadingLevel.HEADING_3, spacing: { before: 200, after: 100 } }));
children.push(buildTable4Animal(table4.animal));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("Acknowledgments, Funding, and Conflict of Interest"));
children.push(bodyPara("Acknowledgments: none."));
children.push(bodyPara("Funding: this work received no external funding."));
children.push(bodyPara("Conflict of interest: the author declares no conflict of interest."));
children.push(bodyPara("Data availability: the full extraction dataset, search logs, screening records, benchmarking tables, and figure-generation scripts underlying this review are maintained in a version-controlled project repository and are available from the corresponding author upon reasonable request."));

children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("References"));
children.push(h2("A. Primary benchmarking corpus (100 records)"));
children.push(...refParas(refs.primary));
children.push(h2("B. Background / introductory citation"));
children.push(...refParas(refs.background));
children.push(h2("C. External physiological / epidemiological reference sources"));
children.push(...refParas(refs.external));

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
  },
  sections: [{
    properties: { page: PAGE },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })] })] }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const outPath = path.join(__dirname, "manuscript_final.docx");
  fs.writeFileSync(outPath, buf);
  console.log("Written:", outPath, buf.length, "bytes");
});
