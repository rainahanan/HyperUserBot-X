FROM ahirearyan2/HYPERUSERBOT-X:latest

#clonning repo 
RUN git clone -b assistant https://github.com/ahirearyan2/HyperUserBot-X.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
