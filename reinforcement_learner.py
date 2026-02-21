from ray.rllib.agents.ppo import PPOTrainer

class ReinforcementLearner:
    def __init__(self, neural_network, knowledge_base):
        self.trainer = PPOTrainer