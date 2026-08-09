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
    <section className={['bp-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="bp-card__head">
          {title !== undefined && <h3 className="bp-card__title">{title}</h3>}
          {meta !== undefined && <span className="bp-card__meta">{meta}</span>}
        </div>
      )}
      <div className="bp-card__body">{children}</div>
    </section>
  );
}
