#!/usr/bin/env python3
"""Check whether each URL in telugu.m3u returns an HLS manifest.

This is a lightweight reachability check, not a guarantee of playback.
A CDN may allow the manifest but block segments, or geo-block the runner.
"""
import csv
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PLAYLIST = Path(__file__).resolve().parents[1] / "telugu.m3u"
REPORT = Path(__file__).resolve().parents[1] / "health-report.csv"
TIMEOUT = 12
UA = "Mozilla/5.0 (compatible; MY-TV-Telugu-HealthCheck/1.0)"

def entries(text):
    name = ""
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#EXTINF"):
            name = line.split(",", 1)[-1].strip()
        elif line and not line.startswith("#") and line.startswith(("http://", "https://")):
            yield name or "Unnamed", line

def check(url):
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            sample = response.read(8192).decode("utf-8", "replace")
            if response.status == 200 and "#EXTM3U" in sample:
                return "MANIFEST_OK", response.status, ""
            return "NOT_HLS_OR_BLOCKED", response.status, sample[:160].replace("\n", " ")
    except Exception as exc:
        return "UNREACHABLE_OR_GEO_BLOCKED", "", str(exc)[:240]

rows = []
for name, url in entries(PLAYLIST.read_text(encoding="utf-8")):
    status, code, detail = check(url)
    rows.append((name, url, status, code, detail))
    print(f"{status:26} {name}")

with REPORT.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["checked_utc", "channel", "url", "status", "http_status", "detail"])
    stamp = datetime.now(timezone.utc).isoformat()
    for name, url, status, code, detail in rows:
        writer.writerow([stamp, name, url, status, code, detail])

bad = sum(row[2] != "MANIFEST_OK" for row in rows)
print(f"Checked {len(rows)} streams; {bad} did not return a readable HLS manifest.")
sys.exit(1 if bad else 0)
