#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Simulacro de Examen de Matemáticas y Guía Pedagógica
Versión con cuerpos 3D semitransparentes (con aristas traseras y bases claramente visibles)
y cajas de dibujo limpias y ampliadas con cuadrícula de puntos guía (sin texto interno).
"""

import os
import subprocess

def get_svg_cube(width=95, height=80, stroke="#1e40af", fill_front="#93c5fd", fill_top="#bfdbfe", fill_side="#60a5fa"):
    x, y, w, h = 16, 26, 46, 46
    dx, dy = 24, -16
    A = (x, y)
    B = (x+w, y)
    C = (x+w, y+h)
    D = (x, y+h)
    E = (x+dx, y+dy)
    F = (x+w+dx, y+dy)
    G = (x+w+dx, y+h+dy)
    H = (x+dx, y+h+dy)
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Aristas traseras discontinuas visibles por la semitransparencia -->
      <line x1="{E[0]}" y1="{E[1]}" x2="{H[0]}" y2="{H[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.8"/>
      <line x1="{D[0]}" y1="{D[1]}" x2="{H[0]}" y2="{H[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.8"/>
      <line x1="{H[0]}" y1="{H[1]}" x2="{G[0]}" y2="{G[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.8"/>
      <circle cx="{H[0]}" cy="{H[1]}" r="2.6" fill="#1e40af" fill-opacity="0.7"/>

      <!-- Base inferior visible y sombreada (D-C-G-H) -->
      <polygon points="{D[0]},{D[1]} {C[0]},{C[1]} {G[0]},{G[1]} {H[0]},{H[1]}" fill="#93c5fd" fill-opacity="0.25"/>

      <!-- Caras semitransparentes -->
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {F[0]},{F[1]} {E[0]},{E[1]}" fill="{fill_top}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{B[0]},{B[1]} {C[0]},{C[1]} {G[0]},{G[1]} {F[0]},{F[1]}" fill="{fill_side}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {D[0]},{D[1]}" fill="{fill_front}" fill-opacity="0.35" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Aristas frontales continuas -->
      <line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="{stroke}" stroke-width="1.8"/>
      <line x1="{D[0]}" y1="{D[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{stroke}" stroke-width="1.8"/>
      
      <!-- Los 8 vértices -->
      <circle cx="{A[0]}" cy="{A[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{B[0]}" cy="{B[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{C[0]}" cy="{C[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{D[0]}" cy="{D[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{E[0]}" cy="{E[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{F[0]}" cy="{F[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{G[0]}" cy="{G[1]}" r="2.8" fill="{stroke}"/>
    </svg>'''

def get_svg_square_pyramid(width=95, height=80, stroke="#c2410c", fill="#ffedd5", fill_right="#fed7aa"):
    # Base CUADRADA claramente de 4 lados en perspectiva
    A = (15, 66)  # vértice base izquierda
    B = (52, 78)  # vértice base frontal
    C = (88, 66)  # vértice base derecha
    D = (51, 52)  # vértice base trasera (se nota claramente el cuadrilátero)
    S = (51, 12)  # cúspide
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Aristas traseras de la base cuadrada y arista hacia la cúspide (discontinuas con color vivo) -->
      <line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{D[0]}" y1="{D[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{S[0]}" y1="{S[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      <circle cx="{D[0]}" cy="{D[1]}" r="2.8" fill="#ea580c" fill-opacity="0.85"/>

      <!-- Base cuadrada resaltada en tono ámbar translúcido (4 lados) -->
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {D[0]},{D[1]}" fill="#fde047" fill-opacity="0.38"/>

      <!-- Caras laterales traseras translúcidas -->
      <polygon points="{S[0]},{S[1]} {A[0]},{A[1]} {D[0]},{D[1]}" fill="#fed7aa" fill-opacity="0.22"/>
      <polygon points="{S[0]},{S[1]} {D[0]},{D[1]} {C[0]},{C[1]}" fill="#fed7aa" fill-opacity="0.22"/>

      <!-- Caras laterales frontales semitransparentes -->
      <polygon points="{S[0]},{S[1]} {A[0]},{A[1]} {B[0]},{B[1]}" fill="{fill}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{S[0]},{S[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="{fill_right}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Aristas frontales de la base -->
      <line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{stroke}" stroke-width="2"/>
      <line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{stroke}" stroke-width="2"/>

      <!-- Vértices frontales y cúspide (Total: 5 vértices) -->
      <circle cx="{S[0]}" cy="{S[1]}" r="3.4" fill="{stroke}"/>
      <circle cx="{A[0]}" cy="{A[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{B[0]}" cy="{B[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{C[0]}" cy="{C[1]}" r="2.8" fill="{stroke}"/>
    </svg>'''

def get_svg_triangular_prism(width=95, height=80, stroke="#047857", fill="#d1fae5", fill_top="#a7f3d0", fill_right="#6ee7b7"):
    T1 = (18, 22)
    T2 = (62, 32)
    T3 = (44, 11)
    H = 43
    B1 = (T1[0], T1[1] + H)
    B2 = (T2[0], T2[1] + H)
    B3 = (T3[0], T3[1] + H)
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Aristas traseras discontinuas (vertical y base inferior) -->
      <line x1="{T3[0]}" y1="{T3[1]}" x2="{B3[0]}" y2="{B3[1]}" stroke="#059669" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{B1[0]}" y1="{B1[1]}" x2="{B3[0]}" y2="{B3[1]}" stroke="#059669" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{B3[0]}" y1="{B3[1]}" x2="{B2[0]}" y2="{B2[1]}" stroke="#059669" stroke-width="1.8" stroke-dasharray="3,3"/>
      <circle cx="{B3[0]}" cy="{B3[1]}" r="2.8" fill="#047857" fill-opacity="0.8"/>

      <!-- Base inferior triangular sombreada translúcida -->
      <polygon points="{B1[0]},{B1[1]} {B2[0]},{B2[1]} {B3[0]},{B3[1]}" fill="#6ee7b7" fill-opacity="0.32"/>

      <!-- Caras laterales translúcidas -->
      <polygon points="{T2[0]},{T2[1]} {T3[0]},{T3[1]} {B3[0]},{B3[1]} {B2[0]},{B2[1]}" fill="{fill_right}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{T1[0]},{T1[1]} {T2[0]},{T2[1]} {B2[0]},{B2[1]} {B1[0]},{B1[1]}" fill="{fill}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{T1[0]},{T1[1]} {T3[0]},{T3[1]} {B3[0]},{B3[1]} {B1[0]},{B1[1]}" fill="#a7f3d0" fill-opacity="0.2"/>

      <!-- Base superior triangular -->
      <polygon points="{T1[0]},{T1[1]} {T2[0]},{T2[1]} {T3[0]},{T3[1]}" fill="{fill_top}" fill-opacity="0.48" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Arista frontal de la base inferior -->
      <line x1="{B1[0]}" y1="{B1[1]}" x2="{B2[0]}" y2="{B2[1]}" stroke="{stroke}" stroke-width="2"/>

      <!-- Los 6 vértices (3 arriba + 3 abajo) -->
      <circle cx="{T1[0]}" cy="{T1[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{T2[0]}" cy="{T2[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{T3[0]}" cy="{T3[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{B1[0]}" cy="{B1[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{B2[0]}" cy="{B2[1]}" r="2.8" fill="{stroke}"/>
    </svg>'''

def get_svg_triangular_pyramid(width=95, height=80, stroke="#86198f", fill="#fdf4ff", fill_right="#f5d0fe"):
    # Pirámide TRIANGULAR (Tetraedro): La base tiene EXACTAMENTE 3 lados y 3 vértices
    # A(16, 70), B(64, 78), C(84, 58)
    At = (16, 70)
    Bt = (64, 78)
    Ct = (84, 58)
    St = (48, 12)  # cúspide
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Arista trasera de la base triangular At-Ct (discontinua con color púrpura) -->
      <line x1="{At[0]}" y1="{At[1]}" x2="{Ct[0]}" y2="{Ct[1]}" stroke="#a21caf" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{St[0]}" y1="{St[1]}" x2="{Ct[0]}" y2="{Ct[1]}" stroke="#a21caf" stroke-width="1.8" stroke-dasharray="3,3"/>
      <circle cx="{Ct[0]}" cy="{Ct[1]}" r="2.8" fill="#a21caf" fill-opacity="0.85"/>

      <!-- Base TRIANGULAR resaltada translúcida (claramente un triángulo de 3 lados) -->
      <polygon points="{At[0]},{At[1]} {Bt[0]},{Bt[1]} {Ct[0]},{Ct[1]}" fill="#e879f9" fill-opacity="0.35"/>

      <!-- Cara trasera SAC translúcida -->
      <polygon points="{St[0]},{St[1]} {At[0]},{At[1]} {Ct[0]},{Ct[1]}" fill="#f5d0fe" fill-opacity="0.22"/>

      <!-- Caras laterales frontales semitransparentes -->
      <polygon points="{St[0]},{St[1]} {At[0]},{At[1]} {Bt[0]},{Bt[1]}" fill="{fill}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{St[0]},{St[1]} {Bt[0]},{Bt[1]} {Ct[0]},{Ct[1]}" fill="{fill_right}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Aristas frontales de la base (solo 2 aristas visibles continuas) -->
      <line x1="{At[0]}" y1="{At[1]}" x2="{Bt[0]}" y2="{Bt[1]}" stroke="{stroke}" stroke-width="2"/>
      <line x1="{Bt[0]}" y1="{Bt[1]}" x2="{Ct[0]}" y2="{Ct[1]}" stroke="{stroke}" stroke-width="2"/>

      <!-- Los 4 vértices (3 en la base triangular + 1 cúspide) -->
      <circle cx="{St[0]}" cy="{St[1]}" r="3.4" fill="{stroke}"/>
      <circle cx="{At[0]}" cy="{At[1]}" r="2.8" fill="{stroke}"/>
      <circle cx="{Bt[0]}" cy="{Bt[1]}" r="2.8" fill="{stroke}"/>
    </svg>'''

def get_svg_pentagonal_prism(width=95, height=80, stroke="#1e293b", fill="#e2e8f0", fill_top="#cbd5e1", fill_right="#94a3b8"):
    top = [(30, 17), (59, 13), (81, 24), (65, 36), (28, 32)]
    H = 41
    bot = [(p[0], p[1] + H) for p in top]
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Aristas traseras discontinuas visibles -->
      <line x1="{top[0][0]}" y1="{top[0][1]}" x2="{bot[0][0]}" y2="{bot[0][1]}" stroke="#475569" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{top[1][0]}" y1="{top[1][1]}" x2="{bot[1][0]}" y2="{bot[1][1]}" stroke="#475569" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{bot[4][0]}" y1="{bot[4][1]}" x2="{bot[0][0]}" y2="{bot[0][1]}" stroke="#475569" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{bot[0][0]}" y1="{bot[0][1]}" x2="{bot[1][0]}" y2="{bot[1][1]}" stroke="#475569" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{bot[1][0]}" y1="{bot[1][1]}" x2="{bot[2][0]}" y2="{bot[2][1]}" stroke="#475569" stroke-width="1.6" stroke-dasharray="3,3"/>
      
      <circle cx="{bot[0][0]}" cy="{bot[0][1]}" r="2.4" fill="#334155" fill-opacity="0.7"/>
      <circle cx="{bot[1][0]}" cy="{bot[1][1]}" r="2.4" fill="#334155" fill-opacity="0.7"/>

      <!-- Base inferior pentagonal translúcida -->
      <polygon points="{bot[0][0]},{bot[0][1]} {bot[1][0]},{bot[1][1]} {bot[2][0]},{bot[2][1]} {bot[3][0]},{bot[3][1]} {bot[4][0]},{bot[4][1]}" fill="#cbd5e1" fill-opacity="0.32"/>

      <!-- Caras laterales semitransparentes -->
      <polygon points="{top[4][0]},{top[4][1]} {top[3][0]},{top[3][1]} {bot[3][0]},{bot[3][1]} {bot[4][0]},{bot[4][1]}" fill="{fill}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{top[3][0]},{top[3][1]} {top[2][0]},{top[2][1]} {bot[2][0]},{bot[2][1]} {bot[3][0]},{bot[3][1]}" fill="{fill_right}" fill-opacity="0.4" stroke="{stroke}" stroke-width="1.8"/>
      <polygon points="{top[0][0]},{top[0][1]} {top[4][0]},{top[4][1]} {bot[4][0]},{bot[4][1]} {bot[0][0]},{bot[0][1]}" fill="#f1f5f9" fill-opacity="0.3" stroke="{stroke}" stroke-width="1.8"/>
      
      <!-- Base superior pentagonal -->
      <polygon points="{top[0][0]},{top[0][1]} {top[1][0]},{top[1][1]} {top[2][0]},{top[2][1]} {top[3][0]},{top[3][1]} {top[4][0]},{top[4][1]}" fill="{fill_top}" fill-opacity="0.48" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Aristas frontales inferiores -->
      <line x1="{bot[4][0]}" y1="{bot[4][1]}" x2="{bot[3][0]}" y2="{bot[3][1]}" stroke="{stroke}" stroke-width="1.8"/>
      <line x1="{bot[3][0]}" y1="{bot[3][1]}" x2="{bot[2][0]}" y2="{bot[2][1]}" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Los 10 vértices -->
      {"".join([f'<circle cx="{p[0]}" cy="{p[1]}" r="2.4" fill="#334155"/>' for p in top])}
      <circle cx="{bot[4][0]}" cy="{bot[4][1]}" r="2.4" fill="#334155"/>
      <circle cx="{bot[3][0]}" cy="{bot[3][1]}" r="2.4" fill="#334155"/>
      <circle cx="{bot[2][0]}" cy="{bot[2][1]}" r="2.4" fill="#334155"/>
    </svg>'''

def get_svg_hexagonal_pyramid(width=95, height=80, stroke="#3730a3", fill="#e0e7ff", fill_right="#c7d2fe"):
    H = [(15, 60), (35, 73), (68, 73), (87, 60), (71, 50), (32, 50)]
    S = (49, 11)
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 100 85" xmlns="http://www.w3.org/2000/svg">
      <!-- Aristas traseras de la base de 6 lados y hacia la cúspide (discontinuas con color) -->
      <line x1="{H[3][0]}" y1="{H[3][1]}" x2="{H[4][0]}" y2="{H[4][1]}" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{H[4][0]}" y1="{H[4][1]}" x2="{H[5][0]}" y2="{H[5][1]}" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{H[5][0]}" y1="{H[5][1]}" x2="{H[0][0]}" y2="{H[0][1]}" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{S[0]}" y1="{S[1]}" x2="{H[4][0]}" y2="{H[4][1]}" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="3,3"/>
      <line x1="{S[0]}" y1="{S[1]}" x2="{H[5][0]}" y2="{H[5][1]}" stroke="#6366f1" stroke-width="1.6" stroke-dasharray="3,3"/>
      <circle cx="{H[4][0]}" cy="{H[4][1]}" r="2.4" fill="#4338ca" fill-opacity="0.85"/>
      <circle cx="{H[5][0]}" cy="{H[5][1]}" r="2.4" fill="#4338ca" fill-opacity="0.85"/>

      <!-- Base hexagonal sombreada translúcida (6 lados visibles) -->
      <polygon points="{H[0][0]},{H[0][1]} {H[1][0]},{H[1][1]} {H[2][0]},{H[2][1]} {H[3][0]},{H[3][1]} {H[4][0]},{H[4][1]} {H[5][0]},{H[5][1]}" fill="#a5b4fc" fill-opacity="0.32"/>

      <!-- Caras laterales semitransparentes -->
      <polygon points="{S[0]},{S[1]} {H[0][0]},{H[0][1]} {H[1][0]},{H[1][1]}" fill="{fill}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.6"/>
      <polygon points="{S[0]},{S[1]} {H[1][0]},{H[1][1]} {H[2][0]},{H[2][1]}" fill="{fill_right}" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.6"/>
      <polygon points="{S[0]},{S[1]} {H[2][0]},{H[2][1]} {H[3][0]},{H[3][1]}" fill="#a5b4fc" fill-opacity="0.45" stroke="{stroke}" stroke-width="1.6"/>

      <!-- Aristas frontales de la base -->
      <line x1="{H[0][0]}" y1="{H[0][1]}" x2="{H[1][0]}" y2="{H[1][1]}" stroke="{stroke}" stroke-width="1.8"/>
      <line x1="{H[1][0]}" y1="{H[1][1]}" x2="{H[2][0]}" y2="{H[2][1]}" stroke="{stroke}" stroke-width="1.8"/>
      <line x1="{H[2][0]}" y1="{H[2][1]}" x2="{H[3][0]}" y2="{H[3][1]}" stroke="{stroke}" stroke-width="1.8"/>

      <!-- Los 7 vértices (6 en la base + 1 cúspide) -->
      <circle cx="{S[0]}" cy="{S[1]}" r="3.2" fill="{stroke}"/>
      <circle cx="{H[0][0]}" cy="{H[0][1]}" r="2.4" fill="{stroke}"/>
      <circle cx="{H[1][0]}" cy="{H[1][1]}" r="2.4" fill="{stroke}"/>
      <circle cx="{H[2][0]}" cy="{H[2][1]}" r="2.4" fill="{stroke}"/>
      <circle cx="{H[3][0]}" cy="{H[3][1]}" r="2.4" fill="{stroke}"/>
    </svg>'''

def get_svg_anatomy_cube(width=320, height=140):
    x, y, w, h = 90, 36, 68, 68
    dx, dy = 34, -23
    A = (x, y)
    B = (x+w, y)
    C = (x+w, y+h)
    D = (x, y+h)
    E = (x+dx, y+dy)
    F = (x+w+dx, y+dy)
    G = (x+w+dx, y+h+dy)
    H = (x+dx, y+h+dy)
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 320 140" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ar-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#dc2626"/>
        </marker>
        <marker id="ar-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#2563eb"/>
        </marker>
      </defs>
      
      <!-- Aristas traseras visibles discontinuas -->
      <line x1="{E[0]}" y1="{E[1]}" x2="{H[0]}" y2="{H[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.75"/>
      <line x1="{D[0]}" y1="{D[1]}" x2="{H[0]}" y2="{H[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.75"/>
      <line x1="{H[0]}" y1="{H[1]}" x2="{G[0]}" y2="{G[1]}" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="3,3" stroke-opacity="0.75"/>
      
      <!-- Caras semitransparentes -->
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {F[0]},{F[1]} {E[0]},{E[1]}" fill="#dbeafe" fill-opacity="0.45" stroke="#1d4ed8" stroke-width="2"/>
      <polygon points="{B[0]},{B[1]} {C[0]},{C[1]} {G[0]},{G[1]} {F[0]},{F[1]}" fill="#bfdbfe" fill-opacity="0.45" stroke="#1d4ed8" stroke-width="2"/>
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {D[0]},{D[1]}" fill="#93c5fd" fill-opacity="0.38" stroke="#1d4ed8" stroke-width="2"/>
      
      <!-- Vértice destacado -->
      <circle cx="{A[0]}" cy="{A[1]}" r="5.2" fill="#ef4444" stroke="#ffffff" stroke-width="1.5"/>
      <!-- Arista destacada -->
      <line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#dc2626" stroke-width="4.2"/>
      
      <!-- Indicador: VÉRTICE -->
      <line x1="45" y1="20" x2="{A[0]-3}" y2="{A[1]-3}" stroke="#dc2626" stroke-width="1.6" marker-end="url(#ar-red)"/>
      <rect x="5" y="8" width="62" height="24" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1.5"/>
      <text x="36" y="24" font-family="Lato, sans-serif" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">VÉRTICE</text>
      
      <!-- Indicador: ARISTA -->
      <line x1="230" y1="70" x2="{B[0]+3}" y2="{B[1]+h/2}" stroke="#dc2626" stroke-width="1.6" marker-end="url(#ar-red)"/>
      <rect x="235" y="58" width="64" height="24" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1.5"/>
      <text x="267" y="74" font-family="Lato, sans-serif" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">ARISTA</text>
      
      <!-- Indicador: CARA -->
      <line x1="48" y1="106" x2="{x+w/3}" y2="{y+h/2}" stroke="#dc2626" stroke-width="1.6" marker-end="url(#ar-red)"/>
      <rect x="10" y="104" width="65" height="24" rx="4" fill="#ffffff" stroke="#dc2626" stroke-width="1.5"/>
      <text x="42" y="120" font-family="Lato, sans-serif" font-size="9.5" font-weight="bold" fill="#dc2626" text-anchor="middle">CARA</text>
      
      <!-- Indicador: BASE SUPERIOR -->
      <line x1="230" y1="22" x2="{x+w/2+dx/2}" y2="{y+dy/2}" stroke="#2563eb" stroke-width="1.6" marker-end="url(#ar-blue)"/>
      <rect x="232" y="10" width="80" height="24" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1.5"/>
      <text x="272" y="26" font-family="Lato, sans-serif" font-size="8.8" font-weight="bold" fill="#2563eb" text-anchor="middle">BASE SUPERIOR</text>
    </svg>'''

def get_svg_anatomy_pyramid(width=320, height=140):
    A = (88, 106)
    B = (140, 120)
    C = (192, 106)
    D = (140, 92)
    S = (140, 20)
    
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 320 140" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ar-pyr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="#c2410c"/>
        </marker>
      </defs>
      
      <!-- Aristas traseras de la base cuadrada discontinua visible -->
      <line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{D[0]}" y1="{D[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      <line x1="{S[0]}" y1="{S[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="3,3"/>
      
      <!-- Base cuadrada translúcida -->
      <polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {D[0]},{D[1]}" fill="#fde047" fill-opacity="0.35"/>

      <!-- Caras laterales semitransparentes -->
      <polygon points="{S[0]},{S[1]} {A[0]},{A[1]} {B[0]},{B[1]}" fill="#ffedd5" fill-opacity="0.45" stroke="#ea580c" stroke-width="1.8"/>
      <polygon points="{S[0]},{S[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="#fed7aa" fill-opacity="0.45" stroke="#ea580c" stroke-width="1.8"/>
      <line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="#ea580c" stroke-width="1.8"/>
      <line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#ea580c" stroke-width="1.8"/>
      
      <!-- Cúspide y vértice basal destacados -->
      <circle cx="{S[0]}" cy="{S[1]}" r="5.2" fill="#dc2626" stroke="#ffffff" stroke-width="1.5"/>
      <circle cx="{B[0]}" cy="{B[1]}" r="3.8" fill="#c2410c"/>
      <line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#b91c1c" stroke-width="3.8"/>
      
      <!-- Indicador: CÚSPIDE -->
      <line x1="70" y1="20" x2="{S[0]-6}" y2="{S[1]}" stroke="#c2410c" stroke-width="1.6" marker-end="url(#ar-pyr)"/>
      <rect x="5" y="8" width="65" height="26" rx="4" fill="#ffffff" stroke="#c2410c" stroke-width="1.5"/>
      <text x="37" y="21" font-family="Lato, sans-serif" font-size="8.8" font-weight="bold" fill="#c2410c" text-anchor="middle">CÚSPIDE</text>
      <text x="37" y="30" font-family="Lato, sans-serif" font-size="7.8" fill="#64748b" text-anchor="middle">(Vértice sup.)</text>
      
      <!-- Indicador: CARA LATERAL -->
      <line x1="52" y1="74" x2="120" y2="72" stroke="#c2410c" stroke-width="1.6" marker-end="url(#ar-pyr)"/>
      <rect x="5" y="62" width="78" height="26" rx="4" fill="#ffffff" stroke="#c2410c" stroke-width="1.5"/>
      <text x="44" y="74" font-family="Lato, sans-serif" font-size="8.8" font-weight="bold" fill="#c2410c" text-anchor="middle">CARA LATERAL</text>
      <text x="44" y="84" font-family="Lato, sans-serif" font-size="7.8" fill="#64748b" text-anchor="middle">(Triangular)</text>
      
      <!-- Indicador: BASE -->
      <line x1="230" y1="116" x2="174" y2="112" stroke="#c2410c" stroke-width="1.6" marker-end="url(#ar-pyr)"/>
      <rect x="232" y="103" width="78" height="26" rx="4" fill="#ffffff" stroke="#c2410c" stroke-width="1.5"/>
      <text x="271" y="115" font-family="Lato, sans-serif" font-size="8.8" font-weight="bold" fill="#c2410c" text-anchor="middle">BASE</text>
      <text x="271" y="125" font-family="Lato, sans-serif" font-size="7.8" fill="#64748b" text-anchor="middle">(1 sola base)</text>
      
      <!-- Indicador: ARISTA -->
      <line x1="230" y1="60" x2="165" y2="112" stroke="#c2410c" stroke-width="1.6" marker-end="url(#ar-pyr)"/>
      <rect x="235" y="48" width="68" height="24" rx="4" fill="#ffffff" stroke="#c2410c" stroke-width="1.5"/>
      <text x="269" y="64" font-family="Lato, sans-serif" font-size="9.5" font-weight="bold" fill="#c2410c" text-anchor="middle">ARISTA</text>
    </svg>'''

def build_exam_html():
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Simulacro de Examen - Matemáticas Primaria</title>
<style>
  @page {{
    size: letter portrait;
    margin: 10mm 12mm 10mm 12mm;
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: 'Lato', 'DejaVu Sans', sans-serif;
    color: #1e293b;
    margin: 0;
    padding: 0;
    font-size: 10pt;
    line-height: 1.34;
    background: #ffffff;
  }}
  .page {{
    page-break-after: always;
    height: 256mm;
    max-height: 256mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }}
  .page:last-child {{
    page-break-after: avoid;
  }}
  
  /* Encabezado */
  .header-card {{
    border: 2px solid #2563eb;
    border-radius: 8px;
    padding: 8px 12px;
    background: #f8fafc;
    margin-bottom: 7px;
  }}
  .header-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 5px;
  }}
  .school-title {{
    font-size: 13pt;
    font-weight: 800;
    color: #1e40af;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .badge-exam {{
    background: #1e40af;
    color: white;
    font-size: 8pt;
    font-weight: bold;
    padding: 3px 8px;
    border-radius: 12px;
  }}
  .header-info-grid {{
    display: grid;
    grid-template-columns: 2.2fr 1fr 1fr;
    gap: 8px;
    font-size: 8.5pt;
  }}
  .info-field {{
    display: flex;
    align-items: baseline;
  }}
  .info-field b {{
    margin-right: 4px;
    color: #334155;
  }}
  .line-fill {{
    flex: 1;
    border-bottom: 1px dotted #64748b;
    min-height: 14px;
  }}
  .header-sub-row {{
    display: flex;
    justify-content: space-between;
    background: #eff6ff;
    padding: 4px 8px;
    border-radius: 4px;
    margin-top: 5px;
    font-size: 8pt;
    color: #1e40af;
    font-weight: 600;
  }}
  
  /* Mini cabecera páginas 2-4 */
  .mini-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 3px;
    margin-bottom: 7px;
    font-size: 8pt;
    color: #475569;
  }}
  .mini-header b {{
    color: #1e40af;
  }}
  
  /* Secciones */
  .section-badge {{
    background: #1e40af;
    color: #ffffff;
    font-weight: 700;
    font-size: 8.5pt;
    padding: 3px 10px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 4px;
    letter-spacing: 0.3px;
  }}
  .section-intro {{
    font-size: 8pt;
    color: #475569;
    margin-bottom: 5px;
    font-style: italic;
  }}
  
  /* Tarjetas de actividades */
  .activity-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 6px 10px;
    margin-bottom: 6px;
    background: #ffffff;
  }}
  .activity-title {{
    font-size: 9pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
  }}
  .activity-pts {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    color: #0f172a;
    font-size: 7.5pt;
    padding: 1px 6px;
    border-radius: 10px;
    font-weight: 600;
  }}
  
  /* Grilla de poliedros */
  .poly-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    margin-top: 3px;
  }}
  .poly-item {{
    border: 1.5px solid #cbd5e1;
    border-radius: 6px;
    padding: 5px 6px;
    text-align: center;
    background: #fcfcfd;
  }}
  .poly-item-tag {{
    font-size: 7.5pt;
    font-weight: 800;
    color: #1e40af;
    background: #e0e7ff;
    display: inline-block;
    padding: 1px 6px;
    border-radius: 4px;
    margin-bottom: 2px;
  }}
  .poly-fields {{
    font-size: 7.5pt;
    text-align: left;
    margin-top: 3px;
    line-height: 1.4;
  }}
  .poly-input-line {{
    border-bottom: 1.2px solid #64748b;
    height: 13px;
    display: inline-block;
    width: 100%;
    margin-top: 1px;
  }}
  .poly-check-row {{
    display: flex;
    justify-content: space-between;
    margin-top: 3px;
  }}
  
  /* Pregunta 2 */
  .choice-block {{
    background: #f8fafc;
    border-left: 3px solid #3b82f6;
    padding: 5px 8px;
    font-size: 8pt;
    margin-bottom: 5px;
  }}
  .vf-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin-top: 4px;
  }}
  .vf-table td {{
    padding: 3.5px 5px;
    border-bottom: 1px solid #e2e8f0;
  }}
  .vf-col-box {{
    width: 42px;
    text-align: center;
    font-weight: bold;
  }}
  .box-vf {{
    border: 1.5px solid #64748b;
    border-radius: 4px;
    padding: 2px 7px;
    display: inline-block;
    background: #fff;
    font-size: 8.5pt;
  }}
  
  /* Tabla de conteo */
  .counting-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 8pt;
    margin-top: 4px;
    text-align: center;
  }}
  .counting-table th {{
    background: #1e3a8a;
    color: #ffffff;
    padding: 5px 4px;
    font-size: 7.5pt;
    font-weight: 700;
    border: 1px solid #1e3a8a;
  }}
  .counting-table td {{
    border: 1px solid #cbd5e1;
    padding: 5px 4px;
  }}
  .counting-table tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .cell-name {{
    text-align: left;
    font-weight: 600;
    color: #1e293b;
    padding-left: 6px !important;
  }}
  
  /* Secuencias */
  .seq-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 9px;
    margin: 4px 0 6px 0;
  }}
  .seq-step {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }}
  .seq-label {{
    font-size: 7.2pt;
    font-weight: 700;
    color: #475569;
    margin-bottom: 2px;
  }}
  .seq-box {{
    border: 1.5px solid #94a3b8;
    background: #ffffff;
    border-radius: 6px;
    padding: 4px 6px;
    min-width: 80px;
    min-height: 48px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 3px;
  }}
  /* Caja de dibujo ampliada, limpia y con cuadrícula de puntos guía */
  .seq-draw-box {{
    border: 2px dashed #2563eb;
    background-color: #ffffff;
    background-image: radial-gradient(#93c5fd 1.3px, transparent 1.3px);
    background-size: 11px 11px;
    border-radius: 6px;
    width: 165px;
    min-width: 165px;
    height: 56px;
    display: block;
    position: relative;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.03);
  }}
  .seq-arrow {{
    font-size: 13pt;
    color: #94a3b8;
    font-weight: bold;
  }}
  
  /* Líneas de redacción */
  .write-line {{
    border-bottom: 1.5px dashed #94a3b8;
    min-height: 18px;
    width: 100%;
    margin-top: 3px;
  }}
  
  /* Pie de página */
  .footer-exam {{
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748b;
  }}
  
  /* Figuras geométricas planas */
  .tri-shape {{
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 14px solid #059669;
    display: inline-block;
  }}
  .sq-shape {{
    width: 12px;
    height: 12px;
    background: #2563eb;
    border-radius: 2px;
    display: inline-block;
  }}
  .cir-shape {{
    width: 13px;
    height: 13px;
    background: #ea580c;
    border-radius: 50%;
    display: inline-block;
  }}
  
  .badge-inc {{
    background: #dcfce7;
    color: #166534;
    border: 1px solid #86efac;
    padding: 1px 6px;
    border-radius: 3px;
    font-weight: bold;
    font-size: 7.5pt;
  }}
  .badge-dec {{
    background: #fee2e2;
    color: #991b1b;
    border: 1px solid #fca5a5;
    padding: 1px 6px;
    border-radius: 3px;
    font-weight: bold;
    font-size: 7.5pt;
  }}
  
  .riddle-box {{
    background: #f8fafc;
    border-left: 3.5px solid #8b5cf6;
    padding: 5px 8px;
    margin: 4px 0;
    font-size: 8pt;
    border-radius: 0 4px 4px 0;
  }}

  /* Cajas creativas de dibujo para la Pregunta 10 (libres de texto interno con cuadrícula guía) */
  .creative-box {{
    border: 1.5px dashed #3b82f6;
    border-radius: 6px;
    background-color: #ffffff;
    background-image: radial-gradient(#93c5fd 1.3px, transparent 1.3px);
    background-size: 11px 11px;
    padding: 4px;
    text-align: center;
    min-height: 82px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.03);
  }}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- PÁGINA 1: IDENTIFICACIÓN Y CLASIFICACIÓN   -->
<!-- ========================================== -->
<div class="page">
  <div>
    <!-- Encabezado del examen -->
    <div class="header-card">
      <div class="header-title-row">
        <div>
          <div class="school-title">Simulacro de Matemáticas</div>
          <div style="font-size: 8pt; color: #475569; font-weight: 500;">Evaluación Diagnóstica: Cuerpos Geométricos 3D y Patrones Secuenciales</div>
        </div>
        <div style="text-align: right;">
          <span class="badge-exam">TIEMPO MÁXIMO: 60 MINUTOS</span>
          <div style="font-size: 7.5pt; color: #64748b; margin-top: 2px;">Puntaje Total: <b>100 pts</b></div>
        </div>
      </div>
      
      <div class="header-info-grid">
        <div class="info-field">
          <b>Nombre de la estudiante:</b>
          <div class="line-fill"></div>
        </div>
        <div class="info-field">
          <b>Fecha:</b>
          <div class="line-fill"></div>
        </div>
        <div class="info-field">
          <b>Grado:</b>
          <div class="line-fill"></div>
        </div>
      </div>
      
      <div class="header-sub-row">
        <span>Instrucciones: Lee cada pregunta con calma. Tienes 1 hora. Escribe con letra clara y dibuja con precisión.</span>
        <span><b>Calificación:</b> [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 100 ]</span>
      </div>
    </div>

    <!-- SECCIÓN 1 -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-badge">SECCIÓN 1: CUERPOS GEOMÉTRICOS — PRISMAS Y PIRÁMIDES</span>
      <span style="font-size: 8pt; font-weight: bold; color: #1e40af;">Valor: 25 Puntos</span>
    </div>
    <div class="section-intro">
      Identifica las características de los poliedros. Recuerda: los prismas tienen dos bases iguales y las pirámides terminan en una cúspide o punta. Los cuerpos son transparentes para que puedas observar la forma de su base en el fondo.
    </div>

    <!-- ACTIVIDAD 1 -->
    <div class="activity-card" style="padding: 6px 9px; margin-bottom: 6px;">
      <div class="activity-title">
        <span>1. Galería Geométrica: Reconocimiento Visual y Clasificación</span>
        <span class="activity-pts">15 Puntos (2.5 pts c/u)</span>
      </div>
      <div style="font-size: 7.8pt; color: #334155; margin-bottom: 3px;">
        Observa cada cuerpo geométrico a través de sus caras transparentes. Escribe su <b>nombre completo</b>, marca si es <b>Prisma o Pirámide</b>, e indica la <b>figura de su base</b>.
      </div>
      
      <div class="poly-grid">
        <!-- Cuerpo A -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo A</div>
          <div>{get_svg_cube(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
        
        <!-- Cuerpo B -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo B</div>
          <div>{get_svg_square_pyramid(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
        
        <!-- Cuerpo C -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo C</div>
          <div>{get_svg_triangular_prism(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
        
        <!-- Cuerpo D -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo D</div>
          <div>{get_svg_triangular_pyramid(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
        
        <!-- Cuerpo E -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo E</div>
          <div>{get_svg_pentagonal_prism(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
        
        <!-- Cuerpo F -->
        <div class="poly-item">
          <div class="poly-item-tag">Cuerpo F</div>
          <div>{get_svg_hexagonal_pyramid(width=90, height=75)}</div>
          <div class="poly-fields">
            <b>Nombre:</b> <span class="poly-input-line"></span>
            <div class="poly-check-row">
              <label><input type="checkbox"> Prisma</label>
              <label><input type="checkbox"> Pirámide</label>
            </div>
            <b>Forma base:</b> <span class="poly-input-line"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- ACTIVIDAD 2 -->
    <div class="activity-card" style="padding: 6px 9px;">
      <div class="activity-title">
        <span>2. Diferencias Fundamentales: ¿Prisma o Pirámide?</span>
        <span class="activity-pts">10 Puntos</span>
      </div>
      
      <div class="choice-block">
        <b>A. Opción Múltiple con Justificación (4 pts):</b><br>
        ¿Cuál es la diferencia principal entre las <b>caras laterales</b> de un prisma recto y las de una pirámide?
        <div style="margin-top: 2px; font-size: 8pt;">
          <label style="display: block; margin: 2px 0;"><input type="radio" name="p2a"> <b>a)</b> Los prismas tienen caras laterales triangulares y las pirámides caras circulares.</label>
          <label style="display: block; margin: 2px 0;"><input type="radio" name="p2a"> <b>b)</b> Los prismas tienen caras laterales con forma de rectángulo, mientras que las pirámides tienen caras laterales triangulares que se unen en la punta.</label>
          <label style="display: block; margin: 2px 0;"><input type="radio" name="p2a"> <b>c)</b> No hay diferencia, ambos cuerpos tienen siempre las mismas caras laterales.</label>
        </div>
        <div style="margin-top: 4px; font-size: 7.8pt;">
          <b>Explica con tus palabras por qué elegiste esa opción:</b>
          <div class="write-line"></div>
          <div class="write-line"></div>
        </div>
      </div>

      <div style="font-size: 8pt;">
        <b>B. Detective de la Verdad: Escribe (V) si es Verdadero o (F) si es Falso (6 pts - 2 pts c/u):</b>
        <table class="vf-table">
          <tr>
            <td class="vf-col-box"><span class="box-vf">&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
            <td>1. Un prisma siempre tiene <b>dos bases</b> que son polígonos exactamente iguales y paralelos.</td>
          </tr>
          <tr>
            <td class="vf-col-box"><span class="box-vf">&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
            <td>2. Una pirámide cuadrangular tiene dos bases con forma de cuadrado.</td>
          </tr>
          <tr>
            <td class="vf-col-box"><span class="box-vf">&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
            <td>3. El punto más alto donde se juntan las caras triangulares de una pirámide se llama <b>cúspide o vértice superior</b>.</td>
          </tr>
        </table>
      </div>
    </div>
  </div>

  <!-- Pie de página -->
  <div class="footer-exam">
    <span>Simulacro de Matemáticas | Temas: Cuerpos Geométricos y Secuencias</span>
    <span>Página <b>1</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- PÁGINA 2: CARACTERIZACIÓN (CARAS, VÉRTICES) -->
<!-- ========================================== -->
<div class="page">
  <div>
    <!-- Running header -->
    <div class="mini-header">
      <div><b>Simulacro de Matemáticas</b> | Sección 2: Caracterización de Cuerpos</div>
      <div>Nombre de la estudiante: _____________________________________ | Pág. <b>2</b> de <b>4</b></div>
    </div>

    <!-- SECCIÓN 2 -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-badge">SECCIÓN 2: CARACTERIZACIÓN — CARAS, VÉRTICES Y ARISTAS</span>
      <span style="font-size: 8pt; font-weight: bold; color: #1e40af;">Valor: 25 Puntos</span>
    </div>
    <div class="section-intro">
      Los elementos fundamentales de un poliedro son sus caras (superficies), aristas (líneas) y vértices (puntos).
    </div>

    <!-- ACTIVIDAD 3 -->
    <div class="activity-card" style="padding: 6px 9px; margin-bottom: 6px;">
      <div class="activity-title">
        <span>3. Anatomía de los Poliedros: Identificación de Partes</span>
        <span class="activity-pts">9 Puntos</span>
      </div>
      <div style="font-size: 7.8pt; color: #334155; margin-bottom: 3px;">
        Observa los diagramas anatómicos del <b>Prisma</b> y de la <b>Pirámide</b>. Revisa las flechas que señalan cada elemento.
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <div style="border: 1px solid #cbd5e1; border-radius: 6px; padding: 4px; text-align: center; background: #fafafa;">
          <div style="font-size: 7.5pt; font-weight: bold; color: #1e40af; margin-bottom: 1px;">PRISMA (Cubo / Prisma Rectangular)</div>
          {get_svg_anatomy_cube(width=305, height=130)}
        </div>
        <div style="border: 1px solid #cbd5e1; border-radius: 6px; padding: 4px; text-align: center; background: #fafafa;">
          <div style="font-size: 7.5pt; font-weight: bold; color: #c2410c; margin-bottom: 1px;">PIRÁMIDE CUADRANGULAR</div>
          {get_svg_anatomy_pyramid(width=305, height=130)}
        </div>
      </div>

      <div style="margin-top: 5px; font-size: 8pt;">
        <b>Define brevemente con tus palabras qué es cada parte (1 pt c/u):</b>
        <div style="margin-top: 3px;">
          • <b>Una CARA es:</b> <span class="poly-input-line" style="width: 85%;"></span>
        </div>
        <div style="margin-top: 3px;">
          • <b>Una ARISTA es:</b> <span class="poly-input-line" style="width: 83%;"></span>
        </div>
        <div style="margin-top: 3px;">
          • <b>Un VÉRTICE es:</b> <span class="poly-input-line" style="width: 83%;"></span>
        </div>
      </div>
    </div>

    <!-- ACTIVIDAD 4 -->
    <div class="activity-card" style="padding: 6px 9px; margin-bottom: 6px;">
      <div class="activity-title">
        <span>4. Gran Tabla de Conteo Sistemático</span>
        <span class="activity-pts">10 Puntos (2 pts por fila completa)</span>
      </div>
      <div style="font-size: 7.8pt; color: #334155; margin-bottom: 2px;">
        Cuenta con mucha atención las partes de cada cuerpo geométrico y completa la tabla:
      </div>

      <table class="counting-table">
        <thead>
          <tr>
            <th style="width: 25%;">Cuerpo Geométrico</th>
            <th style="width: 15%;">Forma de la Base</th>
            <th style="width: 12%;">N° de Bases</th>
            <th style="width: 14%;">Caras Laterales</th>
            <th style="width: 12%;">TOTAL CARAS</th>
            <th style="width: 11%;">VÉRTICES</th>
            <th style="width: 11%;">ARISTAS</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="cell-name"><b>1. Cubo</b> (Prisma cuadrangular)</td>
            <td>Cuadrado</td>
            <td>2</td>
            <td>4</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td class="cell-name"><b>2. Prisma Triangular</b></td>
            <td>Triángulo</td>
            <td>&nbsp;</td>
            <td>3</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td class="cell-name"><b>3. Pirámide Cuadrangular</b></td>
            <td>Cuadrado</td>
            <td>&nbsp;</td>
            <td>4</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td class="cell-name"><b>4. Pirámide Triangular</b></td>
            <td>Triángulo</td>
            <td>1</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
          <tr>
            <td class="cell-name"><b>5. Prisma Pentagonal</b></td>
            <td>Pentágono</td>
            <td>2</td>
            <td>5</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ACTIVIDAD 5 -->
    <div class="activity-card" style="padding: 6px 9px;">
      <div class="activity-title">
        <span>5. Detective de Cuerpos: Adivinanzas Geométricas</span>
        <span class="activity-pts">6 Puntos (3 pts c/u)</span>
      </div>
      
      <div class="riddle-box">
        <b>Misterio A:</b> <i>"Soy un cuerpo que tiene en total <b>5 caras</b>: una base cuadrada y 4 caras laterales triangulares que se juntan en una punta. Mis esquinas son <b>5 vértices</b> y tengo <b>8 aristas</b>. ¿Quién soy?"</i>
        <div style="margin-top: 4px; font-size: 8pt;">
          <b>Respuesta del Detective:</b> Soy la / el ____________________________________________________
        </div>
      </div>

      <div class="riddle-box">
        <b>Misterio B:</b> <i>"Tengo exactamente <b>2 bases</b> con forma de triángulo y <b>3 caras laterales</b> rectangulares. Si cuentas mis esquinas verás <b>6 vértices</b> y tengo <b>9 aristas</b>. ¿Quién soy?"</i>
        <div style="margin-top: 4px; font-size: 8pt;">
          <b>Respuesta del Detective:</b> Soy la / el ____________________________________________________
        </div>
      </div>
    </div>
  </div>

  <!-- Pie de página -->
  <div class="footer-exam">
    <span>Simulacro de Matemáticas | Temas: Cuerpos Geométricos y Secuencias</span>
    <span>Página <b>2</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- PÁGINA 3: SECUENCIAS GEOMÉTRICAS           -->
<!-- ========================================== -->
<div class="page">
  <div>
    <!-- Running header -->
    <div class="mini-header">
      <div><b>Simulacro de Matemáticas</b> | Sección 3: Secuencias y Patrones</div>
      <div>Nombre de la estudiante: _____________________________________ | Pág. <b>3</b> de <b>4</b></div>
    </div>

    <!-- SECCIÓN 3 -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-badge">SECCIÓN 3: SECUENCIAS GEOMÉTRICAS (INCREMENTALES Y DECREMENTALES)</span>
      <span style="font-size: 8pt; font-weight: bold; color: #1e40af;">Valor: 30 Puntos</span>
    </div>
    <div class="section-intro">
      Analiza cómo cambian las figuras. Una secuencia es <b>incremental</b> si crece (suma figuras) y <b>decremental</b> si disminuye (resta figuras). En el Paso 4, utiliza los puntos guía para dibujar con comodidad.
    </div>

    <!-- ACTIVIDAD 6 -->
    <div class="activity-card" style="padding: 5px 8px; margin-bottom: 5px;">
      <div class="activity-title">
        <span>6. Secuencia con Triángulos: Descubre la Regla</span>
        <span class="activity-pts">10 Puntos</span>
      </div>

      <div class="seq-container">
        <!-- Paso 1 -->
        <div class="seq-step">
          <span class="seq-label">Paso 1</span>
          <div class="seq-box">
            <span class="tri-shape"></span> <span class="tri-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(2 triángulos)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 2 -->
        <div class="seq-step">
          <span class="seq-label">Paso 2</span>
          <div class="seq-box">
            <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(5 triángulos)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 3 -->
        <div class="seq-step">
          <span class="seq-label">Paso 3</span>
          <div class="seq-box" style="min-width: 95px;">
            <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span> <span class="tri-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(8 triángulos)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 4 (Dibujo limpio sin texto invasivo adentro) -->
        <div class="seq-step">
          <span class="seq-label" style="color: #1e40af; font-weight: 800; font-size: 7.8pt;">Paso 4 (Dibuja aquí)</span>
          <div class="seq-draw-box"></div>
          <span style="font-size: 7.3pt; font-weight: bold; margin-top: 2px; color: #1e40af;">Total: [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] triángulos</span>
        </div>
      </div>

      <div style="font-size: 8pt; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <div>
          <b>a) Tipo de secuencia (marca con X) (2 pts):</b><br>
          <label><input type="radio" name="p6_tipo"> <span class="badge-inc">Incremental (Creciente)</span></label>&nbsp;&nbsp;
          <label><input type="radio" name="p6_tipo"> <span class="badge-dec">Decremental (Decreciente)</span></label>
        </div>
        <div>
          <b>b) Predicción numérica (2 pts):</b><br>
          ¿Cuántos triángulos tendrá el <b>Paso 5</b>?: [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> ] &nbsp;|&nbsp;
          ¿Y el <b>Paso 6</b>?: [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> ]
        </div>
      </div>

      <div style="margin-top: 4px; font-size: 8pt;">
        <b>c) Explica con tus palabras la regla de esta secuencia (¿cómo se obtiene el siguiente paso?) (6 pts):</b>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>

    <!-- ACTIVIDAD 7 -->
    <div class="activity-card" style="padding: 5px 8px; margin-bottom: 5px;">
      <div class="activity-title">
        <span>7. Secuencia con Cuadrados: Disminución Paso a Paso</span>
        <span class="activity-pts">10 Puntos</span>
      </div>

      <div class="seq-container">
        <!-- Paso 1 -->
        <div class="seq-step">
          <span class="seq-label">Paso 1</span>
          <div class="seq-box" style="max-width: 100px;">
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(14 cuadrados)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 2 -->
        <div class="seq-step">
          <span class="seq-label">Paso 2</span>
          <div class="seq-box" style="max-width: 95px;">
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
            <span class="sq-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(11 cuadrados)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 3 -->
        <div class="seq-step">
          <span class="seq-label">Paso 3</span>
          <div class="seq-box" style="max-width: 85px;">
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
            <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span> <span class="sq-shape"></span>
          </div>
          <span style="font-size: 7.2pt; font-weight: bold; margin-top: 2px;">(8 cuadrados)</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 4 (Dibujo limpio sin texto invasivo adentro) -->
        <div class="seq-step">
          <span class="seq-label" style="color: #1e40af; font-weight: 800; font-size: 7.8pt;">Paso 4 (Dibuja aquí)</span>
          <div class="seq-draw-box"></div>
          <span style="font-size: 7.3pt; font-weight: bold; margin-top: 2px; color: #1e40af;">Total: [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] cuadrados</span>
        </div>
      </div>

      <div style="font-size: 8pt; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
        <div>
          <b>a) Tipo de secuencia (marca con X) (2 pts):</b><br>
          <label><input type="radio" name="p7_tipo"> <span class="badge-inc">Incremental (Creciente)</span></label>&nbsp;&nbsp;
          <label><input type="radio" name="p7_tipo"> <span class="badge-dec">Decremental (Decreciente)</span></label>
        </div>
        <div>
          <b>b) Pregunta de análisis (2 pts):</b><br>
          ¿Cuántos cuadrados tendrá el <b>Paso 5</b>?: [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> ]<br>
          ¿En qué paso los cuadrados se acabarán (llegará a cero)?: [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> ]
        </div>
      </div>

      <div style="margin-top: 4px; font-size: 8pt;">
        <b>c) Explica con tus palabras la regla de esta secuencia (¿cómo cambia la cantidad de figuras?) (6 pts):</b>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>

    <!-- ACTIVIDAD 8 -->
    <div class="activity-card" style="padding: 5px 8px;">
      <div class="activity-title">
        <span>8. Secuencia Combinada: Círculos y Cuadrados</span>
        <span class="activity-pts">10 Puntos</span>
      </div>
      <div style="font-size: 7.8pt; color: #334155; margin-bottom: 2px;">
        Esta secuencia combina dos figuras a la vez: <b>Círculos naranjas</b> y <b>Cuadrados azules</b>.
      </div>

      <div class="seq-container" style="padding: 5px 8px; margin-bottom: 4px;">
        <!-- Paso 1 -->
        <div class="seq-step">
          <span class="seq-label">Paso 1</span>
          <div class="seq-box" style="min-width: 75px; min-height: 44px;">
            <span class="cir-shape"></span> &nbsp; <span class="sq-shape"></span><span class="sq-shape"></span>
          </div>
          <span style="font-size: 7pt; color: #475569;">1 Círc., 2 Cuad.</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 2 -->
        <div class="seq-step">
          <span class="seq-label">Paso 2</span>
          <div class="seq-box" style="min-width: 85px; min-height: 44px;">
            <span class="cir-shape"></span><span class="cir-shape"></span> &nbsp; <span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span>
          </div>
          <span style="font-size: 7pt; color: #475569;">2 Círc., 4 Cuad.</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 3 -->
        <div class="seq-step">
          <span class="seq-label">Paso 3</span>
          <div class="seq-box" style="min-width: 95px; min-height: 44px;">
            <span class="cir-shape"></span><span class="cir-shape"></span><span class="cir-shape"></span> &nbsp; <span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span><span class="sq-shape"></span>
          </div>
          <span style="font-size: 7pt; color: #475569;">3 Círc., 6 Cuad.</span>
        </div>
        <span class="seq-arrow">➔</span>
        <!-- Paso 4 (Dibujo limpio sin texto adentro) -->
        <div class="seq-step">
          <span class="seq-label" style="color: #1e40af; font-weight: 800; font-size: 7.8pt;">Paso 4 (Dibuja aquí)</span>
          <div class="seq-draw-box"></div>
          <span style="font-size: 7.3pt; color: #1e40af; font-weight: bold; margin-top: 2px;">Total: [ &nbsp;&nbsp;&nbsp; ] Círc. y [ &nbsp;&nbsp;&nbsp; ] Cuad.</span>
        </div>
      </div>

      <div style="font-size: 8pt; line-height: 1.4;">
        <b>a) Analiza cada figura por separado (4 pts):</b><br>
        • Los <b>círculos</b> van de: 1 ➔ 2 ➔ 3 ➔ ____. Es una secuencia __________________ que aumenta de ____ en ____.<br>
        • Los <b>cuadrados</b> van de: 2 ➔ 4 ➔ 6 ➔ ____. Es una secuencia __________________ que aumenta de ____ en ____.
      </div>
      <div style="margin-top: 3px; font-size: 8pt;">
        <b>b) Explica en palabras la regla general para dibujar cualquier paso siguiente (6 pts):</b>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>
  </div>

  <!-- Pie de página -->
  <div class="footer-exam">
    <span>Simulacro de Matemáticas | Temas: Cuerpos Geométricos y Secuencias</span>
    <span>Página <b>3</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- PÁGINA 4: APLICACIÓN Y RETO CREATIVO       -->
<!-- ========================================== -->
<div class="page">
  <div>
    <!-- Running header -->
    <div class="mini-header">
      <div><b>Simulacro de Matemáticas</b> | Sección 4: Aplicación y Desafío Creativo</div>
      <div>Nombre de la estudiante: _____________________________________ | Pág. <b>4</b> de <b>4</b></div>
    </div>

    <!-- SECCIÓN 4 -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-badge">SECCIÓN 4: DESAFÍOS DE APLICACIÓN Y PENSAMIENTO CREATIVO</span>
      <span style="font-size: 8pt; font-weight: bold; color: #1e40af;">Valor: 20 Puntos</span>
    </div>
    <div class="section-intro">
      Aplica lo que sabes a situaciones de la vida real y demuestra tu creatividad inventando tu propio patrón geométrico.
    </div>

    <!-- ACTIVIDAD 9 -->
    <div class="activity-card" style="padding: 6px 9px; margin-bottom: 6px;">
      <div class="activity-title">
        <span>9. Desafíos del Mundo Real: Modelando Cuerpos</span>
        <span class="activity-pts">10 Puntos (5 pts por situación)</span>
      </div>

      <!-- Situación A -->
      <div style="background: #f8fafc; border-left: 3.5px solid #0284c7; padding: 5px 8px; margin-bottom: 5px; font-size: 8pt;">
        <b>Situación A: El Taller de Esculturas con Palillos y Plastilina (5 pts)</b><br>
        Mateo quiere armar en su clase de ciencias dos maquetas utilizando <b>palillos para las aristas</b> y <b>bolitas de plastilina para los vértices</b>:
        <div style="margin-top: 3px; font-size: 7.8pt; line-height: 1.45;">
          1. Para construir una maqueta de un <b>Prisma Triangular</b>, ¿cuántos palillos y cuántas bolitas necesita Mateo?<br>
          &nbsp;&nbsp;&nbsp;&nbsp;➔ Palillos (aristas): <b>__________</b> &nbsp;&nbsp;|&nbsp;&nbsp; Bolitas (vértices): <b>__________</b><br>
          2. Para construir una maqueta de una <b>Pirámide Cuadrangular</b>, ¿cuántos palillos y cuántas bolitas necesita?<br>
          &nbsp;&nbsp;&nbsp;&nbsp;➔ Palillos (aristas): <b>__________</b> &nbsp;&nbsp;|&nbsp;&nbsp; Bolitas (vértices): <b>__________</b><br>
          3. Si Mateo tiene una caja con <b>12 palillos</b> y <b>8 bolitas de plastilina</b>, ¿cuál de los siguientes cuerpos puede armar <i>exactamente</i> sin que le sobre ningún material?<br>
          &nbsp;&nbsp;&nbsp;&nbsp;<label><input type="radio" name="p9_cubo"> Un Cubo</label> &nbsp;&nbsp;&nbsp;&nbsp;
          <label><input type="radio" name="p9_cubo"> Una Pirámide Pentagonal</label> &nbsp;&nbsp;&nbsp;&nbsp;
          <label><input type="radio" name="p9_cubo"> Un Prisma Triangular</label>
        </div>
      </div>

      <!-- Situación B -->
      <div style="background: #f8fafc; border-left: 3.5px solid #16a34a; padding: 5px 8px; font-size: 8pt;">
        <b>Situación B: El Campamento de Geometría (5 pts)</b><br>
        En una excursión escolar, dos grupos armaron sus carpas para acampar:<br>
        • La carpa del Grupo Verde tiene forma de <b>Pirámide Cuadrangular</b>.<br>
        • La carpa del Grupo Azul tiene forma de <b>Prisma Triangular</b>.<br>
        <div style="margin-top: 3px; font-size: 7.8pt; line-height: 1.45;">
          a) ¿Cuántas caras en total tiene la carpa del Grupo Verde? [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> caras ]<br>
          b) ¿Cuántas caras en total tiene la carpa del Grupo Azul? [ <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b> caras ]<br>
          c) ¿Cuál de las dos carpas tiene <b>más vértices (esquinas)</b>? Explica demostrando la cantidad de vértices de cada carpa:<br>
          <div class="write-line"></div>
        </div>
      </div>
    </div>

    <!-- ACTIVIDAD 10 -->
    <div class="activity-card" style="padding: 6px 9px;">
      <div class="activity-title">
        <span>10. ¡Tú eres la Diseñadora!: Crea tu Propia Secuencia Geométrica</span>
        <span class="activity-pts">10 Puntos</span>
      </div>
      <div style="font-size: 7.8pt; color: #334155; margin-bottom: 3px;">
        Diseña una secuencia usando <b>cuadrados</b>, <b>círculos</b> o <b>triángulos</b>. Elige si quieres que sea incremental (creciente) o decremental (decreciente). Debe tener 4 pasos con una regla constante.
      </div>

      <div style="font-size: 8pt; margin-bottom: 4px;">
        <b>a) Mi secuencia será (marca una con X):</b> &nbsp;&nbsp;
        <label><input type="checkbox"> <b>Incremental (suma figuras)</b></label> &nbsp;&nbsp;&nbsp;&nbsp;
        <label><input type="checkbox"> <b>Decremental (resta figuras)</b></label>
      </div>

      <!-- Cajas de dibujo limpias para la estudiante con puntos guía -->
      <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin: 4px 0;">
        <div class="creative-box">
          <div style="font-size: 7.5pt; font-weight: bold; color: #475569;">Paso 1</div>
          <div></div>
          <div style="font-size: 7.5pt; font-weight: bold;">Cantidad: [ &nbsp;&nbsp;&nbsp; ]</div>
        </div>
        <div class="creative-box">
          <div style="font-size: 7.5pt; font-weight: bold; color: #475569;">Paso 2</div>
          <div></div>
          <div style="font-size: 7.5pt; font-weight: bold;">Cantidad: [ &nbsp;&nbsp;&nbsp; ]</div>
        </div>
        <div class="creative-box">
          <div style="font-size: 7.5pt; font-weight: bold; color: #475569;">Paso 3</div>
          <div></div>
          <div style="font-size: 7.5pt; font-weight: bold;">Cantidad: [ &nbsp;&nbsp;&nbsp; ]</div>
        </div>
        <div class="creative-box">
          <div style="font-size: 7.5pt; font-weight: bold; color: #475569;">Paso 4</div>
          <div></div>
          <div style="font-size: 7.5pt; font-weight: bold;">Cantidad: [ &nbsp;&nbsp;&nbsp; ]</div>
        </div>
      </div>

      <div style="margin-top: 4px; font-size: 8pt;">
        <b>b) Explica en palabras cuál es la regla secreta de tu secuencia para que otra persona la pueda resolver:</b>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>

    <!-- AUTOEVALUACIÓN Y CIERRE -->
    <div style="border: 1.5px solid #e2e8f0; border-radius: 6px; padding: 6px 10px; background: #f8fafc; margin-top: 5px;">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #1e40af;">
          🌟 ¡Felicitaciones por completar tu simulacro de matemáticas!
        </div>
        <div style="font-size: 7.8pt; color: #64748b;">
          Firma de la estudiante: _______________________
        </div>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 8pt; margin-top: 4px; color: #334155;">
        <span>¿Cómo te sentiste con la prueba?: &nbsp;
          <label><input type="checkbox"> Muy fácil 😊</label> &nbsp;&nbsp;
          <label><input type="checkbox"> Bien 🙂</label> &nbsp;&nbsp;
          <label><input type="checkbox"> Tuvo su reto 🤔</label>
        </span>
        <span>Tiempo empleado: [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] minutos</span>
      </div>
    </div>
  </div>

  <!-- Pie de página -->
  <div class="footer-exam">
    <span>Simulacro de Matemáticas | Temas: Cuerpos Geométricos y Secuencias</span>
    <span>Página <b>4</b> de <b>4</b></span>
  </div>
</div>

</body>
</html>'''

def build_solution_guide_html():
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Solucionario y Guía Pedagógica de Evaluación</title>
<style>
  @page {{
    size: letter portrait;
    margin: 10mm 12mm 10mm 12mm;
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: 'Lato', 'DejaVu Sans', sans-serif;
    color: #1e293b;
    margin: 0;
    padding: 0;
    font-size: 9.5pt;
    line-height: 1.34;
    background: #ffffff;
  }}
  .page {{
    page-break-after: always;
    height: 256mm;
    max-height: 256mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }}
  .page:last-child {{
    page-break-after: avoid;
  }}
  
  .guide-header {{
    border: 2px solid #0f766e;
    background: #f0fdfa;
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 7px;
  }}
  .guide-title-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #99f6e4;
    padding-bottom: 4px;
    margin-bottom: 4px;
  }}
  .guide-title {{
    font-size: 12.5pt;
    font-weight: 800;
    color: #0f766e;
    text-transform: uppercase;
  }}
  .badge-guide {{
    background: #0f766e;
    color: white;
    font-size: 7.8pt;
    font-weight: bold;
    padding: 3px 8px;
    border-radius: 10px;
  }}
  
  .section-tag {{
    background: #0f766e;
    color: white;
    font-weight: bold;
    font-size: 8pt;
    padding: 2px 8px;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 3px;
  }}
  
  .ans-card {{
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 6px 9px;
    margin-bottom: 6px;
    background: #ffffff;
  }}
  .ans-title {{
    font-size: 8.8pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 3px;
    display: flex;
    justify-content: space-between;
  }}
  .badge-pts {{
    background: #e0f2fe;
    color: #0369a1;
    font-size: 7.2pt;
    padding: 1px 5px;
    border-radius: 8px;
    font-weight: 700;
  }}
  
  .correct-box {{
    background: #ecfdf5;
    border-left: 3.5px solid #10b981;
    padding: 4px 7px;
    font-size: 8pt;
    margin: 2px 0;
    border-radius: 0 4px 4px 0;
  }}
  .rubric-box {{
    background: #fffbeb;
    border-left: 3.5px solid #f59e0b;
    padding: 4px 7px;
    font-size: 7.8pt;
    margin: 2px 0;
    border-radius: 0 4px 4px 0;
  }}
  .pedagogy-tip {{
    background: #eff6ff;
    border-left: 3.5px solid #3b82f6;
    padding: 4px 7px;
    font-size: 7.8pt;
    margin: 2px 0;
    border-radius: 0 4px 4px 0;
  }}
  
  .table-ans {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    margin: 3px 0;
    text-align: center;
  }}
  .table-ans th {{
    background: #0f766e;
    color: white;
    padding: 4px 3px;
    font-size: 7.2pt;
    border: 1px solid #0f766e;
  }}
  .table-ans td {{
    border: 1px solid #cbd5e1;
    padding: 4px 3px;
  }}
  .table-ans tr:nth-child(even) {{
    background: #f8fafc;
  }}
  
  .mini-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #0f766e;
    padding-bottom: 3px;
    margin-bottom: 5px;
    font-size: 7.8pt;
    color: #475569;
  }}
  
  .footer-exam {{
    border-top: 1px solid #cbd5e1;
    padding-top: 3px;
    display: flex;
    justify-content: space-between;
    font-size: 7.2pt;
    color: #64748b;
  }}
  
  .traffic-light {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 5px;
    margin: 3px 0;
  }}
  .tl-card {{
    border-radius: 6px;
    padding: 4px 6px;
    font-size: 7.2pt;
  }}
  .tl-green {{ background: #dcfce7; border: 1px solid #86efac; color: #14532d; }}
  .tl-yellow {{ background: #fef9c3; border: 1px solid #fde047; color: #713f12; }}
  .tl-red {{ background: #fee2e2; border: 1px solid #fca5a5; color: #7f1d1d; }}

  .mini-tri {{
    width: 0;
    height: 0;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-bottom: 9px solid #059669;
    display: inline-block;
    margin: 1px;
  }}
  .mini-sq {{
    width: 8px;
    height: 8px;
    background: #2563eb;
    border-radius: 1px;
    display: inline-block;
    margin: 1px;
  }}
  .mini-cir {{
    width: 8px;
    height: 8px;
    background: #ea580c;
    border-radius: 50%;
    display: inline-block;
    margin: 1px;
  }}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- GUÍA PÁGINA 1: INTRODUCCIÓN Y SECCIÓN 1    -->
<!-- ========================================== -->
<div class="page">
  <div>
    <div class="guide-header">
      <div class="guide-title-row">
        <div>
          <div class="guide-title">Solucionario y Guía Pedagógica</div>
          <div style="font-size: 8pt; color: #334155;">Documento de apoyo para el Evaluador / Padre de Familia</div>
        </div>
        <div style="text-align: right;">
          <span class="badge-guide">USO EXCLUSIVO EVALUADOR</span>
          <div style="font-size: 7.2pt; color: #475569; margin-top: 2px;">Simulacro de 60 minutos | 100 Puntos</div>
        </div>
      </div>
      <div style="font-size: 7.8pt; color: #134e4a; line-height: 1.35;">
        <b>Consejo de aplicación:</b> Brinda un espacio silencioso y cómodo. Permite que trabaje de forma autónoma durante los 60 minutos. En esta versión actualizada, los cuerpos 3D poseen <b>caras semitransparentes</b> para que pueda ver la base interior y no confunda la pirámide cuadrangular con la triangular.
      </div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-tag">SECCIÓN 1: CUERPOS GEOMÉTRICOS — PRISMAS Y PIRÁMIDES</span>
      <span style="font-size: 7.8pt; font-weight: bold; color: #0f766e;">Total Sección: 25 Puntos</span>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 1 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 1: Reconocimiento Visual (15 Puntos - 2.5 pts c/u)</span>
        <span class="badge-pts">15 Pts</span>
      </div>
      
      <div style="font-size: 7.8pt; display: grid; grid-template-columns: 1fr 1fr; gap: 5px;">
        <div class="correct-box">
          <b>• Cuerpo A:</b> <b>Cubo</b> (o Prisma Cuadrangular / Hexaedro).<br>
          Tipo: <b>[X] Prisma</b> | Forma de base: <b>Cuadrado</b> (2 bases).
        </div>
        <div class="correct-box">
          <b>• Cuerpo B:</b> <b>Pirámide Cuadrangular</b>.<br>
          Tipo: <b>[X] Pirámide</b> | Forma de base: <b>Cuadrado</b> (base de 4 lados visible al fondo).
        </div>
        <div class="correct-box">
          <b>• Cuerpo C:</b> <b>Prisma Triangular</b>.<br>
          Tipo: <b>[X] Prisma</b> | Forma de base: <b>Triángulo</b> (2 bases triangulares).
        </div>
        <div class="correct-box">
          <b>• Cuerpo D:</b> <b>Pirámide Triangular</b> (Tetraedro).<br>
          Tipo: <b>[X] Pirámide</b> | Forma de base: <b>Triángulo</b> (base de 3 lados visible al fondo).
        </div>
        <div class="correct-box">
          <b>• Cuerpo E:</b> <b>Prisma Pentagonal</b>.<br>
          Tipo: <b>[X] Prisma</b> | Forma de base: <b>Pentágono</b> (5 lados).
        </div>
        <div class="correct-box">
          <b>• Cuerpo F:</b> <b>Pirámide Hexagonal</b>.<br>
          Tipo: <b>[X] Pirámide</b> | Forma de base: <b>Hexágono</b> (6 lados).
        </div>
      </div>
      
      <div class="pedagogy-tip">
        <b>💡 Distinción clave entre Cuerpo B y Cuerpo D:</b> Gracias a las caras semitransparentes, en el <b>Cuerpo B</b> se observan 4 lados en la base y 5 vértices en total, mientras que en el <b>Cuerpo D</b> se observan 3 lados en la base y 4 vértices en total. Si tu hija nota esta diferencia, valora su capacidad de observación espacial.
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 2 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 2: Diferencias Fundamentales (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      
      <div class="correct-box">
        <b>A. Opción Múltiple (4 pts):</b><br>
        Respuesta correcta: <b>Opción b)</b> <i>"Los prismas tienen caras laterales con forma de rectángulo, mientras que las pirámides tienen caras laterales triangulares que se unen en la punta."</i><br>
        <b>Rúbrica de Justificación (2 pts):</b> Es correcta si menciona que en los prismas los lados son rectangulares conectando dos bases, mientras que en las pirámides las caras son triángulos que suben hasta la cúspide.
      </div>

      <div class="correct-box" style="margin-top: 3px;">
        <b>B. Verdadero o Falso (6 pts - 2 pts c/u):</b><br>
        <b>1. ( V ) Verdadero:</b> Todo prisma tiene dos bases iguales y paralelas.<br>
        <b>2. ( F ) Falso:</b> Una pirámide cuadrangular tiene <b>una sola base</b> cuadrada (no dos).<br>
        <b>3. ( V ) Verdadero:</b> La cúspide es el vértice superior donde coinciden las caras laterales triangulares.
      </div>

      <div class="rubric-box">
        <b>⚠️ Error común frecuente:</b> Algunos niños confunden el número de lados de la base (4) con el número de bases (1). Si comete este error, pídele que imagine la Pirámide de Egipto: ¿puede apoyarse arriba y abajo a la vez? No, solo se apoya en el suelo (1 base).
      </div>
    </div>
  </div>

  <div class="footer-exam">
    <span>Guía de Respuestas y Rúbrica de Calificación | Simulacro de Matemáticas</span>
    <span>Página <b>1</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- GUÍA PÁGINA 2: SECCIÓN 2 (CARACTERIZACIÓN) -->
<!-- ========================================== -->
<div class="page">
  <div>
    <div class="mini-header">
      <div><b>Solucionario y Guía Pedagógica</b> | Sección 2: Caracterización</div>
      <div>Uso Exclusivo Evaluador | Pág. <b>2</b> de <b>4</b></div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-tag">SECCIÓN 2: CARACTERIZACIÓN — CARAS, VÉRTICES Y ARISTAS</span>
      <span style="font-size: 7.8pt; font-weight: bold; color: #0f766e;">Total Sección: 25 Puntos</span>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 3 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 3: Anatomía y Definiciones (9 Puntos)</span>
        <span class="badge-pts">9 Pts</span>
      </div>
      <div class="correct-box">
        <b>Definiciones esperadas (3 pts - 1 pt c/u):</b><br>
        • <b>Cara:</b> Es cada una de las superficies planas que limitan o forman el cuerpo geométrico.<br>
        • <b>Arista:</b> Es la línea o segmento donde se unen o intersectan dos caras (el "borde").<br>
        • <b>Vértice:</b> Es la esquina o punto donde se unen tres o más aristas (la "punta" o esquina).<br>
        <i>Nota evaluativa:</i> No se requiere definición formal; es excelente si utiliza palabras como "superficie", "línea/borde" y "esquina/punto".
      </div>
      <div class="rubric-box">
        <b>Asignación de puntos en diagramas anatómicos (6 pts):</b><br>
        Verificar que comprenda qué parte está señalada en el prisma (cara frontal/lateral, arista lateral, vértice, base superior) y en la pirámide (cúspide, cara triangular, arista basal, base).
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 4 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 4: Gran Tabla de Conteo (10 Puntos - 2 pts por fila)</span>
        <span class="badge-pts">10 Pts</span>
      </div>

      <table class="table-ans">
        <thead>
          <tr>
            <th>Cuerpo Geométrico</th>
            <th>Forma de Base</th>
            <th>N° Bases</th>
            <th>Caras Laterales</th>
            <th>TOTAL CARAS</th>
            <th>VÉRTICES</th>
            <th>ARISTAS</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="text-align: left; font-weight: bold;">1. Cubo / Prisma Cuadrangular</td>
            <td>Cuadrado</td>
            <td><b>2</b></td>
            <td><b>4</b></td>
            <td><b>6</b></td>
            <td><b>8</b></td>
            <td><b>12</b></td>
          </tr>
          <tr>
            <td style="text-align: left; font-weight: bold;">2. Prisma Triangular</td>
            <td>Triángulo</td>
            <td><b>2</b></td>
            <td><b>3</b></td>
            <td><b>5</b></td>
            <td><b>6</b></td>
            <td><b>9</b></td>
          </tr>
          <tr>
            <td style="text-align: left; font-weight: bold;">3. Pirámide Cuadrangular</td>
            <td>Cuadrado</td>
            <td><b>1</b></td>
            <td><b>4</b></td>
            <td><b>5</b></td>
            <td><b>5</b></td>
            <td><b>8</b></td>
          </tr>
          <tr>
            <td style="text-align: left; font-weight: bold;">4. Pirámide Triangular</td>
            <td>Triángulo</td>
            <td><b>1</b></td>
            <td><b>3</b></td>
            <td><b>4</b></td>
            <td><b>4</b></td>
            <td><b>6</b></td>
          </tr>
          <tr>
            <td style="text-align: left; font-weight: bold;">5. Prisma Pentagonal</td>
            <td>Pentágono</td>
            <td><b>2</b></td>
            <td><b>5</b></td>
            <td><b>7</b></td>
            <td><b>10</b></td>
            <td><b>15</b></td>
          </tr>
        </tbody>
      </table>

      <div class="pedagogy-tip">
        <b>🔍 Las "Fórmulas Mágicas" para deducir sin equivocarse:</b><br>
        • <b>En los Prismas (base de n lados):</b> Caras = n + 2 | Vértices = 2 × n | Aristas = 3 × n.<br>
        • <b>En las Pirámides (base de n lados):</b> Caras = n + 1 | Vértices = n + 1 | Aristas = 2 × n.<br>
        ¡Observa que en las pirámides el número de caras SIEMPRE es exactamente igual al número de vértices!
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 5 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 5: Detective de Cuerpos (6 Puntos - 3 pts c/u)</span>
        <span class="badge-pts">6 Pts</span>
      </div>
      <div class="correct-box">
        <b>Misterio A:</b> <b>Pirámide Cuadrangular</b> (1 base cuadrada + 4 caras triangulares = 5 caras; 5 vértices, 8 aristas).<br>
        <b>Misterio B:</b> <b>Prisma Triangular</b> (2 bases triangulares + 3 caras rectangulares = 5 caras; 6 vértices, 9 aristas).
      </div>
      <div class="pedagogy-tip">
        <b>💡 Valor formativo:</b> Ambos cuerpos tienen 5 caras, pero uno tiene 5 vértices y el otro 6 vértices. Esta pregunta evalúa si discrimina entre dos cuerpos que comparten la misma cantidad de caras totales.
      </div>
    </div>
  </div>

  <div class="footer-exam">
    <span>Guía de Respuestas y Rúbrica de Calificación | Simulacro de Matemáticas</span>
    <span>Página <b>2</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- GUÍA PÁGINA 3: SECCIÓN 3 (SECUENCIAS)      -->
<!-- ========================================== -->
<div class="page">
  <div>
    <div class="mini-header">
      <div><b>Solucionario y Guía Pedagógica</b> | Sección 3: Secuencias y Patrones</div>
      <div>Uso Exclusivo Evaluador | Pág. <b>3</b> de <b>4</b></div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-tag">SECCIÓN 3: SECUENCIAS GEOMÉTRICAS (INCREMENTALES Y DECREMENTALES)</span>
      <span style="font-size: 7.8pt; font-weight: bold; color: #0f766e;">Total Sección: 30 Puntos</span>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 6 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 6: Secuencia Incremental de Triángulos (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      <div class="correct-box">
        <b>• Dibujo Paso 4:</b> Debe dibujar exactamente <b>11 triángulos</b> (2 pts).<br>
        <span style="display: inline-block; background: #fff; padding: 2px 5px; border: 1px solid #cbd5e1; border-radius: 4px; margin: 2px 0;">
          <b>Visualización:</b>
          {" ".join(['<span class="mini-tri"></span>' for _ in range(11)])}
          (11 triángulos)
        </span><br>
        <b>• a) Clasificación:</b> <b>[X] Incremental (Creciente)</b> (2 pts).<br>
        <b>• b) Predicción:</b> Paso 5 = <b>14 triángulos</b> | Paso 6 = <b>17 triángulos</b> (2 pts - 1 pt c/u).<br>
        <b>• c) Regla en palabras (4 pts):</b><br>
        <i>Respuesta modelo:</i> "Es una secuencia incremental porque en cada paso se suman 3 triángulos a la figura anterior" (o "va aumentando de 3 en 3 triángulos cada vez").
      </div>
      <div class="rubric-box">
        <b>Rúbrica para calificar la regla verbal:</b><br>
        • <b>4 pts (Completa):</b> Dice que es creciente/incremental y especifica que se suman 3 triángulos.<br>
        • <b>2-3 pts (Parcial):</b> Dice "se suman 3" pero omite la palabra incremental o no menciona qué figura es.<br>
        • <b>0-1 pt (Insuficiente):</b> Solo dice "se hacen más grandes" o "cambia".
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 7 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 7: Secuencia Decremental de Cuadrados (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      <div class="correct-box">
        <b>• Dibujo Paso 4:</b> Debe dibujar exactamente <b>5 cuadrados</b> (8 - 3 = 5) (2 pts).<br>
        <span style="display: inline-block; background: #fff; padding: 2px 5px; border: 1px solid #cbd5e1; border-radius: 4px; margin: 2px 0;">
          <b>Visualización:</b>
          {" ".join(['<span class="mini-sq"></span>' for _ in range(5)])}
          (5 cuadrados)
        </span><br>
        <b>• a) Clasificación:</b> <b>[X] Decremental (Decreciente)</b> (2 pts).<br>
        <b>• b) Análisis:</b> Paso 5 = <b>2 cuadrados</b> (5 - 3 = 2). Se acabarán en el <b>Paso 6</b> (2 - 3 daría número negativo, ya no se pueden dibujar figuras completas) (2 pts).<br>
        <b>• c) Regla en palabras (4 pts):</b><br>
        <i>Respuesta modelo:</i> "Es una secuencia decremental porque en cada paso se restan o quitan 3 cuadrados a la cantidad anterior" (o "va disminuyendo de 3 en 3 cuadrados cada vez").
      </div>
      <div class="pedagogy-tip">
        <b>💡 Habilidad clave evaluada:</b> El uso del vocabulario matemático preciso ("decremental", "disminuye", "resta", "patrón de resta de 3"). Es fundamental que ella aprenda a verbalizar el porqué del número.
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 8 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 8: Secuencia Combinada Círculos y Cuadrados (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      <div class="correct-box">
        <b>• Dibujo Paso 4:</b> Debe dibujar <b>4 círculos</b> y <b>8 cuadrados</b> (2 pts).<br>
        <span style="display: inline-block; background: #fff; padding: 2px 5px; border: 1px solid #cbd5e1; border-radius: 4px; margin: 2px 0;">
          <b>Visualización:</b>
          {" ".join(['<span class="mini-cir"></span>' for _ in range(4)])} &nbsp;
          {" ".join(['<span class="mini-sq"></span>' for _ in range(8)])}
          (4 círculos y 8 cuadrados)
        </span><br>
        <b>• a) Discriminación por figura (4 pts):</b><br>
        - Círculos: 1 ➔ 2 ➔ 3 ➔ <b>4</b>. Es <b>incremental</b> y aumenta de <b>1 en 1</b>.<br>
        - Cuadrados: 2 ➔ 4 ➔ 6 ➔ <b>8</b>. Es <b>incremental</b> y aumenta de <b>2 en 2</b>.<br>
        <b>• b) Regla general en palabras (4 pts):</b><br>
        <i>Respuesta esperada:</i> "En cada paso se agrega 1 círculo nuevo y 2 cuadrados nuevos a la figura" (o "los círculos van de 1 en 1 y los cuadrados van de 2 en 2").
      </div>
    </div>
  </div>

  <div class="footer-exam">
    <span>Guía de Respuestas y Rúbrica de Calificación | Simulacro de Matemáticas</span>
    <span>Página <b>3</b> de <b>4</b></span>
  </div>
</div>


<!-- ========================================== -->
<!-- GUÍA PÁGINA 4: SECCIÓN 4 Y PLAN DE ACCIÓN  -->
<!-- ========================================== -->
<div class="page">
  <div>
    <div class="mini-header">
      <div><b>Solucionario y Guía Pedagógica</b> | Sección 4: Desafíos y Diagnóstico</div>
      <div>Uso Exclusivo Evaluador | Pág. <b>4</b> de <b>4</b></div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
      <span class="section-tag">SECCIÓN 4: APLICACIÓN, CREATIVIDAD Y DIAGNÓSTICO</span>
      <span style="font-size: 7.8pt; font-weight: bold; color: #0f766e;">Total Sección: 20 Puntos</span>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 9 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 9: Problemas del Mundo Real (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      <div class="correct-box">
        <b>Situación A (Palillos y Plastilina) (5 pts):</b><br>
        1. Prisma Triangular: <b>9 palillos</b> (aristas) y <b>6 bolitas</b> (vértices). (2 pts)<br>
        2. Pirámide Cuadrangular: <b>8 palillos</b> (aristas) y <b>5 bolitas</b> (vértices). (2 pts)<br>
        3. Con 12 palillos y 8 bolitas: <b>[X] Un Cubo</b> (el cubo tiene exactamente 12 aristas y 8 vértices). (1 pt)
      </div>
      <div class="correct-box" style="margin-top: 3px;">
        <b>Situación B (Carpas) (5 pts):</b><br>
        a) Carpa Verde (Pirámide Cuadrangular): <b>5 caras</b> (1 base + 4 laterales). (1.5 pts)<br>
        b) Carpa Azul (Prisma Triangular): <b>5 caras</b> (2 bases + 3 laterales). (1.5 pts)<br>
        c) Vértices: La Carpa Azul tiene <b>más vértices (6 vértices)</b> que la Verde (<b>5 vértices</b>). (2 pts)
      </div>
    </div>

    <!-- SOLUCIÓN ACTIVIDAD 10 -->
    <div class="ans-card">
      <div class="ans-title">
        <span>Solución Actividad 10: Reto Creativo (10 Puntos)</span>
        <span class="badge-pts">10 Pts</span>
      </div>
      <div class="rubric-box">
        <b>Criterios para calificar la secuencia inventada por la estudiante:</b><br>
        • <b>Coherencia del patrón (4 pts):</b> Los 4 pasos deben mantener una cantidad que aumente o disminuya de forma constante (ej. +2, +3, -2, etc.).<br>
        • <b>Conteo numérico correcto (2 pts):</b> La cantidad anotada debajo de cada caja debe coincidir exactamente con las figuras dibujadas.<br>
        • <b>Clasificación correcta (2 pts):</b> Marcó correctamente si su patrón es incremental o decremental.<br>
        • <b>Explicación verbal clara (2 pts):</b> Escribió con claridad la regla ("mi secuencia empieza con X y suma/resta Y figuras en cada paso").
      </div>
    </div>

    <!-- SEMÁFORO DIAGNÓSTICO -->
    <div class="ans-card" style="margin-top: 3px;">
      <div class="ans-title" style="color: #0f766e;">
        <span>Semáforo de Diagnóstico y Plan de Refuerzo para el Hogar</span>
      </div>
      
      <div class="traffic-light">
        <div class="tl-card tl-green">
          <b>🟢 90 - 100 PUNTOS: EXCELENTE</b><br>
          <b>Dominio completo:</b> Comprende a cabalidad las diferencias entre prismas y pirámides, cuenta elementos tridimensionales sin omitir bases ni caras ocultas, y expresa con soltura la regla verbal de secuencias. ¡Lista para el examen escolar con total confianza!
        </div>
        <div class="tl-card tl-yellow">
          <b>🟡 70 - 89 PUNTOS: BUENO (EN PROCESO)</b><br>
          <b>Pequeños detalles a afinar:</b> Probablemente cometió algún error menor al contar aristas de figuras con más lados (como prismas pentagonales) o en la redacción de la regla verbal. Refuerza pidiéndole que explique en voz alta la regla usando la frase: <i>"Va sumando/restando ___ figuras cada vez"</i>.
        </div>
        <div class="tl-card tl-red">
          <b>🔴 MENOS DE 70 PUNTOS: REFUERZO</b><br>
          <b>Actividad práctica sugerida:</b> Construyan juntos en casa con plastilina y palillos de dientes un cubo y una pirámide cuadrangular. Tocar físicamente las aristas y las esquinas hace que el concepto sea 100% tangible y memorable para toda la vida.
        </div>
      </div>
    </div>
  </div>

  <div class="footer-exam">
    <span>Guía de Respuestas y Rúbrica de Calificación | Simulacro de Matemáticas</span>
    <span>Página <b>4</b> de <b>4</b></span>
  </div>
</div>

</body>
</html>'''

def main():
    print("Iniciando compilación de documentos actualizados...")
    
    # 1. HTML Examen
    exam_html = build_exam_html()
    with open("simulacro_examen_matematicas.html", "w", encoding="utf-8") as f:
        f.write(exam_html)
    print("-> simulacro_examen_matematicas.html actualizado.")

    # 2. HTML Guía
    guide_html = build_solution_guide_html()
    with open("solucionario_y_guia_evaluacion.html", "w", encoding="utf-8") as f:
        f.write(guide_html)
    print("-> solucionario_y_guia_evaluacion.html actualizado.")

    # 3. Compilación a PDF con Chrome Headless
    print("Compilando simulacro_examen_matematicas.pdf...")
    subprocess.run([
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf=simulacro_examen_matematicas.pdf",
        "simulacro_examen_matematicas.html"
    ], check=True)
    print("-> simulacro_examen_matematicas.pdf listo.")

    print("Compilando solucionario_y_guia_evaluacion.pdf...")
    subprocess.run([
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf=solucionario_y_guia_evaluacion.pdf",
        "solucionario_y_guia_evaluacion.html"
    ], check=True)
    print("-> solucionario_y_guia_evaluacion.pdf listo.")

    # 4. Renderizar previsualizaciones
    os.makedirs("preview_pages", exist_ok=True)
    subprocess.run(["pdftoppm", "-png", "-r", "150", "simulacro_examen_matematicas.pdf", "preview_pages/examen_pag"], check=True)
    subprocess.run(["pdftoppm", "-png", "-r", "150", "solucionario_y_guia_evaluacion.pdf", "preview_pages/solucionario_pag"], check=True)
    print("-> Previsualizaciones PNG generadas exitosamente en ./preview_pages/")

if __name__ == "__main__":
    main()
