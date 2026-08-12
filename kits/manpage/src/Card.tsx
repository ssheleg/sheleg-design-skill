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
    <section className={['mp-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="mp-card__head">
          {title !== undefined && <h3 className="mp-card__title">{title}</h3>}
          {meta !== undefined && <span className="mp-card__meta">{meta}</span>}
        </div>
      )}
      <div className="mp-card__body">{children}</div>
    </section>
  );
}
