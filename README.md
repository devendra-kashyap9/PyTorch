
# 🔥 PyTorch Deep Learning Journey

> A hands-on PyTorch learning repository focused on building strong foundations in Deep Learning, Computer Vision, and modern neural-network architectures.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PyTorch](<https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch>)
![NumPy](<https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy>)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Status](https://img.shields.io/badge/Status-Learning-yellow)

---

## 🎯 Purpose

This repository documents my journey of learning **PyTorch and Deep Learning from fundamentals to advanced model implementation**.

The primary goal is not just to watch tutorials, but to:

* Understand PyTorch fundamentals deeply
* Implement neural networks from scratch
* Understand how modern architectures work internally
* Build Computer Vision models
* Implement important architectures rather than only using pretrained APIs
* Understand training and optimization workflows
* Develop the ability to read and implement research papers
* Build a strong foundation for AI/ML/DL Engineering

---

## 📚 Primary Learning Resource

This repository follows **Aladdin Persson's PyTorch tutorials** as the primary learning resource.

The tutorials are used as a guide, while the implementations in this repository are written and experimented with independently for learning purposes.

> **Learning philosophy:**
> **Watch → Understand → Code → Experiment → Break → Debug → Rebuild**

---

# 🧠 Learning Roadmap

* PyTorch installation & environment setup
* Tensors
* Tensor operations
* Tensor reshaping
* Broadcasting
* GPU acceleration
* Autograd
* Computational graphs
* Gradient computation
* `nn.Module`
* Loss functions
* Optimizers
* Training loops
* Validation loops
* Model saving/loading
* Linear Regression
* Logistic Regression
* Neural Network fundamentals
* Forward propagation
* Backpropagation
* Activation functions
* Gradient Descent
* Learning Rate
* Batch Size
* Epochs
* Overfitting
* Underfitting
* Regularization
* Dropout
* Batch Normalization
* `Dataset`
* `DataLoader`
* Custom Dataset
* Image preprocessing
* Data augmentation
* Train/Validation/Test split
* Custom transforms
* Convolution
* Filters/Kernels
* Padding
* Stride
* Pooling
* Feature maps
* CNN architecture
* LeNet
* VGG
* GoogLeNet / Inception
* ResNet
* EfficientNet
* Pretrained models
* Feature extraction
* Fine-tuning
* Freezing/unfreezing layers
* Transfer learning
* Bounding boxes
* Object detection
* IoU
* Anchor boxes
* Confidence scores
* Non-Maximum Suppression
* Precision
* Recall
* mAP
* YOLO
* YOLO architecture
* YOLO implementation
* Semantic segmentation
* Instance segmentation
* U-Net
* Encoder-Decoder architecture
* Skip connections
* Segmentation loss functions
* Autoencoders
* Variational Autoencoders
* GAN fundamentals
* Generator
* Discriminator
* DCGAN
* CycleGAN
* RNN
* LSTM
* GRU
* Sequence-to-Sequence
* Encoder-Decoder
* Attention mechanism
* Query / Key / Value
* Self-Attention
* Scaled Dot-Product Attention
* Multi-Head Attention
* Positional Encoding
* Transformer Encoder
* Transformer Decoder
* Feed-Forward Network
* Residual Connections
* Layer Normalization
* Transformer from scratch
* Modular PyTorch project structure
* Configuration management
* Reproducibility
* Random seeds
* Checkpointing
* Experiment tracking
* TensorBoard
* Model profiling
* GPU optimization
* Mixed precision
* Model inference
* Model deployment

---

# 🛠️ Tools & Technologies

```text
Python
PyTorch
TorchVision
NumPy
Pandas
Matplotlib
Jupyter Notebook
CUDA
Git
GitHub
Docker
FastAPI
Hugging Face
```

---

# 💻 Device Support

The code is designed to support multiple PyTorch backends.

```python
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"Using device: {device}")
```

Supported environments:

```text
CUDA → NVIDIA GPU
MPS  → Apple Silicon GPU
CPU  → Fallback
```

---

# 🧪 Learning Method

For every tutorial, I follow this process:

```text
1. Watch the concept
       ↓
2. Understand the mathematics
       ↓
3. Write the implementation
       ↓
4. Run the code
       ↓
5. Experiment with parameters
       ↓
6. Intentionally break the code
       ↓
7. Debug the problem
       ↓
8. Reimplement without the tutorial
       ↓
9. Build a small project
       ↓
10. Document what I learned
```

---

# 🧩 Projects

The ultimate goal of this repository is to convert tutorial knowledge into independent projects.

### Project 1 — Image Classification

```text
CNN
Dataset
DataLoader
Augmentation
Training
Evaluation
Transfer Learning
```

### Project 2 — Object Detection

```text
YOLO
Bounding Boxes
IoU
NMS
mAP
Custom Dataset
```

### Project 3 — Image Segmentation

```text
U-Net
Encoder
Decoder
Skip Connections
Segmentation Loss
```

### Project 4 — Transformer From Scratch

```text
Attention
Self-Attention
Multi-Head Attention
Positional Encoding
Encoder
Decoder
Transformer
```

---

# 🎯 Long-Term Goal

The objective is to progress from:

```text
PyTorch Beginner
       ↓
PyTorch Developer
       ↓
Deep Learning Engineer
       ↓
Computer Vision Engineer
       ↓
Transformer / GenAI Engineer
       ↓
AI/ML Engineer
```

Ultimately, I want to be able to **understand, implement, train, fine-tune, evaluate and deploy deep-learning models**, rather than treating frameworks as black boxes.

---

# 📖 Notes

This repository contains:

* Learning notes
* Jupyter notebooks
* PyTorch implementations
* Experiments
* Model architectures
* Training scripts
* Evaluation scripts
* Mini-projects
* Experiments and observations

The code is written primarily for **learning and experimentation**.

---

# 🙏 Learning Resource

Primary resource:

**Aladdin Persson — PyTorch / Deep Learning tutorials**

This repository is an independent learning implementation and is not affiliated with or endorsed by Aladdin Persson.

---

# 📌 Current Status

🚧 **Actively Learning**

> Learning PyTorch one model, one tensor, and one bug at a time. 🔥

---

## ⭐ Goal

**Don't just use Deep Learning models. Understand how they work.**

```text
Learn → Implement → Experiment → Build → Master
```
