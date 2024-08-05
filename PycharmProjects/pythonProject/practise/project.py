import keyboard
import time
import numpy as np


class Reel:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags
        self.score = 0  # Add a score attribute

    def __lt__(self, other):
        return self.score < other.score


class User:
    def __init__(self, id, num_reels):
        self.id = id
        self.likes = set()
        self.dislikes = set()
        self.watched = set()
        self.interests = {}
        self.interaction_matrix = np.zeros((num_reels, num_reels))  # Adjacency matrix for user-reel interactions

    def update_interests(self, reel, action):
        influence = {'like': 2.0, 'dislike': -2.0, 'watched': 1.0}
        weight_change = influence.get(action, 0)

        for tag in reel.tags:
            if tag in self.interests:
                self.interests[tag] += weight_change
            else:
                self.interests[tag] = weight_change

    def interact(self, reel, action):
        if action == 'like':
            self.likes.add(reel.id)
            self.interaction_matrix[self.id][reel.id] = 1  # Update interaction matrix
        elif action == 'dislike':
            self.dislikes.add(reel.id)
            self.interaction_matrix[self.id][reel.id] = -1  # Update interaction matrix
        elif action == 'watched':
            self.watched.add(reel.id)
            self.interaction_matrix[self.id][reel.id] = 0.5  # Update interaction matrix
        self.update_interests(reel, action)


class RecommendationEngine:
    def __init__(self, reels, num_users):
        self.reels = reels
        self.num_users = num_users
        self.adjacency_matrix = np.zeros((num_users, len(reels)))  # Adjacency matrix for user-reel interactions

    def update_adjacency_matrix(self, user_id, reel_id, interaction_value):
        self.adjacency_matrix[user_id][reel_id] = interaction_value

    def recommend(self, user):
        # Calculate scores based on adjacency matrix
        user_scores = np.dot(user.interaction_matrix, self.adjacency_matrix)

        # Update reel scores
        for reel in self.reels:
            reel.score = sum(user_scores[reel.id])

        # Sort reels based on scores
        self.reels.sort(key=lambda x: x.score, reverse=True)

    def get_top_reels(self, number=5):
        # Get the top reels
        return self.reels[:number]


def main_loop(user, engine):
    current_reels = []
    index = 0

    while True:
        if not current_reels:
            engine.recommend(user)
            current_reels = engine.get_top_reels(5)
            index = 0

        if index < len(current_reels):
            current_reel = current_reels[index]
            print(f"\nReel ID: {current_reel.id}, Tags: {current_reel.tags}")
        else:
            continue

        print("\nCommands: Like (L), Dislike (D), Next (↓), Previous (↑), Quit (Q)")

        action_taken = False
        while not action_taken:
            time.sleep(0.2)  # Reduce to lower value if responsiveness is too slow
            if keyboard.is_pressed('L'):
                user.interact(current_reel, 'like')
                engine.update_adjacency_matrix(user.id, current_reel.id, 1)  # Update adjacency matrix
                print("Liked!")
                action_taken = True
            elif keyboard.is_pressed('D'):
                user.interact(current_reel, 'dislike')
                engine.update_adjacency_matrix(user.id, current_reel.id, -1)  # Update adjacency matrix
                print("Disliked!")
                current_reels.pop(index)  # Remove from current view
                action_taken = True
            elif keyboard.is_pressed('down'):
                index = min(index + 1, len(current_reels) - 1)
                action_taken = True
            elif keyboard.is_pressed('up'):
                index = max(0, index - 1)
                action_taken = True
            elif keyboard.is_pressed('Q'):
                print("Quitting...")
                return


# Setup
reels = [
    Reel(0, ['funny', 'entertainment']),
    Reel(1, ['drama', 'action']),
    Reel(2, ['science', 'education']),
    Reel(3, ['science', 'education', 'technology']),
    Reel(4, ['music', 'dance', 'entertainment'])
]
num_users = 1  # Number of users, assuming there's only one user
user = User(0, len(reels))  # Initialize user with the number of reels
engine = RecommendationEngine(reels, num_users)

# Run the main loop
main_loop(user, engine)
