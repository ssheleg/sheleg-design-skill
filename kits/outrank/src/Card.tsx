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
    <section className={['or-card', className].filter(Boolean).join(' ')}>
      {(title || meta) && (
        <header className="or-card__head">
          {title && <h3 className="or-heading--3">{title}</h3>}
          {meta && <span className="or-card__meta">{meta}</span>}
        </header>
      )}
      {children}
    </section>
  );
}
