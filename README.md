# 🎨 lauger NodePack for ComfyUI

#### Welcome to my Custom ComfyUI Nodes Pack repository! This project contains my collection of custom nodes designed to extend the functionality of ComfyUI.

![baniere](https://github.com/user-attachments/assets/c84f68f1-3cbb-4d59-9677-0a4a67ec3d67)

## 📚 Table of Contents

- [✨ Installation](#-installation)
- [🔍 Node Overview](#-node-overview)

## ✨ Installation

To install the custom nodes in this repository, follow these easy steps:

1. Clone this repository into your ComfyUI custom_nodes directory:
    ```bash
    git clone https://github.com/yourusername/custom-comfyui-nodes.git
    ```
2. Restart ComfyUI to load the new nodes and start exploring their potential!

## 🔍 Node Overview

### 🎛️ LatentInterpolatorMulti

The **LatentInterpolatorMulti** node is a powerful and versatile tool for interpolating between two latent vectors using a variety of mathematical algorithms. It's perfect for generating smooth, visually appealing transitions within the latent space of models like GANs.

#### 🌟 Key Features

- **🌐 Multiple Interpolation Algorithms**: Choose from a range of interpolation methods, including:
  - Linear
  - Quadratic
  - Cubic
  - Sinusoidal
  - Noise-Weighted
  - Random-Weighted
  - Per-Channel
  - Logarithmic
- **🎚️ Adjustable Mixing Factor**: Fine-tune the degree of interpolation with a customizable mixing factor to achieve your desired effect.
- **⚙️ Automatic Compatibility Handling**: Automatically aligns latent vectors of differing dimensions or sizes, ensuring seamless interpolation.

#### 🧩 Input Types

- **latent1**: The first latent vector (`LATENT`).
- **latent2**: The second latent vector (`LATENT`).

#### ⚙️ Optional Parameters

- **interpolation_algorithm**: Select the interpolation algorithm to apply. Options include:
  - Linear
  - Quadratic
  - Cubic
  - Sinusoidal
  - Noise-Weighted
  - Random-Weighted
  - Per-Channel
  - Logarithmic
- **mixing_factor**: A float value between `0.0` and `1.0`, determining how much each latent vector influences the interpolation.

#### 🎯 Output Types

- **latent**: The resulting interpolated latent vector (`LATENT`).

Dive into the world of creative interpolation and latent space exploration with the **LatentInterpolatorMulti** node!
