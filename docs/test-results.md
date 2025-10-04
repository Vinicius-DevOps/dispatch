# 📋 Guia Completo de Testes - workflow_dispatch

## 🎯 Objetivo

Validar o comportamento do gatilho `workflow_dispatch` em diferentes branches e cenários.

## 🧪 Cenários de Teste Detalhados

### 🔬 Experimento 1: Workflow apenas na branch main

**Hipótese:** O workflow_dispatch só funciona se o arquivo estiver na branch de onde está sendo acionado.

**Passos:**

1. ✅ Fazer commit inicial na branch `main` com o arquivo de workflow
2. 🔄 Criar branch `develop` **SEM** o arquivo de workflow
3. 🔄 Criar branch `feat/test-dispatch` **SEM** o arquivo de workflow
4. 🧪 Tentar acionar workflow_dispatch de cada branch

**Comandos Git:**

```bash
# 1. Commit inicial na main
git add .
git commit -m "feat: adiciona workflow de teste para workflow_dispatch"
git push origin main

# 2. Criar develop sem workflow
git checkout -b develop
rm -rf .github/
git add .
git commit -m "test: branch develop sem workflow"
git push origin develop

# 3. Criar feature sem workflow
git checkout -b feat/test-dispatch
git commit -m "test: branch feature sem workflow" --allow-empty
git push origin feat/test-dispatch
```

**Resultado Esperado:**

- ✅ Workflow funciona na `main`
- ❌ Workflow **NÃO** aparece/funciona na `develop`
- ❌ Workflow **NÃO** aparece/funciona na `feat/test-dispatch`

---

### 🔬 Experimento 2: Workflow em todas as branches

**Hipótese:** O workflow_dispatch funciona em qualquer branch que contenha o arquivo.

**Passos:**

1. ✅ Garantir que o workflow está na `main`
2. 🔄 Fazer merge do workflow para `develop`
3. 🔄 Criar branch `feat/test-dispatch` a partir de `develop` (com workflow)
4. 🧪 Testar workflow_dispatch em todas as branches

**Comandos Git:**

```bash
# 1. Voltar para main e garantir workflow
git checkout main
# (arquivo já deve estar lá)

# 2. Merge para develop
git checkout develop
git merge main
git push origin develop

# 3. Criar feature COM workflow
git checkout -b feat/test-dispatch-v2
git push origin feat/test-dispatch-v2
```

**Resultado Esperado:**

- ✅ Workflow funciona na `main`
- ✅ Workflow funciona na `develop`
- ✅ Workflow funciona na `feat/test-dispatch-v2`

---

### 🔬 Experimento 3: Modificações específicas por branch

**Hipótese:** Cada branch executa sua própria versão do workflow.

**Passos:**

1. ✅ Modificar o workflow em cada branch para mostrar mensagens diferentes
2. 🧪 Acionar workflow_dispatch de cada branch
3. 🔍 Verificar qual versão é executada

**Exemplo de modificação por branch:**

```yaml
# Na main:
echo "🎯 Executando workflow da branch MAIN"

# Na develop:
echo "🛠️ Executando workflow da branch DEVELOP"

# Na feat/:
echo "✨ Executando workflow da branch FEATURE"
```

---

## 🚀 Como Executar os Testes

### Pré-requisitos

1. Repositório no GitHub
2. Acesso às GitHub Actions
3. Permissões para criar branches

### Passo a Passo

#### 1️⃣ Setup Inicial

```bash
# Clone este repositório
git clone <seu-repo>
cd work-dispatch

# Verifique se os arquivos estão corretos
ls -la .github/workflows/
```

#### 2️⃣ Executando Experimento 1

```bash
# Commit na main
git checkout main
git add .
git commit -m "feat: adiciona teste de workflow_dispatch"
git push origin main

# Criar develop sem workflow
git checkout -b develop
rm -rf .github/
git add .
git commit -m "test: develop sem workflow"
git push origin develop

# Criar feature sem workflow
git checkout -b feat/test-dispatch
git commit -m "test: feature sem workflow" --allow-empty
git push origin feat/test-dispatch
```

#### 3️⃣ Testando no GitHub

1. Vá para `Actions` no seu repositório
2. Procure por "Test Workflow Dispatch"
3. Clique em `Run workflow`
4. **IMPORTANTE:** Teste em cada branch:
   - Mude o dropdown da branch
   - Selecione o cenário de teste
   - Clique em `Run workflow`

#### 4️⃣ Executando Experimento 2

```bash
# Voltar para main
git checkout main

# Merge para develop
git checkout develop
git merge main
git push origin develop

# Atualizar feature
git checkout feat/test-dispatch
git merge develop
git push origin feat/test-dispatch
```

## 📊 Interpretando os Resultados

### ✅ Indicadores de Sucesso

- O workflow aparece na lista de Actions
- O botão "Run workflow" está disponível
- A execução inicia normalmente
- Os logs mostram as informações corretas da branch

### ❌ Indicadores de Falha

- O workflow não aparece na lista
- Erro "Workflow not found"
- Botão "Run workflow" não disponível
- Execução não inicia

### 📋 Checklist de Verificação

Para cada teste, verifique:

- [ ] O workflow aparece na aba Actions?
- [ ] O dropdown de branch mostra a branch correta?
- [ ] O botão "Run workflow" está disponível?
- [ ] A execução inicia ao clicar?
- [ ] Os logs mostram a branch correta?
- [ ] As informações do contexto estão corretas?

## 🔍 Análise Detalhada dos Logs

### O que observar nos logs:

1. **Informações do Contexto:**

   ```
   Branch atual: [nome-da-branch]
   Evento que acionou: workflow_dispatch
   Usuário que acionou: [seu-usuario]
   ```

2. **Scripts de Demonstração:**

   - Saída do `show-branch-info.sh`
   - Resultados do `test-script.py`

3. **Verificação de Arquivos:**
   - Lista de arquivos em `.github/workflows/`
   - Conteúdo do workflow atual

## 📝 Template para Documentar Resultados

```markdown
### Teste [NUMERO] - [DATA]

**Branch testada:** [nome-da-branch]
**Experimento:** [1, 2 ou 3]
**Cenário:** [descrição]

**Resultado:**

- [ ] Workflow apareceu na lista
- [ ] Botão Run workflow disponível
- [ ] Execução iniciou
- [ ] Logs corretos

**Observações:**
[suas anotações aqui]

**Conclusão:**
✅ Sucesso / ❌ Falhou / ⚠️ Parcial
```

## 🎓 Conclusões Esperadas

Com base na documentação oficial do GitHub:

1. **workflow_dispatch** só funciona se o arquivo estiver presente na branch de onde está sendo acionado
2. Cada branch executa sua própria versão do workflow
3. Modificações no workflow só afetam a branch onde foram feitas

**Vamos validar isso na prática! 🚀**
