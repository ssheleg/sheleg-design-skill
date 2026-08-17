import type { ReactNode } from 'react';

export interface RailItem {
  /** The glyph, mark or one-letter fallback drawn inside the circle. */
  mark: ReactNode;
  /** Read out by assistive tech — the circle carries no text of its own. */
  name: string;
}

export interface RailProps {
  items: RailItem[];
  className?: string;
}

export function Rail({ items, className }: RailProps) {
  return (
    <ul className={['bl-rail', className].filter(Boolean).join(' ')}>
      {items.map((item) => (
        <li className="bl-rail__item" key={item.name}>
          <span className="bl-rail__mark" aria-hidden="true">
            {item.mark}
          </span>
          <span className="bl-rail__name">{item.name}</span>
        </li>
      ))}
    </ul>
  );
}
