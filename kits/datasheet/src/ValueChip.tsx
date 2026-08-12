import type { ReactNode } from 'react';
import type { Reading } from './StatusCell.js';

export interface ValueChipProps {
  children: ReactNode;
  reading?: Reading;
  className?: string;
}

export function ValueChip({ children, reading, className }: ValueChipProps) {
  return (
    <span
      className={['ds-vchip', reading ? `ds-vchip--${reading}` : undefined, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
