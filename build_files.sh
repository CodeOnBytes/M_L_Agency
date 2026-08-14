#!/bin/bash
echo "==> Installing dependencies..."
python3.12 -m pip install -r requirements.txt

echo "==> Creating output directory..."
mkdir -p staticfiles

echo "==> Collecting static files..."
python3.12 manage.py collectstatic --noinput --clear

echo "==> Build complete!"
