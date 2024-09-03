# 🎨 lauger NodePack for ComfyUI

[![baniere](https://github.com/user-attachments/assets/c84f68f1-3cbb-4d59-9677-0a4a67ec3d67)](https://github.com/user-attachments/files/16829155/latent_interpolator_with_ksampler.json)
### Copie Workflow ⬆️
#### Hey everyone it's my Custom ComfyUI Nodes Pack repository! This project contains a collection of custom nodes designed to extend the functionality of ComfyUI. These nodes offer capabilities and new creative possibilities, especially in the realms of latent space manipulation and interpolation.


## 📚 Table of Contents

- [✨ Installation](#-installation)
- [🔍 Node Overview](#-node-overview)

## ✨ Installation

To install the custom nodes in this repository, follow these easy steps:

1. Clone this repository into your ComfyUI custom_nodes directory:
    ```bash
    git clone https://github.com/Lilien86/Comfyui_Lilien.git
    ```
2. Restart ComfyUI to load the new nodes and start exploring their potential!

## 🔍 Node Overview

> ### 🎛️ LatentInterpolatorMulti
>
>
> The **LatentInterpolatorMulti** The LatentInterpolatorMulti node is a  tool for interpolating between two latent vectors using a variety of mathematical algorithms. It's perfect for generating smooth transitions within the latent space of models like GANs.
>
>[![presentation](https://github.com/user-attachments/assets/7fe183cb-5e9e-48d0-9024-1f2514ae6603)](https://github.com/user-attachments/files/16829155/latent_interpolator_with_ksampler.json)
> #### 🌟 Key Features
>
> - **🌐 Multiple Interpolation Algorithms**: Choose from a range of interpolation methods, including:
>   - Linear
>   - Quadratic
>   - Cubic
>   - Sinusoidal
>   - Noise-Weighted
>   - Random-Weighted
>   - Per-Channel
>   - Logarithmic
> - **🎚️ Adjustable Mixing Factor**: Fine-tune the degree of interpolation with a customizable mixing factor to achieve your desired effect.
> - **⚙️ Automatic Compatibility Handling**: Automatically aligns latent vectors of differing dimensions or sizes, ensuring seamless interpolation.
>
> #### 🧩 Input Types
>
> - **latent1**: The first latent vector (`LATENT`).
> - **latent2**: The second latent vector (`LATENT`).
>
> #### ⚙️ Optional Parameters
>
> - **interpolation_algorithm**: Select the interpolation algorithm to apply. Options include:
>   - Linear
>   - Quadratic
>   - Cubic
>   - Sinusoidal
>   - Noise-Weighted
>   - Random-Weighted
>   - Per-Channel
>   - Logarithmic
> - **mixing_factor**: A float value between `0.0` and `1.0`, determining how much each latent vector influences the interpolation.
>
> #### 🎯 Output Types
>
> - **latent**: The resulting interpolated latent vector (`LATENT`).
