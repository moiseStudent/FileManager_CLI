import subprocess

def obtener_estadisticas_archivo(ruta_archivo):
    # Ejecutar el programa de Rust
    resultado = subprocess.run(["./file_stats"], capture_output=True, text=True)
    
    if resultado.returncode == 0:
        print("Estadísticas del archivo:")
        print(resultado.stdout)
    else:
        print("Error al ejecutar el programa de Rust:")
        print(resultado.stderr)

# Elemento unicamente de prueba
#obtener_estadisticas_archivo("ruta/al/archivo.txt")
