export interface SkeletonProps {
  /** Bars to draw, in the shape of the content that is coming. */
  lines?: number;
  /** Widths as CSS lengths or percentages, cycled across the lines. */
  widths?: string[];
  className?: string;
}

export function Skeleton({ lines = 3, widths = ['100%', '84%', '62%'], className }: SkeletonProps) {
  return (
    <div
      className={['ch-skel', className].filter(Boolean).join(' ')}
      role="status"
      aria-busy="true"
      aria-live="polite"
    >
      {Array.from({ length: lines }, (_, i) => (
        <span
          key={i}
          className="ch-skel__bar"
          style={{ width: widths[i % widths.length] }}
        />
      ))}
      <span className="ch-skel__sr">Loading</span>
    </div>
  );
}
