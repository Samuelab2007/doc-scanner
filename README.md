# Prototipo de escaner de documentos

Este proyecto tiene como objetivo poner en práctica distintas técnicas de procesamiento de imágenes, utilizando python y la librería opencv como herramientas principales.

## Objetivo

Convertir una foto de un documento en papel a un documento digital binarizado(a blanco y negro), claro y legible; parecido a un escaner real.

Se busca elminar fondos, sombras, deformaciones, ruido, para asegurar una mayor calidad de imagen.

## Conceptos y habilidades aplicadas

- Ecualización de histogramas
- Umbralización adaptativa y método Otsu
- Operaciones morfológicas
- Transformaciones geométricas, principalmente de perspectiva.

## Marco teórico

(opcional)
OCR(Reconocimiento Óptico de Caracteres): Es el proceso por el cual se convierte una imagen de texto en un formato de texto que pueden leer las máquinas. Este se encarga de tomar una imagen de texto, limpiarla y aplicar patrones de reconocmiento de glifos, idiomas, palabras, etc. Para generar un documento digitalizado, con capacidades completas. Por lo general los archivos resultantes son PDFs.

Equalización de histogramas: Es una técnica de mejoramiento de contraste utilizada en procesamiento digital de imágenes por su alta eficiencia y simpleza. Se utiliza para modificar el rango dinámico de la imagen mediante la modificación de la intensidad de los pixeles de la misma, de manera que se puedan describir con histogramas planos. Es especialmente útil cuando tenemos secciones amplias de la imagen que tienen una intensidad muy cercana y difícil de distinguir.  

Binarización: Técnica utilizada para convertir una imagen en escala de grises o a color a una imagen binaria(compuesta de unos y ceros), donde 0 representa el fondo. Es un proceso fundamental para posteriormente aplicar OCR.

Método Otsu:

## Artefacto final

Script de python

    Opcional: App web que haga más fácil la interacción. Y muestre el documento resultado en la misma.

## Referencias y material de ayuda

Binarización: https://deepai.org/machine-learning-glossary-and-terms/binarization?ref=dagshub.com

Equalización de histogramas: https://www.mygreatlearning.com/blog/histogram-equalization-explained/

OCR: https://www.mygreatlearning.com/blog/histogram-equalization-explained/

Otsu: https://medium.com/@vignesh.g1609/image-segmentation-using-otsu-threshold-selection-method-856ccdacf22
