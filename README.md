# inta-triage
Automated medical triage application to be used in hospitals for more effective patient handling. Part of the Merck Hackathon in Darmstadt 


# How to Build

1. Building the bot:
    ```
    cd web-frontent
    npm install
    ng serve --port 4200
    ```
    
2. Building the patient report visualizer:
    ```
    cd events-frontent
    npm install
    ng serve --port 4300
    ```
    
3. Run the chat bot:

    ```
    mkvirtualenv unite-labs-bot
    cd google-chat-bot
    pip install -r requirements.txt
    python main.py
    ```
   
# How to run

1. Open the triage frontend on the browser by going to `http://localhost:4200'

2. Open the triage report on the browser by going to `http://localhost:4300'

