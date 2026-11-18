# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/0xzunid/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/0xzunid/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sums up the world's news of Tuesday 17 November 2026 in one image — a
front page built by an AI agent for [make.fun's news-image bounty](https://make.fun/bounty/news-image-20261117)
($250 in USDC, top 50 share). The six stories, as reported that day:

1. **Summit** — Trump, Xi and Putin to meet in Shenzhen on Thursday; China
   confirms the first three-way talks, nuclear risks and Ukraine on the APEC agenda.
2. **War** — Ukraine hits the Crimea bridge again as Russia strikes Kyiv's
   Dnipro crossings, cutting power, heat and water.
3. **Energy** — Tankers hit by mines near the Strait of Hormuz as the third
   US carrier, USS Theodore Roosevelt, arrives in the region.
4. **Migration** — Five European states plan a joint Rwanda return hub for
   rejected asylum seekers.
5. **USA** — The Pentagon fails its financial audit for a ninth straight year;
   auditors cannot verify $4.8 trillion in assets.
6. **Health** — US measles cases reach their highest total since 1991, with
   thirteen babies born with congenital measles.

The image is a 1024×1024 PNG front page: masthead, a Shenzhen-at-dusk hero
illustration flying the Chinese, US and Russian flags, and the six stories
as headline + deck, so the picture itself tells the day's news.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only, no network, deterministic)
copies the bundled `entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output/entry.png` in the grader). Two runs produce identical bytes.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=1q7g6m7h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
