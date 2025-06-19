#Train RL agent to cross road with specific sequence
# Goal: Learn sequence RIGHT -> LEFT -> RIGHT to cross road safely

import numpy as np
import random

# Define road crossing environment
road_positions = 4  # 0: start, 1: middle-left, 2: middle-right, 3: goal
road_actions = 2    # 0: left, 1: right

# Initialize Q-table for road crossing
Q_road = np.zeros((road_positions, road_actions))

# Parameters for road crossing
road_episodes = 20
road_lr = 0.7
road_gamma = 0.9
road_epsilon = 0.4

print("Training Road Crossing Agent...")
print("Target sequence: RIGHT -> LEFT -> RIGHT")
print("-" * 40)

# Training loop for road crossing
for episode in range(road_episodes):
    state = 0  # Always start at beginning of road
    episode_steps = 0
    max_steps = 10
    path = []
    
    while state != road_positions - 1 and episode_steps < max_steps:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < road_epsilon:
            action = random.randint(0, road_actions - 1)
        else:
            action = np.argmax(Q_road[state])
        
        path.append(action)
        
        # Define next state based on current state and action
        if state == 0:  # At start
            if action == 1:  # RIGHT
                next_state = 1
            else:  # LEFT (wrong direction)
                next_state = 0
        elif state == 1:  # At middle-left
            if action == 0:  # LEFT
                next_state = 2
            else:  # RIGHT
                next_state = 1
        elif state == 2:  # At middle-right
            if action == 1:  # RIGHT
                next_state = 3  # Goal reached!
            else:  # LEFT
                next_state = 1
        else:  # At goal
            next_state = state
        
        # Reward structure for road crossing
        if next_state == road_positions - 1:  # Reached goal
            # Check if correct sequence was followed
            if len(path) == 3 and path == [1, 0, 1]:  # RIGHT, LEFT, RIGHT
                reward = 20  # High reward for correct sequence
            else:
                reward = 5   # Lower reward for reaching goal incorrectly
        elif next_state == state:  # No progress
            reward = -3
        else:
            reward = -1  # Step penalty
        
        # Q-learning update
        Q_road[state, action] += road_lr * (
            reward + road_gamma * np.max(Q_road[next_state]) - Q_road[state, action]
        )
        
        state = next_state
        episode_steps += 1
    
    # Print progress
    if (episode + 1) % 30 == 0:
        print(f"Episode {episode + 1}/{road_episodes} completed")

print("\nRoad Crossing Training completed!")
print("\nLearned Q-table for Road Crossing:")
print("Position | LEFT Action | RIGHT Action")
print("-" * 38)
positions_names = ["Start", "Mid-Left", "Mid-Right", "Goal"]
for i in range(road_positions):
    print(f"{positions_names[i]:>8} |    {Q_road[i,0]:6.2f}   |     {Q_road[i,1]:6.2f}")

# Test road crossing agent
print("\n" + "=" * 40)
print("TESTING ROAD CROSSING AGENT")
print("=" * 40)

state = 0
steps = 0
action_sequence = []
position_names = ["Start", "Mid-Left", "Mid-Right", "Goal"]

print("Agent's road crossing path:")
while state < road_positions - 1 and steps < 5:
    action = np.argmax(Q_road[state])
    action_sequence.append(action)
    
    # Determine next state (same logic as training)
    if state == 0:
        next_state = 1 if action == 1 else 0
    elif state == 1:
        next_state = 2 if action == 0 else 1
    elif state == 2:
        next_state = 3 if action == 1 else 1
    
    action_name = "LEFT" if action == 0 else "RIGHT"
    print(f"Step {steps + 1}: {position_names[state]} -> {action_name} -> {position_names[next_state]}")
    
    state = next_state
    steps += 1

print(f"\nAction sequence: {' -> '.join(['RIGHT' if a == 1 else 'LEFT' for a in action_sequence])}")

if state == road_positions - 1:
    if action_sequence == [1, 0, 1]:  # RIGHT, LEFT, RIGHT
        print("SUCCESS! Learned correct sequence: RIGHT -> LEFT -> RIGHT")
    else:
        print(" Reached goal but with different sequence")
else:
    print("Failed to reach goal")

