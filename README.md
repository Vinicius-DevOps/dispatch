# Teste de workflow_dispatch no GitHub Actions

Este repositório foi criado para testar o comportamento do gatilho `workflow_dispatch` em diferentes branches do GitHub Actions.

## 🎯 Objetivo do Teste

Validar na prática se o gatilho `workflow_dispatch` funciona apenas na branch `main` ou se pode ser acionado de qualquer branch, considerando a hipótese de que o arquivo de workflow precisa estar presente em todas as branches.

## 📋 Cenários de Teste

### Estrutura de Branches Proposta:

- **main** = produção
- **develop** = desenvolvimento
- **feat/test-dispatch** = branch temporária para teste

## 🧪 Experimentos a Realizar

### Experimento 1: Workflow apenas na main

1. Criar workflow na branch `main`
2. Tentar acionar o workflow_dispatch da branch `develop` (sem o arquivo)
3. Tentar acionar o workflow_dispatch da branch `feat/test-dispatch` (sem o arquivo)

### Experimento 2: Workflow em todas as branches

1. Criar workflow na branch `main`
2. Mergear para `develop`
3. Criar branch `feat/test-dispatch` a partir de `develop`
4. Testar workflow_dispatch em cada branch

### Experimento 3: Modificações específicas por branch

1. Modificar o workflow em cada branch para mostrar informações diferentes
2. Validar qual versão do workflow é executada quando acionada de cada branch

## 📁 Estrutura do Projeto

```
work-dispatch/
├── README.md
├── .github/
│   └── workflows/
│       └── test-dispatch.yml
├── scripts/
│   ├── show-branch-info.sh
│   └── test-script.py
└── docs/
    └── test-results.md
```

## 🚀 Como Testar

1. **Faça push deste repositório para o GitHub**
2. **Vá para Actions no seu repositório**
3. **Procure pelo workflow "Test Workflow Dispatch"**
4. **Clique em "Run workflow"**
5. **Teste em diferentes branches conforme os experimentos**

## 📊 Resultados Esperados

Com base na documentação do GitHub:

- ✅ O workflow_dispatch deve funcionar apenas se o arquivo de workflow estiver na branch de onde está sendo acionado
- ❓ Vamos validar se isso é verdade na prática!

## 📝 Anotações dos Testes

Documente aqui os resultados dos seus testes:

### Teste 1 - Data: \_\_\_

**Branch testada:**
**Resultado:**
**Observações:**

### Teste 2 - Data: \_\_\_

**Branch testada:**
**Resultado:**
**Observações:**

### Teste 3 - Data: \_\_\_

**Branch testada:**
**Resultado:**
**Observações:**
