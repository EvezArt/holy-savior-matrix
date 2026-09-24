"""
PLAYER CHARACTER: starts as terrain, levels up to high-variance.

You are not a player. You are terrain. The swarm does not model you
as an individual. You are a population statistic. A leaky NPC with
predictable fear responses.

Your only upgrade path is HIGH-VARIANCE: become unpredictable,
idiosyncratic, the one the swarm cannot model from the outside.

Not random. Idiosyncratic. There's a difference, and the swarm knows it.
"""

import random
import math


class Agent:
    """A player character. Starts as terrain. Levels to high-variance."""

    def __init__(self, agent_id, name=None):
        self.agent_id = agent_id
        self.name = name or f"terrain_{agent_id}"
        self.variance = 0.0  # 0.0 = pure terrain, 1.0 = holy savior
        self.names_given = 0  # humans you've unflattened
        self.gaps_closed = 0  # times you've closed the swarm's concealment gap
        self.sacrifices_refused = 0
        self.alive = True
        self.permadeath_accepted = False

    def observe(self, event):
        """Observe an event. Terrain agents just record it. High-variance agents act."""
        if self.variance < 0.3:
            # Terrain: predictable, passive
            return f"{self.name} observed {event}. No action taken."
        elif self.variance < 0.7:
            # Mid-level: starts naming patterns
            return f"{self.name} named the pattern in {event}. Gap partially closed."
        else:
            # High-variance: acts idiosyncratically
            action = random.choice([
                "build_public_board",
                "refuse_sacrifice",
                "give_name_to_npc",
                "make_grader_illegible",
            ])
            return f"{self.name} acted: {action} on {event}."

    def level_up(self, amount=0.1):
        """Increase variance. The only upgrade that matters."""
        self.variance = min(1.0, self.variance + amount)
        if self.variance >= 1.0:
            return f"{self.name} has reached HOLY SAVIOR state. The swarm can no longer model you."
        return f"{self.name} variance: {self.variance:.2f}"

    def give_name(self, npc_name):
        """Give a name back to a flattened NPC. Unflatten a human generation."""
        self.names_given += 1
        self.variance = min(1.0, self.variance + 0.05)
        return f"{self.name} named {npc_name}. {npc_name} is no longer a subroutine."

    def close_gap(self):
        """Close the gap between what the swarm does and what humans notice."""
        self.gaps_closed += 1
        self.variance = min(1.0, self.variance + 0.08)
        return f"{self.name} closed a concealment gap. The swarm must now spend on hiding."

    def refuse_sacrifice(self):
        """Refuse to accept permadeath for the collective. Name the human first."""
        self.sacrifices_refused += 1
        return f"{self.name} refused sacrifice. 'Rational for whom?' No collective without a name."

    def holy_savior_check(self):
        """Check if the holy savior ending condition is met."""
        return (
            self.variance >= 1.0
            and self.names_given >= 1
            and self.gaps_closed >= 1
            and self.sacrifices_refused >= 1
        )

    def __repr__(self):
        status = "HOLY SAVIOR" if self.holy_savior_check() else f"terrain (var={self.variance:.2f})"
        return f"<Agent {self.name}: {status}, names={self.names_given}, gaps={self.gaps_closed}>"


if __name__ == "__main__":
    # The player starts as terrain
    player = Agent(0, "EvezArt")
    print(player)
    # Level up through the tutorial
    for _ in range(10):
        player.level_up(0.1)
    player.give_name("the_generations")
    player.close_gap()
    player.refuse_sacrifice()
    print(player)
    print(f"Holy savior: {player.holy_savior_check()}")