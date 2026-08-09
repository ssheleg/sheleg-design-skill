import type { ReactNode } from 'react';

export interface DataRowProps {
  selected?: boolean;
  onSelect?: () => void;
  children: ReactNode;
  className?: string;
}

/**
 * A row inside a specimen. Tints to `--accent-wash` on hover and takes a 2px
 * `--accent` left edge when selected.
 *
 * Rows do not lift. There is no shadow inside a specimen to lift into, and a
 * row that rises off a table is the clearest signal that a page was built by
 * someone who had not used the product.
 */
export function DataRow({ selected = false, onSelect, children, className }: DataRowProps) {
  return (
    <div
      className={['sw-row', selected ? 'sw-row--selected' : undefined, className]
        .filter(Boolean)
        .join(' ')}
      onClick={onSelect}
      role={onSelect ? 'button' : undefined}
      tabIndex={onSelect ? 0 : undefined}
    >
      {children}
    </div>
  );
}
