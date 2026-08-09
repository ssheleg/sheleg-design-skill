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
    <section className={['mq-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="mq-card__head">
          {title !== undefined && <h3 className="mq-card__title">{title}</h3>}
          {meta !== undefined && <span className="mq-card__meta">{meta}</span>}
        </div>
      )}
      <div className="mq-card__body">{children}</div>
    </section>
  );
}
