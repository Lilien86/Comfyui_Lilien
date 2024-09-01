## lauger NodePack comfyui

#### Welcome to the my Custom ComfyUI Nodes Pack repository! This project contains a collection of custom nodes designed to extend the functionality of ComfyUI. These nodes provide advanced capabilities and flexibility for various tasks, particularly in the domain of latent space manipulation and interpolation.

![baniere](https://github.com/user-attachments/assets/c84f68f1-3cbb-4d59-9677-0a4a67ec3d67)

### Table of Content

- Instalation 

- Node Overview

#### Instalation

To install the custom nodes in this repository, follow these steps:

1. Clone this repository into your ComfyUI custom_nodes directory:
```
git clone https://github.com/yourusername/custom-comfyui-nodes.git
```
3. Restart ComfyUI to load the new nodes.

#### Node Overview

##### LatentInterpolatorMulti

The LatentInterpolatorMulti node is a powerful tool for interpolating between two latent vectors using various mathematical algorithms. This node is particularly useful for generating smooth transitions in the latent space of models, such as those used in generative adversarial networks (GANs).

###### Key Features

- **Multiple Interpolation Algorithms**: Choose from a variety of interpolation algorithms including Linear, Quadratic, Cubic, Sinusoidal, Noise-Weighted, Random-Weighted, Per-Channel, and Logarithmic.
- **Adjustable Mixing Factor**: Control the degree of interpolation with a customizable mixing factor.
- **Automatic Compatibility Handling**: Ensures latent vectors of different dimensions or sizes are correctly aligned before interpolation.

###### Input Types

- **latent1**: The first latent vector (`LATENT`).
- **latent2**: The second latent vector (`LATENT`).

###### Optional Parameters

- **interpolation_algorithm**: The algorithm to use for interpolation. Options include:
  - Linear
  - Quadratic
  - Cubic
  - Sinusoidal
  - Noise-Weighted
  - Random-Weighted
  - Per-Channel
  - Logarithmic
- **mixing_factor**: A float value between `0.0` and `1.0`, determining the influence of each latent vector in the interpolation.

###### Output Types

- **latent**: The resulting interpolated latent vector (`LATENT`).