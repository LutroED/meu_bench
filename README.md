# 🚀 OpenCV Benchmark - Legacy Hardware

Este é um script de benchmark desenvolvido em Python para testar a performance de processamento matemático e de visão computacional em hardware legado.

## 💻 Ambiente de Teste
* **Dispositivo:** HP ProBook 4530s
* **Processador:** Intel Core i3-2350M (2ª Geração)
* **Sistema Operacional:** Linux Mint 22 (MATE Edition)
* **Armazenamento:** SSD 120GB (Sistema) + HDD 1TB (Dados/Projetos)

## 📊 Resultados Obtidos
No ambiente Linux Mint, o script apresentou os seguintes tempos:
* **Cálculo de Fractal (Mandelbrot):** ~2.28s
* **Processamento OpenCV (50 ciclos):** ~0.30s
* **Tempo Total:** **2.59 segundos**

## 🛠️ Tecnologias Utilizadas
* Python 3.12
* OpenCV (cv2)
* NumPy

## 📝 Como executar
1. Instale as dependências: `sudo apt install python3-opencv python3-numpy`
2. Execute o script: `python3 benchmark.py`