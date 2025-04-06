# install requirements
sudo apt install python3 nginx

# clone project
git clone https://github.com/imarto1/the-local-scene.git
cd the-local-scene/server

# set-up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

service=$(cat << EOF
[Unit]
Description=FastAPI Uvicorn App
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/fastapi-app
Environment="PATH=/home/ubuntu/fastapi-app/venv/bin"
ExecStart=/home/ubuntu/fastapi-app/venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000

[Install]
WantedBy=multi-user.target
EOF)

sudo echo "$service" > /etc/systemd/system/fastapi.service
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi
