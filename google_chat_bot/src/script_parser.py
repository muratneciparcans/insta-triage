import json
import os
import subprocess
import re
import time

from recorder import record
from recorder import RATE
from recognization import recognize

def start_script(server):
    script = utils.load_script()

    question_key = "question_1"
    if question_key not in script:
        raise Exception("Script has to start with question_1")

    while True:
        current_question = script[question_key]
        
        # Joanna Question UI
        print current_question["text"]

        server.send_message('out', current_question["text"])

        # Video File
        video_path = os.path.join("/assets/videos", current_question["video"])

        server.send_video(video_path)

        # Sleep for length of file (@TODO: Send still picture)
        time.sleep(get_length(video_path))

        time.sleep(100000)

        if "answer" in current_question:
            answers = current_question["answer"]
            data = record()
            response = recognize(data, RATE)

            result = response.results[0]
            if not result.alternatives:
                continue

            content = result.alternatives[0].transcript

            # Patient answer
            # server.send_message('in', content)


            key_list = answers.keys();
            key_list.remove("any")

            print key_list

            if not key_list:
                question_key = answers["any"]
            else:
                found_answer = False;
                for answer in key_list:
                    if answer in content:
                        print "Found " + answer + " in " + content
                        question_key = answers[answer]
                        found_answer = True
                        break;

                if not found_answer:
                    question_key = answers["any"]
        elif "data" in current_question:
            server.send_register(current_question["data"])
        elif "next" in current_question:
            question_key = current_question["next"]
        else:
            # End the questionaire
            break


def get_length(filename):
  result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  first_parsing = [x for x in result.stdout.readlines() if "Duration" in x]

  print 'Duration Data'
  print first_parsing[0].strip()
  match_time = re.match( r'Duration:\s*[0-9]*:[0-9]*:([0-9]*).*', first_parsing[0].strip())

  return int(match_time.group(1)) + 1

