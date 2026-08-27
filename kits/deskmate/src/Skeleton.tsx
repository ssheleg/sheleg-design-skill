export interface SkeletonProps {
  /** How many bars stand in for the rows that have not arrived. */
  rows?: number;
  /** The shape the bars are standing in for, so the radius matches it. */
  shape?: 'row' | 'chip' | 'card';
  className?: string;
}

export function Skeleton({ rows = 3, shape = 'row', className }: SkeletonProps) {
  return (
    <div
      className={['dm-skel', `dm-skel--${shape}`, className].filter(Boolean).join(' ')}
      aria-hidden="true"
    >
      {Array.from({ length: rows }, (_, i) => (
        <span className="dm-skel__bar" key={i} />
      ))}
    </div>
  );
}
