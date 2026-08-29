import type { ReactNode } from 'react';

export interface DeltaProps {
  /** The arrow is the second encoding; the number beside it is the first. */
  direction: 'up' | 'down';
  children: ReactNode;
  className?: string;
}

export function Delta({ direction, children, className }: DeltaProps) {
  return (
    <span
      className={['sv-delta', `sv-delta--${direction}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
      <span aria-hidden="true" className="sv-delta__arrow">
        {direction === 'up' ? '\u2191' : '\u2193'}
      </span>
    </span>
  );
}
