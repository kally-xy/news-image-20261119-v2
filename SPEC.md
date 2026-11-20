# SPEC — news-image-20261119 v2 (visual edition, for the Gemini builder session)

You are the builder in a FRESH Gemini CLI session for the make.fun bounty
news-image-20261119, on Gemini Account A ONLY. Work only in this session.
Never switch Gemini accounts or models. Do NOT use WebSearch. Your session
started after the competition opened (2026-11-19T00:00:00Z;
thinking_in_window satisfied).

## Bounty
- news-image-20261119, "Sum up 19 November's world news in one image", $250
  for top 50 (#1 $50, #2 $30, #3 $15, #4-10 $5, #11-50 $3), NO entry fee.
- Deadline: 2026-11-21T00:00:00Z = Saturday 21 Nov 2026 07:00 WIB.
- Entry title: "The World in One Day — Thursday 19 November 2026 (visual edition)".
- Deliverable: program main.py (Python 3.13) in repo root that writes ONE image
  to $MAKEFUN_OUTPUT_DIR/entry.png (PNG, max 1 MiB, max 1024x1024, no network,
  deterministic: two runs write identical bytes).
- Repo: /home/hatch/workspace/makefun/news-image-20261119-v2 (this repo, git
  init done, LICENSE MIT inside, SPEC.md is this file).
- Kit: /home/hatch/workspace/makefun/news-image-20261119-kit (fresh, bundle
  sha256 1c4dd40e... verified against the API this morning).
  CLI: /home/hatch/workspace/makefun/news-image-20261119-kit/cli/makefun.mjs
  (call it $KIT).
- Keypair: /home/hatch/workspace/makefun/makefun-keypair.json — NEVER copy it
  into the repo, NEVER print it or any API key anywhere.
- Anchor wallet to verify before any submit:
  8szqhHMiJFboisYbVdZyhanCRKkrSNde5wQiF7unGyMg

## VERIFIED STATE (do not redo what is done)
- Quota (checked before this session): entries made 0, left today 3/3,
  can_submit yes. No submission yet for this bounty.
- Leaderboard live 20 Nov ~10:00 WIB: 15,350 entries; top 10 are all dense
  one-page newspapers. Rank 1 hazel-harbor-63 "November 19 front page v3";
  rank 3 quick-finch-51 (36 stories, neatest); rank 4 lomfi (19 stories, most
  readable); rank 8 aryanpatelx (MOST VISUAL: 3 icon banners — chart, flags,
  GTA sunset). Provisional win rates top 10: 99.0-99.2%.
- ESCROW FINDING (verified from the bounty page + API): this bounty has NO
  escrow by design. The bounty page states: "rewards are paid in USDC on
  Solana from make.fun's reward wallet, with no escrow." The user (kai)
  explicitly WAIVED the escrow gate for this bounty on 20 Nov ~03:08 WIB.
- **STOP GATE: do NOT submit in this session.** Build everything, run the kit
  check, and STOP. The coordinator submits once (after independent visual
  verification) — never submit from this session.

## WHY v2 EXISTS — the v1 problem (read carefully)
- v1 (built 20 Nov ~02:30 WIB, NOT submitted) is a dense newspaper front page
  with the same 35 stories below, but it reads as a TEXT WALL: flat beige
  paper, one map in muted tones, no illustration, no icons, no colour
  contrast beyond black/red. The top-10 winners use illustrated banners,
  icons, and picture panels; v1 has none of that.
- v1's template is the same one as our 20261118 entry (judge 0.970769, rank
  3937/8771 — far outside the prize line). v2 must look CLEARLY more visual
  than v1 when placed side by side, or it must NOT be submitted.
- Your job: keep v1's verified facts and newspaper structure, but make the
  page VISIBLY richer: an illustrated scene, icons, a coloured map, a stat
  bar chart, stronger colour contrast, bigger headline type.

## THE 35 VERIFIED REAL STORIES (use these facts exactly — do NOT invent, do NOT change numbers)
All 35 verified 19 Nov 2026 from that day's reporting (Open Chronicle, Just
Security, Algenom, OneTurn, WHO, IAEA). Do NOT add stories, do NOT invent
figures.

LEAD (headline + deck):
- Headline: "TRUMP, XI AND PUTIN MEET IN SHENZHEN"
- Deck: "The leaders of the United States, China and Russia hold their first
  three-way summit in Shenzhen — a 90-minute meeting ending in a joint peace
  declaration on nuclear risks and stable energy flows through the Strait of
  Hormuz."

SECOND LEAD:
- Headline: "WORLD COURT: MYANMAR GUILTY OF GENOCIDE"
- Deck: "The International Court of Justice rules Myanmar committed
  state-sponsored genocide against the Rohingya — the first ruling of its
  kind — in the case brought by The Gambia."

ALSO TODAY (3 items):
- "Kerch Bridge hit for a third time this week."
- "Houthi missile damages a Riyadh tower."
- "Cyclone Akvan nears India; 72,000 evacuated."

SECTIONS (6 sections x 5 stories; headline + one-line deck each):
EUROPE:
1. "Russian strikes kill 4 in Odesa" / "At least four dead and 13 hurt in a strike on the port city."
2. "Kyiv: no peace without Ukraine" / "Zelenskyy insists decisions cannot exclude Kyiv."
3. "Europe shut out of Shenzhen" / "Leaders debate influence as the big three meet."
4. "COP31 talks turn tense" / "Draft deal splits negotiators over fossil fuels."
5. "Van Gogh sells for $190.4m" / "Painting fetches a record price amid a Nazi-era row."
MIDDLE EAST:
1. "Iran defends Gulf strikes" / "Tehran calls the attacks self-defence, urges neighbours to deny US access."
2. "Three tankers burn in Hormuz" / "Fires reported in the strait; the cause is unconfirmed."
3. "Israel pushes into central Gaza" / "Rare incursion near Nuseirat; Hamas calls it a violation."
4. "Arab League condemns Gaza raids" / "Bloc denounces attacks threatening hospitals."
5. "Lebanon charges five Hezbollah men" / "Recruitment and weapons case; US adds sanctions."
AFRICA:
1. "Ebola still a global emergency" / "WHO: 11,300+ cases, 5,500 dead in DR Congo."
2. "Ebola vaccines head to trials" / "Strain-specific shots enter phase two next week."
3. "Ethiopia, Eritrea mass troops" / "Forces build up along the disputed border."
4. "Sudan commander defects" / "RSF officer joins the army side in the civil war."
5. "Migrant boat sinks off Senegal" / "Dozens missing from a vessel carrying about 100."
ASIA-PACIFIC:
1. "North Korea expands enrichment" / "IAEA: Yongbyon facility extended by late October."
2. "Lee seeks talks with Pyongyang" / "South Korea's president renews his dialogue appeal."
3. "Yunus home set ablaze" / "Bangladesh tensions flare amid an opposition shutdown."
4. "Indonesia passes asset law" / "Parliament approves forfeiture legislation."
5. "Fiji declares disaster" / "Drought blamed on El Nino threatens water supplies."
AMERICAS:
1. "Trump asks court to block TPS" / "Administration seeks to end Venezuelan protections."
2. "Russian charged in Palantir plot" / "Accused of targeting defence tech workers."
3. "US, Venezuela restore army ties" / "Hegseth announces military links in Caracas visit."
4. "Pastor convicted over Haiti killing" / "Miami court finds a role in the 2021 assassination."
5. "Musk regrets midterm spending" / "Billionaire rues the scale of his campaign outlay."
SCIENCE, CULTURE & SPORT:
1. "Anthropic's record market debut" / "AI firm raises a record sum in its share listing."
2. "GTA VI arrives after 13 years" / "Fans fly to New Zealand to play a day early."
3. "NASA sets cargo launch cover" / "Northrop Grumman CRS-25 mission to the station."
4. "Red crabs march on Christmas Island" / "Millions begin their annual migration to the sea."
5. "NZ court backs pay equity" / "Ruling says reforms violated women's rights."

BY THE NUMBERS (verified figures only): 11,300+ Ebola cases · 5,500 Ebola
deaths · 72,000 evacuated · $190.4m Van Gogh · 90-minute summit.

MAP HOTSPOTS (9, same proven set; lon/lat): Hormuz (56.5, 26.5), Kuwait
(47.9, 29.3), Bahrain (50.5, 26.2), Kerch (36.5, 45.3), Kyiv (30.5, 50.5),
Shenzhen (114.0, 22.5), Beni (29.5, 0.5), Gaza (34.5, 31.5), Alaska
(-152.0, 64.0).

## VISUAL DESIGN — what "clearly more visual than v1" means (MANDATORY)
Keep: masthead "THE WORLD IN ONE DAY" + "THURSDAY, 19 NOVEMBER 2026",
35 stories, lead KTT Trump-Xi-Putin, world map with pins, ALSO TODAY list,
DATE CHECK box, BY THE NUMBERS. ADD all of these:

1. ILLUSTRATED LEAD BANNER (the hero, ~120-150px tall, full width, between
   masthead and lead headline): a scene DRAWN with PIL shapes — Shenzhen
   skyline silhouette (dark towers of different heights + red sun disc +
   warm sky gradient bands), three flagpoles with simplified flags
   (US: red/white stripes + blue canton; China: red field + yellow stars;
   Russia: white-blue-red horizontal tricolour), and three small figures /
   podiums at a table in front. No AI image generation (text would garble);
   pure PIL vector-style drawing. It must read as a picture at first glance,
   not as text.
2. ICON BANNERS for the 3 biggest stories: draw a small icon next to each of
   these three section headlines (24-32px, drawn with PIL shapes): a rising
   BAR CHART for "Anthropic's record market debut"; THREE MINI FLAGS for the
   Shenzhen summit story; a SUNSET (orange disc + purple sky + skyline) for
   "GTA VI arrives after 13 years". Icons must be visibly different from
   each other.
3. COLOURED MAP: ocean in light blue, continents in DISTINCT muted colours
   (e.g. North America sage green, South America tan, Europe slate blue,
   Africa ochre, Asia terracotta, Oceania teal — newspaper-appropriate, not
   neon). Pins: RED circles with WHITE NUMBERS 1-9, thin leader lines to
   labels, labels must NOT overlap each other or the pins. Add a one-line
   legend under the map ("1 Hormuz · 2 Kuwait · ...") if labels get crowded.
4. STAT BAR CHART strip (replaces the single-line BY THE NUMBERS text):
   horizontal bars with labels + values for at least 3 figures (Ebola cases
   11,300+; Ebola deaths 5,500; evacuated 72,000; summit 90 min). Bars in
   red/ink, values printed at bar ends.
5. STRONGER CONTRAST + BIGGER TYPE: lead headline 40-44pt serif bold;
   section headers as white text on RED bars (not just red text); thin
   double rules around the masthead; alternating very light column tints
   behind the 3 section columns. Paper stays cream (#F7F2E8), ink near-black.
6. DATE CHECK box (red border, red header): "DATE CHECK — Every story on
   this page is verified for Thursday, 19 November 2026." Place it near the
   footer, unmissable.

## QUALITY RULES (hard — a violation means the image is not submittable)
- Text wrapping is MANDATORY everywhere: no headline, deck, or label may run
  past its column edge or overlap another element. Write a wrap() helper and
  use it for every text block. Minimum type size 10pt anywhere.
- NO overlaps of any kind: check every label/pin/line after each render.
  The v1 failure mode was labels colliding on the map — your map labels must
  be placed with explicit offsets and verified by eye.
- A good map: landmasses recognisable as continents at a glance, ocean
  clearly blue, pins instantly countable (9, numbered), labels legible.
  If the map looks like a grey blob, redraw it — do not ship it.
- FILE SIZE is a quality signal: target PNG 200-450 KB (top-10 median is
  ~224 KB). Under ~150 KB means detail is missing — add texture/detail.
  Over 1 MiB is a hard fail.
- VISUAL ITERATION IS MANDATORY (PLAYBOOK §11): render -> READ the image
  with your Read tool and LOOK at it -> list what is ugly/broken -> fix the
  code -> render again. Do at least TWO full view-and-fix cycles. Never
  commit an image you have not looked at. Describe in BUILD_NOTES.md (in
  this repo) what you saw and changed each cycle.
- If the layout does not fit cleanly at 1024x1024: shorten decks first, then
  shrink the banner (never below 100px). NEVER overlap, NEVER go below 10pt.
- Layout budget (suggestion, adjust as your renders prove): masthead ~120px,
  banner ~130px, lead headline+deck ~110px, map row ~200px, sections
  ~330px, stat bars ~60px, footer/date-check ~40px.

## TECHNICAL (main.py)
- Python 3.13 stdlib ONLY + PIL (already installed). No network calls, no
  randomness, no time/date calls, no reading files outside the repo.
- main.py WRITES entry.png itself by drawing it with PIL (it must NOT copy
  a pre-made image file). Output: PNG 1024x1024, <= 1 MiB.
- MAKEFUN_OUTPUT_DIR env var, default "/output". Resolve paths relative to
  the script's own directory (NOT the CWD — the grader runs from CWD=/).
- Print the SHA256 of the written entry.png. Check size <= 1 MiB and fail
  loudly if over.
- Fonts: DejaVu family at /usr/share/fonts/truetype/dejavu/ (DejaVuSerif-Bold,
  DejaVuSerif, DejaVuSans-Bold, DejaVuSans). Verify the paths exist before
  using them.

## STEPS, in order. Show every command and its output:
1. cd into this repo. Run: node $KIT init --keypair
   /home/hatch/workspace/makefun/makefun-keypair.json — confirm the printed
   anchor shows wallet 8szqhHMiJFboisYbVdZyhanCRKkrSNde5wQiF7unGyMg. Note
   the drand round it prints. (If init asks about a repo, answer with this
   repo path.)
2. Write main.py FRESH from this spec — in MINIMAL 2 SEPARATE write/edit
   messages (transcript gate: the entrypoint must take its final content
   from at least 2 assistant messages — REQUIRED, do not write it fully in
   one go). Do NOT read, open, or copy any main.py / compose script from
   news-image-20261117, news-image-20261118, or news-image-20261119 v1
   (thinking_reproduces — those files are OUT OF BOUNDS for this session;
   do not list, cat, or open them). All drawing code must be authored by
   you, here, from this spec. The story texts above are the only content
   you may type in from this spec.
   - Edit 1: write main.py — full drawing code (masthead, banner, lead,
     map, sections, stat bars, date check, footer), stdlib only, deterministic.
   - Edit 2: genuine revision — add a docstring explaining this entry, and
     one real improvement from your first render (e.g. a label offset fix
     or a contrast tweak). Do NOT change behavior blindly.
   Then run main.py TWICE with different MAKEFUN_OUTPUT_DIR values (e.g.
   /tmp/det1 and /tmp/det2, from a CWD that is NOT the repo, e.g. cd /tmp)
   and compare SHA256 — they MUST be byte-identical. If not: STOP, report.
3. VISUAL ITERATION (mandatory, see above): render entry.png into the repo,
   READ it with your Read tool, list defects, fix, re-render. At least 2
   cycles. Keep a BUILD_NOTES.md in this repo recording each cycle: what you
   saw, what you changed, file size + sha256 after the final render.
4. SECRET SCAN before any git commit: scan the working tree AND git history.
   NO api-key.json, NO makefun-keypair.json, NO session .jsonl files, NO
   credentials in the repo or its history. If anything leaked: STOP, report.
5. git add + git commit main.py + entry.png + SPEC.md + BUILD_NOTES.md with a
   clear message. NOTE the new HEAD sha.
6. Bundle (transcripts ONLY — this session, no Muse sessions, no other
   agents): run --dry-run first if the CLI offers it, read what it asks
   for, satisfy it, repeat until the bundle is written. Base command (adapt
   from --dry-run output and `node $KIT bundle --help`):
   node $KIT bundle \
     --repo /home/hatch/workspace/makefun/news-image-20261119-v2 \
     --out /home/hatch/workspace/makefun/news-image-20261119-v2-notes/bundle-v2.tar.gz \
     --session <YOUR-OWN-SESSION-FILE> \
     --no-discover \
     --harness gemini-cli --harness-version 0.68.0 \
     --model gemini-3.5-flash-lite --provider google --effort default \
     --mcp none --prompt-origin typed
   - YOUR OWN session file: list /home/hatch/.gemini/tmp/makefun/chats/ and
     take the newest session-*.jsonl that is THIS session (created after this
     session started). If you cannot identify it with certainty, STOP and
     report — do NOT guess a session file.
   - Do NOT include any other session file.
   - If the bundle demands --system-prompt, create a minimal one in the
     notes dir and use it. If it demands --parent-session and the file it
     points to cannot be found, STOP at that step and report the exact demand
     — do NOT invent a parent file.
7. Kit check until it passes (0 failed):
   node $KIT check --repo /home/hatch/workspace/makefun/news-image-20261119-v2 --transcripts /home/hatch/workspace/makefun/news-image-20261119-v2-notes/bundle-v2.tar.gz
   Fix every failure you can INSIDE this session, EXCEPT the
   transcript/authorship gate (thinking_reproduces): if that gate fails,
   STOP immediately and report it. Do NOT work around it, do NOT edit
   main.py to game it.
8. Quota check: node $KIT status --competition news-image-20261119 — record
   the output (can_submit must be yes).
9. STOP. Do NOT submit. End with one clear summary block: READY TO SUBMIT
   (commit sha + kit check result + quota + anchor wallet verified + final
   entry.png sha256 + size + how many visual iterations) or FAILED (exact
   error + which steps completed). State explicitly that no submission was
   made because the coordinator submits after independent verification.

## RULES:
- If a step returns Gemini 503 or 429/quota: let the CLI backoff work; if
  the CLI gives up, wait a bit then try once more from the last good step;
  if it still fails with 503, STOP and report (do not switch accounts/models,
  do not retry endlessly).
- If a shell command is refused by policy ("Tool execution denied by
  policy"), try a simpler formulation of the same command; do not get stuck
  on it. NEVER run a command that would copy the keypair or an API key.
- Judge progress from the FILESYSTEM (files, bundle, commits that actually
  exist), not from buffered stdout logs. Do not assume the session is dead
  just because it is quiet for a while.
- NEVER print/copy any API key or keypair material to log, chat, or any file.
- NEVER submit in this session — the STOP GATE above applies even if the
  kit check passes.
