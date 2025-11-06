#!/bin/bash
# Script para compilar qualquer aula usando main.tex
# Uso: ./build.sh [aula1|aula2|aula3|aula4]
# Ou defina AULA no arquivo config.txt

CONFIG_FILE="config.txt"

# Função para ler configuração do arquivo
get_aula_from_config() {
    if [ -f "$CONFIG_FILE" ]; then
        grep "^AULA=" "$CONFIG_FILE" | cut -d'=' -f2 | tr -d ' ' | tr -d '\n'
    fi
}

# Determinar qual aula compilar
if [ -n "$1" ]; then
    # Se passou argumento, usa ele
    AULA="$1"
elif [ -f "$CONFIG_FILE" ]; then
    # Se não passou argumento, tenta ler do config.txt
    AULA=$(get_aula_from_config)
    if [ -z "$AULA" ]; then
        echo "❌ Erro: AULA não definida em $CONFIG_FILE"
        echo "Use: ./build.sh aula1 (ou aula2, aula3, aula4)"
        exit 1
    fi
else
    echo "❌ Erro: Especifique a aula ou crie o arquivo config.txt"
    echo "Uso: ./build.sh [aula1|aula2|aula3|aula4]"
    exit 1
fi

# Validar aula
if [ "$AULA" != "aula1" ] && [ "$AULA" != "aula2" ] && [ "$AULA" != "aula3" ] && [ "$AULA" != "aula4" ]; then
    echo "❌ Erro: Aula inválida: $AULA"
    echo "Aulas disponíveis: aula1, aula2, aula3, aula4"
    exit 1
fi

# Verificar se a pasta da aula existe
if [ ! -d "$AULA" ]; then
    echo "❌ Erro: Pasta $AULA não encontrada!"
    exit 1
fi

# Verificar se o arquivo .tex da aula existe
if [ ! -f "$AULA/$AULA.tex" ]; then
    echo "❌ Erro: Arquivo $AULA/$AULA.tex não encontrado!"
    exit 1
fi

# Verificar se main.tex existe
if [ ! -f "main.tex" ]; then
    echo "❌ Erro: Arquivo main.tex não encontrado!"
    exit 1
fi

echo "📚 Compilando $AULA usando main.tex..."
echo ""

# Guardar diretório raiz
ROOT_DIR="$(pwd)"

# Criar versão temporária do main.tex com a aula correta
sed "s/\\\\def\\\\\\\\aulanum{aula[0-9]}/\\\\def\\\\\\\\aulanum{$AULA}/" main.tex > main_temp.tex

echo "Compilando main.tex (primeira passagem)..."
pdflatex -interaction=nonstopmode -jobname=main main_temp.tex > /dev/null 2>&1

# Verificar se o PDF foi gerado (mesmo que exit code seja != 0 devido a warnings)
if [ ! -f "main.pdf" ]; then
    echo "❌ Erro na primeira compilação - PDF não foi gerado!"
    rm -f main_temp.tex
    exit 1
fi

# Fazer múltiplas passagens até resolver todas as referências
MAX_PASSES=6
PASS=2
while [ $PASS -le $MAX_PASSES ]; do
    echo "Compilando main.tex (passagem $PASS/$MAX_PASSES)..."
    pdflatex -interaction=nonstopmode -jobname=main main_temp.tex > /dev/null 2>&1
    
    # Verificar se ainda há referências não resolvidas
    if [ -f "main.log" ]; then
        UNDEFINED_REFS=$(grep -c "LaTeX Warning.*Reference.*undefined" main.log 2>/dev/null | head -1)
        if [ -z "$UNDEFINED_REFS" ] || [ "$UNDEFINED_REFS" = "0" ]; then
            echo "Todas as referências foram resolvidas na passagem $PASS"
            break
        fi
    fi
    
    PASS=$((PASS + 1))
done

# Limpar arquivo temporário
rm -f main_temp.tex

# Verificar se o PDF foi gerado (mesmo que exit code seja != 0 devido a warnings)
if [ -f "main.pdf" ]; then
    echo ""
    echo "✅ Compilação bem-sucedida!"
    echo "📄 Arquivo gerado: $ROOT_DIR/main.pdf"
else
    echo ""
    echo "❌ Erro: PDF não foi gerado!"
    exit 1
fi
