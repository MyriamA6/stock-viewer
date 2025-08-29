import streamlit as st
import yfinance as yf
import plotly.express as px

with st.form("quote"):
    nom_action =st.text_input("Nom de l'action",
                              value="",
                              placeholder="Ex: AAPL (US) • AIR.PA (Euronext Paris) • BMW.DE (Xetra)")
    period = st.selectbox(
        "Période historique",
        options=["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"],
        index=0
    )

    interval = st.selectbox(
        "Intervalle d’affichage *:grey[(1m = 1 minute)]*",
        options=["1m","15m", "30m", "60m", "1d", "5d", "1wk", "1mo", "3mo"],
        index=0
    )

    submitted = st.form_submit_button("Afficher")

if submitted:
    ticker = yf.Ticker(nom_action)
    df = ticker.history( period=period,interval=interval)
    df.index=df.index.tz_convert("Europe/Paris")

    fig =px.line(df, x=df.index, y="Close")
    fig.update_layout(
        title=f"{nom_action} - Intervalle {interval} - Période {period}",
        xaxis_title="Date/Heure",
        yaxis_title="Cours"
    )
    fig.update_traces(line_color="green")
    st.plotly_chart(fig, use_container_width=True)
