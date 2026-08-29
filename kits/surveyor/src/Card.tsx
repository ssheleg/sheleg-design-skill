import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a count, an id, a timestamp. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['sv-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="sv-card__head">
          {title !== undefined && <h3 className="sv-card__title">{title}</h3>}
          {meta !== undefined && <span className="sv-card__meta">{meta}</span>}
        </div>
      )}
      <div className="sv-card__body">{children}</div>
    </section>
  );
}
