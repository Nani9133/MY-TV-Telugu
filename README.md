# MY-TV-Telugu

A Telugu-focused, single-channel-at-a-time M3U playlist for VLC and compatible IPTV players.

## VLC playlist URL

Copy this exact URL into **VLC → Media → Open Network Stream (Ctrl+N)**:

```
https://raw.githubusercontent.com/Nani9133/MY-TV-Telugu/main/telugu.m3u
```

## Current playlist

The M3U contains public Telugu stream listings. Stream reachability can change; a channel name or directory listing alone is not proof that it will play on your connection.

## Required channels and premium access

You asked that ETV, Star Maa, Zee Telugu/Zee Cinemalu and Sun Gemini channels be included. These are listed in [premium-channels.md](premium-channels.md), with official viewing options.

**Important:** I will only place a channel into the VLC playlist when there is a broadcaster-authorized direct stream suitable for M3U use. Official app pages, subscription streams, signed playback links and DRM-protected feeds cannot safely be represented as permanent public M3U URLs. I will not insert copied unauthorized feeds that may be pirated or expose your VLC/device to unreliable links.

## Health checks

Run the local manifest checker:

```bash
python tools/check_streams.py
```

It writes `health-report.csv`. A manifest check is only a reachability test; it cannot guarantee that the player can fetch every media segment or bypass geo-restrictions.

The GitHub Actions workflow `.github/workflows/check-streams.yml` is configured for a weekly run. You can also start it manually from the repository's **Actions** tab.

## Sources

- [iptv-org India streams](https://github.com/iptv-org/iptv/blob/master/streams/in.m3u)
- [gnaidu05 India IPTV playlist and health-check project](https://github.com/gnaidu05/Iptv)
- [Official ETV channel page](https://www.etv.co.in/channels/)
- [Official ZEE5 Telugu live TV](https://www.zee5.com/live-tv/lang/telugu-channels)
- [Official Sun Group channel list](https://www.sun.in/television.aspx)
- [Tata Play Telugu channel pack](https://www.tataplay.com/dth/pack/telugu-regional)

This repository organizes stream URLs; it does not host, encode, or re-broadcast television video. Respect broadcaster terms and local law.
