from txt2speech import *
from ChatModel import *

while(1):

    audio2 = listen_()
    if  audio2:
        print(f"Did you say : {recognizer(audio2)}")
        ans = chain_html.invoke(audio2)
        parser = parse_chat_response(ans)
        print(parser)
        

