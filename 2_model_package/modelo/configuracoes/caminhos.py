from pathlib import Path

import os

# caminho absoluto deste script
PATH_SCRIPT= os.path.abspath(__file__)

# caminhos dos diretórios do projeto
MODELO_DIR = Path(PATH_SCRIPT).parent.parent
CONFIGURACOES_DIR = MODELO_DIR / "configurcoes"
DADOS_DIR = MODELO_DIR / "dados"
MODEL_TREINADO_DIR = MODELO_DIR / "modelo_treinado"
ROOT = MODELO_DIR.parent
