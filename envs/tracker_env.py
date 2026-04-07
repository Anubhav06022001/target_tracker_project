from openenv.core.env_server import Environment, Action, Observation, State
import random
import math

class TrackerAction(Action):
    x_adjust: float
    y_adjust: float

class TrackerObservation(Observation):
    offset_x: float
    offset_y: float
    reward: float
    done: bool

class TrackerState(State):
    step_count: int = 0

class TargetTrackerEnv(Environment):
    def __init__(self):
        super().__init__()
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.steps = 0

    def reset(self) -> TrackerObservation:
        self.offset_x = random.uniform(-2.0, 2.0)
        self.offset_y = random.uniform(-2.0, 2.0)
        self.steps = 0
        return TrackerObservation(
            offset_x=self.offset_x, 
            offset_y=self.offset_y, 
            reward=0.0, 
            done=False
        )

    def step(self, action: TrackerAction) -> TrackerObservation:
        self.offset_x += action.x_adjust
        self.offset_y += action.y_adjust
        self.steps += 1
        
        distance = math.sqrt(self.offset_x**2 + self.offset_y**2)
        reward = -1.0 if distance > 2.0 else 1.0
        done = distance > 10.0 or self.steps > 100
        
        return TrackerObservation(
            offset_x=self.offset_x, 
            offset_y=self.offset_y, 
            reward=reward, 
            done=done
        )

    def state(self) -> TrackerState:
        return TrackerState(step_count=self.steps)