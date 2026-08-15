import type { ReactNode } from 'react';

export interface ChipProps {
  children: ReactNode;
  selected?: boolean;
  /** `accent` is the INK fill — this pack has no hue to tint a chip with. */
  tone?: 'neutral' | 'accent';
  className?: string;
}

export function Chip({ children, selected = false, tone = 'neutral', className }: ChipProps) {
  return (
    <span
      className={['aw-chip', `aw-chip--${tone}`, selected ? 'aw-chip--selected' : undefined, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
