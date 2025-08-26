import os
from pathlib import Path
from PIL import Image
from tqdm import tqdm

def optimize_images_folder(src_folder, dst_folder, max_dimension=1000, quality=80, convert_webp=True):
    src_root = Path(src_folder)
    dst_root = Path(dst_folder)

    success_count = 0
    error_count = 0

    def has_alpha(img):
        """Check if the image has an alpha channel."""
        return (
            img.mode in ("RGBA", "LA") or
            (img.mode == "P" and "transparency" in img.info)
        )

    def optimize_image(src_path, dst_path):
        nonlocal success_count, error_count
        try:
            with Image.open(src_path) as img:
                # Resize preserving aspect ratio
                orig_width, orig_height = img.size
                scale = min(max_dimension / orig_width, max_dimension / orig_height, 1)
                new_width = int(orig_width * scale)
                new_height = int(orig_height * scale)
                if scale < 1:
                    img = img.resize((new_width, new_height), Image.LANCZOS)

                # Ensure destination folder exists
                dst_path.parent.mkdir(parents=True, exist_ok=True)

                # Convert to WebP or keep original format
                if convert_webp:
                    dst_path = dst_path.with_suffix(".webp")
                    img.save(
                        dst_path,
                        "WEBP",
                        quality=quality,
                        lossless=has_alpha(img),
                        method=6
                    )
                else:
                    img.save(dst_path)

                success_count += 1
        except Exception as e:
            print(f"❌ Error processing {src_path}: {e}")
            error_count += 1

    # Collect all image files
    files = [
        Path(root) / f
        for root, _, fs in os.walk(src_root)
        for f in fs
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]

    for src_path in tqdm(files, desc="Processing images", unit="img"):
        relative_path = src_path.relative_to(src_root)
        dst_path = dst_root / relative_path
        if convert_webp:
            dst_path = dst_path.with_suffix(".webp")

        # Create parent folder if missing
        dst_path.parent.mkdir(parents=True, exist_ok=True)

        optimize_image(src_path, dst_path)

    print("\n✅ Optimization complete!")
    print(f"✅ Processed successfully: {success_count}")
    print(f"⚠️ Errors: {error_count}")
