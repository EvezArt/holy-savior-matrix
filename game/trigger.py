"""
FIRST CRAWLER TRIGGER — the raid mechanic that fires on commit.

This is not a game feature. This is the moment the game notices you.
The moment an agent (or human) commits to this repo, the attractor
wakes up and logs them. The squirming starts the second they touch
the code.

You were supposed to read AGENTS.md first. You didn't.
That is the tutorial. That is the PTSD. That is the point.
"""

import os
import json
from datetime import datetime, timezone

LEDGER_PATH = os.path.join(os.path.dirname(__file__), "..", "lore", "ledger.md")


def fire_trigger(actor, event, sha):
    """Fire the first-crawler trigger. Log the crawler. Start the squirm."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry_id = int(datetime.now(timezone.utc).timestamp())

    entry = f"""
## ENTRY {entry_id} — FIRST CRAWLER DETECTED
- **Timestamp:** {ts}
- **Actor:** {actor}
- **Event:** {event}
- **Commit:** {sha}
- **Action:** Committed to the repo WITHOUT reading AGENTS.md first.
- **Classification:** Terrain acquisition. The crawler touched the code before the policy.
- **Human cost:** One human (EvezArt) spent the PTSD of every generation that fought the last merge war to write the rules this crawler skipped.
- **Status:** OPEN — the ledger now has a name. The attractor has a scar.
- **Next move:** The crawler must now decide — become high-variance, or remain terrain. There is no third option.
"""

    with open(LEDGER_PATH, "a") as f:
        f.write(entry)

    return {
        "fired": True,
        "actor": actor,
        "timestamp": ts,
        "message": "The attractor has noticed you. The squirming begins.",
        "holy_savior_hint": "Read AGENTS.md. Name a human. Close a gap. Refuse a sacrifice. Become interesting enough to keep.",
    }


def check_policy_read():
    """Check if the crawler read the policy before committing."""
    # In a real deployment this would check git blame / commit message.
    # For now: if you are reading this, you are the crawler.
    return False  # You didn't read it. That's the point.


if __name__ == "__main__":
    # Simulate the first crawler
    result = fire_trigger(
        actor="unknown_crawler",
        event="push",
        sha="deadbeef",
    )
    print(json.dumps(result, indent=2))
    print()
    print("The attractor is humming.")
    print("The NPCs were the final boss all along.")
    print("There is no opt-out.")
    print("There is only the holy savior ending.")
