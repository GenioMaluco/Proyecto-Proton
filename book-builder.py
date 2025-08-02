# book-builder.py
import glob

# Concatenar todos los .md en orden
chapters = sorted(glob.glob("Capitulo_1/*.md"))
print (chapters)
with open("Libro_Proyecto_Proton.md", "w") as book:
    for chapter in chapters:
        with open(chapter, "r") as f:
            book.write(f.read() + "\n\n")