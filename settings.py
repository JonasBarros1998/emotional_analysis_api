from dotenv import load_dotenv
from pathlib import Path 

#Configuração do dotenv
def dotenv():
    load_dotenv()

    load_dotenv(verbose=True)

    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
