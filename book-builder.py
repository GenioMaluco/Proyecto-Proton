# book-builder.py
import glob
import os
import sys

try:
    # Buscar archivos .md en la carpeta chapters
    chapters = sorted(glob.glob("Capitulos/*.md"))
    
    if not chapters:
        print("ERROR: No se encontraron archivos .md en la carpeta 'chapters'")
        print("Verifica que:")
        print("1. La carpeta 'chapters' existe en el mismo directorio que este script")
        print("2. Contiene archivos con extensión .md")
        sys.exit(1)
    
    print(f"Encontrados {len(chapters)} archivos:")
    for i, chapter in enumerate(chapters, 1):
        print(f"{i}. {os.path.basename(chapter)}")
    
    # Crear el libro combinado
    with open("Libro_Proyecto_Proton.md", "w", encoding="utf-8") as book:
        for chapter in chapters:
            with open(chapter, "r", encoding="utf-8") as f:
                book.write(f"<!-- ARCHIVO: {os.path.basename(chapter)} -->\n\n")
                book.write(f.read())
                book.write("\n\n")  # Separador entre capítulos
                
    print("\n¡Libro compilado con éxito en 'proton-book.md'!")

except Exception as e:
    print(f"ERROR: {str(e)}")
    print("Posibles soluciones:")
    print("- Verifica los permisos de escritura")
    print("- Asegura que la carpeta 'chapters' exista")