---
name: fal-ai-image
description: Generate high-end brand website assets using FAL.AI's serverless image generation APIs (FLUX.1, Recraft V3, Stable Diffusion 3.5). Use when creating product photography, hero banners, social media assets, nano banana style images, or custom brand imagery with LoRA fine-tuning support.
---

# FAL.AI Image Generation

Generate production-grade images for brand websites using FAL.AI's serverless API.

## Quick Start

### Authentication
```javascript
import { fal } from "@fal-ai/client";

fal.config({ credentials: process.env.FAL_KEY });
```

### Generate Image
```javascript
const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "Luxury smartwatch on marble surface, studio lighting, 8k",
    image_size: "landscape_16_9",
    num_images: 1
  }
});

const imageUrl = result.data.images[0].url;
```

## Model Selection

| Use Case | Model | Endpoint |
|----------|-------|----------|
| Product photos | FLUX.1 dev | `fal-ai/flux/dev` |
| Brand/logos | Recraft V3 | `fal-ai/recraft-v3` |
| Typography | SD 3.5 Large | `fal-ai/stable-diffusion-v35-large` |
| Hero banners | FLUX Pro Ultra | `fal-ai/flux-pro/v1.1-ultra` |
| Real-time preview | SDXL Turbo | `fal-ai/fast-turbo-diffusion` |
| Nano banana style | Custom LoRA | `fal-ai/flux/dev` + LoRA |

## Brand Guidelines Integration

### Prompt Structure
```
[Subject] + [Style] + [Brand Colors] + [Technical Specs]
```

**Example:**
```javascript
const prompt = `Premium wireless headphones floating on gradient background,
brand colors navy #001F3F and gold #FFD700,
minimalist luxury aesthetic, soft studio lighting,
sharp focus, 16:9 aspect ratio, 8k quality`;
```

### Aspect Ratios
```javascript
const ratios = {
  heroDesktop: "landscape_16_9",    // 1920x1080
  heroMobile: "portrait_9_16",      // 1080x1920
  productGrid: "square",            // 1024x1024
  blogThumb: "landscape_4_3",       // 1024x768
  social: "square"                  // 1024x1024
};
```

## Advanced Parameters

```javascript
{
  prompt: "Detailed description",
  image_size: "landscape_16_9",     // or "1792x1024"
  aspect_ratio: "16:9",              // alternative
  num_images: 1,                     // 1-4 batch
  seed: 42,                          // reproducible
  guidance_scale: 7,                 // 1-20, default 7
  num_inference_steps: 30,           // 20-50
  safety_tolerance: "2",             // 1-6
  enable_safety_checker: true,
  output_format: "jpeg"               // or "png"
}
```

## LoRA Custom Training

Train custom brand styles including specialized aesthetics like **nano banana**:

### Nano Banana Style
Generate images with the distinctive nano banana aesthetic:

```javascript
const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "NANOBANANA futuristic tech product, sleek minimalist design, 
             vibrant yellow and black color scheme, studio lighting, 8k",
    loras: [{ 
      path: "https://v3.fal.media/files/kangaroo/.../nano-banana-lora.safetensors",
      scale: 0.9 
    }]
  }
});
```

**Trigger word:** `NANOBANANA` (must be uppercase)
**Recommended scale:** 0.8-1.0
**Best models:** FLUX.1 dev or FLUX Pro

Train custom brand styles:

1. **Prepare Dataset:** 10-30 images, consistent style, 1024x1024
2. **Train:**
```javascript
const training = await fal.subscribe("fal-ai/flux-lora-fast-training", {
  input: {
    images_data_url: "YOUR_DATASET_ZIP_URL",
    trigger_word: "MYBRAND",
    steps: 1000,
    learning_rate: 0.0004,
    rank: 16
  }
});

const loraUrl = training.data.diffusers_lora_file.url;
```

3. **Use Trained Model:**
```javascript
const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "MYBRAND luxury packaging on display",
    loras: [{ path: loraUrl, scale: 0.8 }]
  }
});
```

## Production Patterns

### Real-Time Generation
```javascript
import { realtime } from "@fal-ai/client";

const conn = realtime.connect("fal-ai/fast-turbo-diffusion", {
  onResult: (result) => updatePreview(result.images[0].url)
});

conn.send({ prompt: userInput, image_size: "square" });
```

### Queue-Based (High Quality)
```javascript
const job = await fal.queue.submit("fal-ai/flux-pro/v1.1-ultra", {
  input: { prompt, image_size: "landscape_16_9" },
  webhookUrl: "https://yourdomain.com/webhook/complete"
});

const result = await fal.queue.result("fal-ai/flux-pro/v1.1-ultra", {
  requestId: job.request_id
});
```

### Error Handling
```javascript
async function generateWithRetry(endpoint, input, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      const result = await fal.subscribe(endpoint, { input });
      return result.data.images[0].url;
    } catch (err) {
      if (err.status === 429) {
        await delay(2000 * (i + 1));
      } else if (err.status === 500 && i < maxRetries - 1) {
        continue;
      } else {
        throw err;
      }
    }
  }
}
```

## Cost Optimization

| Model | Cost/Image | Use For |
|-------|------------|---------|
| SDXL Turbo | $0.01 | Previews/thumbnails |
| Recraft V3 | $0.02 | Standard web assets |
| FLUX Pro | $0.03 | Hero images |
| FLUX Ultra | Premium | Ultra-high-res |

**Batch Processing:**
```javascript
// Generate 4 variations in one call
const result = await fal.subscribe("fal-ai/flux/dev", {
  input: {
    prompt: "Product mockup",
    num_images: 4,
    seed: 42
  }
});
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Check FAL_KEY format: `fal_sk_...` |
| 429 Rate Limited | Add exponential backoff |
| Inconsistent outputs | Set `seed` for reproducibility |
| Poor brand match | Include hex colors in prompt or use LoRA |
| Text rendering issues | Use SD 3.5 or Recraft V3 |
| Slow generation | Use `fast-turbo-diffusion` for previews |

## Security

- Store API keys in environment variables only
- Enable safety checker for public content
- Use `safety_tolerance: "1"` for strictest filtering

## Resources

- **Docs:** https://docs.fal.ai
- **Models:** https://fal.ai/models
- **Dashboard:** https://fal.ai/dashboard