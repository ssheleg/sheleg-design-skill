import { useEffect, useRef } from 'react';

export interface RainProps {
  /** Multiply the fall speed, for example by scroll velocity (1 = resting). */
  boost?: () => number;
  className?: string;
}

// The glyph set the reference falls: katakana, digits, a few capitals and operators.
const GLYPHS = 'アイウエオカキクケコサシスセソタチツテトナニヌネノ0123456789ABCDEFΣλ<>/{}=+*';

/**
 * The signature element: falling glyph columns on a canvas behind the page.
 * Colours and sizes are read from the token layer with getComputedStyle, so the
 * canvas follows the tokens. Under prefers-reduced-motion the loop never starts
 * and the canvas stays hidden (the stylesheet hides it too). It also stops while
 * the tab is hidden.
 */
export function Rain({ boost, className }: RainProps) {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (reduce.matches) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const css = getComputedStyle(canvas);
    const head = css.getPropertyValue('--ink-bright').trim();
    const tail = css.getPropertyValue('--accent').trim();
    const wide = parseFloat(css.getPropertyValue('--rain-glyph')) || 16;
    const narrow = parseFloat(css.getPropertyValue('--rain-glyph-narrow')) || 13;
    const swap = parseFloat(css.getPropertyValue('--dur-glyph')) || 140;

    type Column = { y: number; v: number; len: number; seed: number };
    let cols: Column[] = [];
    let size = wide;
    let dpr = 1;
    let last = performance.now();
    let frame = 0;

    const build = () => {
      dpr = Math.min(1.5, window.devicePixelRatio || 1);
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
      size = window.innerWidth < 700 ? narrow : wide;
      const n = Math.ceil(window.innerWidth / size);
      cols = Array.from({ length: n }, () => ({
        y: Math.random() * -window.innerHeight,
        v: 40 + Math.random() * 90,
        len: 8 + Math.floor(Math.random() * 22),
        seed: Math.floor(Math.random() * 1000),
      }));
    };

    const draw = () => {
      const now = performance.now();
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      const k = Math.max(1, Math.min(7, boost ? boost() : 1));
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
      ctx.font = `${size}px ui-monospace, Menlo, monospace`;
      ctx.textBaseline = 'top';
      for (let i = 0; i < cols.length; i++) {
        const c = cols[i];
        c.y += c.v * dt * k;
        if (c.y - c.len * size > window.innerHeight) {
          c.y = Math.random() * -200;
          c.v = 40 + Math.random() * 90;
        }
        for (let j = 0; j < c.len; j++) {
          const y = c.y - j * size;
          if (y < -size || y > window.innerHeight) continue;
          const step = j === 0 ? Math.floor(now / swap) : 0;
          ctx.globalAlpha = j === 0 ? 0.9 : (1 - j / c.len) * 0.45;
          ctx.fillStyle = j === 0 ? head : tail;
          ctx.fillText(GLYPHS[(c.seed + j * 7 + step) % GLYPHS.length], i * size, y);
        }
      }
      ctx.globalAlpha = 1;
      frame = requestAnimationFrame(draw);
    };

    const start = () => {
      if (!frame && !document.hidden) {
        last = performance.now();
        frame = requestAnimationFrame(draw);
      }
    };
    const stop = () => {
      cancelAnimationFrame(frame);
      frame = 0;
    };
    const onVisibility = () => (document.hidden ? stop() : start());
    const onReduce = () => (reduce.matches ? stop() : start());

    build();
    start();
    window.addEventListener('resize', build);
    document.addEventListener('visibilitychange', onVisibility);
    reduce.addEventListener('change', onReduce);
    return () => {
      stop();
      window.removeEventListener('resize', build);
      document.removeEventListener('visibilitychange', onVisibility);
      reduce.removeEventListener('change', onReduce);
    };
  }, [boost]);

  return (
    <canvas
      ref={ref}
      aria-hidden="true"
      className={['ph-rain', className].filter(Boolean).join(' ')}
    />
  );
}
