import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: an index, an id, a timestamp. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['ic-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="ic-card__head">
          {title !== undefined && <h3 className="ic-card__title">{title}</h3>}
          {meta !== undefined && <span className="ic-card__meta">{meta}</span>}
        </div>
      )}
      <div className="ic-card__body">{children}</div>
    </section>
  );
}
