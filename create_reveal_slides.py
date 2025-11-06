#!/usr/bin/env python3
"""
Gerador de Slides ROS2 - Versão para PDF/PPT
Usa bibliotecas Python para criar slides em formato de apresentação
"""

import os
from datetime import datetime

def create_revealjs_slides():
    """Cria slides usando Reveal.js para apresentação web"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROS2 - Aula 1: Visão Geral + Instalação</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/theme/white.css">
    <style>
        :root {{
            --ufjf-dark: #383435;
            --ufjf-red: #AF1E23;
            --ufjf-gray: #676767;
        }}
        
        .reveal {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        
        .reveal h1, .reveal h2 {{
            color: var(--ufjf-dark);
            text-transform: none;
        }}
        
        .reveal h3 {{
            color: var(--ufjf-red);
            text-transform: none;
        }}
        
        .reveal .slides section {{
            text-align: left;
        }}
        
        .reveal .slides section[data-background] {{
            text-align: center;
        }}
        
        .ufjf-header {{
            background: var(--ufjf-dark);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        
        .code-block {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 0.8em;
            border-left: 4px solid var(--ufjf-red);
        }}
        
        .comparison-table {{
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
        }}
        
        .comparison-column {{
            flex: 1;
            margin: 0 20px;
            padding: 20px;
            border-radius: 10px;
        }}
        
        .ros1-column {{
            background: #f5f5f5;
            border-left: 5px solid var(--ufjf-gray);
        }}
        
        .ros2-column {{
            background: #f0f0f0;
            border-left: 5px solid var(--ufjf-dark);
        }}
        
        .node-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .node-card {{
            background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
            padding: 20px;
            border-radius: 15px;
            border: 3px solid var(--ufjf-dark);
            position: relative;
            text-align: center;
        }}
        
        .node-tag {{
            position: absolute;
            top: -10px;
            right: -10px;
            background: var(--ufjf-red);
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8em;
        }}
        
        .comm-types {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin: 20px 0;
        }}
        
        .comm-type {{
            background: var(--ufjf-red);
            color: white;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        
        .comm-type:nth-child(2) {{
            background: var(--ufjf-gray);
        }}
        
        .comm-type:nth-child(3) {{
            background: var(--ufjf-dark);
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Slide 1: Título -->
            <section data-background="linear-gradient(135deg, #383435 0%, #676767 100%)">
                <div class="ufjf-header">
                    <h2 style="color: white; margin: 0;">UNIVERSIDADE FEDERAL DE JUIZ DE FORA</h2>
                    <p style="color: #cccccc; margin: 5px 0 0 0;">Engenharia Elétrica - Robótica e Automação Industrial</p>
                </div>
                <h1 style="color: white; font-size: 3em;">🤖 ROS2</h1>
                <h2 style="color: white;">Introdução ao ROS2</h2>
                <h3 style="color: white;">Aula 1: Visão Geral + Instalação</h3>
                <div style="background: #AF1E23; color: white; padding: 10px 20px; border-radius: 5px; display: inline-block; margin-top: 30px;">
                    <p style="margin: 0;">Professor: André Marcato | Semestre: 2025.2</p>
                </div>
            </section>

            <!-- Slide 2: O que é ROS2 -->
            <section>
                <h1>O que é ROS2?</h1>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Robot Operating System 2</h3>
                    <p>Framework de software para desenvolvimento de aplicações robóticas distribuídas</p>
                </div>
                
                <h3>Principais características:</h3>
                <ul>
                    <li><strong>Comunicação entre processos</strong> - Nós independentes</li>
                    <li><strong>Gerenciamento de dependências</strong> - Pacotes modulares</li>
                    <li><strong>Ferramentas de desenvolvimento</strong> - Debugging e profiling</li>
                    <li><strong>Bibliotecas reutilizáveis</strong> - Código compartilhado</li>
                    <li><strong>Multi-plataforma</strong> - Linux, Windows, macOS</li>
                </ul>
            </section>

            <!-- Slide 3: Grafo de Nós -->
            <section>
                <h1>Grafo de Nós ROS2</h1>
                
                <div class="node-grid">
                    <div class="node-card">
                        <h3 style="color: var(--ufjf-dark); margin: 0;">Sensor Node</h3>
                        <p style="color: var(--ufjf-gray); margin: 10px 0 0 0; font-size: 0.9em;">Coleta dados dos sensores</p>
                        <div class="node-tag">Publisher</div>
                    </div>
                    
                    <div class="node-card">
                        <h3 style="color: var(--ufjf-dark); margin: 0;">Control Node</h3>
                        <p style="color: var(--ufjf-gray); margin: 10px 0 0 0; font-size: 0.9em;">Processa comandos</p>
                        <div class="node-tag">Subscriber</div>
                    </div>
                    
                    <div class="node-card">
                        <h3 style="color: var(--ufjf-dark); margin: 0;">Planning Node</h3>
                        <p style="color: var(--ufjf-gray); margin: 10px 0 0 0; font-size: 0.9em;">Planeja trajetórias</p>
                        <div class="node-tag">Service</div>
                    </div>
                    
                    <div class="node-card">
                        <h3 style="color: var(--ufjf-dark); margin: 0;">Actuator Node</h3>
                        <p style="color: var(--ufjf-gray); margin: 10px 0 0 0; font-size: 0.9em;">Controla motores</p>
                        <div class="node-tag">Client</div>
                    </div>
                </div>
                
                <div class="comm-types">
                    <div class="comm-type">Tópicos</div>
                    <div class="comm-type">Serviços</div>
                    <div class="comm-type">Ações</div>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Características do Grafo de Nós:</h3>
                    <ul>
                        <li><strong>Nós independentes</strong> - Processos separados que executam simultaneamente</li>
                        <li><strong>Comunicação assíncrona</strong> - Tópicos para dados contínuos</li>
                        <li><strong>Comunicação síncrona</strong> - Serviços para requisições pontuais</li>
                        <li><strong>Descoberta automática</strong> - DDS encontra nós automaticamente</li>
                        <li><strong>Escalabilidade</strong> - Fácil adicionar/remover nós</li>
                    </ul>
                </div>
            </section>

            <!-- Slide 4: ROS1 vs ROS2 -->
            <section>
                <h1>ROS1 vs ROS2</h1>
                <div class="comparison-table">
                    <div class="comparison-column ros1-column">
                        <h3 style="color: var(--ufjf-gray);">ROS1</h3>
                        <ul>
                            <li>Master único</li>
                            <li>TCP/UDP</li>
                            <li>Python 2</li>
                            <li>Sem QoS</li>
                            <li>Linux apenas</li>
                        </ul>
                    </div>
                    <div class="comparison-column ros2-column">
                        <h3 style="color: var(--ufjf-dark);">ROS2</h3>
                        <ul>
                            <li>DDS distribuído</li>
                            <li>DDS nativo</li>
                            <li>Python 3</li>
                            <li>QoS configurável</li>
                            <li>Multi-plataforma</li>
                        </ul>
                    </div>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Principais melhorias:</h3>
                    <ul>
                        <li><strong>Comunicação mais robusta</strong></li>
                        <li><strong>Melhor performance em tempo real</strong></li>
                        <li><strong>Suporte a múltiplas plataformas</strong></li>
                    </ul>
                </div>
            </section>

            <!-- Slide 5: DDS -->
            <section>
                <h1>DDS - Data Distribution Service</h1>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Padrão de middleware para comunicação distribuída em tempo real</h3>
                </div>
                
                <h3>Características do DDS:</h3>
                <ul>
                    <li><strong>Comunicação publisher-subscriber</strong></li>
                    <li><strong>Descoberta automática de serviços</strong></li>
                    <li><strong>Qualidade de serviço (QoS)</strong></li>
                    <li><strong>Suporte a múltiplas plataformas</strong></li>
                    <li><strong>Comunicação em tempo real</strong></li>
                </ul>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>ROS2 usa DDS para:</h3>
                    <ul>
                        <li>Comunicação robusta entre nós</li>
                        <li>Descoberta automática de tópicos</li>
                        <li>Configuração de QoS</li>
                    </ul>
                </div>
            </section>

            <!-- Slide 6: Escolhas de DDS -->
            <section>
                <h1>Escolhas de DDS no ROS2</h1>
                
                <div style="display: flex; justify-content: space-around; margin: 30px 0;">
                    <div style="flex: 1; margin: 0 20px; padding: 20px; background: #f0f0f0; border-radius: 10px; border-left: 5px solid var(--ufjf-dark);">
                        <h3 style="color: var(--ufjf-dark);">Fast DDS</h3>
                        <ul>
                            <li><strong>Padrão no ROS2 Humble</strong></li>
                            <li>Desenvolvido pela eProsima</li>
                            <li>Alta performance</li>
                            <li>Suporte completo a QoS</li>
                        </ul>
                    </div>
                    <div style="flex: 1; margin: 0 20px; padding: 20px; background: #f5f5f5; border-radius: 10px; border-left: 5px solid var(--ufjf-gray);">
                        <h3 style="color: var(--ufjf-gray);">CycloneDX</h3>
                        <ul>
                            <li>Alternativa leve</li>
                            <li>Desenvolvido pela Eclipse</li>
                            <li>Menor overhead</li>
                            <li>Boa para sistemas embarcados</li>
                        </ul>
                    </div>
                </div>
                
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Impacto da escolha:</h3>
                    <ul>
                        <li><strong>Performance de comunicação</strong></li>
                        <li><strong>Uso de recursos</strong></li>
                        <li><strong>Compatibilidade com hardware</strong></li>
                    </ul>
                </div>
            </section>

            <!-- Slide 7: Instalação -->
            <section>
                <h1>Instalação ROS2 Humble</h1>
                <h2>Ubuntu 22.04 LTS</h2>
                
                <h3>Passos da instalação:</h3>
                <ul>
                    <li>Configurar repositório apt</li>
                    <li>Instalar chaves GPG</li>
                    <li>Atualizar lista de pacotes</li>
                    <li>Instalar ROS2 Humble</li>
                    <li>Configurar ambiente</li>
                </ul>
                
                <div class="code-block">
# 1. Configurar repositório
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe

# 2. Instalar ROS2 Humble
sudo apt install ros-humble-desktop

# 3. Configurar ambiente
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc
                </div>
            </section>

            <!-- Slide 8: Turtlesim -->
            <section>
                <h1>Teste com Turtlesim</h1>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Turtlesim é um simulador simples para testar a instalação do ROS2</h3>
                </div>
                
                <h3>Passos do teste:</h3>
                <ul>
                    <li><strong>Terminal 1:</strong> <code>ros2 run turtlesim turtlesim_node</code></li>
                    <li><strong>Terminal 2:</strong> <code>ros2 run turtlesim turtle_teleop_key</code></li>
                    <li>Usar setas para mover a tartaruga</li>
                    <li>Verificar comunicação entre nós</li>
                </ul>
                
                <div class="code-block">
# Terminal 1 - Executar simulador
ros2 run turtlesim turtlesim_node

# Terminal 2 - Executar controle
ros2 run turtlesim turtle_teleop_key
                </div>
            </section>

            <!-- Slide 9: ROS2 Doctor -->
            <section>
                <h1>ROS2 Doctor</h1>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <h3>Ferramenta de diagnóstico que verifica a saúde da instalação do ROS2</h3>
                </div>
                
                <h3>Verificações realizadas:</h3>
                <ul>
                    <li><strong>Configuração do ambiente</strong></li>
                    <li><strong>Variáveis de ambiente</strong></li>
                    <li><strong>Conectividade de rede</strong></li>
                    <li><strong>Configuração de DDS</strong></li>
                    <li><strong>Permissões de arquivo</strong></li>
                </ul>
                
                <div class="code-block">
# Executar diagnóstico completo
ros2 doctor

# Verificar problemas específicos
ros2 doctor --report
                </div>
            </section>

            <!-- Slide 10: Próximas Aulas -->
            <section>
                <h1>Próximas Aulas</h1>
                <div style="columns: 2; column-gap: 40px;">
                    <ul>
                        <li><strong>Aula 2:</strong> Conceitos básicos (Nós, Tópicos, Serviços)</li>
                        <li><strong>Aula 3:</strong> Workspace e pacotes</li>
                        <li><strong>Aula 4:</strong> Publishers e Subscribers</li>
                        <li><strong>Aula 5:</strong> Services e Clients</li>
                        <li><strong>Aula 6:</strong> Actions</li>
                        <li><strong>Aula 7:</strong> Launch files</li>
                        <li><strong>Aula 8:</strong> Parâmetros</li>
                        <li><strong>Aula 9:</strong> Logging e Debugging</li>
                        <li><strong>Aula 10:</strong> TF2 - Transformações</li>
                    </ul>
                    <ul>
                        <li><strong>Aula 11:</strong> URDF - Modelagem de robôs</li>
                        <li><strong>Aula 12:</strong> Gazebo - Simulação</li>
                        <li><strong>Aula 13:</strong> Navigation Stack</li>
                        <li><strong>Aula 14:</strong> MoveIt - Manipulação</li>
                        <li><strong>Aula 15:</strong> ROS2 Bridge</li>
                        <li><strong>Aula 16:</strong> Segurança</li>
                        <li><strong>Aula 17:</strong> Performance e Otimização</li>
                        <li><strong>Aula 18:</strong> Projeto Final</li>
                    </ul>
                </div>
            </section>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.3.1/dist/reveal.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            transition: 'slide',
            transitionSpeed: 'default',
            backgroundTransition: 'fade',
            controls: true,
            progress: true,
            center: true,
            touch: true,
            loop: false,
            rtl: false,
            navigationMode: 'default',
            shuffle: false,
            fragments: true,
            fragmentInURL: false,
            embedded: false,
            help: true,
            showNotes: false,
            autoPlayMedia: null,
            preloadIframes: null,
            autoSlide: 0,
            autoSlideStoppable: true,
            autoSlideMethod: null,
            defaultTiming: null,
            mouseWheel: false,
            previewLinks: false,
            postMessage: true,
            postMessageEvents: false,
            focusBodyOnPageVisibilityChange: true,
            width: 960,
            height: 700,
            margin: 0.1,
            minScale: 0.2,
            maxScale: 1.5,
            disableLayout: false
        }});
    </script>
</body>
</html>"""
    
    return html_content

def create_pdf_html():
    """Cria HTML simplificado específico para PDF"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>ROS2 - Aula 1: Visão Geral + Instalação</title>
</head>
<body>
    <!-- Slide 1: Título -->
    <div class="slide">
        <div class="ufjf-header">
            <h2>UNIVERSIDADE FEDERAL DE JUIZ DE FORA</h2>
            <p>Engenharia Elétrica - Robótica e Automação Industrial</p>
        </div>
        <h1>🤖 ROS2</h1>
        <h2>Introdução ao ROS2</h2>
        <h3>Aula 1: Visão Geral + Instalação</h3>
        <div style="background: #AF1E23; color: white; padding: 8px 15px; border-radius: 5px; display: inline-block; margin-top: 20px;">
            <p style="margin: 0;">Professor: André Marcato | Semestre: 2025.2</p>
        </div>
    </div>

    <!-- Slide 2: O que é ROS2 -->
    <div class="slide">
        <h1>O que é ROS2?</h1>
        <div class="feature-list">
            <h3>Robot Operating System 2</h3>
            <p>Framework de software para desenvolvimento de aplicações robóticas distribuídas</p>
        </div>
        
        <h3>Principais características:</h3>
        <ul>
            <li><span class="highlight">Comunicação entre processos</span> - Nós independentes</li>
            <li><span class="highlight">Gerenciamento de dependências</span> - Pacotes modulares</li>
            <li><span class="highlight">Ferramentas de desenvolvimento</span> - Debugging e profiling</li>
            <li><span class="highlight">Bibliotecas reutilizáveis</span> - Código compartilhado</li>
            <li><span class="highlight">Multi-plataforma</span> - Linux, Windows, macOS</li>
        </ul>
    </div>

    <!-- Slide 3: Grafo de Nós -->
    <div class="slide">
        <h1>Grafo de Nós ROS2</h1>
        
        <div class="node-grid">
            <div class="node-card">
                <h3>Sensor Node</h3>
                <p>Coleta dados dos sensores</p>
                <div class="node-tag">Publisher</div>
            </div>
            
            <div class="node-card">
                <h3>Control Node</h3>
                <p>Processa comandos</p>
                <div class="node-tag">Subscriber</div>
            </div>
            
            <div class="node-card">
                <h3>Planning Node</h3>
                <p>Planeja trajetórias</p>
                <div class="node-tag">Service</div>
            </div>
            
            <div class="node-card">
                <h3>Actuator Node</h3>
                <p>Controla motores</p>
                <div class="node-tag">Client</div>
            </div>
        </div>
        
        <div class="comm-types">
            <div class="comm-type">Tópicos</div>
            <div class="comm-type">Serviços</div>
            <div class="comm-type">Ações</div>
        </div>
        
        <div class="feature-list">
            <h3>Características do Grafo de Nós:</h3>
            <ul>
                <li><span class="highlight">Nós independentes</span> - Processos separados que executam simultaneamente</li>
                <li><span class="highlight">Comunicação assíncrona</span> - Tópicos para dados contínuos</li>
                <li><span class="highlight">Comunicação síncrona</span> - Serviços para requisições pontuais</li>
                <li><span class="highlight">Descoberta automática</span> - DDS encontra nós automaticamente</li>
                <li><span class="highlight">Escalabilidade</span> - Fácil adicionar/remover nós</li>
            </ul>
        </div>
    </div>

    <!-- Slide 4: ROS1 vs ROS2 -->
    <div class="slide">
        <h1>ROS1 vs ROS2</h1>
        <div class="comparison-table">
            <div class="comparison-column ros1-column">
                <h3>ROS1</h3>
                <ul>
                    <li>Master único</li>
                    <li>TCP/UDP</li>
                    <li>Python 2</li>
                    <li>Sem QoS</li>
                    <li>Linux apenas</li>
                </ul>
            </div>
            <div class="comparison-column ros2-column">
                <h3>ROS2</h3>
                <ul>
                    <li>DDS distribuído</li>
                    <li>DDS nativo</li>
                    <li>Python 3</li>
                    <li>QoS configurável</li>
                    <li>Multi-plataforma</li>
                </ul>
            </div>
        </div>
        
        <div class="feature-list">
            <h3>Principais melhorias:</h3>
            <ul>
                <li><span class="highlight">Comunicação mais robusta</span></li>
                <li><span class="highlight">Melhor performance em tempo real</span></li>
                <li><span class="highlight">Suporte a múltiplas plataformas</span></li>
            </ul>
        </div>
    </div>

    <!-- Slide 5: DDS -->
    <div class="slide">
        <h1>DDS - Data Distribution Service</h1>
        <div class="feature-list">
            <h3>Padrão de middleware para comunicação distribuída em tempo real</h3>
        </div>
        
        <h3>Características do DDS:</h3>
        <ul>
            <li><span class="highlight">Comunicação publisher-subscriber</span></li>
            <li><span class="highlight">Descoberta automática de serviços</span></li>
            <li><span class="highlight">Qualidade de serviço (QoS)</span></li>
            <li><span class="highlight">Suporte a múltiplas plataformas</span></li>
            <li><span class="highlight">Comunicação em tempo real</span></li>
        </ul>
        
        <div class="feature-list">
            <h3>ROS2 usa DDS para:</h3>
            <ul>
                <li>Comunicação robusta entre nós</li>
                <li>Descoberta automática de tópicos</li>
                <li>Configuração de QoS</li>
            </ul>
        </div>
    </div>

    <!-- Slide 6: Escolhas de DDS -->
    <div class="slide">
        <h1>Escolhas de DDS no ROS2</h1>
        
        <div style="display: flex; justify-content: space-around; margin: 15px 0;">
            <div style="flex: 1; margin: 0 10px; padding: 15px; background: #f0f0f0; border-radius: 5px; border-left: 3px solid #383435;">
                <h3>Fast DDS</h3>
                <ul>
                    <li><strong>Padrão no ROS2 Humble</strong></li>
                    <li>Desenvolvido pela eProsima</li>
                    <li>Alta performance</li>
                    <li>Suporte completo a QoS</li>
                </ul>
            </div>
            <div style="flex: 1; margin: 0 10px; padding: 15px; background: #f5f5f5; border-radius: 5px; border-left: 3px solid #676767;">
                <h3>CycloneDX</h3>
                <ul>
                    <li>Alternativa leve</li>
                    <li>Desenvolvido pela Eclipse</li>
                    <li>Menor overhead</li>
                    <li>Boa para sistemas embarcados</li>
                </ul>
            </div>
        </div>
        
        <div class="feature-list">
            <h3>Impacto da escolha:</h3>
            <ul>
                <li><span class="highlight">Performance de comunicação</span></li>
                <li><span class="highlight">Uso de recursos</span></li>
                <li><span class="highlight">Compatibilidade com hardware</span></li>
            </ul>
        </div>
    </div>

    <!-- Slide 7: Instalação -->
    <div class="slide">
        <h1>Instalação ROS2 Humble</h1>
        <h2>Ubuntu 22.04 LTS</h2>
        
        <h3>Passos da instalação:</h3>
        <ul>
            <li>Configurar repositório apt</li>
            <li>Instalar chaves GPG</li>
            <li>Atualizar lista de pacotes</li>
            <li>Instalar ROS2 Humble</li>
            <li>Configurar ambiente</li>
        </ul>
        
        <div class="code-block">
# 1. Configurar repositório
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe

# 2. Instalar ROS2 Humble
sudo apt install ros-humble-desktop

# 3. Configurar ambiente
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
source ~/.bashrc
        </div>
    </div>

    <!-- Slide 8: Turtlesim -->
    <div class="slide">
        <h1>Teste com Turtlesim</h1>
        <div class="feature-list">
            <h3>Turtlesim é um simulador simples para testar a instalação do ROS2</h3>
        </div>
        
        <h3>Passos do teste:</h3>
        <ul>
            <li><strong>Terminal 1:</strong> <code>ros2 run turtlesim turtlesim_node</code></li>
            <li><strong>Terminal 2:</strong> <code>ros2 run turtlesim turtle_teleop_key</code></li>
            <li>Usar setas para mover a tartaruga</li>
            <li>Verificar comunicação entre nós</li>
        </ul>
        
        <div class="code-block">
# Terminal 1 - Executar simulador
ros2 run turtlesim turtlesim_node

# Terminal 2 - Executar controle
ros2 run turtlesim turtle_teleop_key
        </div>
    </div>

    <!-- Slide 9: ROS2 Doctor -->
    <div class="slide">
        <h1>ROS2 Doctor</h1>
        <div class="feature-list">
            <h3>Ferramenta de diagnóstico que verifica a saúde da instalação do ROS2</h3>
        </div>
        
        <h3>Verificações realizadas:</h3>
        <ul>
            <li><span class="highlight">Configuração do ambiente</span></li>
            <li><span class="highlight">Variáveis de ambiente</span></li>
            <li><span class="highlight">Conectividade de rede</span></li>
            <li><span class="highlight">Configuração de DDS</span></li>
            <li><span class="highlight">Permissões de arquivo</span></li>
        </ul>
        
        <div class="code-block">
# Executar diagnóstico completo
ros2 doctor

# Verificar problemas específicos
ros2 doctor --report
        </div>
    </div>

    <!-- Slide 10: Próximas Aulas -->
    <div class="slide">
        <h1>Próximas Aulas</h1>
        <div style="columns: 2; column-gap: 30px;">
            <ul>
                <li><strong>Aula 2:</strong> Conceitos básicos (Nós, Tópicos, Serviços)</li>
                <li><strong>Aula 3:</strong> Workspace e pacotes</li>
                <li><strong>Aula 4:</strong> Publishers e Subscribers</li>
                <li><strong>Aula 5:</strong> Services e Clients</li>
                <li><strong>Aula 6:</strong> Actions</li>
                <li><strong>Aula 7:</strong> Launch files</li>
                <li><strong>Aula 8:</strong> Parâmetros</li>
                <li><strong>Aula 9:</strong> Logging e Debugging</li>
                <li><strong>Aula 10:</strong> TF2 - Transformações</li>
            </ul>
            <ul>
                <li><strong>Aula 11:</strong> URDF - Modelagem de robôs</li>
                <li><strong>Aula 12:</strong> Gazebo - Simulação</li>
                <li><strong>Aula 13:</strong> Navigation Stack</li>
                <li><strong>Aula 14:</strong> MoveIt - Manipulação</li>
                <li><strong>Aula 15:</strong> ROS2 Bridge</li>
                <li><strong>Aula 16:</strong> Segurança</li>
                <li><strong>Aula 17:</strong> Performance e Otimização</li>
                <li><strong>Aula 18:</strong> Projeto Final</li>
            </ul>
        </div>
    </div>
</body>
</html>"""
    
    return html_content

def create_pdf_slides():
    """Cria slides em formato PDF usando weasyprint"""
    try:
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        # Criar HTML específico para PDF
        html_content = create_pdf_html()
        
        # CSS específico para PDF
        pdf_css = CSS(string="""
            @page {
                size: A4 landscape;
                margin: 0.5cm;
            }
            
            * {
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Arial', sans-serif;
                font-size: 22px;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                color: #333;
            }
            
            .slide {
                page-break-after: always;
                height: 100vh;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: left;
            }
            
            .slide:last-child {
                page-break-after: avoid;
            }
            
            h1 {
                font-size: 36px;
                color: #383435;
                margin: 0 0 20px 0;
                border-bottom: 3px solid #AF1E23;
                padding-bottom: 10px;
                text-align: center;
            }
            
            h2 {
                font-size: 28px;
                color: #383435;
                margin: 0 0 15px 0;
                text-align: center;
            }
            
            h3 {
                font-size: 24px;
                color: #AF1E23;
                margin: 0 0 12px 0;
                text-align: left;
            }
            
            p {
                margin: 0 0 10px 0;
                font-size: 22px;
                text-align: left;
            }
            
            ul {
                margin: 0 0 15px 0;
                padding-left: 25px;
                text-align: left;
            }
            
            li {
                margin: 0 0 8px 0;
                font-size: 20px;
                text-align: left;
            }
            
            .ufjf-header {
                background: #383435;
                color: white;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 25px;
                text-align: center;
            }
            
            .ufjf-header h2 {
                color: white;
                font-size: 24px;
                margin: 0;
                border: none;
            }
            
            .ufjf-header p {
                color: #cccccc;
                font-size: 18px;
                margin: 5px 0 0 0;
                text-align: center;
            }
            
            .code-block {
                background: #2c3e50;
                color: #ecf0f1;
                padding: 15px;
                border-radius: 5px;
                font-family: 'Courier New', monospace;
                font-size: 16px;
                border-left: 4px solid #AF1E23;
                margin: 15px 0;
                white-space: pre-wrap;
                overflow-wrap: break-word;
                text-align: left;
            }
            
            .comparison-table {
                display: flex;
                width: 100%;
                margin: 20px 0;
                gap: 15px;
            }
            
            .comparison-column {
                flex: 1;
                padding: 15px;
                border-radius: 8px;
            }
            
            .ros1-column {
                background: #f5f5f5;
                border-left: 4px solid #676767;
            }
            
            .ros2-column {
                background: #f0f0f0;
                border-left: 4px solid #383435;
            }
            
            .node-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 12px;
                margin: 20px 0;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            
            .node-card {
                background: linear-gradient(135deg, #f0f0f0, #e0e0e0);
                padding: 12px;
                border-radius: 8px;
                border: 2px solid #383435;
                position: relative;
                text-align: center;
                min-height: 80px;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            
            .node-card h3 {
                color: #383435;
                margin: 0 0 6px 0;
                font-size: 18px;
                text-align: center;
            }
            
            .node-card p {
                color: #676767;
                margin: 0;
                font-size: 14px;
                text-align: center;
            }
            
            .node-tag {
                position: absolute;
                top: -6px;
                right: -6px;
                background: #AF1E23;
                color: white;
                padding: 3px 6px;
                border-radius: 8px;
                font-size: 10px;
            }
            
            .comm-types {
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 15px;
                margin: 15px 0;
            }
            
            .comm-type {
                background: #AF1E23;
                color: white;
                padding: 8px 12px;
                border-radius: 15px;
                font-size: 16px;
            }
            
            .comm-type:nth-child(2) {
                background: #676767;
            }
            
            .comm-type:nth-child(3) {
                background: #383435;
            }
            
            .feature-list {
                background: #f8f9fa;
                padding: 15px;
                border-radius: 8px;
                margin: 15px 0;
                text-align: left;
            }
            
            .highlight {
                background: #AF1E23;
                color: white;
                padding: 2px 4px;
                border-radius: 3px;
            }
        """)
        
        # Gerar PDF
        html_doc = HTML(string=html_content)
        pdf_bytes = html_doc.write_pdf(stylesheets=[pdf_css])
        
        return pdf_bytes
        
    except ImportError:
        print("⚠️  WeasyPrint não está instalado. Instalando...")
        os.system("pip install weasyprint")
        return None

def main():
    """Função principal"""
    print("🤖 Criando slides ROS2 com Reveal.js...")
    
    # Criar slides Reveal.js
    html_content = create_revealjs_slides()
    
    # Salvar arquivo HTML
    filename = "ros2_aula1_reveal.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Slides Reveal.js criados: {filename}")
    print("\n📋 Instruções:")
    print("1. Abra o arquivo HTML no navegador")
    print("2. Use as setas do teclado para navegar")
    print("3. Para apresentar em tela cheia, pressione F11")
    print("4. Para exportar como PDF, use Ctrl+P no navegador")
    
    # Tentar criar PDF
    print("\n🔄 Tentando criar PDF...")
    pdf_bytes = create_pdf_slides()
    
    if pdf_bytes:
        pdf_filename = "ros2_aula1_slides.pdf"
        with open(pdf_filename, 'wb') as f:
            f.write(pdf_bytes)
        print(f"✅ PDF criado: {pdf_filename}")
    else:
        print("⚠️  Para criar PDF, instale: pip install weasyprint")
    
    print(f"\n🌐 Abrindo slides no navegador...")
    os.system(f"xdg-open {filename}")

if __name__ == "__main__":
    main()
