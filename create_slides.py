#!/usr/bin/env python3
"""
Script simplificado para criar slides ROS2 sem dependências gráficas pesadas
Este script cria uma versão HTML dos slides usando apenas bibliotecas básicas
"""

import os
import webbrowser
from datetime import datetime

def create_html_slides():
    """Cria slides HTML para apresentação ROS2"""
    
    html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROS2 - Aula 1: Visão Geral + Instalação</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #383435 0%, #676767 100%);
            color: #333;
        }
        
        .slide {
            display: none;
            min-height: 100vh;
            padding: 40px;
            box-sizing: border-box;
            background: white;
            margin: 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        .slide.active {
            display: block;
        }
        
        .slide h1 {
            color: #383435;
            font-size: 2.5em;
            margin-bottom: 30px;
            text-align: center;
            border-bottom: 3px solid #AF1E23;
            padding-bottom: 20px;
        }
        
        .slide h2 {
            color: #383435;
            font-size: 2em;
            margin-bottom: 20px;
        }
        
        .slide h3 {
            color: #AF1E23;
            font-size: 1.5em;
            margin-bottom: 15px;
        }
        
        .slide p, .slide li {
            font-size: 1.2em;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        .slide ul {
            margin-left: 30px;
        }
        
        .slide li {
            margin-bottom: 10px;
        }
        
        .code-block {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 1em;
            margin: 20px 0;
            overflow-x: auto;
        }
        
        .highlight {
            background: #f39c12;
            color: white;
            padding: 2px 5px;
            border-radius: 3px;
        }
        
        .navigation {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.8);
            padding: 15px 30px;
            border-radius: 25px;
            color: white;
        }
        
        .nav-button {
            background: #383435;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
        }
        
        .nav-button:hover {
            background: #AF1E23;
        }
        
        .nav-button:disabled {
            background: #7f8c8d;
            cursor: not-allowed;
        }
        
        .slide-counter {
            color: #ecf0f1;
            margin: 0 20px;
            font-size: 1.1em;
        }
        
        .ros-logo {
            text-align: center;
            font-size: 3em;
            color: #383435;
            margin-bottom: 20px;
        }
        
        .comparison-table {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
        }
        
        .comparison-column {
            flex: 1;
            margin: 0 20px;
            padding: 20px;
            border-radius: 10px;
        }
        
        .ros1-column {
            background: #f5f5f5;
            border-left: 5px solid #676767;
        }
        
        .ros2-column {
            background: #f0f0f0;
            border-left: 5px solid #383435;
        }
        
        .feature-list {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        
        .command-example {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            margin: 15px 0;
            border-left: 4px solid #AF1E23;
        }
    </style>
</head>
<body>
    <div class="slide active">
        <div style="text-align: center; margin-bottom: 30px;">
            <div style="display: inline-block; background: #383435; color: white; padding: 15px 30px; border-radius: 10px; margin-bottom: 20px;">
                <h2 style="color: white; margin: 0; font-size: 1.8em;">UNIVERSIDADE FEDERAL DE JUIZ DE FORA</h2>
                <p style="color: #cccccc; margin: 5px 0 0 0; font-size: 1.1em;">Engenharia Elétrica - Robótica e Automação Industrial</p>
            </div>
        </div>
        
        <div class="ros-logo">🤖 ROS2</div>
        <h1>Introdução ao ROS2</h1>
        <h2>Aula 1: Visão Geral + Instalação</h2>
        
        <div style="text-align: center; margin-top: 30px;">
            <div style="display: inline-block; background: #AF1E23; color: white; padding: 10px 20px; border-radius: 5px;">
                <p style="margin: 0; font-size: 1em;">Professor: André Marcato | Semestre: 2025.2</p>
            </div>
        </div>
    </div>

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

    <div class="slide">
        <h1>Grafo de Nós ROS2</h1>
        
        <div style="text-align: center; margin: 30px 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 800px; margin: 0 auto;">
                <!-- Sensor Node -->
                <div style="background: linear-gradient(135deg, #f0f0f0, #e0e0e0); padding: 20px; border-radius: 15px; border: 3px solid #383435; position: relative;">
                    <div style="text-align: center;">
                        <h3 style="color: #383435; margin: 0;">Sensor Node</h3>
                        <p style="color: #676767; margin: 10px 0 0 0; font-size: 0.9em;">Coleta dados dos sensores</p>
                    </div>
                    <div style="position: absolute; top: -10px; right: -10px; background: #AF1E23; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em;">
                        Publisher
                    </div>
                </div>
                
                <!-- Control Node -->
                <div style="background: linear-gradient(135deg, #f0f0f0, #e0e0e0); padding: 20px; border-radius: 15px; border: 3px solid #383435; position: relative;">
                    <div style="text-align: center;">
                        <h3 style="color: #383435; margin: 0;">Control Node</h3>
                        <p style="color: #676767; margin: 10px 0 0 0; font-size: 0.9em;">Processa comandos</p>
                    </div>
                    <div style="position: absolute; top: -10px; right: -10px; background: #AF1E23; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em;">
                        Subscriber
                    </div>
                </div>
                
                <!-- Planning Node -->
                <div style="background: linear-gradient(135deg, #f0f0f0, #e0e0e0); padding: 20px; border-radius: 15px; border: 3px solid #383435; position: relative;">
                    <div style="text-align: center;">
                        <h3 style="color: #383435; margin: 0;">Planning Node</h3>
                        <p style="color: #676767; margin: 10px 0 0 0; font-size: 0.9em;">Planeja trajetórias</p>
                    </div>
                    <div style="position: absolute; top: -10px; right: -10px; background: #AF1E23; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em;">
                        Service
                    </div>
                </div>
                
                <!-- Actuator Node -->
                <div style="background: linear-gradient(135deg, #f0f0f0, #e0e0e0); padding: 20px; border-radius: 15px; border: 3px solid #383435; position: relative;">
                    <div style="text-align: center;">
                        <h3 style="color: #383435; margin: 0;">Actuator Node</h3>
                        <p style="color: #676767; margin: 10px 0 0 0; font-size: 0.9em;">Controla motores</p>
                    </div>
                    <div style="position: absolute; top: -10px; right: -10px; background: #AF1E23; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em;">
                        Client
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Conexões visuais -->
        <div style="text-align: center; margin: 20px 0;">
            <div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
                <div style="background: #AF1E23; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.9em;">
                    Tópicos
                </div>
                <div style="background: #676767; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.9em;">
                    Serviços
                </div>
                <div style="background: #383435; color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.9em;">
                    Ações
                </div>
            </div>
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

    <div class="slide">
        <h1>ROS1 vs ROS2</h1>
        <div class="comparison-table">
            <div class="comparison-column ros1-column">
                <h3 style="color: #676767;">ROS1</h3>
                <ul>
                    <li>Master único</li>
                    <li>TCP/UDP</li>
                    <li>Python 2</li>
                    <li>Sem QoS</li>
                    <li>Linux apenas</li>
                </ul>
            </div>
            <div class="comparison-column ros2-column">
                <h3 style="color: #383435;">ROS2</h3>
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

    <div class="slide">
        <h1>Escolhas de DDS no ROS2</h1>
        
        <div style="display: flex; justify-content: space-around; margin: 30px 0;">
            <div style="flex: 1; margin: 0 20px; padding: 20px; background: #f0f0f0; border-radius: 10px; border-left: 5px solid #383435;">
                <h3 style="color: #383435;">Fast DDS</h3>
                <ul>
                    <li><strong>Padrão no ROS2 Humble</strong></li>
                    <li>Desenvolvido pela eProsima</li>
                    <li>Alta performance</li>
                    <li>Suporte completo a QoS</li>
                </ul>
            </div>
            <div style="flex: 1; margin: 0 20px; padding: 20px; background: #f5f5f5; border-radius: 10px; border-left: 5px solid #676767;">
                <h3 style="color: #676767;">CycloneDX</h3>
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
        
        <div class="command-example">
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
        
        <div class="command-example">
# Terminal 1 - Executar simulador
ros2 run turtlesim turtlesim_node

# Terminal 2 - Executar controle
ros2 run turtlesim turtle_teleop_key
        </div>
    </div>

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
        
        <div class="command-example">
# Executar diagnóstico completo
ros2 doctor

# Verificar problemas específicos
ros2 doctor --report
        </div>
    </div>

    <div class="slide">
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
    </div>

    <div class="navigation">
        <button class="nav-button" id="prevBtn" onclick="changeSlide(-1)">← Anterior</button>
        <span class="slide-counter" id="slideCounter">1 / 10</span>
        <button class="nav-button" id="nextBtn" onclick="changeSlide(1)">Próximo →</button>
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;

        function showSlide(n) {
            slides[currentSlide].classList.remove('active');
            currentSlide = (n + totalSlides) % totalSlides;
            slides[currentSlide].classList.add('active');
            
            document.getElementById('slideCounter').textContent = `${currentSlide + 1} / ${totalSlides}`;
            document.getElementById('prevBtn').disabled = currentSlide === 0;
            document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
        }

        function changeSlide(direction) {
            if (direction === 1 && currentSlide < totalSlides - 1) {
                showSlide(currentSlide + 1);
            } else if (direction === -1 && currentSlide > 0) {
                showSlide(currentSlide - 1);
            }
        }

        // Navegação por teclado
        document.addEventListener('keydown', function(e) {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                changeSlide(1);
            } else if (e.key === 'ArrowLeft') {
                changeSlide(-1);
            }
        });

        // Inicializar
        showSlide(0);
    </script>
</body>
</html>
    """
    
    return html_content

def main():
    """Função principal"""
    print("🤖 Criando slides ROS2 - Aula 1...")
    
    # Criar conteúdo HTML
    html_content = create_html_slides()
    
    # Salvar arquivo HTML
    filename = "ros2_aula1_slides.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Slides criados com sucesso: {filename}")
    print("\n📋 Instruções:")
    print("1. Abra o arquivo HTML no seu navegador")
    print("2. Use as setas do teclado ou botões para navegar")
    print("3. Para apresentar em tela cheia, pressione F11")
    
    # Tentar abrir automaticamente no navegador
    try:
        file_path = os.path.abspath(filename)
        webbrowser.open(f"file://{file_path}")
        print(f"\n🌐 Abrindo automaticamente no navegador...")
    except Exception as e:
        print(f"\n⚠️  Não foi possível abrir automaticamente: {e}")
        print(f"   Abra manualmente: {file_path}")

if __name__ == "__main__":
    main()
