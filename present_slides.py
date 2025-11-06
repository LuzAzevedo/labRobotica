#!/usr/bin/env python3
"""
Script para facilitar a apresentação dos slides ROS2
"""

import os
import sys
import webbrowser
import subprocess
from pathlib import Path

def check_file_exists(filename):
    """Verifica se o arquivo existe"""
    return Path(filename).exists()

def open_slides():
    """Abre os slides no navegador"""
    html_file = "ros2_aula1_slides.html"
    
    if not check_file_exists(html_file):
        print("❌ Arquivo de slides não encontrado!")
        print("Execute primeiro: python3 create_slides.py")
        return False
    
    try:
        # Tentar diferentes navegadores
        browsers = [
            'google-chrome',
            'chromium-browser', 
            'firefox',
            'sensible-browser'
        ]
        
        file_path = os.path.abspath(html_file)
        url = f"file://{file_path}"
        
        print(f"🌐 Abrindo slides: {html_file}")
        
        # Tentar abrir com navegador específico
        for browser in browsers:
            try:
                subprocess.run([browser, url], check=True)
                print(f"✅ Slides abertos com {browser}")
                return True
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        
        # Fallback para webbrowser padrão
        webbrowser.open(url)
        print("✅ Slides abertos no navegador padrão")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao abrir slides: {e}")
        return False

def show_instructions():
    """Mostra instruções de uso"""
    print("\n" + "="*60)
    print("🤖 SLIDES ROS2 - AULA 1: VISÃO GERAL + INSTALAÇÃO")
    print("="*60)
    print("\n📋 CONTROLES DE NAVEGAÇÃO:")
    print("  ← →  : Navegar entre slides")
    print("  F11  : Modo tela cheia")
    print("  ESC  : Sair da apresentação")
    print("\n🎯 CONTEÚDO DOS SLIDES:")
    print("  1. Introdução ao ROS2")
    print("  2. Grafo de Nós")
    print("  3. DDS - Data Distribution Service")
    print("  4. Diferenças ROS1 vs ROS2")
    print("  5. Escolhas de DDS")
    print("  6. Instalação ROS2 Humble")
    print("  7. Teste com Turtlesim")
    print("  8. ROS2 Doctor")
    print("  9. Próximas Aulas")
    print("\n💡 DICAS:")
    print("  • Use F11 para apresentação em tela cheia")
    print("  • Os slides incluem comandos práticos")
    print("  • Tempo estimado: 60-90 minutos")
    print("="*60)

def main():
    """Função principal"""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_instructions()
        return
    
    print("🚀 Iniciando apresentação ROS2...")
    
    # Verificar se os slides existem
    if not check_file_exists("ros2_aula1_slides.html"):
        print("📝 Criando slides...")
        try:
            subprocess.run([sys.executable, "create_slides.py"], check=True)
        except subprocess.CalledProcessError:
            print("❌ Erro ao criar slides!")
            return
    
    # Abrir slides
    if open_slides():
        show_instructions()
    else:
        print("\n🔧 SOLUÇÃO ALTERNATIVA:")
        print("1. Abra manualmente o arquivo: ros2_aula1_slides.html")
        print("2. Ou execute: python3 create_slides.py")

if __name__ == "__main__":
    main()
