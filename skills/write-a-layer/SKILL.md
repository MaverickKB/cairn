---
name: write-a-layer
description: Use when a decision, correction, or real uncertainty should outlive the turn. Append one store record. Do not edit old records.
---

# Write a layer

Use this when a fact should still be true for the next session.

1. Confirm you are on the machine that owns the project files.
2. Read the store before you write, so you do not repeat a settled correction.
3. Append one record with the `aethermind` command or the library. Do not edit `layers.aem` by hand.
4. If you are correcting an older record, name its id. Leave the old record in place.
5. Read the new record back before you say it landed.

A greeting, a progress note, and a guess do not earn a record.

Done when the read-back shows the new id and the body you wrote.
