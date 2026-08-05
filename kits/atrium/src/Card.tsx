import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** The quiet second line on the title row: a date, a source, a duration. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['at-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="at-card__head">
          {title !== undefined && <h3 className="at-card__title">{title}</h3>}
          {meta !== undefined && <span className="at-card__meta">{meta}</span>}
        </div>
      )}
      <div className="at-card__body">{children}</div>
    </section>
  );
}
