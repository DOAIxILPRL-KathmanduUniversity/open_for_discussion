# LoRA: Low-Rank Adaptation

> [!IMPORTANT] Gist
> Fine-tuning billion-parameter models is computationally expensive. **LoRA (Hu et al., 2021)** freezes the original model weights and only trains a tiny set of auxiliary "adapter" matrices, reducing GPU memory requirements by over 90%.

## 1. The Core Idea: Intrinsic Dimension
Large models have an "intrinsic dimension" that is much smaller than their actual number of parameters. This means we can achieve similar performance by updating only a small subset of the weights.

## 2. Mathematical Framework
Instead of updating the full weight matrix $W$ (size $d \times k$):
- **Freeze $W$**: It remains unchanged during training.
- **Add Low-Rank Matrices**: $W + \Delta W$, where $\Delta W = B \times A$.
    - $A$ is $r \times k$ and $B$ is $d \times r$.
    - $r$ is the **Rank** (typically 4, 8, or 16).
- **Update Only $A$ and $B$**: The number of trainable parameters is proportional to $r \cdot (d + k)$, which is much smaller than $d \cdot k$.

## 3. Advantages of LoRA
- **GPU Memory Efficiency**: Since we only store gradients for the tiny adapter matrices, we can fine-tune huge models (like Llama-70B) on consumer hardware.
- **No Inference Latency**: At inference time, the adapter weights can be merged back into the main weights ($\Delta W$ is just added to $W$), so the model runs at full speed.
- **Portability**: You can share just the LoRA weights (a few megabytes) instead of the whole model (gigabytes).

## 4. QLoRA (Quantized LoRA)
A further improvement that combines LoRA with 4-bit quantization.
- **NF4 (NormalFloat 4-bit)**: A specialized data type that stores weights even more efficiently.
- **Double Quantization**: Quantizing the quantization constants themselves.
- **Result**: Fine-tuning 65B parameter models on a single 48GB GPU (e.g., A6000).

---

#modern-frontiers #peft #lora #qlora #finetuning #efficiency
