import json
import os
import subprocess
import re
import time

import utils
from recorder import record
from recorder import RATE
from recognization import recognize

DEMO_MODE = True

def start_script(server):
    script = utils.load_script()

    question_key = "question_1"
    if question_key not in script:
        raise Exception("Script has to start with question_1")

    while True:
        time.sleep(0.5)

        current_question = script[question_key]
        
        # Joanna Question UI
        print current_question["text"]

        server.send_message('out', current_question["text"])

        # Video File
        video_path = os.path.join("/assets/videos", current_question["video"])

        server.send_video(video_path)

        # Sleep for length of file
        time.sleep(get_length(video_path))

        if "answer" in current_question:
            answers = current_question["answer"]

            if DEMO_MODE:
                content = current_question["demo_answer"]
                time.sleep(3)
            else:
                data = record()
                response = recognize(data, RATE)

                if len(response.results) == 0:
                    continue

                result = response.results[0]
                if not result.alternatives:
                    continue

                content = result.alternatives[0].transcript

            
            # Patient answer
            server.send_message('in', content)

            key_list = answers.keys();
            key_list.remove("any")

            if not key_list:
                question_key = answers["any"]
            else:
                found_answer = False;
                for answer in key_list:
                    if answer in content:
                        print "Found " + answer + " in " + content
                        question_key = answers[answer]
                        found_answer = True

                        update_form(server, current_question)
                        break;

                if not found_answer:
                    question_key = answers["any"]
        elif "next" in current_question:
            print 'found next'
            question_key = current_question["next"]
            print question_key
            update_form(server, current_question)
        else:
            update_form(server, current_question)
            # End the questionaire
            break

def update_form(server, current_question):
    if "data" in current_question:
        for d in current_question["data"]:
            server.send_data(d)


def get_length(filename):
  curr_path = os.path.dirname(utils.__file__)
  file_path = curr_path + '/../../web-frontend/src' + filename

  print file_path

  assert (os.path.isfile(file_path)), "Should be a file"
  result = subprocess.Popen(["ffprobe", file_path], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  first_parsing = [x for x in result.stdout.readlines() if "Duration" in x]
  print result.stdout.readlines()
  print 'Duration Data'
  print first_parsing[0].strip()
  match_time = re.match( r'Duration:\s*[0-9]*:[0-9]*:([0-9]*).*', first_parsing[0].strip())

  return int(match_time.group(1)) + 1

