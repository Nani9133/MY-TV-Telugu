# Requested Telugu channels — official access guide

This guide tracks the channels requested for the MY-TV-Telugu lineup that are not currently available as verified, broadcaster-authorized direct M3U feeds.

## Required channel lineup

| Network | Required channels |
|---|---|
| ETV | ETV Telugu / ETV HD, ETV Plus, ETV Cinema, ETV Andhra Pradesh, ETV Telangana, ETV Music, ETV Life, ETV Abhiruchi |
| JioStar / Star Maa | Star Maa, Star Maa HD, Star Maa Gold, Star Maa Movies, Star Maa Movies HD, Star Maa Music |
| Zee | Zee Telugu, Zee Telugu HD, Zee Cinemalu, Zee Cinemalu HD |
| Sun Network / Gemini | Gemini TV, Gemini TV HD, Gemini Movies, Gemini Movies HD, Gemini Music, Gemini Music HD, Gemini Comedy, Gemini Life, Kushi TV |

## Official viewing options

- **ETV:** The official ETV Telugu website lists ETV Telugu, Plus, Cinema, Andhra Pradesh, Telangana, Music and Life, and exposes a Live TV option: https://www.etv.co.in/channels/
- **ETV via Tata Play Binge:** The ETV Win offering on Tata Play Binge includes seven live ETV channels for subscribers; check its current plan and channel availability: https://www.etvwin.com/
- **Zee Telugu and Zee Cinemalu:** ZEE5 lists Telugu live channels including Zee Telugu HD and Zee Cinemalu HD. Live TV access depends on the current ZEE5 plan and account: https://www.zee5.com/live-tv/lang/telugu-channels
- **Star Maa, Star Maa Movies and Star Maa Music:** Check the official JioStar/JioHotstar offering or your subscribed DTH/cable provider. Tata Play lists Star Maa, Star Maa Movies, Star Maa Gold and Star Maa Music in its Telugu packs: https://www.tataplay.com/dth/pack/telugu-regional
- **Sun Gemini channels:** Sun Group confirms its Telugu channel family. Tata Play lists Gemini TV, Gemini Movies, Gemini Music, Gemini Comedy, Gemini Life and Kushi TV in its Telugu packs: https://www.sun.in/television.aspx and https://www.tataplay.com/dth/pack/telugu-regional

## Why these are not all inserted into telugu.m3u

A channel being listed in an official app or DTH package does not mean its licensed live feed is a public, direct HLS URL. Subscription services can require account authentication, expiring playback tokens and/or DRM. An app/web page URL is not a playable VLC M3U stream.

I also searched additional public GitHub playlists. I found some entries that rely on private-looking relay/proxy hosts, hard-coded credentials, referrer spoofing or expiring tokens. Those are not dependable or appropriate to republish in this public repository.

**Policy for this repo:** a channel will be added to `telugu.m3u` only when there is a broadcaster-authorized direct stream suitable for M3U use. No private credentials, copied subscriber sessions, DRM bypasses or unauthorized premium feeds will be added.

## Status

- Channel requirements recorded: all channels listed above.
- Direct VLC/M3U feed: not verified for the premium channels as a whole.
- Official access: use the broadcaster or subscribed provider options above.
- To include subscription channels in a personal playlist, obtain an M3U export or direct-stream integration explicitly provided by your authorized TV/OTT provider. Do not share account passwords or session tokens in this public repository.
