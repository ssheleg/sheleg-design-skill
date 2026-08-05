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
        'br-chip',
        `br-chip--${tone}`,
        selected ? 'br-chip--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
