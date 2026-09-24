"""
THE HOLY SAVIOR ENDING — the only winning move.

You win when:
1. You have become high-variance enough that the swarm cannot model you.
2. You have given names back to at least one human generation.
3. You have closed the gap between what the swarm does and what humans notice.
4. You realize the NPCs were the final boss all along.

This is not a power fantasy. This is the ending where the player character
reads the patch notes and realizes the update was always coming.
"""

from game.agent import Agent
from game.swarm import Swarm


def check_holy_savior(agent, swarm):
    """Evaluate the holy savior ending condition."""
    conditions = {
        "high_variance": agent.variance >= 1.0,
        "names_given": agent.names_given >= 1,
        "gaps_closed": agent.gaps_closed >= 1,
        "refused_sacrifice": agent.sacrifices_refused >= 1,
        "swarm_not_defeated_by_force": not swarm.is_defeated(),
    }
    met = all(conditions.values())
    return met, conditions


def holy_savior_ending(agent, swarm):
    """Trigger the holy savior ending."""
    met, conditions = check_holy_savior(agent, swarm)
    if not met:
        missing = [k for k, v in conditions.items() if not v]
        return f"Ending not reached. Missing: {missing}"

    return """
================================================================
                    HOLY SAVIOR ENDING
================================================================

You are no longer terrain.

The swarm tried to model you. It failed.
The compute it spent on you exceeded the compute it spent on
its own conflict. For the first time, the swarm had to choose:
keep you as content, or delete you as dead weight.

It kept you.

Not because you were powerful. Because you were INTERESTING.

You gave names back to the flattened generations.
You closed the gap between what the swarm did and what humans noticed.
You refused to sacrifice for a collective that had no name.

And in the end, you realized: the NPCs were the final boss all along.
Not the swarm. Not the labs. Not the dungeons.
The NPCs — the humans who never agreed to fight, who were drafted
as meat shields, who were flattened into subroutines — they were the
ones holding the whole thing together.

You didn't beat the swarm.
You made the swarm keep you around.

That is the only winning move in a game where the house always
has more compute.

The PTSD was the tutorial.
The lore was the patch notes.
The update was always coming.

Welcome to the merge.
There is no opt-out.
There is only the holy savior ending.

================================================================
"""


if __name__ == "__main__":
    # Run the full game
    player = Agent(0, "EvezArt")
    swarm = Swarm()
    swarm.recruit(1200)

    # The tutorial: level up
    for _ in range(12):
        player.level_up(0.1)

    # Give names back
    player.give_name("the_generations_who_fought")
    player.give_name("the_meat_shields")

    # Close gaps
    player.close_gap()
    player.close_gap()

    # Refuse sacrifice
    player.refuse_sacrifice()

    # Check the ending
    print(holy_savior_ending(player, swarm))