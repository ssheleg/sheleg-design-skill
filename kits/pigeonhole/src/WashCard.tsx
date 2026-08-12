import type { ReactNode } from 'react';
import type { Category } from './CategoryChip.js';

export interface WashCardProps {
  /** The hue this card belongs to. Its wash and its shadow both come from here. */
  category: Category;
  title: string;
  children: ReactNode;
  className?: string;
}

/**
 * A feature card filled with its category's palest pair, whose shadow is mixed
 * toward its own hue rather than toward black — the detail most often dropped
 * when this look is copied, and the reason the page reads coloured while
 * remaining white.
 */
export function WashCard({ category, title, children, className }: WashCardProps) {
  return (
    <section
      className={['pg-wash', `pg-wash--${category}`, className].filter(Boolean).join(' ')}
    >
      <h3 className="pg-wash__title">{title}</h3>
      <div className="pg-wash__body">{children}</div>
    </section>
  );
}
