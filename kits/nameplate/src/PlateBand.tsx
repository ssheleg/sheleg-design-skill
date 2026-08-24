import type { ReactNode } from 'react';

export interface PlateBandProps {
  /** The plates. They wrap; they never scroll — the count is the argument. */
  children: ReactNode;
  /** The field the band stands on. `slab` is the pack's cool near-white. */
  field?: 'slab' | 'page';
  className?: string;
}

export function PlateBand({ children, field = 'slab', className }: PlateBandProps) {
  return (
    <div
      className={['np-band', `np-band--${field}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </div>
  );
}
