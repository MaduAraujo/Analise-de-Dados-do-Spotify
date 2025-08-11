import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Análise do Spotify",
    page_icon="🎵",
    layout="wide",
)

# --- Carregamento dos dados ---
@st.cache_data
def load_data():
    """
    Carrega o DataFrame, renomeia colunas para melhor visualização
    e mapeia colunas numéricas para valores textuais.
    """
    try:
        # Carregando o novo arquivo CSV
        df = pd.read_csv('dataset.csv')

        # Normalizando os nomes das colunas para evitar erros de digitação e diferenças de caso
        df.columns = [col.strip().lower() for col in df.columns]

        # Renomeando as colunas
        df.rename(columns={
            'track_id': 'ID da Música',
            'album_name': 'Nome do Álbum',
            'explicit': 'Explícito',
            'speechiness': 'Expressividade Vocal',
            'track_name': 'Nome da Música',
            'artists': 'Artista',
            'track_genre': 'Gênero',
            'popularity': 'Popularidade',
            'danceability': 'Danceabilidade',
            'energy': 'Energia',
            'loudness': 'Volume',
            'acousticness': 'Acusticidade',
            'instrumentalness': 'Instrumentalidade',
            'liveness': 'Vivacidade',
            'valence': 'Valência',
            'tempo': 'Tempo (BPM)',
            'duration_ms': 'Duração (ms)',
            'key': 'Chave',
            'mode': 'Modo',
            'time_signature': 'Fórmula de Compasso'
        }, inplace=True)
        
        # Mapeando a coluna 'Modo' de numérico para texto
        df['Modo'] = df['Modo'].map({1: 'Maior', 0: 'Menor'})

        # Mapeando a coluna 'Chave' de numérico para texto
        key_mapping = {
            0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#',
            7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
        }
        df['Chave'] = df['Chave'].map(key_mapping)
        
        return df
    except FileNotFoundError:
        st.error('Arquivo "dataset.csv" não encontrado. Por favor, verifique se o arquivo está no mesmo diretório.')
        return None

# Carrega os dados e armazena na variável
dados_musicas = load_data()

# --- Estrutura da UI ---
if dados_musicas is not None:
    st.title('Análise de Dados do Spotify')

    # Como o novo arquivo não possui a coluna de data, o filtro de ano foi removido.
    dados_filtrados = dados_musicas.copy()

    # Exibe os dados
    st.subheader(f'Análise das Músicas ({len(dados_filtrados)} registros)')
    st.dataframe(dados_filtrados)
    st.markdown('---')

    # --- Filtros na barra lateral ---
    st.sidebar.header('Filtros')

    # Filtro de Gênero
    all_genres = dados_musicas['Gênero'].unique()
    selected_genres = st.sidebar.multiselect(
        'Selecione o(s) gênero(s):',
        all_genres,
        default=list(all_genres)[:5]
    )

    # Filtro de Popularidade
    popularity_range = st.sidebar.slider(
        'Popularidade (0-100):',
        min_value=0,
        max_value=100,
        value=(0, 100)
    )

    # Aplica os filtros
    dados_filtrados = dados_musicas[
        (dados_musicas['Gênero'].isin(selected_genres)) &
        (dados_musicas['Popularidade'] >= popularity_range[0]) &
        (dados_musicas['Popularidade'] <= popularity_range[1])
    ].copy()

    # Colunas para organizar os gráficos
    col1, col2 = st.columns(2)

    with col1:
        # Gráfico 1: Histograma da Distribuição de Recursos
        st.header('Distribuição de Características Musicais')
        features = ['Danceabilidade', 'Energia', 'Volume', 'Acusticidade', 'Instrumentalidade', 'Vivacidade', 'Valência']
        selected_feature = st.selectbox('Selecione a característica para o histograma:', features)

        fig_hist = px.histogram(
            dados_filtrados,
            x=selected_feature,
            nbins=30,
            title=f'Distribuição de {selected_feature}',
            labels={selected_feature: selected_feature, 'count': 'Contagem'},
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        st.plotly_chart(fig_hist)

    with col2:
        # Gráfico 2: Relação entre as Características
        st.header('Relação entre as Características')
        x_axis_feature = st.selectbox('Selecione a característica para o Eixo X:', features, index=0)
        y_axis_feature = st.selectbox('Selecione a característica para o Eixo Y:', features, index=1)
        
        fig_scatter = px.scatter(
            dados_filtrados,
            x=x_axis_feature,
            y=y_axis_feature,
            hover_data=['Nome da Música', 'Artista', 'Popularidade'],
            title=f'Correlação entre {x_axis_feature} e {y_axis_feature}',
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        st.plotly_chart(fig_scatter)
    
    st.markdown('---')

    # Gráfico 3: Mapa de Calor (Matriz de Correlação)
    st.header('Matriz de Correlação')
    numeric_df = dados_filtrados[features + ['Popularidade']].corr()
    fig_corr, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(numeric_df, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig_corr)
    st.markdown('---')

    # Gráfico 4 e 5: Músicas e Artistas Mais Populares
    col3, col4 = st.columns(2)
    with col3:
        top_10_songs = dados_filtrados.sort_values(by='Popularidade', ascending=False).head(10)
        fig_songs = px.bar(
            top_10_songs,
            x='Popularidade',
            y='Nome da Música',
            orientation='h',
            title='Músicas Mais Populares',
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        st.plotly_chart(fig_songs)
    
    with col4:
        # Calculamos a popularidade média dos artistas
        top_10_artists = dados_filtrados.groupby('Artista')['Popularidade'].mean().nlargest(10).reset_index()
        fig_artists = px.bar(
            top_10_artists,
            x='Popularidade',
            y='Artista',
            orientation='h',
            title='Artistas Mais Populares (Popularidade Média)',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        st.plotly_chart(fig_artists)
    st.markdown('---')

    # Gráfico 6: Proporção de Modo Musical
    st.header('Distribuição de Modo Musical')
    mode_counts = dados_filtrados['Modo'].value_counts().reset_index()
    mode_counts.columns = ['Modo', 'Contagem']
    fig_mode = px.pie(
        mode_counts,
        values='Contagem',
        names='Modo',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_mode)
    st.markdown('---')

    # Gráfico 7: Comparação de Danceability por Modo
    st.header('Danceabilidade por Modo Musical')
    fig_boxplot = px.box(
        dados_filtrados,
        x='Modo',
        y='Danceabilidade',
        color_discrete_sequence=px.colors.qualitative.T10
    )
    st.plotly_chart(fig_boxplot)

    # Gráfico 8: Popularidade Média por Gênero
    st.subheader('Popularidade Média por Gênero')
    avg_popularity_by_genre = dados_filtrados.groupby('Gênero')['Popularidade'].mean().sort_values(ascending=False).head(10).reset_index()
    fig_avg_pop_genre = px.bar(
        avg_popularity_by_genre,
        x='Popularidade',
        y='Gênero',
        orientation='h',
        color_discrete_sequence=px.colors.qualitative.Dark2
    )
    st.plotly_chart(fig_avg_pop_genre)