export interface WaveProps {
  /** The colour of the act BELOW — the wave is cut out of the next field. */
  into?: 'page' | 'slab';
  className?: string;
}

/** The act separator: a 150px arc overspilling to 150% width, gone under 768px. */
export function Wave({ into = 'page', className }: WaveProps) {
  return (
    <div
      className={['np-wave', `np-wave--${into}`, className].filter(Boolean).join(' ')}
      aria-hidden="true"
    >
      <svg viewBox="0 0 1200 150" preserveAspectRatio="none" focusable="false">
        <path d="M0,80 C300,140 900,20 1200,80 L1200,150 L0,150 Z" />
      </svg>
    </div>
  );
}
