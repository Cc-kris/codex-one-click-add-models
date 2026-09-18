#!/bin/bash
cd "$(dirname "$0")" || exit 1
PY="./codex-add-models/scripts/install_ccai_catalog.py"
if command -v python3 >/dev/null 2>&1; then
  python3 "$PY"
elif command -v python >/dev/null 2>&1; then
  python "$PY"
else
  echo "Python 3 not found. Install Python 3 and retry."
  read -r _
  exit 1
fi
echo
read -r -p "Press Enter to close..." _
