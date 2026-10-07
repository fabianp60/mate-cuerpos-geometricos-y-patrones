# Aventura Matemática: Cuerpos Geométricos y Patrones 📐✨

Aplicación interactiva y material de evaluación para 4.º grado, enfocada en:
1. **Cuerpos geométricos:** Prismas y pirámides (identificación, nombres según la base, propiedades distintivas).
2. **Caracterización geométrica:** Caras (basales y laterales), vértices (y cúspide) y aristas con modelos 3D interactivos.
3. **Secuencias y patrones:** Patrones incrementales y decrementales, deducción de reglas y predicción del siguiente término.

---

## 🎮 Juego Interactivo Web (GitHub Pages)

El proyecto cuenta con una aplicación web completa y autónoma (HTML5, CSS3, JavaScript puro) lista para jugarse en navegadores web en PC, tablets y smartphones:

- **Modo Lección:** Explicaciones visuales y modelos geométricos 3D translúcidos renderizados en tiempo real con Canvas.
- **Minijuegos de Práctica:** Desafíos de caras/vértices/aristas y secuencias numéricas/geométricas.
- **Simulacro Interactivo:** Evaluación con retroalimentación instantánea, estrellas, puntos de experiencia (XP) y sonido sintetizado con Web Audio API.
- **Progreso automático:** Se guarda automáticamente en el navegador (`localStorage`).

---

## 🌟 Mejoras Aplicadas en esta Versión

1. **Cuerpos 3D con Semitransparencia:**
   - Todas las caras de los poliedros ahora son translúcidas (`opacity 0.35 - 0.45`), permitiendo ver el interior y el fondo del cuerpo geométrico.
   - **Distinción visual inmediata entre el Cuerpo B (Pirámide cuadrangular) y el Cuerpo D (Pirámide triangular):**
     * En el **Cuerpo B**, la base cuadrada en perspectiva es visible con sus **4 aristas basales (2 continuas y 2 discontinuas en color vivo) y sus 4 vértices basales + 1 cúspide (Total: 5 vértices)**.
     * En el **Cuerpo D**, la base triangular en perspectiva es visible con sus **3 aristas basales y sus 3 vértices basales + 1 cúspide (Total: 4 vértices)**.
     * En todos los cuerpos se pueden contar con facilidad las aristas ocultas y los vértices traseros.
2. **Cajas de Dibujo de Secuencias Optimizadas:**
   - **Completamente libres de texto interior:** Se eliminó cualquier mensaje que pudiera estorbar el trazo del lápiz.
   - **Cuadrícula de puntos guía:** Fondo blanco con puntos guía suaves para ayudar a alinear y dibujar figuras con precisión.
   - **Espacio ampliado:** El área de dibujo del Paso 4 en los puntos 6, 7 y 8 creció considerablemente para que quepan cómodamente 11 triángulos, 5 cuadrados o 12 figuras compuestas (4 círculos y 8 cuadrados).
   - **Instrucción y conteo exteriores:** El rótulo *"Paso 4 (Dibuja aquí)"* se ubica arriba de la caja y la casilla de conteo abajo.
3. **Cajas Creativas de la Pregunta 10:**
   - Se removió el texto interior `(Dibuja aquí)` para dejar las 4 cajas con una cuadrícula punteada limpia y espaciosa donde diseñar su propia secuencia.

---

## 📁 Archivos Disponibles

1. **[simulacro_examen_matematicas.pdf](file:///home/fabian/projects/estudiar-mate-2/simulacro_examen_matematicas.pdf)**  
   *Cuadernillo de Examen para la Estudiante (4 páginas)*  
   - Diseñado exactamente en **formato Carta (Letter, 8.5" x 11")**, listo para imprimir a doble cara (2 hojas) o en 4 hojas sueltas.
   - Tiempo límite: **60 minutos** (1 hora).
   - Puntaje total: **100 puntos**.

2. **[solucionario_y_guia_evaluacion.pdf](file:///home/fabian/projects/estudiar-mate-2/solucionario_y_guia_evaluacion.pdf)**  
   *Guía del Evaluador / Padre de Familia (4 páginas)*  
   - Respuestas correctas pregunta a pregunta con soluciones visuales de los dibujos requeridos.
   - Rúbricas detalladas para calificar las explicaciones en palabras (nivel excelente, parcial e inicial).
   - Errores comunes frecuentes de primaria y cómo explicárselos.
   - **Semáforo Diagnóstico:** Plan de acción según el puntaje obtenido (Verde > 90 pts, Amarillo 70-89 pts, Rojo < 70 pts).

3. **[generate_all.py](file:///home/fabian/projects/estudiar-mate-2/generate_all.py)**  
   Script automatizado en Python para regenerar los PDFs y previsualizaciones PNG.

4. **Carpeta `preview_pages/`:**  
   Imágenes PNG de alta resolución de cada página para inspección visual rápida.
