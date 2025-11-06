# Slides ROS2 - Sistema de Compilação de Aulas

## 🔨 Sistema de Build

### Compilação de Aulas LaTeX

Este projeto inclui um sistema simples para compilar qualquer aula (aula1, aula2, aula3, etc.) sem precisar navegar até cada pasta.

#### Método 1: Usando o arquivo de configuração (Recomendado)

1. Edite o arquivo `config.txt` na raiz do projeto:
   ```
   AULA=aula2
   ```

2. Execute o script de build:
   ```bash
   ./build.sh
   ```

#### Método 2: Especificando a aula diretamente

```bash
./build.sh aula1    # Compila a aula 1
./build.sh aula2    # Compila a aula 2
./build.sh aula3    # Compila a aula 3
```

O PDF será gerado na raiz do projeto como `main.pdf`, independente de qual aula foi compilada.

### Estrutura do Projeto

```
.
├── build.sh          # Script principal de compilação
├── config.txt        # Arquivo de configuração (defina AULA=aulaX)
├── main.pdf          # PDF gerado na raiz (sempre este nome)
├── aula1/
│   └── aula1.tex
├── aula2/
│   └── aula2.tex
└── aula3/
    └── aula3.tex
```

---

# Slides ROS2 - Aula 1: Visão Geral + Instalação

## 📋 Conteúdo dos Slides

Este conjunto de slides cobre a primeira aula do curso de ROS2, incluindo:

1. **Introdução ao ROS2** - O que é e principais características
2. **Grafo de Nós** - Conceito fundamental de comunicação distribuída
3. **DDS (Data Distribution Service)** - Middleware de comunicação
4. **Diferenças ROS1 vs ROS2** - Principais melhorias
5. **Escolhas de DDS** - Fast DDS vs CycloneDX
6. **Instalação ROS2 Humble** - Ubuntu 22.04
7. **Teste com Turtlesim** - Verificação da instalação
8. **ROS2 Doctor** - Ferramenta de diagnóstico
9. **Próximas Aulas** - Visão geral do curso completo

## 🚀 Como Usar os Slides

### Opção 1: Slides HTML (Recomendado)
```bash
# Executar o script para criar os slides HTML
python3 create_slides.py

# Abrir o arquivo HTML no navegador
firefox ros2_aula1_slides.html
# ou
google-chrome ros2_aula1_slides.html
```

### Opção 2: Manim Slides (Avançado)
```bash
# Instalar dependências (se necessário)
pip3 install manim manim-slides

# Executar os slides com Manim
manim-slides ros2_aula1 ROS2Aula1

# Apresentar os slides
manim-slides present ros2_aula1 ROS2Aula1
```

## 🎮 Controles de Navegação

### Slides HTML:
- **Setas do teclado**: ← → para navegar
- **Barra de espaço**: Próximo slide
- **Botões**: Usar os botões na parte inferior
- **F11**: Modo tela cheia

### Manim Slides:
- **Setas**: ← → para navegar
- **ESC**: Sair da apresentação
- **F**: Modo tela cheia

## 📁 Arquivos Incluídos

- `ros2_aula1.py` - Código fonte dos slides Manim
- `create_slides.py` - Script para gerar slides HTML
- `ros2_aula1_slides.html` - Slides HTML prontos para apresentação
- `README_slides.md` - Instruções básicas
- `README.md` - Este arquivo com instruções detalhadas

## 🎯 Objetivos da Aula

Ao final desta aula, os alunos devem:

- [ ] Entender o que é ROS2 e suas principais características
- [ ] Compreender o conceito de grafo de nós
- [ ] Saber explicar o papel do DDS na comunicação
- [ ] Conhecer as principais diferenças entre ROS1 e ROS2
- [ ] Ser capaz de instalar ROS2 Humble no Ubuntu 22.04
- [ ] Conseguir executar testes básicos com Turtlesim
- [ ] Usar ROS2 Doctor para diagnosticar problemas

## 🔧 Requisitos do Sistema

### Para Slides HTML:
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Python 3 (para gerar os slides)

### Para Manim Slides:
- Python 3.7+
- Manim e Manim Slides
- Bibliotecas gráficas (opcional)

## 📚 Recursos Adicionais

- [Documentação oficial ROS2](https://docs.ros.org/en/humble/)
- [Tutorial ROS2 Humble](https://docs.ros.org/en/humble/Tutorials.html)
- [ROS2 Installation Guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

## 🎨 Personalização

Os slides podem ser facilmente personalizados:

1. **Cores**: Modificar as variáveis CSS no arquivo HTML
2. **Conteúdo**: Editar o texto diretamente no HTML ou no código Python
3. **Layout**: Ajustar o CSS para diferentes tamanhos de tela
4. **Animações**: Adicionar transições CSS ou usar Manim para animações avançadas

## 📝 Notas para o Professor

- Os slides incluem comandos práticos que podem ser executados durante a aula
- Recomenda-se ter uma instalação ROS2 funcionando para demonstrações ao vivo
- O tempo estimado para esta aula é de 60-90 minutos
- Incluir exercícios práticos entre os slides para melhor engajamento

## 🐛 Solução de Problemas

### Problemas com Manim:
- Instalar dependências do sistema: `sudo apt install libpango1.0-dev libpangocairo-1.0-0`
- Usar versão mais simples: `pip install manim-slides --no-deps`

### Problemas com Slides HTML:
- Verificar se o navegador suporta JavaScript
- Usar servidor local se necessário: `python3 -m http.server 8000`

---

**Desenvolvido para o curso de ROS2 - 18 aulas**
**Versão: 1.0 | Data: 2024**
# labRobotica
