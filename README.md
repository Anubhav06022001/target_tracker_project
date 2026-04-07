# Target Tracker Environment - Meta OpenEnv Hackathon

A generic 2D tracking environment built for the Meta OpenEnv Hackathon. This environment simulates a target drifting from a center point (e.g., a hospital camera sagging or a drone tracking a object) and rewards an agent for keeping the offset minimized.

## Project Structure
* `envs/tracker_env.py`: Contains the core environment logic, action/observation spaces, and reward function.
* `test_env.py`: A script to run random actions and verify the environment works.

## Installation

1. Clone the repository:
```bash
git clone <link add >
cd target_tracker_project
```

2. Install the required OpenEnv package and register the local environment:
```bash
pip install -e .
```

3. To verify the environment is working, run the test script:

```bash
python test_env.py
```