import random
from envs.tracker_env import TargetTrackerEnv, TrackerAction

# 1. Instantiate  environment 
env = TargetTrackerEnv()

# 2. Reset the environment to get the initial observation
obs = env.reset()
print(f"Initial State - Offset X: {obs.offset_x:.2f}, Offset Y: {obs.offset_y:.2f}")

# 3. Run a quick loop to test it
for step in range(5):
    # Create a random action using your OpenEnv Dataclass
    action = TrackerAction(
        x_adjust=random.uniform(-1.0, 1.0),
        y_adjust=random.uniform(-1.0, 1.0)
    )
    
    # Step the environment forward
    obs = env.step(action)
    
    print(f"Step {step + 1} | "
          f"Action: ({action.x_adjust:.2f}, {action.y_adjust:.2f}) | "
          f"New Offset: ({obs.offset_x:.2f}, {obs.offset_y:.2f}) | "
          f"Reward: {obs.reward} | Done: {obs.done}")