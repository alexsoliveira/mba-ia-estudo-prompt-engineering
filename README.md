# Curso de Prompt Engineering

Este repositório contém os exercícios práticos e exemplos da disciplina de Prompt Engineering do MBA em Engenharia de Software com IA.

## Estrutura dos capítulos

### 1-tipos-de-prompts
Fundamentos de prompt engineering com 9 técnicas essenciais:
- Role-based prompting

## Configuração do Ambiente

**Importante:** Cada pasta do curso é auto-contida, possuindo seu próprio ambiente virtual, arquivo de dependências (requirements.txt) e configuração de variáveis de ambiente (.env).

### 1. Criar e Ativar Ambiente Virtual

```bash
# Navegue até a pasta desejada
cd [pasta-do-capítulo]

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar o arquivo .env e adicionar suas chaves
# Minimamente necessário: OPENAI_API_KEY=sua_chave_aqui
#                         MODEL=modelo_aqui
```
## Dependências Principais

As dependências variam entre os capítulos:

- **Capítulos 1 e 7:** LangChain 1.x.x (versão estável)

Para detalhes específicos de cada capítulo, consulte o arquivo `requirements.txt` correspondente.