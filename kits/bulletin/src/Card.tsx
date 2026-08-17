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
    <section className={['bl-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="bl-card__head">
          {title !== undefined && <h3 className="bl-card__title">{title}</h3>}
          {meta !== undefined && <span className="bl-card__meta">{meta}</span>}
        </div>
      )}
      <div className="bl-card__body">{children}</div>
    </section>
  );
}
