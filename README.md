# 🧑‍💻 Criando um Modelo de Previsão com Ponto de Extremidade no Azure Machine Learning

Neste tutorial, vou mostrar como eu criei um modelo de machine learning, treinei e implantei o modelo em um ponto de extremidade no Azure Machine Learning para que eu possa fazer previsões em tempo real.

📋 Pré-requisitos
Antes de começar, eu verifiquei se eu tinha os seguintes itens:
- Uma conta no Azure 🖥️
- Acesso ao Azure Machine Learning Studio ou ao Azure Portal
- Conhecimento básico em Machine Learning e Azure ML

🚀 Parte 1: Criando um Workspace no Azure Machine Learning
- Passo 1.1: Criando um Workspace no Azure
Primeiro, acessei o Portal do Azure (https://portal.azure.com) e criei um Workspace no Azure Machine Learning. Aqui está o que fiz:
1. No portal, cliquei em "Criar um recurso" e pesquisei por "Machine Learning".
2. Selecionei "Azure Machine Learning" e cliquei em "Criar".
3. Preenchi os detalhes:
- Assinatura: Selecionei minha assinatura do Azure.
- Grupo de recursos: Escolhi ou criei um novo grupo de recursos.
- Nome do Workspace: Dei um nome para o meu Workspace (por exemplo, "MeuWorkspaceML").
- Localização: Escolhi uma região.
4. Após revisar, cliquei em "Criar" e aguardei o provisionamento do Workspace.

🔧 Parte 2: Criando o Modelo de Machine Learning
Passo 2.1: Carregando os Dados no Workspace
Com o Workspace criado, o próximo passo foi carregar meus dados para o Azure ML Studio.
1. No Azure Machine Learning Studio, acessei o meu Workspace e, no painel "Datasets", cliquei em "Create Dataset".
2. Fiz o upload do meu conjunto de dados, que estava em formato CSV. Caso você não tenha dados prontos, pode usar um conjunto de dados de exemplo como o Iris Dataset.

Passo 2.2: Criando o Experimento de Treinamento
Agora, criei um novo experimento de treinamento.
1. No Azure ML Studio, cliquei em "Designer" para usar a interface visual de arrastar e soltar, onde eu poderia configurar facilmente o fluxo de dados.
2. No painel "Palette", busquei o modelo de regressão logística para classificação e arrastei-o para o canvas.
3. Carreguei os dados para o modelo e conectei os módulos:
Dataset → Train Model → Evaluate Model.

Passo 2.3: Treinando o Modelo
- No meu caso, escolhi um modelo de regressão logística para classificação. Aqui está o código que usei para treinar o modelo no Azure ML Studio:

Passo 2.4: Registrando o Modelo
- Após o treinamento, registre o modelo no Azure Machine Learning para garantir que ele possa ser reutilizado depois.

📡 Parte 3: Implantando o Modelo com Ponto de Extremidade
Passo 3.1: Criando o Endpoint de Inferência
Agora, criei um ponto de extremidade para poder acessar o modelo em tempo real. No Azure Machine Learning Studio, segui os seguintes passos:
1. No painel de Endpoints, cliquei em "Create" e selecionei "Real-time inference".
2. Configurei a implantação do modelo:
- Defini a quantidade de CPU e memória necessária.
- Escolhi uma imagem do container para hospedar o modelo (o Azure oferece imagens prontas, o que facilita a implantação).
3. Criei o script de inferência (score.py) que iria fazer as previsões a partir dos dados recebidos:

Passo 3.2: Implantando o Serviço
Implantei o modelo criando o serviço de real-time inference. Para isso, segui os seguintes passos:
- No Azure Machine Learning Studio, cliquei em "Deploy".
- Selecionei o modelo registrado e o script de inferência.
- Cliquei em "Deploy" e aguardei o Azure criar o serviço e o ponto de extremidade.

💻 Parte 4: Testando o Ponto de Extremidade
Agora que meu modelo foi implantado, o próximo passo foi testar o ponto de extremidade criado para garantir que ele estivesse funcionando corretamente.
- Obtendo a URL do ponto de extremidade: No painel de Endpoints, cliquei no nome do serviço implantado e copiei a URL.
- Testando com Python: Para testar, criei um script Python que envia os dados para o ponto de extremidade e recebe as previsões.
