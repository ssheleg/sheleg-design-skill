import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a count, a window, a state. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['dy-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="dy-card__head">
          {title !== undefined && <h3 className="dy-card__title">{title}</h3>}
          {meta !== undefined && <span className="dy-card__meta">{meta}</span>}
        </div>
      )}
      <div className="dy-card__body">{children}</div>
    </section>
  );
}
