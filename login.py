import curses
import time


PASSWORD="your password here"

 
def animate_login_screen(stdscr):
    # Clear the screen
    stdscr.clear()
 
    # Get screen dimensions
    height, width = stdscr.getmaxyx()
 
    # Set up text
    login_text = "Termux Login"
    username_text = "Username: "
    password_text = "Password: "
 
    # Predefined username and password
    username = "yaspro"
    password = ""
 
    # Calculate the positions of text elements
    login_x = width // 2 - len(login_text) // 2
    username_x = width // 2 - len(username_text) // 2
    password_x = width // 2 - len(password_text) // 2
    text_y = height // 2
 
    # Animation loop
    while True:
        # Clear the screen
        stdscr.clear()
 
        # Print login text
        stdscr.addstr(text_y - 2, login_x, login_text)
 
        # Print username input
        stdscr.addstr(text_y, username_x, username_text + username)
 
        # Print password input
        stdscr.addstr(text_y + 1, password_x, password_text + "*" * len(password))
 
        # Refresh the screen
        stdscr.refresh()
 
        # Wait for user input
        key = stdscr.getch()
 
        # Check if Enter key is pressed
        if key == ord('\n') and PASSWORD in password :
            # Clear the screen
            stdscr.clear()
 
            # Print login success message
            success_message = "Login successful!"
            success_x = width // 2 - len(success_message) // 2
            stdscr.addstr(text_y, success_x, success_message)
 
            # Refresh the screen
            stdscr.refresh()
 
            # Pause for a short duration
            time.sleep(2)
            break
 
        # Check if backspace key is pressed
        elif key == curses.KEY_BACKSPACE or key == 127:
            password = password[:-1]  # Remove the last character
 
        else:
            password += chr(key)  # Append the typed character to the password
 
# Initialize curses and run the animation
curses.wrapper(animate_login_screen)
