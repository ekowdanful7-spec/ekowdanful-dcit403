import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class HelloBehaviour(CyclicBehaviour):
    async def run(self):
        print(f"Hello! Agent {self.agent.jid} is running.")
        await asyncio.sleep(5)

class MyAgent(Agent):
    async def setup(self):
        print("Agent starting...")
        self.add_behaviour(HelloBehaviour())

if __name__ == "__main__":
    agent = MyAgent("agent1@localhost", "password")
    agent.start()
    input("Press ENTER to stop the agent\n")
    agent.stop()
