#!/bin/bash
# Script para preparar commit com apenas arquivos essenciais
# Uso: ./prepare_commit.sh

echo "📦 Preparando commit com arquivos essenciais..."
echo ""

# Verificar se é um repositório git
if [ ! -d .git ]; then
    echo "⚠️  Repositório Git não inicializado."
    echo "   Execute primeiro: git init"
    exit 1
fi

# Adicionar arquivos de configuração
echo "➕ Adicionando arquivos de configuração..."
git add .gitignore .latexmkrc

# Adicionar arquivos principais
echo "➕ Adicionando arquivos principais..."
git add main.tex build.sh config.txt

# Adicionar arquivos .tex das aulas
echo "➕ Adicionando arquivos .tex das aulas..."
git add aula*/aula*.tex
git add aula*/sections/*.tex 2>/dev/null

# Adicionar imagens
echo "➕ Adicionando imagens..."
git add aula*/images/*.png aula*/images/*.jpg aula*/images/*.jpeg aula*/images/*.tex 2>/dev/null

# Adicionar scripts e arquivos de código
echo "➕ Adicionando scripts e código..."
git add aula*/code_images/*.tex aula*/code_images/*.sh 2>/dev/null
git add *.py *.sh 2>/dev/null

# Adicionar documentação
echo "➕ Adicionando documentação..."
git add README*.md 2>/dev/null

# Adicionar .vscode/settings.json se existir
if [ -f .vscode/settings.json ]; then
    echo "➕ Adicionando .vscode/settings.json..."
    git add .vscode/settings.json
fi

echo ""
echo "✅ Arquivos essenciais adicionados!"
echo ""
echo "📋 Resumo dos arquivos que serão commitados:"
git status --short | head -50

echo ""
echo "💡 Para fazer o commit, execute:"
echo "   git commit -m 'Sua mensagem de commit'"
echo ""
echo "⚠️  Arquivos ignorados (não serão commitados):"
echo "   - Arquivos de build LaTeX (*.aux, *.log, *.out, etc.)"
echo "   - PDFs gerados (main.pdf)"
echo "   - Arquivos temporários"

