import type { ReactNode } from 'react';

export interface ChipProps {
  children: ReactNode;
  /** The cacao state. In a rail, exactly one chip carries it. */
  selected?: boolean;
  tone?: 'neutral' | 'accent';
  className?: string;
}

export function Chip({ children, selected = false, tone = 'neutral', className }: ChipProps) {
  return (
    <span
      className={[
        'orch-chip',
        `orch-chip--${tone}`,
        selected ? 'orch-chip--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
