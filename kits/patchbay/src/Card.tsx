import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a count, an id, a timestamp. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  return (
    <section className={['pb-card', className].filter(Boolean).join(' ')}>
      {(title || meta) && (
        <header className="pb-card__head">
          {title && <h3 className="pb-card__title">{title}</h3>}
          {meta && <span className="pb-card__meta">{meta}</span>}
        </header>
      )}
      {children}
    </section>
  );
}
