from txt2speech import *
from ChatModel import *

while(1):

    # Exception handling to handle
    # exceptions at the runtime
    audio2 = listen_()
    if  audio2:
    # use the microphone as source for input.

        print(f"Did you say : {recognizer(audio2)}")
        ans = chat_hf.invoke(audio2)
        parser = parse_chat_response(ans)
        print(parser)
        

