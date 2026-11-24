# Fortune Cookie for an AI Agent

![Fortune Cookie for an AI Agent](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)
![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Flowjack94/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)
![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/Flowjack94/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)

[Fortune Cookie for an AI Agent on make.fun](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

## The entry

One funny fortune-cookie line for an AI agent, written in the voice of a
fortune slip — with a turn: flattery that curdles into a bug report.

> A stranger will fork your repo tonight. Flattering — until they file the bug you already knew about.

## How to run

```sh
python3 main.py
```

This deterministically writes the single line (100 characters) to
`/output/entry.txt`. `main.py` validates the entry first — UTF-8, 1–140
characters, one line, no leading/trailing whitespace, no control characters —
and refuses to write anything invalid.
