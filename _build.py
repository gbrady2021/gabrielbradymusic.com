"""Regenerates index.html, film/, records/ and press/ (press list lives in _press.html). Run: python3 _build.py"""
import os
SITE = os.path.dirname(os.path.abspath(__file__))
# Version the stylesheet URL so browsers fetch new CSS right after a change.
import hashlib
CSS_V = hashlib.md5(open(os.path.join(SITE, "style.css"), "rb").read()).hexdigest()[:8]
BIFF = "https://www.biff.kr/eng/html/program/prog_view.asp?idx=84111&amp;c_idx=431"

def head(title, desc, image, path):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://gabrielbradymusic.com/{image}">
<meta property="og:url" content="https://gabrielbradymusic.com{path}">
<link rel="icon" href="/icon.png">
<link rel="apple-touch-icon" href="/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css?v={CSS_V}">
</head>
<body>

<h1><a href="/">GABRIEL BRADY</a></h1>
'''

def nav(current):
    items = [("Scores", "/scores/"), ("Recordings", "/recordings/"), ("Press", "/press/"), ("Info", "/info/")]
    cur = ' aria-current="page"'
    links = "\n".join(
        f'  <a href="{href}"{cur if name == current else ""}>{name}</a>'
        for name, href in items)
    return f"<nav>\n{links}\n</nav>\n"

FOOTER = '''
<footer>
<p>Contact: <a href="mailto:hello@gabrielbradymusic.com">hello@gabrielbradymusic.com</a></p>
<div class="icons">
  <a href="https://www.instagram.com/gabrielbradymusic/" aria-label="Instagram">
    <svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/><circle cx="12" cy="12" r="4.3"/><circle cx="17.6" cy="6.4" r="0.6" fill="#000" stroke="none"/></svg>
  </a>
  <a href="https://open.spotify.com/artist/0ywhuJfpfzQJtSwu3rqV7p" aria-label="Spotify">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#000"/><g fill="none" stroke="#fff" stroke-linecap="round"><path d="M6.2 9.2c3.9-1.2 8.3-.9 11.8 1" stroke-width="1.9"/><path d="M6.8 12.5c3.2-.9 6.6-.6 9.6.9" stroke-width="1.6"/><path d="M7.4 15.6c2.5-.7 5.1-.5 7.4.7" stroke-width="1.3"/></g></svg>
  </a>
  <a href="https://music.apple.com/us/artist/gabriel-brady/1469277718" aria-label="Apple Music">
    <svg viewBox="0 0 24 24" fill="#000"><path d="M9 4.5 20 2v13.2a3 3 0 1 1-2-2.8V6.3l-7 1.6v9.3a3 3 0 1 1-2-2.8z"/></svg>
  </a>
  <a href="https://gabrielbrady.bandcamp.com/" aria-label="Bandcamp">
    <svg viewBox="0 0 24 24" fill="#000"><path d="M0 18.5 6.6 5.5H24l-6.6 13z"/></svg>
  </a>
</div>
</footer>

</body>
</html>
'''

def page(path, title, desc, image, current, body):
    out = os.path.join(SITE, path.strip("/"), "index.html") if path != "/" else os.path.join(SITE, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(head(title, desc, image, path) + "\n" + nav(current) + "\n" + body.strip() + "\n" + FOOTER)
    print("wrote", out)

page("/", "Gabriel Brady", "Composer. Original score for Hinotama: Ball of Fire, Busan International Film Festival 2026.", "hinotama.jpg", None, f'''
<a class="hero poster" href="{BIFF}"><img src="/hinotama.jpg" width="1179" height="1572" alt="Hinotama: Ball of Fire poster"></a>

<p>Original score for <a href="{BIFF}"><i>Hinotama: Ball of Fire</i></a>, <span class="nowrap">dir. Takenoshin Yaza.</span><br>
Vision Asia, <span class="nowrap">Busan International Film Festival 2026.</span></p>
''')

page("/scores/", "Scores · Gabriel Brady", "Film scores by Gabriel Brady.", "hinotama.jpg", "Scores", f'''
<!-- Film reel: paste the Vimeo/YouTube embed URL into src, then delete `hidden`. -->
<div class="reel" hidden>
  <iframe src="" title="Film reel" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
</div>

<section class="list">
  <h2>Features</h2>
  <ul>
    <li><a href="{BIFF}"><i>Hinotama: Ball of Fire</i></a> (2026), <span class="nowrap">dir. Takenoshin Yaza</span></li>
    <li><a href="https://www.meanttobemaddie.com/"><i>Meant To Be Maddie</i></a> (forthcoming), <span class="nowrap">dir. Anna Clare Spelman</span></li>
  </ul>
  <h2>Shorts</h2>
  <ul>
    <li><i>Rockhound</i>, <span class="nowrap">dir. Eddie Dai</span></li>
  </ul>
</section>
''')

page("/recordings/", "Recordings · Gabriel Brady", "Day-blind out now on Tonal Union.", "day-blind.jpg", "Recordings", '''
<a class="hero cover" href="https://bfan.link/dayblind"><img src="/day-blind.jpg" width="1200" height="1200" alt="Day-blind album cover"></a>

<p><a href="https://bfan.link/dayblind"><i>Day-blind</i></a> out now on Tonal Union.</p>
<p><a href="https://gabrielbrady.bandcamp.com/album/day-blind">Bandcamp</a> · <a href="https://midheaven.com/item/brady-gabriel/day-blind">Vinyl</a> · <a href="https://bfan.link/dayblind">Stream</a></p>
''')

PRESS = open(os.path.join(SITE, "_press.html")).read() if os.path.exists(os.path.join(SITE, "_press.html")) else '''
  <ul>
    <li><i>Flow State</i>, <a href="https://www.flowstate.fm/p/gabriel-brady-interview">interview</a></li>
  </ul>
'''
page("/press/", "Press · Gabriel Brady", "Press for Gabriel Brady.", "day-blind.jpg", "Press", f'''
<section class="list">
{PRESS.strip()}
</section>
''')

page("/info/", "Info · Gabriel Brady", "Gabriel Brady is a composer, pianist, producer and recording artist from Alexandria, Virginia.", "hinotama.jpg", "Info", f'''
<section class="bio">
<p>Gabriel Brady is a prize-winning composer, pianist, producer and recording artist from Alexandria, Virginia, based in Brooklyn.</p>
<p>He composed the score for <a href="{BIFF}"><i>Hinotama: Ball of Fire</i></a>, the debut feature from writer-director Takenoshin Yaza, which had its world premiere in the Vision Asia section of the 2026 Busan International Film Festival. The film was made with the Venice Grand Jury Prize-winning production and cinematography team behind <i>Evil Does Not Exist</i>, alongside members of the production team of the Oscar-winning <i>Drive My Car</i>. He is now scoring <a href="https://www.meanttobemaddie.com/"><i>Meant To Be Maddie</i></a>, a feature documentary directed by Anna Clare Spelman.</p>
<p>His debut album, <a href="/recordings/"><i>Day-blind</i></a>, was released in 2025 by Tonal Union, the U.K. independent ambient-jazz label he signed with in 2023. It was named among NPR\u2019s best new albums of its release week, featured by Flow State, and played on BBC Radio 6 Music, BBC Radio 3 and NTS.</p>
</section>
''')

# Earlier page names (/film/, /records/, /releases/); send visitors on to the current ones.
for old, new in [("film", "/scores/"), ("records", "/recordings/"), ("releases", "/recordings/")]:
    os.makedirs(os.path.join(SITE, old), exist_ok=True)
    open(os.path.join(SITE, old, "index.html"), "w").write(
        f'<!doctype html><meta charset="utf-8"><title>Gabriel Brady</title>'
        f'<link rel="canonical" href="https://gabrielbradymusic.com{new}">'
        f'<meta http-equiv="refresh" content="0; url={new}">\n')
