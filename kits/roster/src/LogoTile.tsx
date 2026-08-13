import type { ReactNode } from 'react';

export interface LogoTileProps {
  /** One third-party mark: an `<img>` or an inline `<svg>`, never a letterform stand-in. */
  children: ReactNode;
  /** Whose mark this is. Required — a mark with no accessible name is decoration. */
  label: string;
  /** Scattered over the hero's pattern grid, rather than gridded in a band. */
  scattered?: boolean;
  className?: string;
}

/**
 * A square tile holding somebody else's mark. Greyscale at rest, full colour on
 * hover, and nothing moves: a mark that jumps reads as an advert.
 */
export function LogoTile({ children, label, scattered = false, className }: LogoTileProps) {
  return (
    <span
      className={['ro-tile', scattered && 'ro-tile--scattered', className]
        .filter(Boolean)
        .join(' ')}
      role="img"
      aria-label={label}
    >
      {children}
    </span>
  );
}
