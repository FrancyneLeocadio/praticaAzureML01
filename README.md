# Modelo de Previsão com Azure Machine Learning

Este projeto demonstra como construir um modelo de previsão utilizando o **Azure Machine Learning**, incluindo a criação de um ponto de extremidade para fazer previsões em tempo real.

## 🚀 Como Criar o Modelo

### 1. Criando o Workspace no Azure Machine Learning

Primeiro, criei um Workspace no Azure. Para isso:
- Acesse o portal do [Azure](https://portal.azure.com).
- Crie um novo recurso de **Machine Learning** e configure as opções como assinatura, grupo de recursos, nome e região.

### 2. Carregando Dados

Eu carreguei o conjunto de dados **Iris** no **Azure ML Studio**, que é ideal para classificação. Para isso, fui até o painel de **Datasets**, cliquei em **"Create Dataset"** e carreguei o arquivo CSV.

### 3. Treinando o Modelo de Machine Learning

Utilizando o **Azure ML Designer**, criei um experimento de treinamento. Conectei o dataset ao módulo de treinamento e escolhi o modelo de **Regressão Logística** para classificação. Após treinar o modelo, eu o registrei para futuras utilizações.

### 4. Implantando o Modelo com Ponto de Extremidade

- Criei um ponto de extremidade de **Real-time inference** no Azure ML.
- Criei o script `score.py`, que foi utilizado para fazer as previsões a partir dos dados de entrada.
  
Aqui está o código do script de inferência:

```python
import json
import numpy as np
from azureml.core.model import Model
from sklearn.linear_model import LogisticRegression

def init():
    global model
    model_path = Model.get_model_path("modelo_classificacao")
    model = LogisticRegression()
    model.load(model_path)

def run(data):
    try:
        data = json.loads(data)
        predictions = model.predict(np.array(data['features']))
        return json.dumps(predictions.tolist())
    except Exception as e:
        return str(e)
```

💻 Parte 4: Testando o Ponto de Extremidade
Agora que meu modelo foi implantado, o próximo passo foi testar o ponto de extremidade criado para garantir que ele estivesse funcionando corretamente.
- Obtendo a URL do ponto de extremidade: No painel de Endpoints, cliquei no nome do serviço implantado e copiei a URL.
- Testando com Python: Para testar, criei um script Python que envia os dados para o ponto de extremidade e recebe as previsões.
