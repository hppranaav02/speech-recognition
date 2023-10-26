import deepspeech
import pyaudio
import wave

def initialize_deepspeech(model_path, scorer_path):
    model = deepspeech.Model(model_path)
    model.enableExternalScorer(scorer_path)
    return model

def record_audio(filename, duration=5):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)

    frames = []
    print("Recording...")

    for i in range(0, int(16000 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()

def recognize_speech(model, audio_file):
    with open(audio_file, 'rb') as file:
        audio = file.read()
        text = model.stt(audio)
    return text

def main():
    model_path = 'path/to/deepspeech/model'
    scorer_path = 'path/to/deepspeech/scorer'
    audio_file = 'order.wav'

    ds_model = initialize_deepspeech(model_path, scorer_path)
    record_audio(audio_file)
    recognized_text = recognize_speech(ds_model, audio_file)
    print("You said:", recognized_text)
    response = process_pizza_order(recognized_text)
    print(response)

    # Implement pizza order processing based on recognized_text
def process_pizza_order(recognized_text):
    pizza_type = None
    pizza_quantity = None
    toppings = []

    # Split the recognized text into words
    words = recognized_text.split()

    for word in words:
        # Identify pizza type
        if word.lower() in ['cheese', 'pepperoni', 'tuna']:
            pizza_type = word.lower()

        # Identify pizza quantity
        if word.isdigit() and 1 <= int(word) <= 10:
            pizza_quantity = int(word)

        # Identify pizza toppings
        if word.lower() in ['with', 'and']:
            toppings.append(words[words.index(word) + 1])

    if pizza_type and pizza_quantity:
        total_cost = calculate_total_cost(pizza_type, pizza_quantity, toppings)
        return f"Order confirmed: {pizza_quantity} {pizza_type} pizza(s) with {', '.join(toppings)}. Total cost: ${total_cost:.2f}"
    else:
        return "Sorry, I couldn't understand your order."

def calculate_total_cost(pizza_type, pizza_quantity, toppings):
    pizza_prices = {
        'cheese': 5.99,
        'pepperoni': 6.99,
        'tuna': 7.99,
    }
    topping_prices = {
        'salad': 3.00,
    }

    pizza_cost = pizza_prices.get(pizza_type, 0)
    topping_cost = sum([topping_prices.get(topping, 0) for topping in toppings])

    total_cost = (pizza_cost + topping_cost) * pizza_quantity
    return total_cost

if __name__ == "__main__":
    main()
