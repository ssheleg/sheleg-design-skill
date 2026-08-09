import type { ReactNode } from 'react';

export interface ColumnHeaderProps {
  /** A 14px glyph before the label — what makes a table read as an application. */
  icon?: ReactNode;
  sorted?: 'asc' | 'desc';
  onSort?: () => void;
  children: ReactNode;
  className?: string;
}

/**
 * A column header inside a specimen: `--ink-soft` at 12px/500, a 14px icon
 * ahead of the label, a `1px --line` bottom rule.
 *
 * The icon is not decoration. A header row with icons reads as a real
 * application; the same row without them reads as a styled `<table>`, and the
 * specimen stops being evidence.
 */
export function ColumnHeader({ icon, sorted, onSort, children, className }: ColumnHeaderProps) {
  return (
    <div
      className={['sw-col', sorted ? `sw-col--${sorted}` : undefined, className]
        .filter(Boolean)
        .join(' ')}
      onClick={onSort}
      role={onSort ? 'columnheader' : undefined}
    >
      {icon !== undefined && <span className="sw-col__icon" aria-hidden="true">{icon}</span>}
      <span className="sw-col__label">{children}</span>
    </div>
  );
}
