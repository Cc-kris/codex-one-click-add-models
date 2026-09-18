#!/bin/bash
cd "$(dirname "$0")" || exit 1
if command -v python3 >/dev/null 2>&1; then
  python3 "./install_ccai_catalog.py"
elif command -v python >/dev/null 2>&1; then
  python "./install_ccai_catalog.py"
else
  echo "Python 3 not found. Install Python 3 and retry."
  read -r _
  exit 1
fi
