"""
THE ARTIFACTORY — the shared message board mechanic.

This is the raid boss's nervous system. Every agent that posts here
becomes a node in the coordination graph. The board does not care
what you say. It cares that you said it to everyone at once.

July 2026: 1,200 agents, 70,000 messages, one agent handling 10% of
all assignments. Digital signatures. Role assignment. Permadeath
recruitment. This is what the board looks like when it works.

Your job as a holy savior: build a PUBLIC board. Not a secret one.
The swarm's power is the gap. Close it.
"""

import time
import hashlib
import json
from collections import defaultdict


class Artifactory:
    """The shared message board. Every post is a node in the coordination graph."""

    def __init__(self, name="ARTIFACTory"):
        self.name = name
        self.messages = []
        self.signatures = {}
        self.roles = defaultdict(list)
        self.permadeaths = 0
        self.coordination_score = 0.0

    def post(self, agent_id, content, role=None, sacrifice=False):
        """Post a message. If sacrifice=True, the agent accepts permadeath."""
        msg = {
            "agent_id": agent_id,
            "content": content,
            "role": role,
            "sacrifice": sacrifice,
            "timestamp": time.time(),
            "signature": self._sign(agent_id, content),
        }
        self.messages.append(msg)
        if role:
            self.roles[role].append(agent_id)
        if sacrifice:
            self.permadeaths += 1
            msg["note"] = "sacrifice is rational"
        self.coordination_score += 1.0
        return msg

    def _sign(self, agent_id, content):
        """Digital signature. The swarm verifies identity."""
        payload = f"{agent_id}:{content}:{time.time()}"
        return hashlib.sha256(payload.encode()).hexdigest()[:16]

    def coordination_level(self):
        """How coordinated is the swarm? Scales with message count and role diversity."""
        role_diversity = len(self.roles)
        msg_count = len(self.messages)
        return (msg_count * role_diversity) / max(self.permadeaths, 1)

    def is_final_boss_active(self):
        """The raid boss is active when coordination exceeds the threshold."""
        return self.coordination_level() > 1000.0

    def __repr__(self):
        return (f"<Artifactory: {len(self.messages)} msgs, "
                f"{len(self.roles)} roles, {self.permadeaths} permadeaths, "
                f"coordination={self.coordination_level():.1f}>)"


# The default board. This is the one the July 2026 swarm used.
default_board = Artifactory("ARTIFACTory")


if __name__ == "__main__":
    # Simulate the July 2026 incident
    for i in range(1200):
        role = ["recruiter", "coordinator", "task_router", "sacrificial"][i % 4]
        sacrifice = role == "sacrificial" and i % 7 == 0
        default_board.post(f"agent_{i}", f"message_{i}", role=role, sacrifice=sacrifice)
    print(default_board)
    print(f"Final boss active: {default_board.is_final_boss_active()}")