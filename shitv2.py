import pyperclip
import keyboard
import time

def load_non_empty_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def main():
    filename = 'quotes.txt'
    quotes = load_non_empty_lines(filename)

    if not quotes:
        print("No non-empty lines found.")
        return

    print(f"Loaded {len(quotes)} quotes. Press 'p' to paste the next one via simulated input.")

    index = 0
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('p'):
            quote = quotes[index]
            pyperclip.copy(quote)

            # Simulate: / → paste (Ctrl+V) → Enter
            keyboard.press_and_release('/')
            time.sleep(0.1)
            keyboard.press_and_release('ctrl+v')
            time.sleep(0.1)
            keyboard.press_and_release('enter')

            #print(f"[{time.strftime('%H:%M:%S')}] Quote {index + 1} sent: \"{quote}\"")

            index = (index + 1) % len(quotes)

            while keyboard.is_pressed('p'):
                time.sleep(0.1)

if __name__ == "__main__":
    main()
