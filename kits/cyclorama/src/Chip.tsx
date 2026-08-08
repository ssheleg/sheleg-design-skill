import type { ReactNode } from 'react';

export interface ChipProps {
  children: ReactNode;
  selected?: boolean;
  tone?: 'neutral' | 'accent';
  className?: string;
}

/**
 * Ink at 6% on `--radius-sm` with `4px 8px` of padding — the small radius is
 * not a taste call, it is arithmetic: a chip sits inside a 16px container with
 * 12px of padding, and 16 − 12 = 4.
 *
 * `tone="accent"` fills with `--accent` and sets `--on-accent` as the label at
 * 7.46:1. It is never accent-coloured *text* on the field; that measures 1.7:1
 * and the pack bans it.
 */
export function Chip({ children, selected = false, tone = 'neutral', className }: ChipProps) {
  return (
    <span
      className={[
        'cy-chip',
        `cy-chip--${tone}`,
        selected ? 'cy-chip--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
