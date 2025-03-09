import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

def main():
    print("Welcome to the Countdown Timer!")
    seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
