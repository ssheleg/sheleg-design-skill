export interface CapsuleCurtainProps {
  /** Columns across. The reference draws 8 on a 70px pitch. */
  columns?: number;
  /** Capsules per column. Each covers all but `step` of the one above it. */
  capsules?: number;
  /** Capsule width in user units; the pitch equals it, so columns touch. */
  width?: number;
  /** Capsule height. `rx` is always width / 2 — a stadium, never a rounded box. */
  height?: number;
  /** Hue of the top stop of the first capsule, in degrees. */
  hueTop?: number;
  /** Hue of the bottom stop of the first capsule, in degrees. */
  hueBottom?: number;
  className?: string;
}

/**
 * The signature element: a curtain of gradient capsules, generated rather than
 * chosen. The top stop rotates forward around the hue wheel and the bottom stop
 * rotates backward, so the two stay near-complementary and every column inverts
 * its own gradient between its first capsule and its last.
 *
 * Decoration only — `aria-hidden`, `pointer-events: none`, and it carries no
 * information. Position it with the page's own transform; this component draws.
 */
export function CapsuleCurtain({
  columns = 8,
  capsules = 12,
  width = 70,
  height = 170,
  hueTop = 247,
  hueBottom = 29,
  className,
}: CapsuleCurtainProps) {
  const stepTop = 12.4;
  const stepBottom = -10.3;
  const overlap = height / 4.93; // 34.5 at the reference's 170
  const w = columns * width;
  const h = (capsules - 1) * overlap + height;

  return (
    <svg
      className={['pc-curtain', className].filter(Boolean).join(' ')}
      viewBox={`0 0 ${w} ${h}`}
      width={w}
      height={h}
      aria-hidden="true"
      focusable="false"
    >
      <defs>
        <filter id="pc-dither" x="0" y="0" width="100%" height="100%">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="2.95"
            numOctaves="5"
            seed="9"
            stitchTiles="stitch"
          />
        </filter>
        <mask id="pc-curtain-mask" maskUnits="userSpaceOnUse" x="0" y="0" width={w} height={h}>
          <use href="#pc-caps" />
        </mask>
        {Array.from({ length: columns * capsules }, (_, n) => {
          const i = n % capsules;
          return (
            <linearGradient
              key={n}
              id={`pc-g${n}`}
              gradientUnits="objectBoundingBox"
              x1="0"
              y1="0"
              x2="1"
              y2="0"
              gradientTransform="rotate(90 0.5 0.5)"
            >
              <stop offset="0%" stopColor={`hsl(${hueTop + i * stepTop} 92% 53%)`} />
              <stop offset="100%" stopColor={`hsl(${hueBottom + i * stepBottom} 88% 46%)`} />
            </linearGradient>
          );
        })}
      </defs>
      <g id="pc-caps">
        {Array.from({ length: columns }, (_, c) => (
          <g key={c} className="pc-curtain__column">
            {Array.from({ length: capsules }, (_, i) => (
              <rect
                key={i}
                x={c * width}
                y={i * overlap}
                width={width}
                height={height}
                rx={width / 2}
                ry={width / 2}
                fill={`url(#pc-g${c * capsules + i})`}
              />
            ))}
          </g>
        ))}
      </g>
      <rect
        width={w}
        height={h}
        filter="url(#pc-dither)"
        mask="url(#pc-curtain-mask)"
        className="pc-curtain__grain"
      />
    </svg>
  );
}
