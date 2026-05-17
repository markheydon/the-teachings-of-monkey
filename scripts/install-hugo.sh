#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-0.152.2}"

TMP_DEB="$(mktemp -t hugo_XXXXXX.deb)"
trap 'rm -f "$TMP_DEB"' EXIT

URL="https://github.com/gohugoio/hugo/releases/download/v${VERSION}/hugo_extended_${VERSION}_linux-amd64.deb"
echo "Installing Hugo v${VERSION} from ${URL}"

wget -q -O "$TMP_DEB" "$URL"
sudo dpkg -i "$TMP_DEB"

hugo version
