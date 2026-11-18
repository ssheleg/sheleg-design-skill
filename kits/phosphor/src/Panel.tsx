import type { ReactNode } from 'react';

export interface PanelProps {
  /** The panel number, set in the phosphor tag. */
  number?: string;
  title: string;
  /** Full-width panel instead of the 760px one. */
  wide?: boolean;
  children: ReactNode;
  className?: string;
}

export function Panel({ number, title, wide = false, children, className }: PanelProps) {
  return (
    <article className={['ph-panel', wide ? 'ph-panel--wide' : null, className].filter(Boolean).join(' ')}>
      <header className="ph-panel__title">
        {number && <span className="ph-panel__tag">{number}</span>}
        <h2 className="ph-panel__heading">{title}</h2>
      </header>
      {children}
    </article>
  );
}

export interface CellsProps {
  items: string[];
  className?: string;
}

/** Instrument cells inside a panel; the grid answers to the panel's width. */
export function Cells({ items, className }: CellsProps) {
  return (
    <ul className={['ph-cells', className].filter(Boolean).join(' ')}>
      {items.map((item) => (
        <li key={item} className="ph-cell">
          {item}
        </li>
      ))}
    </ul>
  );
}
