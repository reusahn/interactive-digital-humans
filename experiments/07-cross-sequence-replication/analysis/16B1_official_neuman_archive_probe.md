# Step 16B1 - Official NeuMan archive probe

Date: 2026-09-15

Official HUGS NeuMan archive:

```text
https://docs-assets.developer.apple.com/ml-research/models/hugs/neuman_data.zip
```

Probe result:

```text
HTTP status: 206
Content-Range: bytes 0-0/4513980377
Content-Length: 1
Accept-Ranges: bytes
Content-Type: application/zip
Archive size: 4.204 GiB (4304.9 MiB)
Byte-range support: true
```

Storage at probe time:

```text
/content free:       65.01 GiB
/content/drive free: 61.76 GiB
```

No full `neuman_data.zip` was already stored locally or in project Drive.

## Decision

Do not download the full 4.2 GiB archive yet. Because the server supports byte-range requests, inspect the remote ZIP central directory and selectively extract only the small per-sequence `4d_humans/smpl_optimized_aligned_scale.npz` pose assets needed to choose an independent replication sequence.

This preserves storage and avoids persisting unnecessary image/video data before the mechanism test requires it.
