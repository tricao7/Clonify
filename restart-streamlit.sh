#!/bin/bash

LOGNAME=rishimohan
gcloud compute ssh --project=ds-entrepreneurship --zone=us-west4-a ds-compute-cloud-20240416-213051 --command="
    source /opt/conda/etc/profile.d/conda.sh && \
    echo 'Changing directories to ~/tts/VoiceCloning' && \
    cd ~/tts/VoiceCloning && \
    echo 'Activating environment metavoice-tts' && \
    conda activate metavoice-tts && \
    echo 'Stopping active Streamlit and tmux shell' && \
    tmux kill-session -t streamlit && \
    echo 'Pulling new files' && \
    git pull && \
    echo 'Restarting Streamlit server in tmux shell streamlit' && \
    tmux new-session -d -s 'streamlit' 'streamlit run app.py' && \
    echo 'Done!'
"