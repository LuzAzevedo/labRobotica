# Docker Tutorial - Instruções de Compilação

## Compilação Automática

O projeto está configurado para compilar automaticamente quando você salvar arquivos `.tex`.

### Pré-requisitos

1. **Instalar LaTeX**: 
   - Windows: Instale [MiKTeX](https://miktex.org/download) ou [TeX Live](https://www.tug.org/texlive/windows.html)
   - Certifique-se de que `pdflatex` está no PATH

2. **Instalar Extensão VS Code**:
   - A extensão `LaTeX Workshop` será sugerida automaticamente
   - Ou instale manualmente: `james-yu.latex-workshop`

### Como Usar

1. **Compilação Automática**:
   - Abra qualquer arquivo `.tex` no VS Code
   - Salve o arquivo (Ctrl+S)
   - O PDF será gerado automaticamente em alguns segundos
   - O PDF aparecerá na aba ao lado do editor

2. **Compilação Manual**:
   - Pressione `Ctrl+Shift+P`
   - Digite "LaTeX Workshop: Build LaTeX project"
   - Ou use a task: `Ctrl+Shift+B` (Build Task)

3. **Mudar de Aula**:
   - Edite `config.txt` e mude `AULA=docker_tutorial` para outra aula
   - Ou edite `main.tex` linha 3: `\def\aulanum{docker_tutorial}`

### Estrutura

- `main.tex` - Arquivo principal que compila a aula
- `docker_tutorial/docker_tutorial.tex` - Conteúdo dos slides
- `docker_tutorial/images/` - Imagens usadas nos slides
- `config.txt` - Define qual aula compilar

### Troubleshooting

Se a compilação automática não funcionar:
1. Verifique se o LaTeX está instalado: `pdflatex --version` no terminal
2. Verifique se a extensão LaTeX Workshop está instalada
3. Tente compilar manualmente com `Ctrl+Shift+B`
