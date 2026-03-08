import speech_recognition as sr
import llm

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(mic)
        audio_data = recognizer.listen(mic)

    try:
        spoken_text = recognizer.recognize_google(audio_data)
        print("You said:", spoken_text)

        reply = llm.generate_response(spoken_text)
        print("AI:", reply)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
