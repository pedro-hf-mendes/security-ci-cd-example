# security-ci-cd-example

Repositório mínimo para teste de ferramentas de ci/cd focadas em segurança 

## Pipeline 

Os [arquivos de configuração de ci/cd](.github/workflows/) estão configurados para rodar um scan utilizando da ferramenta CodeQL a cada push e PR na branch main

A branch insecure-development contém um código em Python intencionalmente inseguro, servindo de teste para entender como as ferramentas se comportam diante deste cenário. 

## Pre-commit hook

Um outro teste interessante é configurar um pre-commit hook. Segue um passo-a-passo de como configurá-lo para rodar a ferramenta Bandit, de SAST em Python:

- Recomenda-se a criação de um ambiente virtual Python 

- Rodar o comando `pip install bandit pre-commit`

- Criar um arquivo de nome `.pre-commit-config.yaml` na raiz do repositório, com o seguinte conteúdo 

```
repos:
- repo: https://github.com/PyCQA/bandit
  rev: 1.8.6
  hooks:
    - id: bandit
```

- Rodar o comando `pre-commit install`

Para testar a efetividade da ferramenta, recomenda-se tentar dar um commit utilizando o código contido na branch `insecure-development`

