# 🛡️ CyberSOC — Sistema de Monitoramento de Segurança

Sistema web educacional desenvolvido em Python e Flask para simular atividades de um **SOC (Security Operations Center)**, permitindo visualizar logs, monitorar eventos de segurança e identificar endereços IP com comportamento suspeito.

O projeto tem como objetivo praticar conceitos de **Blue Team, análise de logs, detecção de atividades suspeitas, desenvolvimento web e armazenamento de eventos em banco de dados**.

> **Status:** Em desenvolvimento  
> **Tipo:** Projeto educacional de cibersegurança  
> **Foco:** Blue Team / SOC / Monitoramento de segurança

---

## 📌 Sobre o projeto

Um Security Operations Center (SOC) é responsável por monitorar ambientes tecnológicos, investigar alertas e identificar possíveis incidentes de segurança.

O CyberSOC foi criado como um laboratório prático para reproduzir parte desse fluxo de trabalho em uma aplicação web simples.

A aplicação utiliza eventos simulados para representar atividades como tentativas de login bem-sucedidas e malsucedidas. Os eventos são armazenados em um banco de dados SQLite e podem ser consultados pela interface web.

A partir desses registros, o sistema pode identificar endereços IP com múltiplas tentativas de login malsucedidas, classificando o risco de acordo com regras definidas no código.

### 🎯 Objetivos

- Aprender Python aplicado à cibersegurança.
- Praticar análise e organização de logs.
- Entender como funciona a detecção baseada em regras.
- Identificar padrões que podem indicar tentativas de acesso indevido.
- Desenvolver uma aplicação web com Flask.
- Utilizar SQLite para persistência de dados.
- Construir uma base prática para estudos futuros em Blue Team e SOC.

---

## ⚙️ Funcionalidades

### 📊 Dashboard

Interface central para visualizar os eventos registrados e acompanhar informações gerais sobre a atividade simulada.

### 📋 Monitoramento de logs

Exibe registros de eventos contendo informações como:

- Endereço IP de origem.
- Usuário associado ao evento.
- Status da tentativa de login.
- Data e horário do registro.

### 🚨 Detecção de IPs suspeitos

Analisa os registros armazenados e identifica endereços IP com três ou mais tentativas de login malsucedidas.

A classificação implementada utiliza as seguintes regras:

| Tentativas malsucedidas | Classificação |
|---|---|
| 3 a 5 | Médio |
| 6 ou mais | Alto |

Esses limites são regras didáticas do projeto e não representam um padrão universal de classificação de risco.

### 🗄️ Banco de dados

O SQLite é utilizado para armazenar os eventos e permitir consultas posteriores, mesmo depois de reiniciar a aplicação.

### 🧪 Geração de eventos simulados

A aplicação possui lógica para gerar eventos fictícios, possibilitando testar o dashboard e a análise de logs sem precisar acessar um ambiente real de produção.

### 📝 Histórico de incidentes

O projeto possui uma estrutura inicial para registrar incidentes de alto risco e exibir um histórico na interface. Essa funcionalidade ainda precisa ser validada e integrada ao fluxo automático da aplicação.

---

## 🧰 Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Lógica da aplicação e análise de eventos |
| Flask | Framework web |
| SQLite | Armazenamento dos registros |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização da interface |
| JavaScript | Interatividade no navegador |
| Git | Controle de versão |
| GitHub | Hospedagem do código-fonte |

---

## 📁 Estrutura do projeto

```text
cybersoc/
├── app.py
├── requirements.txt
├── cybersoc.db
│
├── routes/
│   ├── __init__.py
│   ├── api.py
│   └── dashboard.py
│
├── services/
│   ├── __init__.py
│   ├── database.py
│   └── logs.py
│
├── templates/
│   ├── index.html
│   ├── logs.html
│   ├── ips_suspeitos.html
│   └── incidentes.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .gitignore
```

**Responsabilidade de cada parte:**

- `app.py`: inicializa a aplicação Flask e registra as rotas.
- `routes/`: define as páginas e os endpoints da aplicação.
- `services/database.py`: configura a conexão e a criação das tabelas SQLite.
- `services/logs.py`: gera, consulta e analisa eventos.
- `templates/`: contém as páginas HTML.
- `static/style.css`: concentra os estilos visuais.
- `static/script.js`: implementa funcionalidades executadas no navegador.
- `requirements.txt`: lista as dependências Python necessárias.
- `.gitignore`: impede que arquivos locais, bancos de dados e ambientes virtuais sejam enviados ao repositório.

O arquivo `cybersoc.db` é criado localmente quando necessário e deve permanecer fora do controle de versão.

---

## 🖥️ Requisitos

Para executar o projeto localmente, você precisa de:

- Windows, Linux ou macOS.
- Python 3 instalado.
- Git instalado.
- Visual Studio Code ou outro editor.
- Terminal com acesso à pasta do projeto.

---

## 🚀 Como instalar e executar

### 1. Clone o repositório

Depois que o projeto estiver publicado no GitHub, execute:

```bash
git clone https://github.com/SEU-USUARIO/cybersoc.git
```

Entre na pasta:

```bash
cd cybersoc
```

Substitua `SEU-USUARIO` pelo nome da sua conta no GitHub.

### 2. Crie um ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

Se o arquivo `requirements.txt` ainda não existir, gere-o no ambiente em que o projeto funciona:

```bash
python -m pip freeze > requirements.txt
```

### 4. Inicie a aplicação

Na pasta que contém o arquivo `app.py`, execute:

```bash
python app.py
```

Se o comando `python` não funcionar no Windows, tente:

```powershell
py app.py
```

### 5. Acesse no navegador

Utilize o endereço local exibido pelo Flask no terminal. Se a aplicação estiver usando a configuração padrão de desenvolvimento, normalmente será:

```text
http://127.0.0.1:5000
```

---

## 🔍 Como funciona a detecção

O fluxo básico da aplicação é:

1. Um evento de login simulado é gerado.
2. O evento é armazenado no banco SQLite.
3. O sistema consulta os registros existentes.
4. As tentativas malsucedidas são agrupadas por endereço IP.
5. Os endereços que atingem os limites configurados são classificados.
6. Os resultados podem ser exibidos na interface para análise.

Essa abordagem é um exemplo de **detecção baseada em regras**. Em um SOC real, as regras precisariam considerar contexto adicional, falsos positivos, histórico dos usuários, origem dos acessos e outras evidências.

---

## 🔐 Segurança e limitações

O CyberSOC é um projeto de aprendizado e não deve ser utilizado como plataforma de monitoramento de produção.

- Os eventos são simulados, não provenientes de uma infraestrutura real.
- Um IP com várias falhas não é necessariamente malicioso.
- Os limites de detecção são simplificados para fins didáticos.
- A aplicação deve ser executada localmente durante o desenvolvimento.
- O modo de depuração do Flask não deve ser habilitado em produção.
- O projeto ainda não substitui um SIEM ou uma solução profissional de monitoramento.

Não inclua senhas, tokens, dados pessoais reais ou informações confidenciais nos logs e no repositório público.

---

## 🗺️ Próximas melhorias

- [ ] Validar todas as páginas e rotas.
- [ ] Integrar automaticamente a geração e o registro de incidentes.
- [ ] Criar filtros de logs por IP, status e data.
- [ ] Adicionar gráficos de eventos e falhas de autenticação.
- [ ] Implementar atualização periódica do dashboard.
- [ ] Criar testes automatizados com `pytest`.
- [ ] Adicionar documentação dos endpoints da API.
- [ ] Melhorar o tratamento de erros e a validação de entradas.
- [ ] Implementar autenticação e controle de acesso antes de disponibilizar a aplicação em rede.
- [ ] Explorar a análise de logs reais de laboratório, com dados controlados e autorizados.

---

## 🎓 Objetivo de aprendizado

Este projeto faz parte dos meus estudos práticos em Python, redes e cibersegurança, com foco em Blue Team e nas atividades de monitoramento e análise de eventos comuns em um SOC.

A proposta é evoluir gradualmente a aplicação, documentando as funcionalidades e aplicando os conhecimentos adquiridos durante o desenvolvimento.

---

## 📄 Licença

A licença ainda não foi definida. Até que uma licença seja adicionada ao repositório, não presuma que terceiros têm autorização para redistribuir ou reutilizar o código.

---

**Projeto desenvolvido para fins educacionais e de estudo em cibersegurança.**