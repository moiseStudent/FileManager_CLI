use std::fs; //Importacion de un modulo
use std::io;

/// Crea una funcion padre
fn main() -> io::Result<()> {
    let path = "test.txt";

    // Obtener metadata del archivo
    let metadata = fs::metadata(path)?;

    // Obtener tamaño
    let size = metadata.len();
    
    // Obtener permisos
    let permissions = metadata.permissions();

    println!("Tamano: {} bytes", size);
    println!("Permisos: {:?}", permissions);

    Ok(())
}

// Este archivo debe ser compilado para que python pueda ejecutarlo
// Este archivo es solo de prueba
