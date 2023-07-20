# TimeWise
 A simple timer application built using Python with the customtkinter library

## Requirements
Before running the TimeWise app, ensure you have the following dependencies installed:

- Python (version 3.6 or higher)
- pygame library
- customtkinter library
```
pip install pygame
pip install customtkinter
```

# How to Use
1. Clone or download this repository to your local machine.
2. Run the program.
3. The TimeWise Timer app window will open, showing the initial timer value set to 00:00:00.
4. Enter the desired countdown time in the format hh:mm:ss into the respective input fields (hours, minutes, and seconds).
5. Click the "Start" button to start the timer countdown. The timer will update every second, and the text color will turn red when there are only 10 seconds left.
6. To pause the timer, click the "Pause" button. Clicking it again will resume the countdown.
7. When the timer reaches zero, an audio notification will play, and the timer will reset to 00:00:00. You can also manually reset the timer by clicking the "Reset" button.

# Note
The "Change Alarm" button is currently under development and disabled. Future versions may include this functionality.

# Licence
The TimeWise Timer app is licensed under the MIT License.
