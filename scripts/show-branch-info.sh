#!/bin/bash

echo "🔍 SCRIPT DE INFORMAÇÕES DA BRANCH 🔍"
echo "======================================"

# Informações básicas do Git
echo "📊 Informações do Git:"
echo "  - Branch atual: $(git branch --show-current 2>/dev/null || echo 'N/A')"
echo "  - Commit atual: $(git rev-parse --short HEAD 2>/dev/null || echo 'N/A')"
echo "  - Último commit: $(git log -1 --pretty=format:'%h - %s (%an, %ar)' 2>/dev/null || echo 'N/A')"

# Informações do ambiente
echo ""
echo "🖥️ Informações do Ambiente:"
echo "  - Sistema: $(uname -s)"
echo "  - Hostname: $(hostname)"
echo "  - Usuário: $(whoami)"
echo "  - Diretório: $(pwd)"

# Verificar arquivos do workflow
echo ""
echo "📁 Arquivos de Workflow:"
if [ -d ".github/workflows" ]; then
    echo "  ✅ Diretório .github/workflows existe"
    echo "  📄 Arquivos encontrados:"
    ls -la .github/workflows/ | sed 's/^/    /'
else
    echo "  ❌ Diretório .github/workflows NÃO encontrado"
fi

# Verificar se estamos em um repositório Git
echo ""
echo "🌿 Status do Repositório:"
if git status >/dev/null 2>&1; then
    echo "  ✅ Repositório Git válido"
    echo "  🔄 Status: $(git status --porcelain | wc -l) arquivo(s) modificado(s)"
    
    # Listar branches
    echo "  🌲 Branches disponíveis:"
    git branch -a 2>/dev/null | sed 's/^/    /' || echo "    Não foi possível listar branches"
else
    echo "  ❌ NÃO é um repositório Git válido"
fi

echo ""
echo "✅ Script executado com sucesso!"
echo "======================================"