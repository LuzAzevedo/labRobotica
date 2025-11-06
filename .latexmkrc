# Configuração do latexmk para main.tex
# Este arquivo configura o latexmk para fazer múltiplas passagens
# e resolver todas as referências, incluindo bibtex quando necessário

$pdf_mode = 1;
$postscript_mode = 0;
$dvi_mode = 0;

# Usar bibtex quando necessário
$bibtex_use = 2;  # 2 = usar bibtex automaticamente quando encontrar \bibliography

# Fazer múltiplas passagens para resolver referências
$max_repeat = 8;

# Não parar em warnings - continuar mesmo com exit code != 0
$pdflatex = 'pdflatex -interaction=nonstopmode %O %S';
$pdflatex_silent = 'pdflatex -interaction=nonstopmode %O %S';

# Configurar bibtex
$bibtex = 'bibtex %O %S';

# Não tratar warnings como erros
$warnings_as_errors = 0;

# Forçar múltiplas passagens mesmo com referências não resolvidas
$force_mode = 1;

# Sequência de compilação: pdflatex -> bibtex -> pdflatex -> pdflatex
# O latexmk detecta automaticamente quando bibtex é necessário

# Limpar arquivos auxiliares após compilação bem-sucedida
$clean_ext = 'bbl synctex.gz';

