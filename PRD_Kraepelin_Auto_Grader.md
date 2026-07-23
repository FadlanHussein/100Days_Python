# PRD: Kraepelin Auto Grader

**Version:** 1.0  
**Status:** Draft  
**Author:** [Your Name]  
**Date:** 2026-07-23

---

## 1. Product Overview

### 1.1 Problem Statement
Manual koreksi lembar test Kraepelin (tes penjumlahan) memakan waktu lama dan melelahkan. Setiap kandidat memiliki 1-3 lembar dengan ~300-400 cell per lembar. Butuh alat otomatis yang akurat (≥99%), gratis, dan jalan lokal.

### 1.2 Solution
Aplikasi CLI berbasis Python yang:
- Menerima foto lembar jawaban (HP, berbagai kondisi)
- Melakukan preprocessing (perspective correction, enhancement)
- Mendeteksi grid 51 baris × 7 kolom
- Mengekstrak tiap cell → klasifikasi digit (0-9/kosong) via CNN ringan
- Memvalidasi aturan penjumlahan Kraepelin (rule-based cross-check)
- Output: CSV/JSON per lembar + ringkasan per kandidat (benar/salah/lubang, skor, grafik)

### 1.3 Target User
- HRD / Psikolog / Assessor yang koreksi Kraepelin manual
- Skala: 1-3 lembar per kandidat, batch kecil (<100 lembar/hari)

---

## 2. Functional Requirements

### 2.1 Input
| Spec | Detail |
|------|--------|
| Format | JPG/PNG (foto HP) |
| Resolusi | Min 800px lebar, ideal 1600px+ |
| Kondisi | Variasi cahaya, sudut (45-90°), background, kualitas tulisan |
| Batch | Folder berisi 1-N foto |

### 2.2 Output
| Format | Content |
|--------|---------|
| `results.csv` | Per cell: `file,row,col,predicted_digit,ground_truth_digit,status(benar/salah/lubang),confidence` |
| `summary.csv` | Per lembar: `file,total_cells,benar,salah,lubang,accuracy_pct,avg_confidence` |
| `kandidat_summary.csv` | Per kandidat (gabungan 1-3 lembar): agregat skor + statistik kecepatan/akurasi per blok |

### 2.3 Core Pipeline
```
Load Image → Rectify Perspective → Enhance (binarize) → Detect Grid → Extract Cells → 
Classify Digits (CNN) → Validate Rules → Score → Export
```

### 2.4 Grid Specification
- **Rows**: 51 (fixed)
- **Cols**: 7 (fixed, confirmed)
- **Cell content**: Single digit (0-9) atau kosong
- **Rule**: Kolom 0+1=2, 1+2=3, 2+3=4, 3+4=5, 4+5=6, 5+6=7 (standar Kraepelin)

### 2.5 Accuracy Target
| Layer | Target | Method |
|-------|--------|--------|
| OCR per digit | 97-98% | CNN + augmentasi |
| Rule validation | +1.5% | Cross-check penjumlahan |
| Confidence threshold | +0.5% | Low-conf → manual review flag |
| **Overall** | **≥99%** | Combined |

---

## 3. Non-Functional Requirements

| Category | Requirement |
|----------|-------------|
| **Cost** | $0 (local CPU, free Colab GPU untuk training) |
| **Hardware** | CPU-only inference (RAM ≥4GB), optional GPU untuk training |
| **Latency** | <10 detik per lembar (CPU) |
| **Portability** | Windows/Linux/Mac, Python 3.10+ |
| **Extensibility** | Modular: ganti model, aturan, output format mudah |
| **Privacy** | 100% lokal, tidak upload data |

---

## 4. Technical Architecture

### 4.1 Tech Stack
| Layer | Tools |
|-------|-------|
| Image Processing | OpenCV, NumPy, Albumentations |
| ML Framework | PyTorch (training), ONNX Runtime (inference) |
| Config | YAML + dataclass |
| CLI | argparse, logging, tqdm |
| Data | pandas (CSV), PyTorch Dataset/DataLoader |
| Labeling | LabelImg / CVAT (local) |

### 4.2 Model Spec
- **Architecture**: Lightweight CNN (~40k params)
- **Input**: 32×32 grayscale cell crop
- **Output**: 11 classes (0-9 + empty)
- **Size**: <5 MB (ONNX)
- **Training**: 30 epoch, batch 64, Adam lr=1e-3, ~15 min di Colab T4

### 4.3 Project Structure
```
kraepelin-auto/
├── config.yaml
├── main.py
├── requirements.txt
├── src/
│   ├── config.py
│   ├── io/loader.py, writer.py
│   ├── preprocess/rectify.py, enhance.py
│   ├── grid/detect.py, extract.py
│   ├── ocr/dataset.py, model.py, train.py, infer.py, onnx_export.py
│   ├── rules/validate.py, score.py
│   └── pipeline.py
├── data/raw, cells, labeled, samples/
├── models/
├── notebooks/ (EDA, training, error analysis)
└── tests/
```

---

## 5. Data Requirements

### 5.1 Training Data
| Set | Quantity | Source |
|-----|----------|--------|
| Train | 50-80 lembar (~20k cell) | Simulasi mandiri (print → isi → foto) |
| Val | 10-15 lembar | Terpisah dari train |
| Test | 10-15 lembar | Holdout, final eval only |

### 5.2 Data Variation (Critical)
- Cahaya: terang, redup, bayangan, warna lampu
- Sudut: 90°, 75°, 60°, 45°, miring
- Jarak: full frame, zoom, crop
- Background: putih, kayu, kertas, lantai
- HP: minimal 2-3 merek
- Tulisan: rapi, kurut, tebal, tipis, bolpen/pensil

### 5.3 Ground Truth Collection
- **Method**: Label saat isi (Excel paralel per lembar) → 100% akurasi GT
- **Format**: `baris, kolom, digit_asli(0-9/kosong)` → convert ke YOLO/COCO untuk labeling tool

---

## 6. Development Phases

### Phase 0: Data Collection (Minggu 1-2)
- [ ] Buat template lembar standar (51×7 kolom, Excel/Word)
- [ ] Print 60-80 lembar HVS
- [ ] Isi manual + catat GT di Excel
- [ ] Foto 3-5 variasi per lembar
- [ ] Organisasi file + convert GT ke LabelImg/CVAT
- [ ] Label 10 lembar pertama → baseline dataset

### Phase 1: Preprocessing & Grid (Minggu 2-3)
- [ ] Perspective correction (deteksi 4 sudut kertas, warp)
- [ ] Enhancement (grayscale, CLAHE, adaptive threshold)
- [ ] Grid detection (projection profile / Hough lines)
- [ ] Cell extraction → array (N, 32, 32)
- [ ] Unit test tiap komponen

### Phase 2: OCR Model (Minggu 3-4)
- [ ] PyTorch Dataset + DataLoader + augmentasi
- [ ] CNN model definition
- [ ] Training loop (Colab GPU)
- [ ] Evaluasi akurasi per digit + confusion matrix
- [ ] Error analysis → iterasi augment/data

### Phase 3: Rule Engine & Scoring (Minggu 4)
- [ ] Validasi aturan penjumlahan per baris
- [ ] Koreksi error OCR via rules
- [ ] Scoring: benar/salah/lubang per cell
- [ ] Statistik per kandidat (akurasi, kecepatan, pola kelelahan)

### Phase 4: CLI & Packaging (Minggu 5)
- [ ] Pipeline orchestrator
- [ ] CLI dengan argparse (--input, --output, --config)
- [ ] Export ONNX + ONNX Runtime inference
- [ ] README, requirements, .gitignore
- [ ] End-to-end test pada holdout set

### Phase 5: Polish & Deploy (Minggu 6+)
- [ ] Confidence threshold + manual review flag
- [ ] Batch processing + progress bar
- [ ] Optional: simple GUI (Tkinter/Streamlit)
- [ ] Dokumentasi retrain untuk format lembar baru

---

## 7. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Overall accuracy** | ≥99% | Holdout test set (10-15 lembar) |
| **Per-digit OCR** | ≥97% | Validation set |
| **Inference time** | <10s/lembar | CPU (Intel i5/Ryzen 5) |
| **False positive (salah→benar)** | <0.5% | Critical: tidak boleh luluskan jawaban salah |
| **Manual review rate** | <5% | Low-confidence cells |

---

## 8. Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Foto kualitas buram (blur, gelap) | Tinggi | Tinggi | Augmentasi agresif + confidence threshold + flag manual |
| Variasi format lembar (kolom beda) | Rendah | Tinggi | Config-driven grid size; validasi awal |
| Handwriting aneh (kuret, bergaya) | Sedang | Sedang | Data augmentasi elastik, rotasi, noise |
| Grid detection gagal (garis tipis) | Sedang | Tinggi | Multiple method: projection + Hough + template fallback |
| Overfitting (data sedikit) | Tinggi | Tinggi | Heavy augment, dropout, early stopping, simple model |

---

## 9. Future Enhancements (Post-MVP)

- **Multi-format support**: Config-driven untuk format Kraepelin lain (kolom/baris beda)
- **Batch web UI**: Drag-drop folder → progress → download CSV
- **Analytics dashboard**: Grafik kecepatan/akurasi per blok, deteksi kecurangan (pola aneh)
- **API mode**: FastAPI endpoint untuk integrasi sistem HR
- **Active learning**: Model flag low-conf → user label → auto-retrain

---

## 10. Appendix

### 10.1 Kraepelin Rule Detail
```
Kolom:  0   1   2   3   4   5   6
Aturan: 0+1=2, 1+2=3, 2+3=4, 3+4=5, 4+5=6, 5+6=7
        (sum modulo 10, tulis satuan saja)
```

### 10.2 Label Schema (LabelImg/YOLO)
```
Class IDs:
0-9  → digit 0-9
10   → empty/kosong

YOLO format per cell:
<class_id> <x_center> <y_center> <width> <height>  (normalized 0-1)
```

### 10.3 Config.yaml Reference
```yaml
grid:
  rows: 51
  cols: 7
  cell_size: 32

preprocess:
  target_width: 1600
  clip_limit: 2.0

ocr:
  num_classes: 11
  batch_size: 64
  epochs: 30
  lr: 1e-3
  device: "cpu"

rules:
  addition_pairs:
    - [0, 1, 2]
    - [1, 2, 3]
    - [2, 3, 4]
    - [3, 4, 5]
    - [4, 5, 6]

paths:
  input_dir: "data/raw"
  output_dir: "output"
  model_path: "models/best.pt"
```

---

## 11. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | [You] | | |
| Developer | [You] | | |