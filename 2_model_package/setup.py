from setuptools import find_packages, setup

#le a versao do pacote
strFile= "modelo/VERSION"
_versao=open(strFile,).readline().strip()

#OBS.: é necessário usar readline() (para ler a primeira linha do arquivo)
#e também strip() (para eliminar a leitura da quebra de linha do arquivo)


setup(
    name="modelo_body_performance",
    version=_versao,
    description="Implementa um modelo de classificacao",
    author= "Joao Paulo Gambaro",
    author_email="joaopaulogambaro@gmail.com",
    python_requires= ">=3.7",
    #packages=find_packages(exclude=("tests",)),
    packages=find_packages(),
    install_requires=[
      'feature-engine==1.4.1',  #OBS: quando eu removi esta funcao deu erro no circleci, entender o pq
      'joblib==1.1.0',
      'numpy==1.23.2',
      'pandas==1.4.3',
      'scikit-learn==1.1.2',
      'scipy==1.9.0',
      'pydantic==1.9.2'
      ],
    include_package_data=True,
    #package_data={"modelo_": ["VERSION"]},
)


#setup(
#    packages=find_packages(exclude=("teste",)),
#    version=_versao
#    )
