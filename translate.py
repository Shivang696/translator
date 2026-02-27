import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load once (very important)
model = load_model("model/translation_model.h5")
tokenizer = pickle.load(open("model/tokenizer.pkl", "rb"))

MAX_LEN = 40

def translate_text(text: str, src: str, tgt: str) -> str:
    input_text = f"{src} {tgt} {text}"

    seq = tokenizer.texts_to_sequences([input_text])
    seq = pad_sequences(seq, maxlen=MAX_LEN, padding="post")

    prediction = model.predict([seq, seq])
    output_seq = np.argmax(prediction[0], axis=1)

    result = ""
    for idx in output_seq:
        if idx == 0:
            break
        result += tokenizer.index_word.get(idx, "")

    return result