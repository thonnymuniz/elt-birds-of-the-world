# ELT Birds of the World

🔗 Repositório principal:
https://github.com/seu-usuario/mba-bird-conservation-data-platform

Os objetivos deste projeto são:
- Extração das imagens das aves e carregamento na GCP(Storage e BigQuery)

### Configurar o dbt na sua máquina

Crie um ambiente virtual Python:


### Crie um ambiente virtual Python (LINUX)

**Instalação do python**
``` sh
apt install python3.12-venv 
```

**Crie um ambiente virtual Python**

``` sh
python3.12 -m venv .venv

source .venv/bin/activate
```

### Instale as dependências

```sh
pip3 install -r requirements.txt
```

```sh
dbt deps
```

### Google SDK
Você irá precisar fazer o download da [google-cloud-sdk](https://cloud.google.com/sdk?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-pt-dr-BKWS-all-all-trial-e-dr-1605194-LUAC0008672&utm_content=text-ad-none-any-DEV_c-CRE_526696106061-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20Dev-Tools_SDK-KWID_43700040369790130-kwd-610235859304&utm_term=KW_google%20cloud%20sdk-ST_Google%20Cloud%20SDK&gclid=Cj0KCQjwiIOmBhDjARIsAP6YhSVKjAjopS3ryD-myeprNpCK20IfHcZ9mLoWaVv-fQq5dDsw0_oIO5caAtDzEALw_wcB&gclsrc=aw.ds&hl=pt-br)

**Autenticação**

```sh
gcloud auth application-default login
```

# Taxonomia URL
[https://birdsoftheworld.org/bow/api/v1/taxonomy?depth=2&categoriesForCounts=species&showIucnStatusCounts=true&locale=en](https://birdsoftheworld.org/bow/api/v1/taxonomy?depth=2&categoriesForCounts=species&showIucnStatusCounts=true&locale=en)
