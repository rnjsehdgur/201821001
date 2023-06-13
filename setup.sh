mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCOPS = false\n\
\n\
" > ~/.streamlit/config.toml
