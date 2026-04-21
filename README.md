# 📸 Digital Image Enhancement Project

##  Overview

This project focuses on enhancing low-light images using traditional image processing techniques. The goal is to improve **brightness, contrast, and visual quality** of images captured under poor lighting conditions.

We implemented and compared multiple algorithms to understand their behavior and performance.

---

##  Objectives

* Enhance low-light images
* Compare different enhancement techniques
* Analyze strengths and limitations of each algorithm
* Build a practical image enhancement pipeline

---

##  Algorithms Implemented

### 1️⃣ Histogram Equalization (HE)

* Global contrast enhancement technique
* Redistributes pixel intensity values
* Fast and simple (O(n))

**Pros:**

* Very fast
* Easy to implement

**Cons:**

* Produces unnatural results
* Amplifies noise
* Not suitable for very dark images

---

### 2️⃣ CLAHE (Contrast Limited Adaptive Histogram Equalization)

* Applies histogram equalization locally
* Limits contrast amplification to reduce noise

**Pros:**

* Preserves details
* Works better than HE
* More natural output

**Cons:**

* Requires parameter tuning
* Slightly slower than HE

---

### 3️⃣ Gamma Correction

* Uses power-law transformation to adjust brightness

**Formula:**
I_out = (I_in / 255)^(1/γ) × 255

**Pros:**

* Very fast
* Good for brightness adjustment
* No artifacts

**Cons:**

* Not adaptive
* Limited contrast improvement

---

### 4️⃣ Retinex (Multi-Scale Retinex)

* Based on human visual perception
* Separates illumination and reflectance
* Uses logarithmic transformation

**Pros:**

* Best for extreme low-light
* Natural-looking results
* High quality output

**Cons:**

* Computationally expensive
* Slower than other methods

---

##  Hybrid Approaches

###  CLAHE + Gamma

* CLAHE → improves local contrast
* Gamma → boosts brightness

**Result:**

* Balanced enhancement
* Good for most low-light images

---

###  Retinex + Gamma

* Retinex → handles illumination
* Gamma → fine-tunes brightness

**Result:**

* Best overall performance
* Works well for extremely dark images

---

##  Project Structure

```
project/
│
├── he.py
├── clahe.py
├── gamma.py
├── retinex.py
├── hybrid_clahe_gamma.py
├── hybrid_retinex_gamma.py
├── images/
└── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

2. Run any script:

```bash
python clahe.py
python gamma.py
python retinex.py
```

---

##  Key Learnings

* No single algorithm works best for all cases
* Enhancement depends on image brightness level
* Hybrid approaches provide better results
* Retinex performs best for extreme low-light conditions

---

## 📌 Conclusion

This project demonstrates that **algorithm selection is context-dependent**. While simple methods like HE and Gamma are fast, advanced techniques like Retinex and hybrid models provide superior visual quality.

---
