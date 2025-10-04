# 🛠️ Comandos Git Prontos para os Testes

## 🚀 Setup Inicial do Repositório

```bash
# 1. Inicializar repositório (se necessário)
git init
git add .
git commit -m "feat: setup inicial do teste workflow_dispatch"

# 2. Conectar com GitHub (substitua pela sua URL)
git remote add origin https://github.com/SEU-USUARIO/work-dispatch.git
git branch -M main
git push -u origin main
```

## 📋 Experimento 1: Workflow apenas na main

### Passo 1: Commit inicial na main

```bash
git checkout main
git add .
git commit -m "feat: adiciona workflow de teste para workflow_dispatch"
git push origin main
```

### Passo 2: Criar develop SEM workflow

```bash
git checkout -b develop
rm -rf .github/
echo "# Branch develop - SEM workflow" > README-develop.md
git add .
git commit -m "test: branch develop sem workflow para teste"
git push origin develop
```

### Passo 3: Criar feature SEM workflow

```bash
git checkout develop
git checkout -b feat/test-dispatch-sem-workflow
echo "# Branch feature - SEM workflow" > README-feature.md
git add .
git commit -m "test: branch feature sem workflow para teste"
git push origin feat/test-dispatch-sem-workflow
```

## 📋 Experimento 2: Workflow em todas as branches

### Resetar branches com workflow

```bash
# Voltar para main
git checkout main

# Recriar develop COM workflow
git checkout develop
git merge main
echo "# Branch develop - COM workflow" > README-develop.md
git add .
git commit -m "test: develop agora com workflow"
git push origin develop

# Recriar feature COM workflow
git checkout -b feat/test-dispatch-com-workflow develop
echo "# Branch feature - COM workflow" > README-feature.md
git add .
git commit -m "test: branch feature com workflow"
git push origin feat/test-dispatch-com-workflow
```

## 📋 Experimento 3: Modificar workflows por branch

### Modificar workflow na main

```bash
git checkout main

# Backup do workflow original
cp .github/workflows/test-dispatch.yml .github/workflows/test-dispatch.yml.backup

# Adicionar identificador da branch no workflow
sed -i 's/echo "🎯 WORKFLOW EXECUTADO COM SUCESSO"/echo "🎯 WORKFLOW EXECUTADO NA BRANCH MAIN"/' .github/workflows/test-dispatch.yml

git add .
git commit -m "test: customiza workflow para branch main"
git push origin main
```

### Modificar workflow na develop

```bash
git checkout develop

# Modificar mensagem para develop
sed -i 's/echo "🎯 WORKFLOW EXECUTADO COM SUCESSO"/echo "🛠️ WORKFLOW EXECUTADO NA BRANCH DEVELOP"/' .github/workflows/test-dispatch.yml

git add .
git commit -m "test: customiza workflow para branch develop"
git push origin develop
```

### Modificar workflow na feature

```bash
git checkout feat/test-dispatch-com-workflow

# Modificar mensagem para feature
sed -i 's/echo "🎯 WORKFLOW EXECUTADO COM SUCESSO"/echo "✨ WORKFLOW EXECUTADO NA BRANCH FEATURE"/' .github/workflows/test-dispatch.yml

git add .
git commit -m "test: customiza workflow para branch feature"
git push origin feat/test-dispatch-com-workflow
```

## 🔄 Comandos de Reset (caso precise recomeçar)

### Deletar branches remotas

```bash
git push origin --delete develop
git push origin --delete feat/test-dispatch-sem-workflow
git push origin --delete feat/test-dispatch-com-workflow
```

### Deletar branches locais

```bash
git branch -D develop
git branch -D feat/test-dispatch-sem-workflow
git branch -D feat/test-dispatch-com-workflow
```

### Restaurar workflow original

```bash
git checkout main
cp .github/workflows/test-dispatch.yml.backup .github/workflows/test-dispatch.yml
git add .
git commit -m "restore: volta workflow original"
git push origin main
```

## 🧪 Comandos de Verificação

### Verificar status atual

```bash
# Ver branch atual
git branch

# Ver branches remotas
git branch -r

# Ver últimos commits
git log --oneline -5

# Ver arquivos do workflow
ls -la .github/workflows/
```

### Verificar diferenças entre branches

```bash
# Comparar workflows entre branches
git checkout main
cat .github/workflows/test-dispatch.yml | head -20

git checkout develop
cat .github/workflows/test-dispatch.yml | head -20

git checkout feat/test-dispatch-com-workflow
cat .github/workflows/test-dispatch.yml | head -20
```

## 📊 Comandos para Análise dos Resultados

### Verificar execuções via API do GitHub (opcional)

```bash
# Listar workflows (precisa do GitHub CLI - gh)
gh workflow list

# Ver execuções recentes
gh run list --workflow="Test Workflow Dispatch"

# Ver detalhes de uma execução específica
gh run view [RUN_ID]
```

### Verificar logs localmente

```bash
# Ver estrutura de arquivos criados
find . -name "test-results" -type d
find . -name "*.txt" -o -name "*.json" | grep test-results
```

---

## 🎯 Checklist de Execução

Para cada experimento, execute na ordem:

1. **Experimento 1:**

   - [ ] Commit na main com workflow
   - [ ] Criar develop sem workflow
   - [ ] Criar feature sem workflow
   - [ ] Testar workflow_dispatch em cada branch

2. **Experimento 2:**

   - [ ] Merge workflow para develop
   - [ ] Criar feature com workflow
   - [ ] Testar workflow_dispatch em cada branch

3. **Experimento 3:**
   - [ ] Modificar workflow na main
   - [ ] Modificar workflow na develop
   - [ ] Modificar workflow na feature
   - [ ] Testar e comparar execuções

**Lembre-se:** Após cada push, vá para GitHub Actions e teste o workflow_dispatch! 🚀
