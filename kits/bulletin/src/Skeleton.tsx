export interface SkeletonProps {
  /** Match the real element: the skeleton is a placeholder, not a spinner. */
  lines?: number;
  radius?: 'control' | 'card';
  className?: string;
}

export function Skeleton({ lines = 3, radius = 'control', className }: SkeletonProps) {
  return (
    <div
      className={['bl-skel', `bl-skel--${radius}`, className].filter(Boolean).join(' ')}
      aria-hidden="true"
    >
      {Array.from({ length: lines }, (_, i) => (
        <span className="bl-skel__line" key={i} />
      ))}
    </div>
  );
}
