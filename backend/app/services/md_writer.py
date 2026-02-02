# app/services/md_writer.py

import os
import frontmatter

CONTENT_ROOT = "app/content"

def write_draft(collection: str, slug: str, metadata: dict, content: str):
    path = os.path.join(CONTENT_ROOT, collection)
    os.makedirs(path, exist_ok=True)

    post = frontmatter.Post(content, **metadata)

    file_path = os.path.join(path, f"{slug}.md")

    # ✅ Let frontmatter handle writing
    frontmatter.dump(post, file_path)
