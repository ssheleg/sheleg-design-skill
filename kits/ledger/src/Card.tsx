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
    <section className={['lg-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="lg-card__head">
          {title !== undefined && <h3 className="lg-card__title">{title}</h3>}
          {meta !== undefined && <span className="lg-card__meta">{meta}</span>}
        </div>
      )}
      <div className="lg-card__body">{children}</div>
    </section>
  );
}
