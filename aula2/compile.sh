#!/bin/bash
# Script para compilar aula2.tex
# Uso: ./compile.sh

echo "Compilando aula2.tex (primeira passagem)..."
pdflatex -interaction=nonstopmode aula2.tex

if [ $? -ne 0 ]; then
    echo "❌ Erro na primeira compilação!"
    exit 1
fi

echo "Compilando aula2.tex (segunda passagem para referências)..."
pdflatex -interaction=nonstopmode aula2.tex

if [ $? -eq 0 ]; then
    echo "✅ Compilação bem-sucedida!"
    echo "📄 Arquivo gerado: aula2.pdf"
else
    echo "❌ Erro na compilação!"
    exit 1
fi
