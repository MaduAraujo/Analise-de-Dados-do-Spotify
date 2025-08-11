## 📊🎵 Dashboard de Análise de Dados do Spotify

Este projeto é um dashboard interativo construído com **Streamlit** para explorar e analisar dados musicais do Spotify. Ele permite aos usuários visualizar e filtrar um conjunto 
de dados de músicas, compreendendo as características de diferentes gêneros, a popularidade de artistas e faixas, e as correlações entre diversos atributos musicais.

## Projeto no ar

https://github.com/user-attachments/assets/9665e8b3-4394-4444-95a3-cd6b6f5f846b

### ✨ Funcionalidades Principais

  * **Visualização de Dados Interativa:** Explore o conjunto de dados completo em uma tabela dinamicamente filtrável.
  * **Filtros Personalizáveis:** Use a barra lateral para filtrar os dados por **gênero** e **popularidade**, ajustando a visualização em tempo real.
  * **Análise Detalhada de Características Musicais:**
      * **Histogramas** da distribuição de atributos como `Danceabilidade`, `Energia`, `Acusticidade` e outros.
      * **Gráficos de dispersão** para visualizar a correlação entre quaisquer duas características musicais.
  * **Visualização de Métricas de Popularidade:**
      * Gráficos de barras com as **músicas mais populares** e os **artistas com maior popularidade média**.
  * **Análise de Estrutura Musical:**
      * Gráfico de pizza da distribuição de `Modo Musical` (maior/menor).
      * Boxplot para comparar a `Danceabilidade` entre os diferentes modos musicais.
  * **Matriz de Correlação:** Um mapa de calor detalhado que mostra a correlação entre todas as características numéricas das músicas, oferecendo insights sobre como os atributos se relacionam entre si.

### 🚀 Como Executar o Projeto

#### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina. O projeto foi desenvolvido com Python 3.8 ou superior.

#### 1\. Clonar o Repositório

```bash
git clone https://github.com/MaduAraujo/Analise-de-Dados-do-Spotify.git
cd Analise-de-Dados-do-Spotify
```

#### 2\. Instalar as Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Instale-as usando `pip`:

```bash
pip install -r requirements.txt
```

#### 3\. Obter o Conjunto de Dados

Este projeto requer um arquivo chamado `dataset.csv` no diretório raiz. O arquivo deve conter os dados do Spotify com as seguintes colunas (os nomes das colunas são convertidos internamente, mas a estrutura inicial é importante):

  * `track_id`
  * `album_name`
  * `artists`
  * `track_name`
  * `popularity`
  * `duration_ms`
  * `explicit`
  * `danceability`
  * `energy`
  * `key`
  * `loudness`
  * `mode`
  * `speechiness`
  * `acousticness`
  * `instrumentalness`
  * `liveness`
  * `valence`
  * `tempo`
  * `time_signature`
  * `track_genre`

**Se o arquivo não for encontrado, o dashboard exibirá uma mensagem de erro.**

#### 4\. Executar o Aplicativo

Com o arquivo `dataset.csv` no lugar, execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

Isso abrirá o dashboard automaticamente em seu navegador padrão. Se não abrir, você pode acessar o endereço fornecido no terminal (geralmente `http://localhost:8501`).

### 🛠️ Tecnologias Utilizadas

  * **Streamlit:** Framework para a construção da interface do dashboard.
  * **Pandas:** Usado para manipulação e análise de dados.
  * **Plotly Express:** Biblioteca para a criação de gráficos interativos e dinâmicos.
  * **Matplotlib e Seaborn:** Utilizados para a visualização da matriz de correlação (heatmap).

## 🔗 Fonte dos Dados
Os dados utilizados neste projeto são extraídos do seguinte repositório: https://raw.githubusercontent.com/MaduAraujo/Analise-de-Dados-do-Spotify/main/dataset.csv
