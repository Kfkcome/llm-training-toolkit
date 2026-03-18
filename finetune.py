"""StarCoder fine-tuning script (bootstrap)

This toolkit repo is for learning. In this environment we can't automatically vendor upstream files.

Upstream source (recommended to study directly):
https://github.com/bigcode-project/starcoder/blob/main/finetune/finetune.py

Run this file to download the upstream script into this repo for local study:
    python finetune.py

This will write: finetune_upstream.py
"""

from __future__ import annotations

import pathlib
import urllib.request


def download_upstream(dst: pathlib.Path | str = "finetune_upstream.py") -> pathlib.Path:
    url = "https://raw.githubusercontent.com/bigcode-project/starcoder/main/finetune/finetune.py"
    dst = pathlib.Path(dst)
    urllib.request.urlretrieve(url, dst)
    return dst


if __name__ == "__main__":
    path = download_upstream()
    print(f"Downloaded upstream script to: {path.resolve()}")
