/* =========================================================
   Aventura Matemática de Luciana
   Temas: cuerpos geométricos · caras/vértices/aristas · patrones
   ========================================================= */
'use strict';
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const rnd = (a, b) => Math.floor(Math.random() * (b - a + 1)) + a;
const pick = a => a[rnd(0, a.length - 1)];
const shuffle = a => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = rnd(0, i);[a[i], a[j]] = [a[j], a[i]]; } return a; };
const app = $('#app');

/* ---------- Estado y guardado ---------- */
const KEY = 'aventura-mate-luciana-v1';
const defaultState = () => ({ name: '', xp: 0, stars: {}, lessons: {}, hist: { cuerpos: [], partes: [], patrones: [] }, badges: {}, sound: true, examBest: null, played: 0, maxStreak: 0 });
let S = (() => { try { return Object.assign(defaultState(), JSON.parse(localStorage.getItem(KEY)) || {}); } catch { return defaultState(); } })();
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch { } };

const TOPICS = {
  cuerpos: { name: 'Cuerpos geométricos', emoji: '🔷', tip: 'Repasa las lecciones de la Isla de los Cuerpos: prismas (2 bases) y pirámides (1 base y una cúspide).' },
  partes: { name: 'Caras, vértices y aristas', emoji: '🔢', tip: 'Repasa la Montaña de las Partes: cuenta con calma caras, vértices y aristas, y recuerda los trucos.' },
  patrones: { name: 'Secuencias y patrones', emoji: '🧩', tip: 'Repasa el Valle de los Patrones: busca cuánto cambia de un término a otro y dilo con palabras.' }
};
const TITLES = ['Aprendiz', 'Exploradora', 'Aventurera', 'Detective de Formas', 'Ingeniera', 'Arquitecta', 'Maestra de las Formas', 'Genio Matemática', 'Leyenda de la Geometría'];
const level = () => Math.floor(S.xp / 100) + 1;
const levelTitle = () => TITLES[Math.min(level() - 1, TITLES.length - 1)];
const totalStars = () => Object.values(S.stars).reduce((a, b) => a + b, 0);

function mastery(topic) {
  const h = S.hist[topic];
  if (h.length < 5) return null;
  return Math.round(100 * h.filter(Boolean).length / h.length);
}
const light = p => p === null ? 'n' : p >= 90 ? 'g' : p >= 70 ? 'y' : 'r';

/* ---------- Sonido y confeti ---------- */
let AC = null;
function tone(f, d = .12, type = 'sine', when = 0, v = .12) {
  if (!S.sound) return;
  try {
    AC = AC || new (window.AudioContext || window.webkitAudioContext)();
    const o = AC.createOscillator(), g = AC.createGain();
    o.type = type; o.frequency.value = f; o.connect(g); g.connect(AC.destination);
    const t = AC.currentTime + when;
    g.gain.setValueAtTime(v, t); g.gain.exponentialRampToValueAtTime(.001, t + d);
    o.start(t); o.stop(t + d + .02);
  } catch { }
}
const sfx = {
  ok: () => { tone(660, .1); tone(880, .16, 'sine', .1); },
  bad: () => { tone(260, .22, 'triangle'); tone(200, .25, 'triangle', .15); },
  win: () => [523, 659, 784, 1046].forEach((f, i) => tone(f, .2, 'sine', i * .13)),
  click: () => tone(500, .05, 'square', 0, .05)
};
window.toggleSound = () => { S.sound = !S.sound; save(); $('#soundBtn').textContent = S.sound ? '🔊' : '🔇'; };

function confetti() {
  const c = $('#confetti'), x = c.getContext('2d');
  c.width = innerWidth; c.height = innerHeight;
  const cols = ['#ffc933', '#ff5fa8', '#19c3b1', '#6c4cf1', '#3aa0ff', '#ff9442'];
  const ps = Array.from({ length: 140 }, () => ({ x: Math.random() * c.width, y: -20 - Math.random() * c.height * .5, r: 5 + Math.random() * 7, c: pick(cols), vy: 2 + Math.random() * 4, vx: -2 + Math.random() * 4, a: Math.random() * 6, s: Math.random() > .5 }));
  let f = 0;
  (function loop() {
    x.clearRect(0, 0, c.width, c.height);
    ps.forEach(p => {
      p.x += p.vx; p.y += p.vy; p.a += .1; x.save(); x.translate(p.x, p.y); x.rotate(p.a); x.fillStyle = p.c;
      p.s ? x.fillRect(-p.r, -p.r / 2, p.r * 2, p.r) : (x.beginPath(), x.arc(0, 0, p.r / 2, 0, 7), x.fill()); x.restore();
    });
    if (++f < 200) requestAnimationFrame(loop); else x.clearRect(0, 0, c.width, c.height);
  })();
}
function toast(msg) {
  const t = document.createElement('div'); t.className = 'toast'; t.textContent = msg; document.body.appendChild(t);
  setTimeout(() => t.remove(), 3200);
}

/* ---------- XP, HUD, insignias ---------- */
function updateHud() {
  $('#hudLevel').textContent = 'Nv ' + level();
  $('#hudXp').style.width = (S.xp % 100) + '%';
  $('#hudXpText').textContent = (S.xp % 100) + ' / 100 XP';
  $('#hudStars').textContent = totalStars();
  $('#soundBtn').textContent = S.sound ? '🔊' : '🔇';
}
function addXp(n) {
  const before = level();
  S.xp += n; save(); updateHud();
  if (level() > before) { toast(`🎉 ¡Subiste al nivel ${level()}: ${levelTitle()}!`); sfx.win(); confetti(); }
}
const BADGES = [
  { id: 'first', ic: '🚀', n: 'Primer juego', ok: () => S.played >= 1 },
  { id: 'streak5', ic: '🔥', n: 'Racha de 5', ok: () => S.maxStreak >= 5 },
  { id: 'streak10', ic: '⚡', n: 'Racha de 10', ok: () => S.maxStreak >= 10 },
  { id: 'lessons', ic: '📚', n: 'Lectora', ok: () => Object.keys(S.lessons).length >= LESSON_COUNT() },
  { id: 'cuerpos', ic: '🔷', n: 'Experta en cuerpos', ok: () => (mastery('cuerpos') || 0) >= 90 },
  { id: 'partes', ic: '🔢', n: 'Experta en partes', ok: () => (mastery('partes') || 0) >= 90 },
  { id: 'patrones', ic: '🧩', n: 'Experta en patrones', ok: () => (mastery('patrones') || 0) >= 90 },
  { id: 'stars10', ic: '🌟', n: '10 estrellas', ok: () => totalStars() >= 10 },
  { id: 'exam', ic: '🏆', n: 'Torneo completado', ok: () => S.examBest !== null },
  { id: 'examgreen', ic: '👑', n: 'Torneo ¡verde!', ok: () => (S.examBest || 0) >= 90 }
];
function checkBadges() {
  BADGES.forEach(b => { if (!S.badges[b.id] && b.ok()) { S.badges[b.id] = true; save(); setTimeout(() => toast(`${b.ic} ¡Nueva insignia: ${b.n}!`), 400); sfx.win(); } });
}

/* =========================================================
   GEOMETRÍA 3D (lienzo con rotación)
   ========================================================= */
const BASE_NAMES = { 3: 'triangular', 4: 'cuadrangular', 5: 'pentagonal', 6: 'hexagonal' };
const BASE_SHAPE = { 3: 'triángulo', 4: 'cuadrilátero', 5: 'pentágono', 6: 'hexágono' };
const fullName = (k, n) => (k === 'prism' ? 'Prisma ' : 'Pirámide ') + BASE_NAMES[n];
const counts = (k, n) => k === 'prism' ? { F: n + 2, V: 2 * n, E: 3 * n } : { F: n + 1, V: n + 1, E: 2 * n };

function makeSolid(kind, n) {
  const off = n === 4 ? Math.PI / 4 : -Math.PI / 2, R = n === 4 ? 1.0 : 1.05;
  const V = [], F = [];
  const ring = y => { for (let i = 0; i < n; i++) { const a = off + i * 2 * Math.PI / n; V.push([R * Math.cos(a), y, R * Math.sin(a)]); } };
  const idx = [...Array(n).keys()];
  if (kind === 'prism') {
    ring(-.8); ring(.8);
    F.push({ v: idx, role: 'base' }, { v: idx.map(i => n + i), role: 'base' });
    idx.forEach(i => F.push({ v: [i, (i + 1) % n, n + (i + 1) % n, n + i], role: 'lat' }));
  } else {
    ring(-.8); V.push([0, 1.05, 0]);
    F.push({ v: idx, role: 'base' });
    idx.forEach(i => F.push({ v: [i, (i + 1) % n, n], role: 'lat' }));
  }
  const E = new Map();
  F.forEach((f, fi) => f.v.forEach((a, i) => {
    const b = f.v[(i + 1) % f.v.length], key = Math.min(a, b) + '-' + Math.max(a, b);
    if (!E.has(key)) E.set(key, { a, b, faces: [], role: 'lat' });
    const e = E.get(key); e.faces.push(fi); if (f.role === 'base') e.role = 'base';
  }));
  return { kind, n, V, F, E: [...E.values()], apex: kind === 'pyr' ? n : -1 };
}

function drawSolid(canvas, s, ang, hl) {
  const dpr = window.devicePixelRatio || 1, W = canvas.clientWidth, H = canvas.clientHeight;
  if (!W || !H) return;
  if (canvas.width !== Math.round(W * dpr) || canvas.height !== Math.round(H * dpr)) { canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr); }
  const ctx = canvas.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
  const sc = Math.min(W, H) / 3.1, cx = W / 2, cy = H / 2 + 4, tilt = .5;
  const rv = s.V.map(([x, y, z]) => {
    const x1 = x * Math.cos(ang) + z * Math.sin(ang), z1 = -x * Math.sin(ang) + z * Math.cos(ang);
    const y2 = y * Math.cos(tilt) - z1 * Math.sin(tilt), z2 = y * Math.sin(tilt) + z1 * Math.cos(tilt);
    return { x: cx + x1 * sc, y: cy - y2 * sc, z: z2, X: x1, Y: y2 };
  });
  const ctr = rv.reduce((a, p) => [a[0] + p.X / rv.length, a[1] + p.Y / rv.length, a[2] + p.z / rv.length], [0, 0, 0]);
  const info = s.F.map(f => {
    const p = f.v.map(i => rv[i]);
    const a = [p[1].X - p[0].X, p[1].Y - p[0].Y, p[1].z - p[0].z], b = [p[2].X - p[0].X, p[2].Y - p[0].Y, p[2].z - p[0].z];
    let nrm = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
    const c = p.reduce((q, r) => [q[0] + r.X / p.length, q[1] + r.Y / p.length, q[2] + r.z / p.length], [0, 0, 0]);
    if (nrm[0] * (c[0] - ctr[0]) + nrm[1] * (c[1] - ctr[1]) + nrm[2] * (c[2] - ctr[2]) < 0) nrm = nrm.map(q => -q);
    return { f, p, z: c[2], vis: nrm[2] > 0 };
  });
  const match = (sel, role) => sel === 'all' || sel === role;
  // caras (de atrás hacia adelante)
  [...info].sort((a, b) => a.z - b.z).forEach(({ f, p }) => {
    let col;
    if (hl && hl.faces) col = match(hl.faces, f.role) ? (f.role === 'base' ? 'rgba(255,95,168,.55)' : 'rgba(25,195,177,.5)') : 'rgba(150,140,200,.08)';
    else if (hl && hl.neutral) col = 'rgba(108,76,241,.26)';
    else col = f.role === 'base' ? 'rgba(255,201,51,.38)' : 'rgba(108,76,241,.26)';
    ctx.beginPath(); p.forEach((q, i) => i ? ctx.lineTo(q.x, q.y) : ctx.moveTo(q.x, q.y)); ctx.closePath(); ctx.fillStyle = col; ctx.fill();
  });
  // aristas
  const edges = s.E.map(e => ({ e, vis: e.faces.some(fi => info[fi].vis) })).sort((a, b) => a.vis - b.vis);
  edges.forEach(({ e, vis }) => {
    const A = rv[e.a], B = rv[e.b];
    let col = '#3b2f9e', w = 2.6;
    if (hl && hl.edges) { if (match(hl.edges, e.role)) { col = e.role === 'base' ? '#e0207f' : '#0a8f80'; w = 5; } else { col = '#b8b2d8'; w = 2; } }
    ctx.strokeStyle = col; ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.globalAlpha = vis ? 1 : .8;
    ctx.setLineDash(vis ? [] : [6, 5]);
    ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke();
  });
  ctx.setLineDash([]); ctx.globalAlpha = 1;
  // vértices
  if (hl && hl.verts) {
    rv.forEach((p, i) => {
      const isApex = i === s.apex;
      if (hl.verts === 'apex' && !isApex) return;
      if (hl.verts === 'base' && isApex) return;
      ctx.beginPath(); ctx.arc(p.x, p.y, isApex ? 9 : 7, 0, 7);
      ctx.fillStyle = isApex ? '#ffc933' : '#6c4cf1'; ctx.fill(); ctx.lineWidth = 2; ctx.strokeStyle = '#fff'; ctx.stroke();
      if (hl.number) { ctx.fillStyle = isApex ? '#4a2b00' : '#fff'; ctx.font = '700 10px Fredoka,sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(i + 1, p.x, p.y + .5); }
    });
    if (hl.verts === 'apex') {
      const p = rv[s.apex]; ctx.fillStyle = '#4a2b00'; ctx.font = '700 15px Fredoka,sans-serif'; ctx.textAlign = 'left'; ctx.fillText('cúspide', p.x + 14, p.y - 6);
    }
  }
}

const SOLIDS = [];
let rafOn = false;
function mountSolids(root = document) {
  $$('canvas[data-solid]', root).forEach(cv => {
    if (cv._m) return; cv._m = 1;
    const [k, n] = cv.dataset.solid.split(',');
    const o = { cv, s: makeSolid(k, +n), ang: Math.random() * 6, hl: cv.dataset.hl ? JSON.parse(cv.dataset.hl) : null };
    cv._o = o; SOLIDS.push(o);
  });
  if (!rafOn) { rafOn = true; requestAnimationFrame(loop); }
}
function loop() {
  for (let i = SOLIDS.length - 1; i >= 0; i--) { const o = SOLIDS[i]; if (!o.cv.isConnected) { SOLIDS.splice(i, 1); continue; } o.ang += .012; drawSolid(o.cv, o.s, o.ang, o.hl); }
  requestAnimationFrame(loop);
}
const solidTag = (k, n, hl, extra = '') => `<canvas class="solid" ${extra} data-solid="${k},${n}" ${hl ? `data-hl='${JSON.stringify(hl)}'` : ''}></canvas>`;

/* Explorador interactivo */
function mountExplorer(root, opts = {}) {
  const box = $('.explorer', root); if (!box) return;
  const st = { kind: 'prism', n: 3, mode: 'normal' };
  const cv = $('canvas', box);
  const modes = { normal: null, faces: { faces: 'all' }, edges: { edges: 'all' }, verts: { verts: 'all', number: true, neutral: true } };
  function refresh() {
    const o = cv._o; if (!o) return;
    o.s = makeSolid(st.kind, st.n); o.hl = modes[st.mode];
    const c = counts(st.kind, st.n);
    $('[data-c=F] b', box).textContent = c.F; $('[data-c=V] b', box).textContent = c.V; $('[data-c=E] b', box).textContent = c.E;
    $$('[data-c]', box).forEach(el => el.classList.toggle('hot', (st.mode === 'faces' && el.dataset.c === 'F') || (st.mode === 'verts' && el.dataset.c === 'V') || (st.mode === 'edges' && el.dataset.c === 'E')));
    const nm = $('.exname', box); if (nm) nm.textContent = fullName(st.kind, st.n);
    $$('[data-k]', box).forEach(b => b.classList.toggle('sel', b.dataset.k === st.kind));
    $$('[data-n]', box).forEach(b => b.classList.toggle('sel', +b.dataset.n === st.n));
    $$('[data-m]', box).forEach(b => b.classList.toggle('sel', b.dataset.m === st.mode));
    const lg = $('.legend', box);
    if (lg) lg.innerHTML = { normal: 'Gira el cuerpo y mira sus partes.', faces: '<span class="hl-b">Rosado</span> = caras basales · <span class="hl-t">Verde</span> = caras laterales', edges: '<span class="hl-b">Rosado</span> = aristas basales · <span class="hl-t">Verde</span> = aristas laterales. Las <b>punteadas</b> están detrás.', verts: 'Cada punto es un vértice. El <b style="color:#c99200">dorado</b> de la pirámide es la cúspide.' }[st.mode];
  }
  box.addEventListener('click', e => {
    const b = e.target.closest('button'); if (!b) return; sfx.click();
    if (b.dataset.k) st.kind = b.dataset.k; if (b.dataset.n) st.n = +b.dataset.n; if (b.dataset.m) st.mode = b.dataset.m;
    refresh();
  });
  setTimeout(refresh, 30);
}
const explorerHTML = (withModes = true) => `
<div class="explorer">
  ${solidTag('prism', 3)}
  <div class="ctrls"><button class="pill" data-k="prism">Prisma</button><button class="pill" data-k="pyr">Pirámide</button></div>
  <div class="ctrls">Base de: ${[3, 4, 5, 6].map(n => `<button class="pill" data-n="${n}">${n} lados</button>`).join('')}</div>
  <p style="text-align:center;font-size:1.5rem;font-weight:700;color:var(--purple)" class="exname"></p>
  ${withModes ? `<div class="ctrls"><button class="pill" data-m="normal">👀 Normal</button><button class="pill" data-m="faces">🟦 Caras</button><button class="pill" data-m="edges">📏 Aristas</button><button class="pill" data-m="verts">🔵 Vértices</button></div>` : ''}
  <div class="counters">
    <div class="counter" data-c="F">Caras<b>0</b></div><div class="counter" data-c="V">Vértices<b>0</b></div><div class="counter" data-c="E">Aristas<b>0</b></div>
  </div>
  <p class="legend" style="text-align:center;font-size:.95rem"></p>
</div>`;

/* =========================================================
   SECUENCIAS
   ========================================================= */
const SH = { ci: { s: 'círculo', p: 'círculos', c: '#ff5fa8', e: '🔴' }, sq: { s: 'cuadrado', p: 'cuadrados', c: '#3aa0ff', e: '🟦' }, tr: { s: 'triángulo', p: 'triángulos', c: '#ff9442', e: '🔺' } };
const ORDER = ['ci', 'sq', 'tr'];
const shapeHTML = (k, anim) => `<i class="sh ${k} ${anim ? 'pop' : ''}" style="--c:${SH[k].c}"></i>`;
const grpHTML = t => ORDER.filter(k => t[k]).map(k => `<div class="grp">${shapeHTML(k).repeat(t[k])}</div>`).join('');
function termHTML(t, i, extra = '', id = '') {
  const inner = grpHTML(t);
  return `<div class="term ${extra}" ${id ? `id="${id}"` : ''}>${i ? `<span class="n">${i}</span>` : ''}${inner}</div>`;
}
const countTxt = (n, k) => `${n} ${n === 1 ? SH[k].s : SH[k].p}`;
const termText = (t, keys) => keys.map(k => countTxt(t[k], k)).join(' y ');
function seqHTML(terms, showNext = true) {
  return `<div class="seq">${terms.map((t, i) => (i ? '<span class="arrow">➜</span>' : '') + termHTML(t, i + 1)).join('')}${showNext ? '<span class="arrow">➜</span><div class="term next">?</div>' : ''}</div>`;
}
function genSeq(dir, nkeys) {
  const keys = shuffle(ORDER).slice(0, nkeys), len = 4, spec = {};
  keys.forEach(k => {
    const step = dir === 'inc' ? rnd(1, nkeys === 1 ? 3 : 2) : rnd(1, 2);
    spec[k] = { step, start: dir === 'inc' ? rnd(1, 3) : step * len + rnd(1, 2) };
  });
  const term = i => { const t = {}; keys.forEach(k => t[k] = spec[k].start + (dir === 'inc' ? 1 : -1) * spec[k].step * i); return t; };
  return { dir, keys, spec, terms: [0, 1, 2, 3].map(term), next: term(4) };
}
const ruleText = (keys, steps, dir) =>
  'Cada término tiene ' + keys.map((k, i) => countTxt(steps[i], k)).join(' y ') + (dir === 'inc' ? ' más' : ' menos') + ' que el anterior';
const seqRule = q => ruleText(q.keys, q.keys.map(k => q.spec[k].step), q.dir);

/* =========================================================
   GENERADORES DE PREGUNTAS
   ========================================================= */
function mc(topic, prompt, correct, wrongs, why, visual, say) {
  const wr = [...new Set(wrongs)].filter(w => w !== correct).slice(0, 3);
  const opts = shuffle([correct, ...wr]);
  return { type: 'mc', topic, prompt, opts, ans: opts.indexOf(correct), why, visual, say };
}
const kindName = k => k === 'prism' ? 'Prisma' : 'Pirámide';
const solidVis = (k, n, hl) => ({ t: 'solid', k, n, hl });

function qDetective() {
  const k = pick(['prism', 'pyr']), n = rnd(3, 6), v = solidVis(k, n, { neutral: true }), t = rnd(1, 3);
  if (t === 1) {
    const others = [3, 4, 5, 6].filter(x => x !== n);
    return mc('cuerpos', '¿Cómo se llama este cuerpo geométrico?', fullName(k, n),
      [fullName(k === 'prism' ? 'pyr' : 'prism', n), fullName(k, others[0]), fullName(k, others[1]), fullName(k === 'prism' ? 'pyr' : 'prism', others[2])],
      `Tiene ${k === 'prism' ? 'dos bases' : 'una sola base'} de ${BASE_SHAPE[n]} → ${fullName(k, n)}.`, v);
  }
  if (t === 2) return mc('cuerpos', '¿Es un prisma o una pirámide?', kindName(k), [k === 'prism' ? 'Pirámide' : 'Prisma'],
    k === 'prism' ? 'Tiene DOS bases iguales y paralelas, por eso es un prisma.' : 'Tiene UNA sola base y todas sus caras laterales terminan en una punta (cúspide): es una pirámide.', v);
  return mc('cuerpos', '¿Qué forma tiene la BASE de este cuerpo?', BASE_SHAPE[n], Object.values(BASE_SHAPE),
    `La base tiene ${n} lados, es un ${BASE_SHAPE[n]}. Por eso se llama ${fullName(k, n).toLowerCase()}.`, v);
}
function qPistas() {
  const k = pick(['prism', 'pyr']), n = rnd(3, 6);
  const gen = {
    prism: ['Tengo dos bases iguales y paralelas.', 'Mis caras laterales son rectángulos.', 'No tengo cúspide.', 'Mis bases son iguales y están una frente a la otra.'],
    pyr: ['Tengo una sola base.', 'Mis caras laterales son triángulos.', 'Todas mis caras laterales se juntan en un punto.', 'Tengo una cúspide.']
  };
  if (rnd(0, 1)) return mc('cuerpos', `🕵️ Pista: «${pick(gen[k])}» ¿Qué soy?`, kindName(k), [k === 'prism' ? 'Pirámide' : 'Prisma'],
    k === 'prism' ? 'Los prismas tienen 2 bases y caras laterales rectangulares.' : 'Las pirámides tienen 1 base y caras laterales triangulares que se juntan en la cúspide.');
  const feat = k === 'prism' ? `Tengo dos bases ${BASE_SHAPE[n]}s y mis caras laterales son rectángulos.` : `Tengo una base ${BASE_NAMES[n] === 'cuadrangular' ? 'cuadrada' : 'de ' + BASE_SHAPE[n]} y una cúspide.`;
  const o = k === 'prism' ? 'pyr' : 'prism';
  return mc('cuerpos', `🕵️ Pista: «${feat}» ¿Quién soy?`, fullName(k, n),
    [fullName(o, n), fullName(k, n === 3 ? 4 : n - 1), fullName(k, n === 6 ? 5 : n + 1), fullName(o, n === 3 ? 4 : n - 1)],
    `El nombre sale del tipo (${kindName(k).toLowerCase()}) y de la forma de la base (${BASE_SHAPE[n]}): ${fullName(k, n)}.`);
}
function qCuenta() {
  const k = pick(['prism', 'pyr']), n = rnd(3, 6), c = counts(k, n);
  const part = pick([['F', 'caras', 'Caras'], ['V', 'vértices', 'Vértices'], ['E', 'aristas', 'Aristas']]);
  const val = c[part[0]];
  const f = {
    prism: { F: `${n} caras laterales + 2 bases = ${val}`, V: `${n} vértices arriba + ${n} abajo = ${val}`, E: `${n} aristas arriba + ${n} abajo + ${n} laterales = ${val}` },
    pyr: { F: `${n} caras laterales + 1 base = ${val}`, V: `${n} vértices en la base + 1 cúspide = ${val}`, E: `${n} aristas en la base + ${n} laterales = ${val}` }
  }[k][part[0]];
  return mc('partes', `¿Cuántas ${part[1]} tiene este cuerpo? (¡cuenta también las de atrás!)`, String(val), [val + 1, val - 1, val + 2, val - 2, val + 3].filter(x => x > 0).map(String), f, solidVis(k, n, { neutral: true }));
}
function qCazador() {
  const k = pick(['prism', 'pyr']), n = rnd(3, 6), t = rnd(1, 7);
  const O = ['Caras basales', 'Caras laterales', 'Aristas basales', 'Aristas laterales', 'Vértices', 'Cúspide'];
  const wr = (c) => shuffle(O.filter(o => o !== c));
  if (t === 1) return mc('partes', 'Las caras de color rosado se llaman…', 'Caras basales', wr('Caras basales'), 'La cara (o caras) sobre las que “se apoya” el cuerpo son las BASES: caras basales.', solidVis(k, n, { faces: 'base' }));
  if (t === 2) return mc('partes', 'Las caras de color verde se llaman…', 'Caras laterales', wr('Caras laterales'), 'Las caras que rodean al cuerpo, entre las bases, son las caras laterales.', solidVis(k, n, { faces: 'lat' }));
  if (t === 3) return mc('partes', 'Las líneas rosadas gruesas son…', 'Aristas basales', wr('Aristas basales'), 'Las aristas son las líneas donde se juntan dos caras. Las de la base se llaman basales.', solidVis(k, n, { edges: 'base' }));
  if (t === 4) return mc('partes', 'Las líneas verdes gruesas son…', 'Aristas laterales', wr('Aristas laterales'), 'Las aristas laterales unen las bases (prisma) o la base con la cúspide (pirámide).', solidVis(k, n, { edges: 'lat' }));
  if (t === 5) return mc('partes', '¿Cómo se llama el vértice dorado donde se juntan todas las caras laterales?', 'Cúspide', ['Base', 'Arista', 'Cara lateral'], 'La cúspide es el vértice más alto de una pirámide.', solidVis('pyr', n, { verts: 'apex', neutral: true }));
  if (t === 6) { const c = n; return mc('partes', '¿Cuántas caras laterales tiene este cuerpo?', String(c), [c + 1, c - 1, c + 2, c - 2].filter(x => x > 0).map(String), `Hay una cara lateral por cada lado de la base: ${n}.`, solidVis(k, n, { faces: 'lat' })); }
  const c = k === 'prism' ? 2 : 1;
  return mc('partes', '¿Cuántas caras basales (bases) tiene este cuerpo?', String(c), ['0', '1', '2', '3', '4'], k === 'prism' ? 'Los prismas tienen 2 bases.' : 'Las pirámides tienen 1 sola base.', solidVis(k, n, { faces: 'base' }));
}
function qQuien() {
  const k = pick(['prism', 'pyr']), n = rnd(3, 6), c = counts(k, n);
  const all = []; ['prism', 'pyr'].forEach(a => [3, 4, 5, 6].forEach(b => all.push([a, b])));
  const wr = shuffle(all.filter(([a, b]) => !(a === k && b === n))).slice(0, 3).map(([a, b]) => fullName(a, b));
  return mc('partes', `🧩 Acertijo: tengo ${c.V} vértices y ${c.E} aristas. ¿Quién soy?`, fullName(k, n), wr,
    `${fullName(k, n)}: ${c.F} caras, ${c.V} vértices y ${c.E} aristas.`);
}
function seqVis(q, next = true) { return { t: 'seq', q, next }; }
function qClasifica() {
  const dir = pick(['inc', 'dec']), q = genSeq(dir, rnd(1, 2));
  return mc('patrones', 'Mira la secuencia. ¿Es incremental o decremental?', dir === 'inc' ? 'Incremental (crece)' : 'Decremental (decrece)', [dir === 'inc' ? 'Decremental (decrece)' : 'Incremental (crece)'],
    dir === 'inc' ? 'Cada término tiene MÁS figuras que el anterior: es incremental.' : 'Cada término tiene MENOS figuras que el anterior: es decremental.', seqVis(q),
    seqRule(q) + '.');
}
function qSiguiente() {
  const dir = pick(['inc', 'dec']), q = genSeq(dir, rnd(1, 2)), keys = q.keys, last = q.terms[3];
  const val = t => termText(t, keys), cor = val(q.next), w = [];
  const opp = {}; keys.forEach(k => opp[k] = last[k] + (dir === 'inc' ? -1 : 1) * q.spec[k].step); if (keys.every(k => opp[k] > 0)) w.push(val(opp));
  w.push(val(last));
  const k0 = keys[0]; [1, -1, 2].forEach(d => { const t = { ...q.next }; t[k0] += d; if (t[k0] > 0) w.push(val(t)); });
  if (keys.length > 1) { const t = { ...q.next }; t[keys[1]] += 1; w.push(val(t)); }
  return mc('patrones', '¿Cómo es el término que sigue (el 5.º)?', cor, shuffle(w), `La regla es: «${seqRule(q)}». El 4.º tiene ${val(last)}, así que el 5.º tiene ${cor}.`, seqVis(q), `Dilo en voz alta: «${seqRule(q)}».`);
}
function qRegla() {
  const dir = pick(['inc', 'dec']), q = genSeq(dir, rnd(1, 2)), steps = q.keys.map(k => q.spec[k].step);
  const cor = seqRule(q), w = [];
  w.push(ruleText(q.keys, steps, dir === 'inc' ? 'dec' : 'inc'));
  const s2 = [...steps]; s2[0] = s2[0] === 3 ? 2 : s2[0] + 1; w.push(ruleText(q.keys, s2, dir));
  const s3 = [...steps]; s3[0] = s3[0] === 1 ? 3 : 1; if (s3[0] === steps[0]) s3[0] = 2; w.push(ruleText(q.keys, s3, dir));
  const other = ORDER.filter(k => !q.keys.includes(k));
  if (other.length) { const ks = [...q.keys]; ks[0] = other[0]; w.push(ruleText(ks, steps, dir)); }
  if (q.keys.length > 1) w.push(ruleText([q.keys[1], q.keys[0]], steps, dir));
  return mc('patrones', '🗝️ ¿Cuál es la REGLA de esta secuencia?', cor, shuffle(w), 'Compara un término con el siguiente: ¿cuántas figuras de cada clase aparecen o desaparecen?', seqVis(q), `Ahora explícaselo a mamá o papá con tus palabras: «${cor}».`);
}
function qConstruye() {
  const dir = pick(['inc', 'dec']), q = genSeq(dir, rnd(1, 2));
  return { type: 'build', topic: 'patrones', prompt: '🧱 Construye el siguiente término de la secuencia con los botones + y −', q, say: `Explica: «${seqRule(q)}».`, why: `La regla es «${seqRule(q)}». El siguiente término es ${termText(q.next, q.keys)}.` };
}

/* =========================================================
   DEFINICIÓN DE MUNDOS Y JUEGOS
   ========================================================= */
const GAMES = {
  detective: { world: 'w1', title: 'Detective de Cuerpos', emoji: '🔍', desc: 'Descubre cómo se llama cada cuerpo geométrico.', gen: qDetective },
  pistas: { world: 'w1', title: 'Adivina por Pistas', emoji: '🕵️', desc: '¿Prisma o pirámide? Resuelve las pistas.', gen: qPistas },
  cuenta: { world: 'w2', title: 'Contador de Partes', emoji: '🔢', desc: 'Cuenta caras, vértices y aristas.', gen: qCuenta },
  cazador: { world: 'w2', title: 'Cazador de Partes', emoji: '🎯', desc: 'Identifica las partes marcadas de colores.', gen: qCazador },
  quien: { world: 'w2', title: 'Acertijos con Números', emoji: '🧩', desc: 'Con vértices y aristas, ¿quién soy?', gen: qQuien },
  clasifica: { world: 'w3', title: 'Crece o Decrece', emoji: '📈', desc: 'Incremental o decremental.', gen: qClasifica },
  siguiente: { world: 'w3', title: '¿Qué sigue?', emoji: '🔮', desc: 'Adivina el siguiente término.', gen: qSiguiente },
  regla: { world: 'w3', title: 'Descubre la Regla', emoji: '🗝️', desc: 'Encuentra y explica la regla del patrón.', gen: qRegla },
  construye: { world: 'w3', title: 'Constructora de Patrones', emoji: '🧱', desc: 'Dibuja el término que sigue.', gen: qConstruye }
};
const WORLDS = {
  w1: { cls: 'i1', emoji: '🏝️', title: 'Isla de los Cuerpos', topic: 'cuerpos', desc: 'Prismas y pirámides: conócelos y ponles nombre.', games: ['detective', 'pistas'] },
  w2: { cls: 'i2', emoji: '⛰️', title: 'Montaña de las Partes', topic: 'partes', desc: 'Caras, aristas, vértices y la cúspide.', games: ['cuenta', 'cazador', 'quien'] },
  w3: { cls: 'i3', emoji: '🌈', title: 'Valle de los Patrones', topic: 'patrones', desc: 'Secuencias que crecen y decrecen. ¡Y su regla!', games: ['clasifica', 'siguiente', 'regla', 'construye'] }
};

/* ---------- Lecciones ---------- */
const solidsRow = list => `<div class="gallery">${list.map(([k, n, hl, cap]) => `<figure>${solidTag(k, n, hl)}<figcaption>${cap}</figcaption></figure>`).join('')}</div>`;
const LESSONS = {
  w1: [
    {
      t: '¡Figuras con volumen!', h: () => `
      <p>Las figuras planas (cuadrado, triángulo, círculo) se dibujan en una hoja. Pero los <b>cuerpos geométricos</b> son como objetos de verdad: <span class="hl-p">tienen largo, ancho y alto</span> y ocupan espacio. ¡Los puedes tocar!</p>
      <div class="key">📦 Una caja, 🔺 una tienda de campaña o 🏛️ una pirámide de Egipto son cuerpos geométricos.</div>
      <p>Hoy conocerás dos familias de cuerpos con caras planas:</p>
      ${solidsRow([['prism', 3, null, 'Prisma'], ['prism', 5, null, 'Prisma'], ['pyr', 4, null, 'Pirámide'], ['pyr', 6, null, 'Pirámide']])}
      <p style="text-align:center">👆 ¡Giran solos para que los veas por todos lados!</p>`},
    {
      t: 'Los prismas', h: () => `
      <div class="cols"><div>
      <p>Un <b class="hl-p">prisma</b> tiene:</p>
      <ul><li><b>2 bases</b> iguales y paralelas (una arriba y otra abajo).</li><li>Caras laterales que son <b>rectángulos</b>.</li><li><b>No</b> tiene punta.</li></ul>
      <div class="tip">💡 Piensa en una caja de cereal o en un vaso de lados rectos.</div></div>
      ${solidTag('prism', 4, { faces: 'all' })}</div>
      <p style="text-align:center"><span class="hl-b">Rosado</span> = las 2 bases · <span class="hl-t">Verde</span> = caras laterales</p>`},
    {
      t: 'Las pirámides', h: () => `
      <div class="cols"><div>
      <p>Una <b class="hl-p">pirámide</b> tiene:</p>
      <ul><li><b>1 sola base</b>.</li><li>Caras laterales que son <b>triángulos</b>.</li><li>Todas las caras laterales se juntan arriba en un punto llamado <b>cúspide</b>.</li></ul>
      <div class="tip">💡 Piensa en las pirámides de Egipto o en un gorro de fiesta.</div></div>
      ${solidTag('pyr', 4, { faces: 'all' })}</div>
      <p style="text-align:center"><span class="hl-b">Rosado</span> = la base · <span class="hl-t">Verde</span> = caras laterales triangulares</p>`},
    {
      t: 'El nombre sale de la base', h: () => `
      <p>Primero decimos si es <b>prisma</b> o <b>pirámide</b>, y luego ponemos <b>la forma de su base</b>.</p>
      <table class="t"><tr><th>Forma de la base</th><th>Lados</th><th>Ejemplos de nombre</th></tr>
      <tr><td>Triángulo</td><td>3</td><td>Prisma triangular · Pirámide triangular</td></tr>
      <tr><td>Cuadrilátero</td><td>4</td><td>Prisma cuadrangular · Pirámide cuadrangular</td></tr>
      <tr><td>Pentágono</td><td>5</td><td>Prisma pentagonal · Pirámide pentagonal</td></tr>
      <tr><td>Hexágono</td><td>6</td><td>Prisma hexagonal · Pirámide hexagonal</td></tr></table>
      <p><b>🎮 ¡Pruébalo tú!</b> Elige un cuerpo y mira cómo se llama:</p>${explorerHTML(false)}
      <div class="warn">⚠️ Cuidado: la <b>pirámide cuadrangular</b> y la <b>pirámide triangular</b> se parecen, ¡cuenta los lados de la base!</div>`, init: r => mountExplorer(r) }
  ],
  w2: [
    {
      t: 'Las caras', h: () => `
      <p>Las <b>caras</b> son las superficies planas del cuerpo. Hay dos tipos:</p>
      <ul><li><b class="hl-b">Caras basales</b>: las bases. El prisma tiene 2 y la pirámide tiene 1.</li><li><b class="hl-t">Caras laterales</b>: las que rodean el cuerpo. Hay una por cada lado de la base.</li></ul>
      ${solidsRow([['prism', 3, { faces: 'all' }, 'Prisma triangular'], ['pyr', 5, { faces: 'all' }, 'Pirámide pentagonal']])}
      <div class="key">Prisma triangular: 2 bases + 3 laterales = <b>5 caras</b>.<br>Pirámide pentagonal: 1 base + 5 laterales = <b>6 caras</b>.</div>`},
    {
      t: 'Las aristas', h: () => `
      <p>Una <b>arista</b> es la línea donde <b>se juntan dos caras</b>. Es como el borde de una caja.</p>
      <ul><li><b class="hl-b">Aristas basales</b>: forman el contorno de las bases.</li><li><b class="hl-t">Aristas laterales</b>: unen una base con la otra (prisma) o la base con la cúspide (pirámide).</li></ul>
      ${solidsRow([['prism', 4, { edges: 'all' }, 'Prisma cuadrangular'], ['pyr', 4, { edges: 'all' }, 'Pirámide cuadrangular']])}
      <div class="tip">💡 Las líneas <b>punteadas</b> son aristas que están detrás. ¡También hay que contarlas!</div>`},
    {
      t: 'Vértices y cúspide', h: () => `
      <p>Un <b>vértice</b> es una <b>esquina</b>: el punto donde se juntan varias aristas.</p>
      <p>En la pirámide, el vértice de arriba donde se juntan todas las caras laterales tiene nombre especial: la <b style="color:#c99200">cúspide</b> ⭐.</p>
      ${solidsRow([['prism', 3, { verts: 'all', number: true, neutral: true }, 'Prisma triangular: 6 vértices'], ['pyr', 4, { verts: 'all', number: true, neutral: true }, 'Pirámide cuadrangular: 5 vértices']])}
      <div class="key">Pirámide cuadrangular: 4 vértices de la base + 1 cúspide = <b>5 vértices</b>.<br>Pirámide triangular: 3 vértices de la base + 1 cúspide = <b>4 vértices</b>.</div>`},
    {
      t: 'Explorador y trucos', h: () => `
      <p>Elige un cuerpo y toca <b>Caras</b>, <b>Aristas</b> o <b>Vértices</b>:</p>${explorerHTML(true)}
      <div class="key"><b>🧠 Trucos para contar (n = lados de la base)</b>
      <table class="t"><tr><th></th><th>Caras</th><th>Vértices</th><th>Aristas</th></tr>
      <tr><td><b>Prisma</b></td><td>n + 2</td><td>n × 2</td><td>n × 3</td></tr>
      <tr><td><b>Pirámide</b></td><td>n + 1</td><td>n + 1</td><td>n × 2</td></tr></table></div>
      <div class="tip">Ejemplo: prisma hexagonal (n = 6) → 8 caras, 12 vértices, 18 aristas.</div>`, init: r => mountExplorer(r) }
  ],
  w3: [
    {
      t: '¿Qué es una secuencia?', h: () => `
      <p>Una <b>secuencia</b> es una fila de figuras que sigue una <b>regla</b>. Cada figura (o grupo) es un <b>término</b>.</p>
      ${seqHTML([{ sq: 1 }, { sq: 2 }, { sq: 3 }, { sq: 4 }], true)}
      <p>Si descubres la regla, ¡puedes adivinar el siguiente término sin equivocarte! 🔮</p>
      <div class="key">Aquí la regla es: «Cada término tiene <b>1 cuadrado más</b> que el anterior». El siguiente tiene 5 cuadrados.</div>`},
    {
      t: 'Secuencias incrementales 📈', h: () => `
      <p>Una secuencia es <b class="hl-t">incremental</b> cuando <b>crece</b>: cada término tiene <b>más</b> figuras que el anterior.</p>
      ${seqHTML([{ ci: 1 }, { ci: 3 }, { ci: 5 }, { ci: 7 }], true)}
      <div class="key">Regla: «Cada término tiene <b>2 círculos más</b> que el anterior». El 5.º tiene 9 círculos.</div>
      <div class="tip">💡 Pista: ¡las palabras “incremento” e “incrementar” significan aumentar!</div>`},
    {
      t: 'Secuencias decrementales 📉', h: () => `
      <p>Una secuencia es <b class="hl-b">decremental</b> cuando <b>decrece</b>: cada término tiene <b>menos</b> figuras que el anterior.</p>
      ${seqHTML([{ tr: 9 }, { tr: 7 }, { tr: 5 }, { tr: 3 }], true)}
      <div class="key">Regla: «Cada término tiene <b>2 triángulos menos</b> que el anterior». El 5.º tiene 1 triángulo.</div>
      <div class="warn">⚠️ Cuidado: no es lo mismo “quitar 2” que “llegar a 2”. Fíjate en <b>cuánto cambia</b> de uno a otro.</div>`},
    {
      t: 'Cómo explicar la regla', h: () => `
      <p>En el examen tienes que <b>dibujar</b> el siguiente término y <b>explicar con palabras</b> la regla. ¡Usa estos 3 pasos!</p>
      <ol style="margin:8px 0 8px 24px"><li><b>Cuenta</b> las figuras de cada término.</li><li><b>Compara</b>: ¿cuántas aparecen o desaparecen de uno a otro?</li><li><b>Di la regla</b>: «Cada término tiene ___ (figura) más/menos que el anterior».</li></ol>
      <p>Ejemplo con dos figuras:</p>
      ${seqHTML([{ ci: 1, sq: 2 }, { ci: 2, sq: 4 }, { ci: 3, sq: 6 }, { ci: 4, sq: 8 }], true)}
      <div class="key">Regla: «Cada término tiene <b>1 círculo</b> y <b>2 cuadrados más</b> que el anterior».<br>Siguiente: <b>5 círculos y 10 cuadrados</b>.</div>
      <div class="tip">🗣️ Practica en voz alta con mamá o papá. ¡Explicar es la mejor forma de aprender!</div>`}
  ]
};
const LESSON_COUNT = () => Object.values(LESSONS).reduce((a, l) => a + l.length, 0);

/* =========================================================
   VISTAS
   ========================================================= */
let view = { name: 'home' };
window.go = (name, arg, arg2) => { sfx.click(); view = { name, arg, arg2 }; render(); scrollTo({ top: 0 }); };

function render() {
  $('#topbar').hidden = !S.name;
  updateHud();
  const v = view.name;
  if (!S.name) return renderWelcome();
  if (v === 'home') return renderHome();
  if (v === 'world') return renderWorld(view.arg);
  if (v === 'lesson') return renderLesson(view.arg, view.arg2 || 0);
  if (v === 'game') return renderQuestion();
  if (v === 'result') return renderResult();
}

function renderWelcome() {
  app.innerHTML = `<section class="view hero card" style="color:var(--ink)">
    <div class="mascot">🦊</div>
    <h1>¡Hola, futura matemática!</h1>
    <p>Soy <b>Luci</b>, tu guía. Juntas vamos a prepararnos para el examen de <b>cuerpos geométricos</b> y <b>patrones</b>.</p>
    <p style="margin-top:12px">¿Cómo te llamas?</p>
    <input id="nameIn" class="name" maxlength="20" placeholder="Escribe tu nombre" value="Luciana" autocomplete="off">
    <br><button class="btn big yellow" onclick="startAdventure()">¡Comenzar la aventura! 🚀</button></section>`;
  $('#nameIn').addEventListener('keydown', e => e.key === 'Enter' && startAdventure());
}
window.startAdventure = () => { const v = $('#nameIn').value.trim(); if (!v) return; S.name = v; save(); sfx.win(); view = { name: 'home' }; render(); };

const starsHTML = n => `<span class="stars">${[1, 2, 3].map(i => `<span class="${i <= n ? 'on' : ''}">★</span>`).join('')}</span>`;
function worldProgress(w) {
  const W = WORLDS[w], gm = W.games.length, ls = LESSONS[w].length;
  let done = 0; LESSONS[w].forEach((_, i) => S.lessons[w + i] && done++); W.games.forEach(g => (S.stars[g] || 0) > 0 && done++);
  return Math.round(100 * done / (gm + ls));
}

function renderHome() {
  const lvl = level();
  const msgs = [`¡Vamos a practicar, ${S.name}!`, 'Cada juego te acerca a ser experta. 💪', 'Gana 3 estrellas ⭐ en todos los juegos.', 'Equivocarse es parte de aprender. ¡Sigue!'];
  app.innerHTML = `<section class="view">
    <div class="hero"><div class="mascot">🦊</div><h1>Aventura Matemática de ${S.name}</h1>
    <p>Nivel ${lvl} · <b>${levelTitle()}</b></p><div class="bubble">${pick(msgs)}</div></div>
    <div class="islands">
      ${Object.entries(WORLDS).map(([id, w], i) => `<button class="island ${w.cls}" onclick="go('world','${id}')">
        <span class="emoji">${w.emoji}</span><h2>${i + 1}. ${w.title}</h2><p>${w.desc}</p>
        <div class="meter"><i style="width:${worldProgress(id)}%"></i></div><span class="tag">${worldProgress(id)}% completado</span></button>`).join('')}
      <button class="island i4" onclick="startExam()"><span class="emoji">🏆</span><h2>Torneo Final</h2>
        <p>12 preguntas de todo: ¡un simulacro como el examen!</p><span class="tag">${S.examBest === null ? 'Aún no lo juegas' : 'Mejor: ' + S.examBest + ' pts'}</span></button>
    </div>
    <div class="card"><h2>📊 Mi semáforo de aprendizaje</h2>
      <p style="color:var(--muted);font-size:.95rem">Se calcula con tus últimas respuestas. Verde = ¡lista! · Amarillo = casi · Rojo = sigue practicando.</p>
      ${Object.entries(TOPICS).map(([k, t]) => { const m = mastery(k), l = light(m); return `<div class="prog-row">
        <div><b>${t.emoji} ${t.name}</b><div style="font-size:.9rem;color:var(--muted)">${m === null ? 'Juega al menos 5 preguntas de este tema.' : l === 'g' ? '¡Excelente, dominas este tema!' : l === 'y' ? 'Vas muy bien, repasa un poquito más.' : t.tip}</div></div>
        <div class="sem"><b>${m === null ? '—' : m + '%'}</b><span class="dot ${l === 'n' ? '' : l}"></span></div>
        <div class="pbar"><i style="width:${m || 0}%;background:${l === 'g' ? 'var(--green)' : l === 'y' ? 'var(--yellow)' : l === 'r' ? 'var(--red)' : '#ccc'}"></i></div></div>`; }).join('')}
    </div>
    <div class="card"><h2>🎖️ Mis insignias</h2><div class="badges">${BADGES.map(b => `<div class="badge ${S.badges[b.id] ? '' : 'locked'}"><span class="ic">${b.ic}</span>${b.n}</div>`).join('')}</div></div>
    <p style="text-align:center"><button class="btn gray" onclick="resetAll()">Borrar mi progreso</button></p>
  </section>`;
}
window.resetAll = () => { if (confirm('¿Seguro que quieres borrar todo el progreso?')) { S = defaultState(); save(); view = { name: 'home' }; render(); } };

function renderWorld(id) {
  const W = WORLDS[id];
  app.innerHTML = `<section class="view"><button class="back" onclick="go('home')">← Mapa</button>
    <div class="world-head"><h1>${W.emoji} ${W.title}</h1><p>${W.desc}</p></div>
    <h2 style="color:#fff;margin:10px 0">📖 Aprende</h2>
    <div class="menu">${LESSONS[id].map((l, i) => `<button class="menu-item" onclick="go('lesson','${id}',${i})">${S.lessons[id + i] ? '<span class="done-mark">✅</span>' : ''}<div class="emoji">📘</div><h3>${i + 1}. ${l.t}</h3><p>Lección corta con ejemplos</p></button>`).join('')}</div>
    <h2 style="color:#fff;margin:22px 0 10px">🎮 Juega y demuestra lo que sabes</h2>
    <div class="menu">${W.games.map(g => `<button class="menu-item" onclick="startGame('${g}')"><div class="emoji">${GAMES[g].emoji}</div><h3>${GAMES[g].title}</h3><p>${GAMES[g].desc}</p>${starsHTML(S.stars[g] || 0)}</button>`).join('')}</div>
  </section>`;
}

function renderLesson(id, i) {
  const L = LESSONS[id][i], n = LESSONS[id].length;
  app.innerHTML = `<section class="view"><button class="back" onclick="go('world','${id}')">← ${WORLDS[id].title}</button>
    <div class="card lesson"><h2>${L.t}</h2>${L.h()}</div>
    <div class="dots">${LESSONS[id].map((_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>
    <div class="nav">${i > 0 ? `<button class="btn gray" onclick="go('lesson','${id}',${i - 1})">← Anterior</button>` : '<span></span>'}
    ${i < n - 1 ? `<button class="btn" onclick="lessonDone('${id}',${i});go('lesson','${id}',${i + 1})">Siguiente →</button>`
      : `<button class="btn green" onclick="lessonDone('${id}',${i});go('world','${id}')">¡Listo! A jugar 🎮</button>`}</div></section>`;
  mountSolids(app); if (L.init) L.init(app);
}
window.lessonDone = (id, i) => { if (!S.lessons[id + i]) { S.lessons[id + i] = true; save(); addXp(15); checkBadges(); } };

/* ---------- Juego ---------- */
let G = null;
window.startGame = id => {
  const d = GAMES[id];
  G = { id, def: d, qs: Array.from({ length: 6 }, d.gen), i: 0, ok: 0, streak: 0, best: 0, xp: 0, done: false, res: { cuerpos: [0, 0], partes: [0, 0], patrones: [0, 0] }, back: d.world };
  view = { name: 'game' }; render(); scrollTo({ top: 0 });
};
window.startExam = () => {
  const mix = (...fs) => fs.map(f => f());
  const qs = [...mix(qDetective, qPistas, qDetective, qPistas), ...mix(qCuenta, qCazador, qQuien, qCazador), ...mix(qClasifica, qSiguiente, qRegla, qConstruye)];
  G = { id: 'exam', exam: true, def: { title: 'Torneo Final', emoji: '🏆' }, qs, i: 0, ok: 0, streak: 0, best: 0, xp: 0, done: false, res: { cuerpos: [0, 0], partes: [0, 0], patrones: [0, 0] }, back: 'home' };
  view = { name: 'game' }; render(); scrollTo({ top: 0 });
};

function visualHTML(v) {
  if (!v) return '';
  if (v.t === 'solid') return `<div class="q-visual">${solidTag(v.k, v.n, v.hl)}</div>`;
  if (v.t === 'seq') return `<div class="q-visual" style="width:100%">${seqHTML(v.q.terms, v.next)}</div>`;
  return '';
}
let B = null;
function renderQuestion() {
  const q = G.qs[G.i]; G.answered = false;
  const pct = Math.round(100 * G.i / G.qs.length);
  let body;
  if (q.type === 'mc') body = `${visualHTML(q.visual)}<div class="opts">${q.opts.map((o, i) => `<button class="opt" onclick="answer(${i})">${o}</button>`).join('')}</div>`;
  else {
    B = { ci: 0, sq: 0, tr: 0 };
    body = `<div class="q-visual" style="width:100%">${seqHTML(q.q.terms, false).replace('</div></div>', '</div></div>')}</div>
      <div class="seq"><div class="term build" id="live" style="min-width:140px;min-height:100px"></div></div>
      <div class="builder">${ORDER.map(k => `<div class="bctl">${shapeHTML(k)}<button onclick="bAdj('${k}',-1)" aria-label="quitar">−</button><b id="bc-${k}">0</b><button onclick="bAdj('${k}',1)" aria-label="agregar">+</button></div>`).join('')}</div>
      <p style="text-align:center"><button class="btn green" id="checkBtn" onclick="checkBuild()">Comprobar ✔</button></p>`;
  }
  app.innerHTML = `<section class="view">
    <div class="game-top"><button class="back" style="margin:0" onclick="quit()">✖ Salir</button><b>${G.def.emoji} ${G.def.title}</b>
      <div class="gprog"><i style="width:${pct}%"></i></div><b>${G.i + 1}/${G.qs.length}</b>${G.streak >= 2 ? `<span class="streak">🔥 ${G.streak}</span>` : ''}</div>
    <div class="card"><div class="q-title">${q.prompt}</div>${body}<div id="fb"></div></div></section>`;
  mountSolids(app);
  if (q.type === 'build') drawLive();
}
window.quit = () => { if (confirm('¿Quieres salir del juego? Perderás esta ronda.')) go(G.exam ? 'home' : 'world', G.back); };
function drawLive() {
  const el = $('#live'); if (!el) return;
  el.innerHTML = grpHTML(B) || '<span style="color:var(--muted);font-size:.9rem">Agrega figuras…</span>';
  ORDER.forEach(k => $('#bc-' + k).textContent = B[k]);
}
window.bAdj = (k, d) => { if (G.answered) return; B[k] = Math.max(0, Math.min(16, B[k] + d)); sfx.click(); drawLive(); };

function record(q, ok) {
  const h = S.hist[q.topic]; h.push(ok); if (h.length > 20) h.shift();
  G.res[q.topic][1]++; if (ok) { G.res[q.topic][0]++; G.ok++; G.streak++; G.best = Math.max(G.best, G.streak); S.maxStreak = Math.max(S.maxStreak, G.streak); }
  else G.streak = 0;
  if (ok) { const gain = 10 + Math.min(G.streak - 1, 5) * 2; G.xp += gain; addXp(gain); }
  save();
}
function feedback(q, ok, extra) {
  const praise = ['¡Excelente!', '¡Genial!', '¡Muy bien!', '¡Increíble!', '¡Eres una crack!'];
  const last = G.i === G.qs.length - 1;
  $('#fb').innerHTML = `<div class="feedback ${ok ? 'ok' : 'bad'}"><h3>${ok ? '✅ ' + pick(praise) + (G.streak >= 3 ? ` 🔥 racha de ${G.streak}` : '') : '💡 ¡Casi! Así se resuelve:'}</h3>
    <p>${extra || ''}${q.why}</p>${q.say ? `<div class="say">🗣️ ${q.say}</div>` : ''}</div>
    <p style="text-align:center;margin-top:14px"><button class="btn ${last ? 'yellow' : ''}" onclick="nextQ()">${last ? 'Ver resultado 🏁' : 'Siguiente →'}</button></p>`;
  $('#fb').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
window.answer = i => {
  if (G.answered) return; G.answered = true;
  const q = G.qs[G.i], ok = i === q.ans, btns = $$('.opt');
  btns.forEach((b, k) => { b.disabled = true; if (k === q.ans) b.classList.add('ok'); else if (k === i) b.classList.add('bad'); });
  ok ? sfx.ok() : sfx.bad(); record(q, ok);
  feedback(q, ok, ok ? '' : `La respuesta correcta era <b>${q.opts[q.ans]}</b>. `);
};
window.checkBuild = () => {
  if (G.answered) return;
  const q = G.qs[G.i], keys = q.q.keys;
  const ok = ORDER.every(k => B[k] === (keys.includes(k) ? q.q.next[k] : 0));
  if (!ok && !ORDER.some(k => B[k])) return toast('Agrega al menos una figura 🙂');
  G.answered = true; $('#checkBtn').disabled = true;
  ok ? sfx.ok() : sfx.bad(); record(q, ok);
  if (!ok) { const c = $('#live'); c.insertAdjacentHTML('afterend', `<div class="term" style="border-color:var(--green);background:#e9fff1"><span class="n" style="background:var(--green)">Correcto</span>${grpHTML(q.q.next)}</div>`); }
  feedback(q, ok);
};
window.nextQ = () => { sfx.click(); if (G.i < G.qs.length - 1) { G.i++; renderQuestion(); scrollTo({ top: 0 }); } else finishGame(); };

function finishGame() {
  const total = G.qs.length, p = Math.round(100 * G.ok / total);
  G.score = p;
  if (G.exam) { G.stars = p >= 90 ? 3 : p >= 70 ? 2 : p >= 40 ? 1 : 0; S.examBest = Math.max(S.examBest || 0, p); }
  else { G.stars = G.ok === total ? 3 : G.ok >= total - 1 ? 3 : G.ok >= total * .7 ? 2 : G.ok >= total * .4 ? 1 : 0; S.stars[G.id] = Math.max(S.stars[G.id] || 0, G.stars); }
  S.played++; save();
  const bonus = G.stars * 10; addXp(bonus); G.xp += bonus; checkBadges();
  if (G.stars >= 2) { sfx.win(); confetti(); }
  view = { name: 'result' }; render(); scrollTo({ top: 0 });
}
function renderResult() {
  const g = G, p = g.score, l = light(p);
  const msg = g.stars === 3 ? ['🌟 ¡Perfecto!', 'Dominas este reto. ¡Estoy orgullosa de ti!'] : g.stars === 2 ? ['👏 ¡Muy bien!', 'Casi perfecto. Un repaso más y lo logras.'] : g.stars === 1 ? ['💪 ¡Buen intento!', 'Lee la lección otra vez y vuelve a jugar.'] : ['🌱 ¡Sigue practicando!', 'Todos aprendemos paso a paso. Repasa la lección y vuelve a intentarlo.'];
  let extra = '';
  if (g.exam) {
    const rows = Object.entries(g.res).map(([k, [a, b]]) => { const pp = Math.round(100 * a / b), ll = light(pp); return `<div class="prog-row"><div><b>${TOPICS[k].emoji} ${TOPICS[k].name}</b><div style="font-size:.9rem;color:var(--muted)">${ll === 'g' ? '¡Dominado!' : ll === 'y' ? 'Casi, repasa un poco.' : TOPICS[k].tip}</div></div><div class="sem"><b>${a}/${b}</b><span class="dot ${ll}"></span></div></div>`; }).join('');
    extra = `<div class="verdict ${l}"><div class="light">${l === 'g' ? '🟢' : l === 'y' ? '🟡' : '🔴'}</div><h3>${l === 'g' ? 'Semáforo VERDE: ¡lista para el examen!' : l === 'y' ? 'Semáforo AMARILLO: vas bien, falta repasar.' : 'Semáforo ROJO: necesitas practicar más.'}</h3>
      <p>${l === 'g' ? 'Sigue jugando un poco cada día para no olvidar.' : l === 'y' ? 'Repasa los temas con punto amarillo/rojo y repite el torneo.' : 'Repasa las lecciones y juega cada isla antes de intentar el torneo otra vez.'}</p></div><div style="text-align:left">${rows}</div>`;
  }
  const again = g.exam ? 'startExam()' : `startGame('${g.id}')`;
  app.innerHTML = `<section class="view"><div class="card result">
    <div class="mascot">${g.stars >= 2 ? '🦊' : '🦊'}</div><h1>${msg[0]}</h1><p>${msg[1]}</p>
    <div class="bigstars">${[1, 2, 3].map(i => `<span class="${i <= g.stars ? 'on' : ''}">★</span>`).join('')}</div>
    <h2 style="margin:10px 0">${g.ok} de ${g.qs.length} correctas (${p}%)</h2>
    <p>+${g.xp} XP ganados · Mejor racha: 🔥 ${g.best}</p>${extra}
    <div style="margin-top:18px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <button class="btn yellow" onclick="${again}">🔄 Jugar de nuevo</button>
      <button class="btn" onclick="go('${g.exam ? 'home' : 'world'}','${g.back}')">${g.exam ? '🗺️ Ir al mapa' : '← Volver a la isla'}</button>
      ${g.stars < 3 && !g.exam ? `<button class="btn pink" onclick="go('world','${g.back}')">📖 Repasar lección</button>` : ''}</div></div></section>`;
}

/* ---------- Inicio ---------- */
updateHud();
render();
