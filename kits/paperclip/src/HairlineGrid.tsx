import type { ReactNode } from 'react';

export interface HairlineGridProps {
  /** Columns at full width. Collapses to one inside a narrow container. */
  columns?: 2 | 3 | 4;
  children: ReactNode;
  className?: string;
}

/**
 * The gap is the rule: a 1px gap over a border-coloured background, clipped by
 * the container's own radius. No cell owns an edge, so no two cells can double
 * one, and the outer corners cut the cells rather than being fought by them.
 */
export function HairlineGrid({ columns = 3, children, className }: HairlineGridProps) {
  return (
    <div
      className={['pc-grid', `pc-grid--${columns}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </div>
  );
}
