import type { ReactNode } from 'react';

export interface MarkProps {
  /** The glyph. An icon, never a word — the hue clears only the non-text floor. */
  children: ReactNode;
  /** Decorative variety across a grid, 1–5, or the neutral. It carries no meaning:
   *  the set does not separate from itself, so nothing may depend on telling two
   *  marks apart. The icon and the label say which feature this is. */
  tone?: 1 | 2 | 3 | 4 | 5 | 'neutral';
  /** Accessible name for the tile, since the glyph inside is decorative. */
  label?: string;
  className?: string;
}

export function Mark({ children, tone = 1, label, className }: MarkProps) {
  return (
    <span
      className={['np-mark', `np-mark--${tone}`, className].filter(Boolean).join(' ')}
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={label ? undefined : true}
    >
      {children}
    </span>
  );
}
