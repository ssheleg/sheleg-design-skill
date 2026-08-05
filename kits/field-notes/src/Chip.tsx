import type { ReactNode } from 'react';

export interface ChipProps {
  children: ReactNode;
  selected?: boolean;
  tone?: 'neutral' | 'accent';
  className?: string;
}

/**
 * The filter atom: `--surface` on a hairline, rust wash behind a rust border
 * when selected. Exactly one chip in a rail is selected at a time — the pack
 * says so, and a rail with two is a set of toggles wearing chip clothes.
 */
export function Chip({ children, selected = false, tone = 'neutral', className }: ChipProps) {
  return (
    <span
      className={[
        'fn-chip',
        `fn-chip--${tone}`,
        selected ? 'fn-chip--selected' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
