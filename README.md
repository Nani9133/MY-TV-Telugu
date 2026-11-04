# MY-TV-Telugu

A Telugu-focused, single-channel-at-a-time M3U playlist for VLC and other IPTV players.

## VLC playlist URL

Copy this exact URL into **VLC → Media → Open Network Stream (Ctrl+N)**:

```
https://raw.githubusercontent.com/Nani9133/MY-TV-Telugu/main/telugu.m3u
```

Do not copy an individual stream from the GitHub-rendered page. Load the raw playlist URL above.

## What is included

Entertainment, movies, music, news, devotional, kids and Telugu public-service channels. Premium subscription channels (for example Star Maa, Zee Telugu, Gemini TV and paid sports feeds) are excluded unless a broadcaster-authorized free stream is publicly documented.

## Stream selection and quality

- Replaced the ETV Cinema CloudFront address that was failing in VLC with an alternate directory-listed YuppTV HLS endpoint.
- ETV Plus also uses an alternate directory-listed YuppTV endpoint.
- ETV Comedy, ETV Josh, ETV Music and ETV News use their separate Amagi HLS endpoints.
- Other channel URLs are selected from the public iptv-org India stream directory and a second community-maintained India playlist.
- Labels are source-reported, not guarantees. Some endpoints may be geo-restricted, require broadcaster-specific access, change without notice, or stop working.
- A playlist URL being reachable is not proof that its video segments will play in every location/player. The upstream India playlist's latest published check report is a point-in-time test, not a guarantee for this Telugu subset.
- No genuine 2160p/4K Telugu live source was verified. VLC cannot create native 4K detail from an HD/SD source.

## Sources

- [iptv-org India streams](https://github.com/iptv-org/iptv/blob/master/streams/in.m3u)
- [gnaidu05 India IPTV playlist and health-check project](https://github.com/gnaidu05/Iptv)
- [gnaidu05 latest India link-check report](https://github.com/gnaidu05/Iptv/blob/main/playlists/CHECK_REPORT.md)

This repository only organizes public stream URLs; it does not host, encode, or re-broadcast channel video. Respect broadcaster terms and local law.
