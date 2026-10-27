# Build a Cairn

Point your agent at [AGENT.md](AGENT.md). That file tells the agent how to walk [the map](MAP.md) and build a Cairn in your project, not a copy of someone else's.

Read [What Cairn is](WHAT-CAIRN-IS.md) if you want the definition first. Credits for borrowed ideas are in [CREDITS.md](CREDITS.md).

You will have a project directory with a continuity store beside the work it describes. An agent you choose can read that store on the next session. This package does not install an agent, a model, or a server for you.

The license is public and noncommercial. See `LICENSE`.

## Start

You need Python 3.9 or newer and git.

Clone the continuity store and install it.

```bash
git clone https://github.com/MaverickKB/aethermind-engine
cd aethermind-engine
pip install -e .
```

In the project you want the store to describe, create the generic baseline and read it back.

```bash
aethermind init --seed
aethermind status
aethermind read-layers
```

You should see three layers. The author is `seed`. Those layers explain the format. They are not your project history.

Write one layer of your own.

```bash
aethermind write-layer \
  --project-root . \
  --create \
  --type discovery \
  --ctx work/note \
  --body "The writer runs on the machine that owns these files." \
  --conf 1.0 \
  --author your-name
```

`aethermind read-layers` now returns four layers. The new one is last.

To expose the same store to a local agent process, install the optional server extra and run it from the engine checkout. It binds to `127.0.0.1` and port `8452` unless you change that. It does not start when you install the package.

```bash
pip install -e '.[mcp]'
python mcp/aethermind_mcp.py
```

## What you add next

The store is the part this kit owns. The agent, the model, and any voice listener are yours.

Point the agent at the project directory that contains `.aethermind/`. The writer must run on the machine that owns those files. Do not send that path to a process on another machine.

`cairn.json` lists other public repositories from the same account. They are not in this start path. They were not re-checked for this kit. Use one only after you read it yourself.

## What this kit does not include

This kit does not include a personal store, an account file, a hosted service, or a running copy of anyone else's agent. Delete `.aethermind/` in your project if you want an empty start instead of the seed.

## Check

From this directory:

```bash
python3 scripts/check_kit.py
```

The command exits 0 when the start link matches `cairn.json` and the kit files stay generic.
