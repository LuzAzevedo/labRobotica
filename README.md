# Slides ROS 2 - UFJF

Sistema de slides para aulas de ROS 2 usando LaTeX/Beamer com compilação centralizada.

## 📋 Estrutura do Projeto

```
.
├── main.tex              # Arquivo principal de compilação
├── aula1/                # Conteúdo da Aula 1
│   ├── aula1.tex
│   ├── images/
│   └── sections/
├── aula2/                # Conteúdo da Aula 2
│   ├── aula2.tex
│   └── images/
├── aula3/                # Conteúdo da Aula 3
│   ├── aula3.tex
│   └── images/
└── aula4/                # Conteúdo da Aula 4
    ├── aula4.tex
    ├── images/
    └── code_images/
```

## 🚀 Como Compilar

1. **Altere a variável de aula no `main.tex`**:
   ```latex
   % Abra main.tex e altere a linha 4:
   \def\aulanum{aula1}  # Mude para aula1, aula2, aula3 ou aula4
   ```

2. **Compile o documento**:

   **Opção A: Usando LaTeX Workshop no VS Code (Recomendado)**
   - Abra `main.tex` no VS Code
   - Pressione `Ctrl+Alt+B` (ou use o botão "Build LaTeX project")
   - O PDF será gerado automaticamente como `main.pdf`

   **Opção B: Compilação manual via terminal**
   ```bash
   pdflatex main.tex
   pdflatex main.tex  # Repita até resolver todas as referências
   ```

   O PDF será gerado como `main.pdf` na raiz do projeto.

## 📦 Pré-requisitos e Instalação

### 1. Instalar LaTeX (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended latexmk
```

**Pacotes adicionais (se necessário):**
```bash
sudo apt install -y texlive-lang-portuguese texlive-bibtex-extra \
  texlive-publishers texlive-science
```

### 2. Instalar extensão LaTeX no VS Code

1. Abra o VS Code
2. Vá em **Extensions** (Ctrl+Shift+X)
3. Procure por **"LaTeX Workshop"** (por James Yu)
4. Clique em **Install**

### 3. Configuração do LaTeX Workshop (Opcional)

O arquivo `.vscode/settings.json` já está configurado com:
- Compilação automática usando `latexmk`
- Suporte a BibTeX
- Visualização de PDF integrada

### 4. Bibliotecas Python (se usar scripts auxiliares)

```bash
pip install -r requirements.txt  # Se houver
```

## 🛠️ Dependências do Projeto

### Pacotes LaTeX necessários:
- `beamer` - Classe para apresentações
- `listings` - Highlight de código
- `graphicx` - Inclusão de imagens
- `hyperref` - Links e referências
- `tikz` - Desenhos vetoriais
- `xcolor` - Cores
- `colortbl` - Tabelas coloridas
- `accsupp` - Suporte a acessibilidade
- `ragged2e` - Alinhamento de texto

Todos esses pacotes estão incluídos na instalação recomendada acima.

## 📝 Como Adicionar uma Nova Aula

1. Crie a pasta `aula5/` na raiz
2. Crie `aula5/aula5.tex` com a estrutura:
   ```latex
   % ---------- Metadata ----------
   \title[Aula 5]{Título da Aula 5}
   \author[Marcato]{Professor: André L. Marcato}
   \institute[UFJF]{Universidade Federal de Juiz de Fora \\ Engenharia Elétrica — Robótica e Automação Industrial}
   
   % ---------- Title ----------
   \begin{frame}
     \titlepage
   \end{frame}
   
   % ... conteúdo dos slides ...
   ```

3. Crie a pasta `aula5/images/` para as imagens
4. Altere `\def\aulanum{aula5}` no `main.tex` (linha 4)
5. Compile o `main.tex` usando LaTeX Workshop ou `pdflatex`

## 🎨 Formatação

O `main.tex` define:
- Tema Beamer (Boadilla)
- Cores personalizadas (UFJF)
- Estilos de código (Python, Bash)
- Configurações de paths para imagens e includes

Cada `aulaX.tex` contém apenas:
- Metadados (título, autor, instituto)
- Conteúdo dos slides (frames, seções)

## 📄 Output

O PDF gerado (`main.pdf`) fica na raiz do projeto, não dentro das pastas das aulas.

## 🔧 Troubleshooting

### Erro: "Command not found: pdflatex"
- Instale o TeX Live: `sudo apt install -y texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk`

### Erro: "Package not found"
- Instale pacotes específicos adicionais conforme necessário

### Erro: "Reference undefined"
- Execute múltiplas passagens do pdflatex (o LaTeX Workshop faz isso automaticamente)

### Imagens não aparecem
- Verifique se as imagens estão em `aulaX/images/`
- Use apenas o nome do arquivo em `\includegraphics`, sem o prefixo `images/`

## 📚 Recursos

- [Documentação ROS 2](https://docs.ros.org/)
- [Beamer User Guide](https://ctan.org/pkg/beamer)
- [LaTeX Workshop Extension](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
