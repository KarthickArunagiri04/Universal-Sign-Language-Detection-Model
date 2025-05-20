import cv2
import pyttsx3
import os
import glob
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Path to hand sign image dataset
# Use absolute path to avoid any issues
dataset_path = "hari dataset"  # Replace with the absolute path if necessary

# Function to play text as speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to display hand sign image
def display_image(word):
    # Search for matching files dynamically
    matching_files = glob.glob(os.path.join(dataset_path, f"{word}*"))
    if matching_files:
        image_path = matching_files[0]
        print(f"Displaying: {image_path}")
        img = cv2.imread(image_path)
        if img is not None:
            cv2.imshow(f"Hand Sign for '{word}'", img)
            cv2.waitKey(0)  # Display for 3 seconds
            cv2.destroyAllWindows()
        else:
            print(f"Failed to load image at {image_path}.")
    else:
        print(f"No hand sign found for '{word}'.")

# Function to recognize voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None

# Main function
def main():
    print("Choose input method:")
    print("1. Text input")
    print("2. Voice input")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        user_input = input("Enter a word: ").lower()
    elif choice == "2":
        user_input = recognize_speech()
        if user_input is None:
            return
    else:
        print("Invalid choice.")
        return

    print(f"Input received: {user_input}")
    speak_text(user_input)
    display_image(user_input)

# Test OpenCV functionality
def test_opencv():
    test_image_path = os.path.join(dataset_path, "test.jpg")  # Add a sample test image
    print(f"Testing OpenCV with {test_image_path}")
    img = cv2.imread(test_image_path)
    if img is not None:
        cv2.imshow("Test Image", img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    else:
        print("Failed to load the test image.")

if __name__ == "__main__":
    # Ensure dataset path exists
    if not os.path.exists(dataset_path):
        print(f"Dataset path does not exist: {dataset_path}")
    else:
        # Uncomment the following line to test OpenCV before running the main program
        # test_opencv()
        main()
