export interface SkeletonProps {
  /** Matches the real element's height, so the layout does not jump on load. */
  height?: number;
  /** A CSS width — a percentage for text lines, a length for blocks. */
  width?: string;
  className?: string;
}

export function Skeleton({ height = 14, width = '100%', className }: SkeletonProps) {
  return (
    <span
      className={['rt-skeleton', className].filter(Boolean).join(' ')}
      style={{ height: `${height}px`, width }}
      aria-hidden="true"
    />
  );
}
