# NOTE - THIS IS NOT MY CODE. I have added only two or three lines of code based on the tutorial watched.
# This is code from a tutorial that I did to learn how to do real time speech recognition in streamlit app. This is research that I did on the future direction
# of this app. In future, a direction that I would like to consider going is "Speech recognition to search data for insights. This would be the first step" 


import websockets
import asyncio
import base64
import json
from configure_transciption import auth_key
import streamlit as st

# if 'run' not in st.session_state:
# 	st.session_state['run'] = False

import pyaudio
 
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
# starts recording
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	frames_per_buffer=FRAMES_PER_BUFFER
)


# def start_listening():
# 		st.session_state['run'] = True

# def stop_listening():
# 		st.session_state['run'] = False
 
st.title('Real Time Voice Transcript for Data Analysis')

# start,stop = st.columns(2)
# start.button('Start listening', on_click=start_listening)
# stop.button('Stop listening',on_click=stop_listening)



# the AssemblyAI endpoint we're going to hit
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
 
async def send_receive():

	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", auth_key),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		r = await asyncio.sleep(0.1)
		print("Receiving SessionBegins ...")

		session_begins = await _ws.recv()
		print(session_begins)
		print("Sending messages ...")


		async def send():
			while True:
				try:
					data = stream.read(FRAMES_PER_BUFFER)
					data = base64.b64encode(data).decode("utf-8")
					json_data = json.dumps({"audio_data":str(data)})
					r = await _ws.send(json_data)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					assert False, "Not a websocket 4008 error"

				r = await asyncio.sleep(0.01)
		  
			return True
	  

		async def receive():
			while True:
				try:
					# I added additional code here based on the tutorial to check if "message type" is final transcript
					result_str = await _ws.recv()
					if json.loads(result_str)['message_type'] == 'FinalTranscript':
						print(json.loads(result_str)['text'])
						st.markdown(json.loads(result_str)['text'])

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					assert False, "Not a websocket 4008 error"
	  
		send_result, receive_result = await asyncio.gather(send(), receive())

while True:
	asyncio.run(send_receive())
