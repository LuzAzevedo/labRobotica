#!/bin/bash
# Script para gerar imagens PNG a partir dos arquivos .tex de código

cd "$(dirname "$0")"

for texfile in code*.tex; do
    if [ -f "$texfile" ]; then
        basename="${texfile%.tex}"
        echo "Compilando $texfile..."
        
        # Compilar para PDF
        pdflatex -interaction=nonstopmode "$texfile" > /dev/null 2>&1
        
        if [ -f "${basename}.pdf" ]; then
            # Converter PDF para PNG com alta resolução
            pdftoppm -png -r 300 "${basename}.pdf" "${basename}" > /dev/null 2>&1
            
            # Renomear para .png
            if [ -f "${basename}-1.png" ]; then
                mv "${basename}-1.png" "${basename}.png"
                echo "✅ Gerado: ${basename}.png"
            fi
            
            # Limpar arquivos temporários
            rm -f "${basename}.pdf" "${basename}.aux" "${basename}.log" "${basename}.out"
        else
            echo "❌ Erro ao compilar $texfile"
        fi
    fi
done

echo "Concluído!"

