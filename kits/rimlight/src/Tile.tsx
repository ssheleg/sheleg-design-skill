import type { ReactNode } from 'react';

export interface TileProps {
  children: ReactNode;
  /** Accessible name — the glyph inside is decorative. */
  label?: string;
  className?: string;
}

/** The 80px icon tile that opens a section. Never interactive. */
export function Tile({ children, label, className }: TileProps) {
  return (
    <span
      className={['rl-tile', className].filter(Boolean).join(' ')}
      role={label ? 'img' : undefined}
      aria-label={label}
      aria-hidden={label ? undefined : true}
    >
      {children}
    </span>
  );
}
