FROM python:3.6

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"michael.diggin@gmail.com\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'


EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_app.py"]
