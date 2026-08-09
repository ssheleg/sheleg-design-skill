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
    <section className={['pr-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="pr-card__head">
          {title !== undefined && <h3 className="pr-card__title">{title}</h3>}
          {meta !== undefined && <span className="pr-card__meta">{meta}</span>}
        </div>
      )}
      <div className="pr-card__body">{children}</div>
    </section>
  );
}
