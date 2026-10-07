# Simulacro de Matemáticas: Geometría y Patrones

Este proyecto contiene el material completo para evaluar y validar los conocimientos matemáticos de tu hija en tres temas fundamentales:
1. **Cuerpos geométricos:** Prismas y pirámides (identificación, nombres según la base, propiedades distintivas).
2. **Caracterización geométrica:** Caras (basales y laterales), vértices (y cúspide) y aristas.
3. **Secuencias y patrones geométricos:** Secuencias con figuras planas (cuadrados, círculos, triángulos), clasificación en **incrementales** y **decrementales**, dibujo del término siguiente y **explicación verbal obligatoria de la regla matemática**.

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
