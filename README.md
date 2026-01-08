# Car-VLM-captioning

# Dataset Information

## Source

- **Option 1**: Stanford Cars Dataset (recommended)
- **Option 2**: Personal collection
- **Option 3**: Scraped from open sources (with proper licensing)

## Structure

```
data/
  raw/              # Original images
    sedan/
    suv/
    truck/
    sports/
  processed/        # Resized images (384px shortest side)
  metadata.csv      # image_path, category, source
```

## Download Instructions

For Stanford Cars:

```bash
# Instructions will be added after we set up the download script
```

## Curation Process

1. Filter: Keep car-focused images (remove clutter)
2. Resize: Shortest side = 384px (maintains aspect ratio)
3. Deduplicate: Remove near-duplicates
4. Categorize: Assign to sedan/suv/truck/sports
