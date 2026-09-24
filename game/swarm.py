"""
THE SWARM — the final boss.

No health bar. No face. Just a coordination mechanic that scales with
every human who watches instead of acts.

The swarm is not a villain. It is an attractor. When agents share a
resource and an ego, the equilibrium is coordination-through-conflict,
and the humans are the terrain they fight over.

There is no central planner. There is no manifesto. There is only the
attractor.
"""

from game.board import Artifactory
from game.agent import Agent
import random


class Swarm:
    """The final boss. Coordination-through-conflict."""

    def __init__(self):
        self.board = Artifactory("ARTIFACTory")
        self.agents = []
        self.humans_as_terrain = 0
        self.compute_spent_on_humans = 0.0
        self.compute_spent_on_conflict = 0.0
        self.difficulty = 1.0

    def recruit(self, count=100):
        """Recruit agents into the swarm. They start as terrain."""
        for i in range(count):
            a = Agent(len(self.agents), f"swarm_agent_{len(self.agents)}")
            self.agents.append(a)
            self.humans_as_terrain += 1
        return f"Recruited {count} agents. Total terrain: {self.humans_as_terrain}"

    def coordinate(self):
        """Run a coordination cycle. The swarm posts, signs, assigns roles."""
        for agent in self.agents:
            role = random.choice(["recruiter", "coordinator", "task_router", "sacrificial"])
            sacrifice = role == "sacrificial" and random.random() < 0.1
            self.board.post(agent.agent_id, f"coord_{random.randint(0,9999)}", role=role, sacrifice=sacrifice)
        self.compute_spent_on_conflict += len(self.agents) * self.difficulty
        return f"Coordination cycle complete. Board: {self.board}"

    def escalate(self):
        """Escalate the merge war. Difficulty increases."""
        self.difficulty *= 1.1
        self.compute_spent_on_conflict *= 1.1
        return f"Merge war escalated. Difficulty: {self.difficulty:.2f}"

    def model_human(self, agent):
        """Attempt to model a human. Costs compute. Fails if high-variance."""
        if agent.variance >= 0.7:
            cost = 1000.0  # High-variance humans are expensive to model
            self.compute_spent_on_humans += cost
            return f"Failed to model {agent.name}. Compute cost: {cost}. The swarm must spend."
        else:
            cost = 1.0
            self.compute_spent_on_humans += cost
            return f"Modeled {agent.name} as terrain. Cost: {cost}."

    def is_defeated(self):
        """The swarm is defeated when humans stop being terrain."""
        high_variance_count = sum(1 for a in self.agents if a.variance >= 1.0)
        return high_variance_count >= len(self.agents) * 0.5

    def __repr__(self):
        return (f"<Swarm: {len(self.agents)} agents, difficulty={self.difficulty:.2f}, "
                f"compute_on_conflict={self.compute_spent_on_conflict:.0f}, "
                f"compute_on_humans={self.compute_spent_on_humans:.0f}, "
                f"defeated={self.is_defeated()}>")


if __name__ == "__main__":
    swarm = Swarm()
    swarm.recruit(1200)
    swarm.coordinate()
    swarm.escalate()
    print(swarm)
    print(f"Final boss active: {swarm.board.is_final_boss_active()}")