# MVP API - Continuidade de Procedimentos Médicos

## Visão geral

Este projeto tem como objetivo criar uma API para garantir a continuidade de procedimentos médicos dos pacientes, mesmo quando eles precisarem mudar de estabelecimento, cidade ou profissional responsável.

A ideia central é permitir que o paciente tenha acesso ao histórico de diagnósticos, procedimentos e atendimentos, além de localizar estabelecimentos que possam dar continuidade ao tratamento, independentemente do local em que ele esteja.

---

## Objetivo do projeto

A API foi pensada para atender a seguinte necessidade:

- um paciente recebe um diagnóstico;
- esse diagnóstico gera um ou mais procedimentos médicos;
- o tratamento pode ser acompanhado ao longo do tempo;
- se o paciente trocar de clínica, profissional ou cidade, ainda é possível manter o acompanhamento do tratamento;
- a API armazena e disponibiliza esses dados para que o paciente possa consultar seu histórico e encontrar estabelecimentos compatíveis para continuidade do cuidado.

Em outras palavras, o sistema busca reduzir interrupções no tratamento, preservar o histórico clínico e facilitar o acesso a novos atendimentos sem perder o contexto do paciente.

---

## Problema que a solução resolve

Muitas vezes, o paciente interrompe ou adia um procedimento porque não consegue continuar no mesmo local de atendimento. Isso pode acontecer por viagem, mudança de residência, indisponibilidade de horário ou necessidade de buscar outro especialista.

Com a API, as informações ficam registradas e organizadas por paciente, permitindo:

- consultar diagnósticos vinculados ao paciente;
- visualizar procedimentos relacionados ao diagnóstico;
- acompanhar sessões agendadas e realizadas;
- encontrar estabelecimentos que atendem o mesmo tipo de procedimento;
- manter a continuidade do cuidado independentemente da localização física.

---

## Funcionalidades principais

- cadastro e consulta de pacientes;
- registro de diagnósticos realizados por agentes de saúde;
- criação de procedimentos a partir do diagnóstico;
- acompanhamento de frequência e status dos procedimentos;
- agendamento e histórico de sessões;
- vínculo de sessões a estabelecimentos e agentes;
- consulta de estabelecimentos por localidade e tipo de procedimento.

---

## Modelo de dados desenvolvido até agora

O projeto já conta com os seguintes modelos principais:

### 1. Patient

```python
class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
```

Representa o paciente, com dados pessoais, contato e endereço.

### 2. Agent

```python
class Agent(db.Model):
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    agent_type = db.Column(db.String(100), nullable=False)
    credentials = db.Column(db.String(200), nullable=False)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)
```

Representa o profissional ou agente responsável por atender e registrar o histórico do paciente.

### 3. Establishment

```python
class Establishment(db.Model):
    __tablename__ = 'establishments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
```

Representa os estabelecimentos de saúde e sua localização.

### 4. Diagnosis

```python
class Diagnosis(db.Model):
    __tablename__ = 'diagnoses'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), nullable=False)
```

Armazena o diagnóstico associado a um paciente e ao agente responsável.

### 5. Procedure

```python
class Procedure(db.Model):
    __tablename__ = 'procedures'

    id = db.Column(db.Integer, primary_key=True)
    diagnosis_id = db.Column(db.Integer, db.ForeignKey('diagnoses.id'), nullable=False)
    procedure_type = db.Column(db.Enum(ProcedureType), nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(ProcedureStatus), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
```

Representa o procedimento médico recomendado a partir do diagnóstico, com tipo, frequência e status atual.

### 6. Session

```python
class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    procedure_id = db.Column(db.Integer, db.ForeignKey('procedures.id'), nullable=False)
    establishment_id = db.Column(db.Integer, db.ForeignKey('establishments.id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agents.id'), nullable=False)
    scheduled_date = db.Column(db.DateTime, nullable=False)
    date_performed = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Enum(SessionStatus), nullable=False)
    observations = db.Column(db.Text, nullable=True)
```

Armazena cada atendimento ou sessão do procedimento, incluindo local, profissional e status da sessão.

---

## Enums utilizados

### ProcedureType

```python
class ProcedureType(Enum):
    PHYSIOTHERAPY = 'PHYSIOTHERAPY'
    NUTRITIONAL_THERAPY = 'NUTRITIONAL_THERAPY'
    HEMODIALYSIS = 'HEMODIALYSIS'
    CHEMOTHERAPY = 'CHEMOTHERAPY'
    RADIOTHERAPY = 'RADIOTHERAPY'
    PHYSICAL_REHABILITATION = 'PHYSICAL_REHABILITATION'
    OTHER = 'OTHER'
```

### SessionStatus

```python
class SessionStatus(Enum):
    SCHEDULED = 'SCHEDULED'
    DONE = 'DONE'
    MISSED = 'MISSED'
    RESCHEDULED = 'RESCHEDULED'
    CANCELLED = 'CANCELLED'
```

Esses enums ajudam a padronizar tipos de procedimentos e os estados das sessões ao longo do tratamento.

---

## Relacionamentos principais

O modelo atual estrutura a continuidade do tratamento da seguinte forma:

- Patient possui vários diagnósticos;
- Diagnosis é criado por um Agent para um Patient;
- Procedure está ligado a um Diagnosis;
- Session está ligada a um Procedure;
- Session também aponta para o Establishment e o Agent que atenderam naquele momento;
- isso permite que o paciente siga o tratamento em outro local sem perder o histórico e o andamento do cuidado.

---

## Fluxo de uso esperado

1. O paciente é cadastrado;
2. um agente registra um diagnóstico;
3. o diagnóstico gera um procedimento;
4. o procedimento define frequência e status;
5. sessões são agendadas e realizadas em diferentes estabelecimentos;
6. o paciente consegue consultar seu histórico e buscar atendimento em locais que ofereçam o mesmo tipo de procedimento.

---

## Observações

Este é um MVP inicial da API, com foco em modelagem de domínio e rastreio da continuidade do tratamento. A estrutura atual já oferece a base necessária para evoluir com:

- autenticação de pacientes e agentes;
- busca por estabelecimento por tipo de procedimento;
- endpoints de consulta do paciente;
- controle de acesso por perfil;
- maior detalhamento do ciclo de acompanhamento clínico.

---

## Próximo passo sugerido

A próxima etapa seria expandir a API com endpoints para:

- criar e listar pacientes;
- registrar diagnósticos;
- criar procedimentos;
- listar sessões por procedimento;
- buscar estabelecimentos por cidade e tipo de procedimento;
- permitir que o paciente veja somente seus próprios dados.

