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
    <section className={['bl-card', className].filter(Boolean).join(' ')}>
      {(title || meta) && (
        <header className="bl-card__head">
          {title && <h3 className="bl-heading--3">{title}</h3>}
          {meta && <span className="bl-card__meta">{meta}</span>}
        </header>
      )}
      {children}
    </section>
  );
}
