import type { ReactNode } from 'react';

export interface ChipProps {
  children: ReactNode;
  selected?: boolean;
  tone?: 'neutral' | 'accent';
  className?: string;
}

export function Chip({ children, selected = false, tone = 'neutral', className }: ChipProps) {
  return (
    <span
      className={[
        'ro-chip',
        `ro-chip--${tone}`,
        selected ? 'ro-chip--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
