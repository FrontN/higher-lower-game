🏆 Higher Lower Game
Welcome to the Higher Lower Game, a fun command-line game built with Python where you test your knowledge of social media popularity!

📖 Description
The game presents you with two celebrities or famous accounts (A and B). Your goal is to guess which one has a higher follower count on Instagram. If you guess correctly, your score increases, and the challenge continues with a new opponent. If you guess wrong, the game ends, and your final score is displayed.

🚀 Key Features
- **Anti-Duplicate Logic**: The system ensures that Account A and Account B are never the same person in a single round.
- **Clean Interface**: The screen clears every round to provide a smooth, focused gaming experience.
- **Detailed Feedback**: Upon losing, the game reveals the exact follower counts for both accounts so you can see how close you were.
- **Robust Input Handling**: The game handles case-insensitivity and invalid inputs to prevent crashes.

🛠️ Requirements
- Python 3.x
- No external dependencies required

📂 File Structure
- **main.py**: The core script containing the game logic.
- **Higher_lower_game_data.py**: A dictionary-based dataset containing names, follower counts, descriptions, and countries.
- **Higher_lower_game_art.py**: Contains the ASCII art for the game logo and the "VS" symbol.

⚙️ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/FrontN/higher-lower-game.git
   cd higher-lower-game
   ```

2. **Ensure all three files are in the same directory** (they should be after cloning):
   - `main.py`
   - `Higher_lower_game_data.py`
   - `Higher_lower_game_art.py`

🎮 How to Play
1. Open your terminal or command prompt
2. Navigate to the project directory
3. Run the game:
   ```bash
   python main.py
   ```
4. Compare the descriptions of the two accounts
5. Type 'A' or 'B' and press Enter to make your guess
6. Try to beat your high score!

**Game Duration**: The game continues until you make an incorrect guess. Each correct answer increases your score by 1.

📝 Code Snippet (Win/Loss Logic)
The game uses a sleek ternary expression to determine the outcome in a single line:

```python
return 'a' == user_guess if account_a["follower_count"] >= account_b["follower_count"] else 'b' == user_guess
```

🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure all three Python files are in the same directory |
| `python: command not found` | Install Python 3.x or use `python3 main.py` instead |
| Game crashes on input | This shouldn't happen due to robust input handling—please report as a bug |
| Files not found error | Verify you're in the correct directory using `ls` (Mac/Linux) or `dir` (Windows) |

🔮 Future Enhancements
Consider expanding this project with:

- **Local Leaderboard**: Save high scores to a `.txt` or `.json` file to track your best performances
- **Timed Mode**: Challenge yourself with only 5 seconds to make each guess
- **Real-time Data**: Fetch live celebrity data using a Web Scraper or public API
- **Difficulty Levels**: Add easy/medium/hard modes with different datasets
- **Statistics Tracking**: Record accuracy percentage, longest streak, and average response time

💡 Contributing
Found a bug or have a feature suggestion? Feel free to open an issue or submit a pull request!

📄 License
This project is created with ❤️ as a Python learning project.
