# Debate Crew

A CrewAI project that researches the day's hottest stocks across NYSE blue chips and NASDAQ growth names, then produces a combined markdown report.

## Agents

- **researcher** — searches the web (via `SerperDevTool`) for current stock news.
- **reporting_analyst** — turns the two research outputs into a single report.

## Tasks (run sequentially)

1. `nyse_research_task` → `output/nyse_research_task.md`
2. `nasdaq_research_task` → `output/nasdaq_research_task.md`
3. `reporting_task` → `output/report.md` (uses both research tasks as context)

## Setup

Requires Python 3.10–3.13 and [`uv`](https://docs.astral.sh/uv/).

```powershell
uv sync
```

Create `.env` in this folder:

```
MODEL=anthropic/claude-haiku-4-5
ANTHROPIC_API_KEY=sk-ant-...
SERPER_API_KEY=...        # free key at https://serper.dev
```

## Run

```powershell
crewai run
```

Outputs are written to `output/` (folder is created automatically).

## Configuration

- Agents: [src/debate/config/agents.yaml](src/debate/config/agents.yaml)
- Tasks: [src/debate/config/tasks.yaml](src/debate/config/tasks.yaml)
- Crew wiring: [src/debate/crew.py](src/debate/crew.py)
- Inputs (`topic`, `current_day`): [src/debate/main.py](src/debate/main.py)
