export interface SweepProps {
  /** 90deg is the measured direction; the stops never reverse. */
  angle?: number;
  height?: number;
  className?: string;
}

export function Sweep({ angle = 90, height = 8, className }: SweepProps) {
  return (
    <span
      aria-hidden="true"
      className={['ch-sweep', className].filter(Boolean).join(' ')}
      style={{ ['--ch-sweep-angle' as string]: `${angle}deg`, height }}
    />
  );
}
