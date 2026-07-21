// Build the assignment-tailored coursework report .docx
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  ImageRun, PageBreak, Footer, PageNumber, VerticalAlign,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const DATA = path.join(__dirname, "build_data");

const recentTable = JSON.parse(fs.readFileSync(path.join(DATA, "recent_2025_2026_table.json")));
const apaRecent = JSON.parse(fs.readFileSync(path.join(DATA, "apa_references_recent.json")));
const apaExternal = JSON.parse(fs.readFileSync(path.join(DATA, "apa_references_external.json")));
const md = fs.readFileSync(path.join(__dirname, "assignment_report_content.md"), "utf-8");

const FONT = "Calibri";
const PAGE = { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } };

function inlineRuns(text) {
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
function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 380, after: 180 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 260, after: 140 } }); }
function h3(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_3, spacing: { before: 200, after: 100 } }); }

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
  return new TableRow({ tableHeader: true, children: cells.map((c, i) => cellText(c, { width: widths[i], shade: "D9D9D9", center: true })) });
}

// ---------------------------------------------------------------------
// Parse markdown body into paragraphs (## => new top section handled by caller split, ### => h2, #### treated as h3)
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
    if (line.startsWith("### ")) { flush(); paras.push(h3(line.replace(/^### /, ""))); continue; }
    if (line.startsWith("## ")) { flush(); continue; }
    if (line.startsWith("*(") && line.endsWith(")*")) { flush(); paras.push(bodyPara(line)); continue; }
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

const sections = [
  ["## 1. Introduction", "## 2. Anatomy"],
  ["## 2. Anatomy and Physiology of the Cornea", "## 3. Biological"],
  ["## 3. Biological and Mechanical Properties of Corneal Tissue", "## 4. Recent Developments"],
  ["## 4. Recent Developments (2025–2026): Biomaterials and Cells", "## 5. Scaffold Fabrication Methods"],
  ["## 5. Scaffold Fabrication Methods", "## 6. Case Studies"],
  ["## 6. Case Studies (2025–2026)", "## 7. Critical Discussion"],
  ["## 7. Critical Discussion and Personal Assessment", "## 8. Ethical Issues"],
  ["## 8. Ethical Issues in Corneal Tissue Engineering", "## 9. Conclusion"],
  ["## 9. Conclusion", "## References"],
];
const titles = [
  "1. Introduction",
  "2. Anatomy and Physiology of the Cornea",
  "3. Biological and Mechanical Properties of Corneal Tissue",
  "4. Recent Developments (2025–2026): Biomaterials and Cells",
  "5. Scaffold Fabrication Methods",
  "6. Case Studies (2025–2026)",
  "7. Critical Discussion and Personal Assessment",
  "8. Ethical Issues in Corneal Tissue Engineering",
  "9. Conclusion",
];

// ---------------------------------------------------------------------
// Title page
// ---------------------------------------------------------------------
const titlePage = [
  new Paragraph({ spacing: { before: 1000 }, children: [] }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 500 },
    children: [new TextRun({ text: "Engineering of Cornea Tissue: Anatomy, Properties, Biomaterials, and Recent Advances in Corneal Tissue Engineering (2025–2026)", bold: true, size: 30, font: FONT })],
  }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Samuel Bertrand Bernard Gonzalves", size: 24, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Matric Number: MKE251020", size: 22, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Faculty of Electrical Engineering, Master of Science (Biomedical Engineering)", size: 22, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Universiti Teknologi Malaysia (UTM)", size: 22, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400 }, children: [new TextRun({ text: "bertrandbernard@graduate.utm.my", size: 20, italics: true, font: FONT })] }),
  new Paragraph({ spacing: { before: 700, after: 100 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "MKEB/MEBC Tissue Engineering — Individual Assignment", bold: true, size: 22, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Academic Session/Semester 2025/2026-2", size: 20, font: FONT })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, children: [new TextRun({ text: "Course lecturer: Dr Norhana Jusoh", size: 20, font: FONT })] }),
  new Paragraph({ children: [new PageBreak()] }),
];

// ---------------------------------------------------------------------
// Abstract
// ---------------------------------------------------------------------
const abstractBlock = [
  h1("Abstract"),
  bodyPara("**Objective.** This report reviews the recent development of corneal tissue engineering, covering the anatomy and physiology of the cornea, the biological and mechanical properties each corneal layer must meet, and the biomaterials, cell sources, and scaffold fabrication methods reported in the 2025–2026 literature."),
  bodyPara("**Methods.** Cornea-focused primary literature was identified via a systematic PubMed search (four layer-specific search blocks, 1,082 unique records after deduplication, screened for relevance to corneal tissue engineering); this report concentrates specifically on the subset of 24 primary studies published in 2025–2026 across the endothelium, stroma, and epithelium/limbus, supplemented by four studies selected for in-depth case analysis."),
  bodyPara("**Findings.** Decellularized/natural-extracellular-matrix materials remain the dominant biomaterial class in the most recent literature (9/24 studies), followed by natural polymers and hybrid/composite hydrogels (5/24 each); decellularization itself is the single most common fabrication route (6/24), with photocurable hydrogel crosslinking, 3D bioprinting/digital light processing, and solvent casting also well represented. Four case studies — a femtosecond-laser-cut lens-capsule endothelial carrier, a digital-light-processing-bioprinted stromal hydrogel that closely matched native compressive modulus, a head-to-head comparison of decellularized Descemet membrane versus amniotic membrane as limbal stem-cell substrates, and an electrospun, surface-functionalized scaffold supporting induced-pluripotent-stem-cell-derived limbal stem cells — illustrate both the field's genuine progress toward native-tissue-matching performance and its persistent reliance on animal-derived or xenogeneic source materials."),
  bodyPara("**Conclusion.** Corneal tissue engineering in 2025–2026 is converging on biomimetic, decellularization-heavy strategies with increasingly precise fabrication control, but mechanical benchmarking against native tissue remains inconsistent, and unresolved ethical questions around donor-tissue sourcing, animal-derived materials, and equitable access to advanced therapies deserve more explicit attention as the field moves toward clinical translation."),
  new Paragraph({ spacing: { after: 300 }, children: [
    new TextRun({ text: "Keywords: ", bold: true, font: FONT }),
    new TextRun({ text: "corneal tissue engineering; cornea anatomy; biomaterials; scaffold fabrication; limbal stem cells; corneal endothelium; ethics", italics: true, font: FONT }),
  ]}),
  new Paragraph({ children: [new PageBreak()] }),
];

// ---------------------------------------------------------------------
// Table 1: recent 2025-2026 studies
// ---------------------------------------------------------------------
function buildRecentTable() {
  const widths = [1550, 1500, 4200, 2110];
  const total = widths.reduce((a,b)=>a+b,0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      headerRow(["Citation", "Layer", "Material", "Fabrication method"], widths),
      ...recentTable.map(r => new TableRow({ children: [
        cellText(r.citekey, { width: widths[0] }),
        cellText(r.layer.replace('_',' / '), { width: widths[1] }),
        cellText(r.material, { width: widths[2] }),
        cellText(r.fabrication, { width: widths[3] }),
      ]})),
    ],
  });
}

// ---------------------------------------------------------------------
// Figures
// ---------------------------------------------------------------------
function imageSizeOf(buf) {
  if (buf[0]===0x89 && buf[1]===0x50) {
    return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
  }
  return { width: 800, height: 600 };
}
function figureBlock(filename, caption, num) {
  const buf = fs.readFileSync(path.join(ROOT, "figures", filename));
  const dims = imageSizeOf(buf);
  const maxWidth = 620;
  const scale = Math.min(1, maxWidth / dims.width);
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 }, children: [new ImageRun({
      type: "png", data: buf,
      transformation: { width: Math.round(dims.width * scale), height: Math.round(dims.height * scale) },
    })]}),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: [new TextRun({ text: `Figure ${num}. ${caption}`, italics: true, size: 20, font: FONT })] }),
  ];
}

// ---------------------------------------------------------------------
// References
// ---------------------------------------------------------------------
function refParas(list) {
  return list.map(r => new Paragraph({ children: inlineRuns(r), spacing: { after: 140 }, indent: { left: 360, hanging: 360 } }));
}

// ---------------------------------------------------------------------
// Assemble
// ---------------------------------------------------------------------
const children = [];
children.push(...titlePage);
children.push(...abstractBlock);

// 1. Introduction
children.push(h1(titles[0]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[0])));

// 2. Anatomy & Physiology + Figure 1
children.push(h1(titles[1]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[1])));
children.push(...figureBlock("figure1_native_layer_requirements.png",
  "Native corneal layer requirements mapped to engineering targets. Sources: Peris-Martínez et al. (2021); Thomasy et al. (2014); Formisano et al. (2021).", 1));

// 3. Biological & mechanical properties
children.push(h1(titles[2]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[2])));

// 4. Recent developments: biomaterials & cells + Figure 2 + Table 1
children.push(h1(titles[3]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[3])));
children.push(...figureBlock("figure_recent_biomaterials_fabrication.png",
  "Biomaterial class and scaffold fabrication method distribution among the 24 studies published in 2025–2026 that form this report's core evidence base.", 2));
children.push(h2("Table 1. Corneal tissue-engineering studies published 2025–2026"));
children.push(bodyPara("All 24 studies forming this report's 2025–2026 evidence base (Sections 4–6), sorted by citation."));
children.push(buildRecentTable());
children.push(new Paragraph({ spacing: { before: 200, after: 200 }, children: [] }));

// 5. Scaffold fabrication methods
children.push(h1(titles[4]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[4])));

// 6. Case studies
children.push(h1(titles[5]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[5])));

// 7. Critical discussion
children.push(h1(titles[6]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[6])));

// 8. Ethics
children.push(h1(titles[7]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[7])));

// 9. Conclusion
children.push(h1(titles[8]));
children.push(...paragraphsFromMdBlock(extractSection(md, ...sections[8])));

// References
children.push(new Paragraph({ children: [new PageBreak()] }));
children.push(h1("References"));
children.push(bodyPara("APA 7th edition style. Section A lists the 24 primary 2025–2026 studies forming this report's core evidence base (Sections 4–6); Section B lists supporting physiological and epidemiological sources used in Sections 1–3 and 8."));
children.push(h2("A. Primary 2025–2026 corneal tissue-engineering studies"));
children.push(...refParas(apaRecent));
children.push(h2("B. Supporting physiological and epidemiological sources"));
children.push(...refParas(apaExternal));
children.push(new Paragraph({ spacing: { before: 200 }, children: [new TextRun({
  text: "Note: one author entry (\"Xxx, S.\") for Aouimeur et al. (2025) is reproduced exactly as returned by the Europe PMC bibliographic database and likely reflects a placeholder or data artifact in the source record rather than an error introduced in this report.",
  italics: true, size: 18, font: FONT, color: "555555",
})]}));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  sections: [{
    properties: { page: PAGE },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const outPath = path.join(__dirname, "assignment_report_final.docx");
  fs.writeFileSync(outPath, buf);
  console.log("Written:", outPath, buf.length, "bytes");
});
