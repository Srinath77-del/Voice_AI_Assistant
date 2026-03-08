import sounddevice as sd
import wave

rate = 16000
record_time = 5


def record_audio():

    print("Recording... speak now")

    data = sd.rec(int(record_time * rate), samplerate=rate, channels=1, dtype="int16")

    sd.wait()

    file_name = "recorded_audio.wav"

    wf = wave.open(file_name, "wb")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(rate)
    wf.writeframes(data.tobytes())
    wf.close()

    print("Recording finished")
    print("Saved as:", file_name)

    return file_name

if __name__ == "__main__":

    result = record_audio()

    print("File ready:", result)