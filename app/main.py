import uvicorn
from fastapi import Request, FastAPI, Depends
from Model import EmotionDetector, EmotionGenre
from recommendations import * 
import pickle
import json
import threading

app = FastAPI()
pickle_in = open('classifier.pkl', "rb")
classifier = pickle.load(pickle_in)

update_thread = threading.Thread(target=update_value)
update_thread.daemon = True
update_thread.start()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/predict")
async def predict_Emotion(req: Request):
    data:EmotionDetector = json.loads(await req.body())
    input =  data['text']
    res = classifier.predict([input])[0]
    print(f'-> text : {input} \n-> emotion : {res}')
    data = get_songs_by_emotion(res)
    return { "status": True, "data": data }



@app.post("/api/dailyMix")
async def preferences(req: Request):
    data:EmotionDetector = json.loads(await req.body())
    id =  data['text']
    print(f'-> Daily Mix : {id}')
    data = get_daily_mix_playlists(id)
    return { "status": True, "data": data }



@app.post("/api/albums")
async def preferences(req: Request):
    data:EmotionDetector = json.loads(await req.body())
    id =  data['text']
    print(f'-> Album : {id}')
    data = get_albums(id)
    return { "status": True, "data": data }


# uvicorn main:app --reload --host 0.0.0.0 --port 5000