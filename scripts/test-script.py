#!/usr/bin/env python3
"""
Script de teste para demonstrar informações do ambiente Python
e validar a execução do workflow_dispatch
"""

import os
import sys
import json
from datetime import datetime

def print_header(title):
    """Imprime um cabeçalho formatado"""
    print(f"\n🐍 {title} 🐍")
    print("=" * (len(title) + 6))

def get_env_info():
    """Coleta informações do ambiente"""
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "executable": sys.executable,
        "path": sys.path[:3],  # Primeiros 3 paths
        "cwd": os.getcwd(),
        "timestamp": datetime.now().isoformat()
    }

def get_github_context():
    """Coleta informações do contexto do GitHub Actions"""
    github_env = {}
    github_vars = [
        'GITHUB_ACTIONS',
        'GITHUB_REPOSITORY',
        'GITHUB_REF_NAME', 
        'GITHUB_SHA',
        'GITHUB_ACTOR',
        'GITHUB_EVENT_NAME',
        'GITHUB_RUN_ID',
        'GITHUB_RUN_NUMBER',
        'GITHUB_WORKFLOW'
    ]
    
    for var in github_vars:
        github_env[var] = os.environ.get(var, 'N/A')
    
    return github_env

def check_workflow_files():
    """Verifica a existência de arquivos de workflow"""
    workflow_dir = '.github/workflows'
    workflow_info = {
        "directory_exists": os.path.exists(workflow_dir),
        "files": []
    }
    
    if workflow_info["directory_exists"]:
        try:
            files = os.listdir(workflow_dir)
            workflow_info["files"] = [f for f in files if f.endswith(('.yml', '.yaml'))]
        except Exception as e:
            workflow_info["error"] = str(e)
    
    return workflow_info

def main():
    print_header("SCRIPT DE TESTE PYTHON - WORKFLOW DISPATCH")
    
    # Informações do ambiente Python
    print_header("Informações do Ambiente Python")
    env_info = get_env_info()
    for key, value in env_info.items():
        if key == "python_version":
            # Mostrar apenas a primeira linha da versão
            version_line = str(value).split('\n')[0]
            print(f"  📋 {key}: {version_line}")
        elif key == "path":
            print(f"  📋 {key}: {value[0]} (e mais {len(sys.path)-1} caminhos)")
        else:
            print(f"  📋 {key}: {value}")
    
    # Contexto do GitHub Actions
    print_header("Contexto do GitHub Actions")
    github_info = get_github_context()
    
    if github_info.get('GITHUB_ACTIONS') == 'true':
        print("  ✅ Executando no GitHub Actions")
        for key, value in github_info.items():
            if key != 'GITHUB_ACTIONS':
                print(f"  🔧 {key}: {value}")
    else:
        print("  ℹ️ NÃO está executando no GitHub Actions")
        print("  🖥️ Executando localmente")
    
    # Verificar arquivos de workflow
    print_header("Verificação de Arquivos de Workflow")
    workflow_info = check_workflow_files()
    
    if workflow_info["directory_exists"]:
        print("  ✅ Diretório .github/workflows encontrado")
        if workflow_info["files"]:
            print(f"  📄 Arquivos encontrados: {len(workflow_info['files'])}")
            for file in workflow_info["files"]:
                print(f"    - {file}")
        else:
            print("  ⚠️ Nenhum arquivo .yml/.yaml encontrado")
    else:
        print("  ❌ Diretório .github/workflows NÃO encontrado")
    
    # Teste específico para branches
    print_header("Teste Específico por Branch")
    current_branch = github_info.get('GITHUB_REF_NAME', 'unknown')
    
    branch_messages = {
        'main': '🎯 Branch MAIN detectada - Ambiente de PRODUÇÃO',
        'develop': '🛠️ Branch DEVELOP detectada - Ambiente de DESENVOLVIMENTO', 
    }
    
    if current_branch in branch_messages:
        print(f"  {branch_messages[current_branch]}")
    elif current_branch.startswith('feat/'):
        print(f"  ✨ Branch FEATURE detectada ({current_branch}) - Branch temporária")
    else:
        print(f"  ❓ Branch não mapeada: {current_branch}")
    
    # Salvar informações em arquivo JSON
    print_header("Salvando Resultados")
    
    result_data = {
        "environment": env_info,
        "github_context": github_info,
        "workflow_files": workflow_info,
        "test_status": "completed_successfully"
    }
    
    try:
        os.makedirs('test-results', exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f'test-results/python-test-{timestamp}.json'
        
        with open(filename, 'w') as f:
            json.dump(result_data, f, indent=2)
        
        print(f"  💾 Dados salvos em: {filename}")
        print(f"  📊 Tamanho do arquivo: {os.path.getsize(filename)} bytes")
        
    except Exception as e:
        print(f"  ❌ Erro ao salvar: {e}")
    
    print_header("TESTE CONCLUÍDO COM SUCESSO")
    print("✅ Todos os testes foram executados")
    print("📊 Verifique os logs acima para análise detalhada")
    print("🚀 Workflow_dispatch funcionando corretamente nesta branch!")

if __name__ == "__main__":
    main()