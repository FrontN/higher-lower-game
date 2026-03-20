🏆 Higher Lower Game
Welcome to the Higher Lower Game, a fun command-line game built with Python where you test your knowledge of social media popularity!

📖 Description
The game presents you with two celebrities or famous accounts (A and B). Your goal is to guess which one has a higher follower count on Instagram. If you guess correctly, your score increases, and the challenge continues with a new opponent. If you guess wrong, the game ends, and your final score is displayed.

🚀 Key Features
Anti-Duplicate Logic: The system ensures that Account A and Account B are never the same person in a single round.

Clean Interface: The screen clears every round to provide a smooth, focused gaming experience.

Detailed Feedback: Upon losing, the game reveals the exact follower counts for both accounts so you can see how close you were.

Robust Input Handling: The game handles case-insensitivity and invalid inputs to prevent crashes.

🛠️ Requirements
To run this game, you need:

Python 3.x

📂 File Structure
main.py: The core script containing the game logic.

Higher_lower_game_data.py: A dictionary-based dataset containing names, follower counts, descriptions, and countries.

Higher_lower_game_art.py: Contains the ASCII art for the game logo and the "VS" symbol.

🎮 How to Play
Ensure all three files are in the same directory.

Open your terminal or command prompt.

Run the game using:

Bash
python main.py
Compare the descriptions of the two accounts.

Type 'A' or 'B' and press Enter.

Try to beat your high score!

📝 Code Snippet (Win/Loss Logic)
The game uses a sleek ternary expression to determine the outcome in a single line:

Python
return 'a' == user_guess if account_a["follower_count"] >= account_b["follower_count"] else 'b' == user_guess
Suggested Next Steps
If you want to expand this project further, you could:

Add a Local Leaderboard saved to a .txt or .json file.

Implement a Timed Mode where the player has only 5 seconds to choose.

Fetch real-time data using a Web Scraper or an API.

Created with ❤️ as a Python learning project.
