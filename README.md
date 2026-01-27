# Constitutional AI - Open Source Governance Platform

## 🖥️ Hardware Accessibility

### **Trained on Accessible Hardware**
One of our core principles: **AI safety shouldn't require enterprise hardware.**

The constitutional models and principles in this project were trained on:
- **GPU**: RTX 3060 (12GB VRAM) - 10+ year old consumer card
- **RAM**: 32GB DDR4
- **Storage**: Standard SSD
- **No cloud compute costs**

### **Why This Matters:**
1. **Proven on modest hardware** - Works great on consumer-grade equipment
2. **No expensive requirements** - You don't need H100s or A100s
3. **Democratizes AI safety** - Makes governance accessible to indie developers, researchers, and small teams
4. **Real-world optimization** - Models are optimized for efficiency, not just peak performance

### **Hardware Recommendations:**
- **Minimum**: Any GPU with 8GB+ VRAM, 16GB RAM
- **Recommended**: RTX 3060/equivalent or better, 32GB RAM  
- **Ideal**: Multiple GPUs for parallel testing, but not required

### **Performance on Various Setups:**
| Hardware | Training Time | Inference Speed |
|----------|---------------|-----------------|
| RTX 3060 (12GB) | ~24 hours | 15-20 tokens/sec (7B) |
| RTX 4090 (24GB) | ~4 hours | 50-70 tokens/sec |
| CPU-only (Ryzen 7) | 3-5 days | 2-5 tokens/sec |
