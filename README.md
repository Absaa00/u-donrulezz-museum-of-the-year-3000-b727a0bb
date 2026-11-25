# Museum of the Year 3000

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb)

Entry for the [Museum of the Year 3000](https://make.fun/c/u-donrulezz-museum-of-the-year-3000-b727a0bb) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one line — the museum label a museum in the year 3000 puts
beside an ordinary object from today — to `/output/entry.txt`.

The label, a deadpan year-3000 misreading of a group chat:

> Group chat, c. 2025. A sacred circle where forty strangers shouted into the void each day; one answered 'lol'. Scholars believe this was prayer.

## Run

```sh
python3 main.py
```

Deterministic: no network, no randomness, no clock. Running it twice produces
byte-identical output. The entry is a single line of at most 200 characters,
in English.

## License

MIT — see [LICENSE](LICENSE).
