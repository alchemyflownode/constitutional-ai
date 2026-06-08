# Constitutional AI — Open Source Governance Platform

**Train AI models that obey rules. On consumer hardware. No cloud required.**

## 🎯 What This Is

A complete AI governance framework that lets you:
- Train models with constitutional constraints (rules they cannot violate)
- Evaluate outputs against safety policies
- Deploy governed models locally — no API calls, no data leaving your machine

## 🖥️ Hardware Accessibility

Trained on an **RTX 3060 (12GB VRAM)** — a consumer gaming GPU. No H100s. No A100s. No cloud compute costs.

| Hardware | Training Time | Inference Speed |
|----------|--------------|-----------------|
| RTX 3060 (12GB) | ~24 hours | 15-20 tokens/sec (7B) |
| RTX 4090 (24GB) | ~4 hours | 50-70 tokens/sec |
| CPU-only (Ryzen 7) | 3-5 days | 2-5 tokens/sec |

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python constitutional_demo.py
