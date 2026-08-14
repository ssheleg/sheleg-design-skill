import type { ReactNode } from 'react';

export interface LatticeProps {
  /** Columns at the widest size. Collapses to 2 then 1 by container width. */
  columns?: 2 | 3;
  children: ReactNode;
  className?: string;
}

/**
 * The container half of the lattice: it draws the top and left hairline, its
 * cells draw right and bottom. Sized against its own container rather than the
 * viewport, so a lattice dropped into a narrow column collapses correctly.
 */
export function Lattice({ columns = 3, children, className }: LatticeProps) {
  return (
    <div
      className={['tn-lattice', `tn-lattice--${columns}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </div>
  );
}
