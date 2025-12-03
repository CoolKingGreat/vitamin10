from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    "tear off the mask; your face is glorious.",
    "the cure for pain is in the pain.",
    "i want to be what i was when i wanted to be what i am now.",
    "to be alive is to be broken; to be broken is to stand in need of grace.",
    "where there is ruin, there is hope for a treasure.",
    "you must have chaos within you to give birth to a dancing star.",
    "all sorrows can be borne if you put them into a story.",
    "the fire that warms us can also consume us; it is not the fault of the fire.",
    "the soul would have no rainbow had the eyes no tears.",
    "the cracks are where the light gets in, if you let it.",
    "we are each of us a secret to the other.",
    "i am seeking, i am striving, i am in it with all my heart.",
    "in three words i can sum up everything i've learned about life: it goes on.",
    "you will lose everything. then the real work begins.",
    "all the darkness in the world cannot extinguish the light of a single candle.",
    "i have been bent and broken, but — i hope — into a better shape.",
    "the world is full of suffering; it is also full of the overcoming of it.",
    "those who have a 'why' to live can bear almost any 'how.'",
    "the deeper that sorrow carves into your being, the more joy you can contain.",
    "there is a crack in everything; that's how the light gets in.",
    "the wound is the place where the light enters you.",
    "the heart that breaks open can contain the whole universe.",
    "grief is the price we pay for love.",
    "no one can build you the bridge on which you must cross the river of life.",
    "the soul becomes dyed with the color of its thoughts."
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    selected_quote = random.choice(quotes)
    return jsonify({"quote": selected_quote})

if __name__ == '__main__':
    app.run(debug=True)