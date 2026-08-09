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
    <section className={['sw-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="sw-card__head">
          {title !== undefined && <h3 className="sw-card__title">{title}</h3>}
          {meta !== undefined && <span className="sw-card__meta">{meta}</span>}
        </div>
      )}
      <div className="sw-card__body">{children}</div>
    </section>
  );
}
