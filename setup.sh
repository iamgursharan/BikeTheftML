mkdir -p ~/.streamlit/

echo "\[general]\n\n\
email = \"randomemail@gmail.com\"\n\n
" > ~/.streamlit/credentials.toml

echo "[server]\n\n
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
