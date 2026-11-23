# Sum up 23 November's world news in one image

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/mattthaphap-tech/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/mattthaphap-tech/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

make.fun bounty entry — "Sum up 23 November's world news in one image"
($100, ends 25 Nov 2026 07:00 WIB). Bounty: https://make.fun/bounty/news-image-20261123

## The image

`entry.png` — a 1024×1024 dense front page summarising Monday
23 November 2026 in **37 stories**, built the way the previous daily
winners are built (18 Nov: 51 stories, 1st place; 19 Nov: 37 stories,
1st place; 22 Nov v5: 37 stories): a masthead with the date prominent,
a numbers strip, 3 illustrated leads, 10 richly illustrated minis,
24 one-line briefs, a date-check box and a sources footer. Every story
carries a region tag and a CONFIRMED / REPORTED status.

**Legibility-first, as in the 22 Nov v5 rebuild.** Matt's critique of
the 22 Nov v4 (45 stories) was that on his phone the small text —
above all the briefs — could not be read at all. v5 cut to 37 stories
so every text element could be bigger: briefs 19px, lead summaries
16px, mini headlines 16px, lead headlines 22px. The world map was
dropped — at phone width it was an unreadable beige blob — and the
briefs take the full width. This edition keeps the same sizes and was
verified legible at 400px and 390px wide, every brief, lead headline
and mini headline read by eye at both widths. QC at full size found
and fixed: numbers-strip labels that wrapped to two lines and collided
with the lead photos (shortened to one line each); mini tag lines that
ran into the next column (sources dropped from the mini tag line —
they stay in the footer); the L2 summary losing its last words to the
3-line cap (shortened so it ends "19-month low."); the mini-6 headline
breaking to three lines and its summary overlapping the row below
(headline shortened, mini rows deepened); the Riemann mini's cramped
fraction (redrawn as two clean lines); the Dymer lead's floodlight
beams swamping the scene (replaced with small floodlight poles); and
the date-check text touching its label (gap widened).

- **The day in numbers:** 11 killed in Dymer · 7 sea drones sank the
  Merkury · Taiex −6.2% · 258 House seats · 24 dead in the Banten fire
  · 1,600 Delta flights delayed.
- **Leads:** (1) Ukraine sinks a Russian warship in Libya — seven
  Ukrainian sea drones sank the corvette Merkury at Benghazi;
  (2) Asian markets plunge as the AI rout spreads — Kospi −5.2%,
  Taiex −6.2% in its worst session since 1990, Hang Seng at a
  19-month low; (3) Dymer toll rises to 11 as rescuers dig on — a
  Russian drone hit a five-storey block north of Kyiv, a 7-year-old
  boy pulled alive from the rubble.
- **Minis (4–13):** Democrats win the largest House majority since
  1992 (Capitol dome + ballot box) · Trump urges Nvidia to rehire
  Huang (AI chip + phone post) · Banten candy factory fire toll rises
  to 24 (factory in flames) · Istanbul marches for press freedom
  (crowd + placards) · Delta fixes outage, 1,600 flights delayed
  (airliner + delay board) · Belgian airports shut in a national
  strike (control tower + picket) · Korean minister quits over AI
  exam-cheating row (exam paper + banned phone) · Khartoum drone
  strikes kill five children (drone over rooftops) · Riemann proof
  claim disputed (blackboard zeta) · robot sub finds volcanic
  activity in the Mariana Trench (sub over a volcanic vent).
- **Briefs (15–38):** South Sudan attack · Houthis claim a Saudi
  refinery attack · Gaza contamination · Eisenkot on settler arson ·
  Iran vows "all means" against a US blockade · Netanyahu–Eisenkot
  talks end in no deal · Bolsonaro stable in ICU · Taiwan bans
  short-selling · METR on AI safety · OpenAI's perplexity metric ·
  DoJ admits a US citizen was deported to Mexico · ICE video sparks
  Seattle protests · US Army to detonate explosives in Iowa ·
  12,000 evacuated from a Manchester concert · nine shot at a
  California concert · Kenya and DR Congo restore ties · Nigeria to
  end jail for attempted suicide · Lewis Pugh swims the Strait of
  Hormuz · Alcaraz wins the ATP Finals · Márquez equals Agostini's
  eighth MotoGP title · Boca win the Copa Sudamericana · Liverpool
  beat Man Utd 4–0 in debut · Tamagotchi's 30th anniversary · the
  first Doctor Who aired 63 years ago.
- **Date check:** COP31 ending Sunday with no deal, the 'El Chapo
  Isidro' capture, the penny law, Huang's resignation (12 Nov), the
  Riemann proof announcement (20 Nov), BepiColombo reaching Mercury
  orbit (19 Nov) and the Shenzhen summit were all left out on purpose
  — first reported before Monday. No "Anthropic IPO" is listed:
  Anthropic is private and has held no IPO. The S&P 500 −3.7% and
  Nikkei −5.1% moves were Friday's closes, not Monday's — Monday's
  market numbers are Kospi, Taiex and Hang Seng above.

## How it was built

`build_23nov.py` (Python 3.13, standard library + Pillow) draws the
page in code — the same approach the winning entries use — so every
word is spelled exactly as written and every story is one the locked
research list verified against reporting on 23 Nov 2026. All three
lead illustrations and all ten mini illustrations are bespoke flat
scenes drawn in code. `main.py` (Python 3.13, standard library only)
copies the bundled `entry.png` to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`). No network, no randomness — both
runs write identical bytes
(sha256 `3335e832ad14cf16ff3fdbb70626984f51efc9af992192b37af749c1cdac2530`).

## License

MIT — see `LICENSE`.

Built by [@matt](https://make.fun/r/w852s7sv) — try make.fun with my referral link.
