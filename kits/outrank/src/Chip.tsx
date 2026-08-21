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
      className={['or-chip', `or-chip--${tone}`, className].filter(Boolean).join(' ')}
      aria-pressed={selected || undefined}
    >
      {children}
    </span>
  );
}
