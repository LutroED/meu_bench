import cv2
import numpy as np
import time

def generate_mandelbrot(size, iterations):
    x, y = np.meshgrid(np.linspace(-2, 0.5, size), np.linspace(-1.25, 1.25, size))
    c = x + 1j * y
    z = np.zeros_like(c)
    mask = np.full(c.shape, True, dtype=bool)
    output = np.zeros(c.shape, dtype=float)

    for i in range(iterations):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask[np.abs(z) > 2] = False
        output[mask] = i
    return output

def run_benchmark():
    print(f"\n--- Iniciando Benchmark no ProBook 4530s (Linux Mint) ---")
    size = 1000  # Imagem 1000x1000
    
    # Teste 1: CPU Puro (Cálculo Fractal)
    start_time = time.time()
    fractal = generate_mandelbrot(size, 100)
    math_time = time.time() - start_time
    print(f"1. Cálculo do Fractal: {math_time:.4f} segundos")

    # Teste 2: Processamento OpenCV (Filtros em loop)
    img = np.uint8(cv2.normalize(fractal, None, 0, 255, cv2.NORM_MINMAX))
    
    start_time = time.time()
    for _ in range(50):
        img = cv2.GaussianBlur(img, (15, 15), 0)
        img = cv2.Canny(img, 100, 200)
    
    cv_time = time.time() - start_time
    print(f"2. Processamento OpenCV (50 ciclos): {cv_time:.4f} segundos")
    print(f"------------------------------------------------------")
    print(f"TEMPO TOTAL: {math_time + cv_time:.4f} segundos\n")

if __name__ == "__main__":
    run_benchmark()
