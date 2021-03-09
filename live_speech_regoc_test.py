# import the module
import speech_recognition as sr
import sys
# create the recognizer
def SpeecRegoc():
    r = sr.Recognizer()
    # define the microphone
    mic = sr.Microphone(device_index=0)
    #for i in range(0, p.get_device_count()):
    print(sr.Microphone.list_microphone_names())
    # record your speech
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    # speech recognition
    result = r.recognize_google(audio)
    print(result)
    return result

#def Output():



    # export the result
#    with open('my_result.txt',mode ='w') as file:
#       file.write("Recognized text:")
#       file.write("\n")
#       file.write(result)
#    print("Exporting process completed!")

#SpeecRegoc()
for x in range(10):
    text = SpeecRegoc()
    if text == "quit" or text == "exit" or text == "stop":
        sys.exit(0)
