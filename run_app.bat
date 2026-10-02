@echo off
title PakWheels Car Price Predictor
echo Starting PakWheels Car Price Predictor Web App...
cd /d "%~dp0"
python -m streamlit run app.py
pause
