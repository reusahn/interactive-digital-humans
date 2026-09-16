#!/usr/bin/env python3
"""Step 18B1G4 hardware-sensitivity runner.

Run from a fresh Colab GPU runtime after Drive has been mounted.
Creates an isolated Python 3.8 / PyTorch 1.13.1+cu117 environment,
downloads the pinned Step 18B1G3 elbow-only regression script, applies
an in-process NumPy pickle compatibility alias, and executes it.

No shoulder computation. No tolerance changes.
"""

from pathlib import Path
import os
import subprocess
import sys
import urllib.request

ENV = Path("/content/hugs_legacy_torch113_py38")
PY = ENV / "bin/python"
SCRIPT = Path("/content/step18b1g3_legacy_elbow_regression.py")

G3_URL = (
    "https://raw.githubusercontent.com/"
    "reusahn/interactive-digital-humans/"
    "69022d559586ac549f4fee3162a7521b22584489/"
    "research/scripts/step18b1g3_legacy_elbow_regression.py"
)

print("=" * 100)
print("STEP 18B1G4 — SECOND-GPU LEGACY RUNTIME AUDIT")
print("=" * 100)

# Install uv if needed.
try:
    subprocess.run(["uv", "--version"], check=True)
except Exception:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "uv"],
        check=True,
    )

# Python 3.8 and isolated legacy environment.
subprocess.run(["uv", "python", "install", "3.8"], check=True)

if not PY.exists():
    subprocess.run(
        ["uv", "venv", "--python", "3.8", str(ENV)],
        check=True,
    )

subprocess.run(
    [
        "uv",
        "pip",
        "install",
        "--python",
        str(PY),
        "torch==1.13.1+cu117",
        "numpy==1.24.4",
        "scipy==1.10.1",
        "smplx==0.1.28",
        "--extra-index-url",
        "https://download.pytorch.org/whl/cu117",
    ],
    check=True,
)

urllib.request.urlretrieve(G3_URL, SCRIPT)
print("legacy regression script:", SCRIPT, SCRIPT.stat().st_size, "bytes")

bootstrap = r'''
import sys
import runpy
import importlib
import numpy as np
import numpy.core

# Compatibility only for the NumPy-2-generated clean SMPL pickle.
_core_modules = [
    "multiarray",
    "_multiarray_umath",
    "numeric",
    "umath",
    "fromnumeric",
    "shape_base",
    "overrides",
    "numerictypes",
    "getlimits",
    "_dtype",
    "_dtype_ctypes",
]

for _name in _core_modules:
    try:
        importlib.import_module("numpy.core." + _name)
    except Exception:
        pass

for _name, _module in list(sys.modules.items()):
    if _name == "numpy.core" or _name.startswith("numpy.core."):
        _alias = "numpy._core" + _name[len("numpy.core"):]
        if _alias not in sys.modules:
            sys.modules[_alias] = _module

print("NumPy compatibility alias active:", "numpy._core" in sys.modules)
runpy.run_path(
    "/content/step18b1g3_legacy_elbow_regression.py",
    run_name="__main__",
)
'''

child_env = os.environ.copy()
child_env["PYTHONUNBUFFERED"] = "1"

result = subprocess.run(
    [str(PY), "-u", "-c", bootstrap],
    env=child_env,
    text=True,
    check=False,
)

print("=" * 100)
print("STEP 18B1G4 CHILD RETURN CODE:", result.returncode)
print("=" * 100)

if result.returncode != 0:
    raise SystemExit(result.returncode)
