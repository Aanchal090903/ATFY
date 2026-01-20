import os
import frontmatter

CONTENT_ROOT = "app/content"

def load_collection(collection: str):
    items = []
    path = os.path.join(CONTENT_ROOT, collection)

    for file in os.listdir(path):
        if not file.endswith(".md"):
            continue

        post = frontmatter.load(os.path.join(path, file))
        if post.get("status") != "published":
            continue

        items.append(post.metadata | {"content": post.content})

    return items


def load_by_slug(collection: str, slug: str):
    path = os.path.join(CONTENT_ROOT, collection)

    for file in os.listdir(path):
        post = frontmatter.load(os.path.join(path, file))
        if post.get("slug") == slug and post.get("status") == "published":
            return post.metadata | {"content": post.content}

    return None
