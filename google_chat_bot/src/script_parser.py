import json
import os

from recorder import record
from recorder import RATE
from recognization import recognize

def start_script(server):
    file_directory = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(file_directory, 'resources/triage_script.json')

    with open(script_path) as f:
        script = json.load(f)

    question_key = "question_1"
    if question_key not in script:
        raise Exception("Script has to start with question_1")

    while True:
        current_question = script[question_key]

        # Joanna Question UI
        server.send_message('out', current_question["text"])

        # Video File
        video_path = os.path.join(file_directory, "videos", current_question["video"])
        server.send_video(video_path)

        if "answer" in current_question:
            answers = current_question["answer"]
            data = record()
            response = recognize(data, RATE)

            result = response.results[0]
            if not result.alternatives:
                continue

            content = result.alternatives[0].transcript

            # Patient answer
            server.send_message('in', content)


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

        elif "next" in current_question:
            question_key = current_question["next"]
        else:
            # End the questionaire
            break

