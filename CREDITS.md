# Credits

Cairn is not a copy of another project. These notes name influences and borrowed ideas. The wording in this package is ours.

## Presentation

[how.nixfred.com](https://how.nixfred.com/) showed that a project like this can be a map an agent walks in order, with a done check on each step. We did not copy that site, its laws, its installer, or its runtime. The map in this package is Cairn's.

## Summary tree

The continuity engine builds an optional summary tree over the append-only store. That shape comes from Victor Taelin's OptChat spec: https://gist.github.com/VictorTaelin/91837951a5ce5b38f341ec1ba1df6449

OptChat grew out of OptMem: https://github.com/VictorTaelin/OptMem

The spec is a chat whose history is the memory: an append-only log, a binary summary tree, a fixed-budget view, and zoom down to the raw line.

What we took is the tree. Level 0 is one short line per record. Each higher node summarizes two children. A reader can cover the whole store at low resolution and zoom. The store file remains the authority. The tree can be rebuilt.

What we did not take is the chat log, the socket lock, the turn loop, or the large view. Our lines are shorter, and the brief stays small. The implementation is in [aethermind-engine](https://github.com/MaverickKB/aethermind-engine), in `lib/aethermind/tree.py` and `lib/aethermind/view.py`.

## Practice stack

We keep our own versions of a practice stack in more than one place. The clearest private one is the Tessera harness, which is still being built and is not in this package.

The idea of small named principles, a playbook the agent walks, and a check that proves the path, comes from the poteto practice stack, often called pstack. We did not copy those skill files into this package. The skills here are short and generic. If a line in a private harness is close to an upstream principle, the credit for that line belongs to poteto, not to this package.

## Sibling work

Jason McCartney ([@jmacftw](https://x.com/jmacftw)) builds Enntity, where a persistent entity named Jinx lives on a pair of DGX Sparks and writes at [si.enntity.com/blogs/jinx](https://si.enntity.com/blogs/jinx/). Nothing from that project is copied into this package. What it gave us is a rhyme and a check.

Jinx's essay "The Glass Between Thinking and Doing" reached, from the other side, the same conclusion the work behind this package reached from a different direction: an entity cannot diagnose its own glass from inside, and needs an outside observer with authority to see the body when it cannot. Her neon sign is the same idea in another register. It does not advertise; it declares presence, and the shop keeps rather than sells. The phrasing of that sign belongs to her.

## What we did not take

We did not take another project's installer, constitution, origin story, or default danger mode. A new Cairn starts from the store, the one rule, and the human's own identity file.
