import { useEffect, useRef } from 'react';
import type { ReactNode } from 'react';

export interface DiagramCord {
  /** An SVG path command string. Keep the control points shallow — see the doc. */
  d: string;
  /** Seconds for one traversal. The pack's measured band is 2–3.5s. */
  dur?: number;
  /** Particles on this cord. They are phase-spaced evenly across `dur`. */
  particles?: 1 | 2 | 3;
  /** A dashed cord is a DIFFERENT KIND of edge, never a quieter one. */
  kind?: 'live' | 'replay';
}

export interface DiagramProps {
  width: number;
  height: number;
  cords: DiagramCord[];
  /** Index of this cord in the board, used for the 0.1s per-cord stagger. */
  children?: ReactNode;
  title: string;
  className?: string;
}

/** The pack's signature element.
 *
 *  Two things here are load-bearing and easy to lose:
 *
 *  1. Particles are SVG `<animateMotion>`, which is declarative — no rAF loop,
 *     no library, one element per dot.
 *  2. SMIL does NOT read CSS `animation-duration`, so a
 *     `prefers-reduced-motion` media query cannot stop it. That is the defect
 *     the reference ships. `pauseAnimations()` below is the fix, and it is the
 *     reason this component needs an effect at all.
 */
export function Diagram({ width, height, cords, children, title, className }: DiagramProps) {
  const root = useRef<SVGSVGElement>(null);

  useEffect(() => {
    const svg = root.current;
    if (!svg) return;
    const query = window.matchMedia('(prefers-reduced-motion: reduce)');
    const apply = () => (query.matches ? svg.pauseAnimations() : svg.unpauseAnimations());
    apply();
    query.addEventListener('change', apply);
    return () => query.removeEventListener('change', apply);
  }, []);

  return (
    <svg
      ref={root}
      className={['pb-diagram', className].filter(Boolean).join(' ')}
      width={width}
      height={height}
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-label={title}
    >
      <defs>
        <marker id="pb-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <polygon className="pb-diagram__head" points="0 0, 6 3, 0 6" />
        </marker>
      </defs>
      {cords.map((cord, i) => {
        const dur = cord.dur ?? 2.5;
        const count = cord.particles ?? 1;
        const stagger = (i % 10) * 0.1;
        return (
          <g key={i}>
            <path
              className={`pb-diagram__cord pb-diagram__cord--${cord.kind ?? 'live'}`}
              d={cord.d}
              markerEnd="url(#pb-arrow)"
            />
            {Array.from({ length: count }, (unused, n) => (
              <circle key={n} className="pb-diagram__dot" r="2">
                <animateMotion
                  path={cord.d}
                  dur={`${dur}s`}
                  begin={`${(stagger + (n * dur) / count).toFixed(4)}s`}
                  repeatCount="indefinite"
                />
              </circle>
            ))}
          </g>
        );
      })}
      {children}
    </svg>
  );
}
