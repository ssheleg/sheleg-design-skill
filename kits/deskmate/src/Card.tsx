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
    <section className={['dm-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="dm-card__head">
          {title !== undefined && <h3 className="dm-card__title">{title}</h3>}
          {meta !== undefined && <span className="dm-card__meta">{meta}</span>}
        </div>
      )}
      <div className="dm-card__body">{children}</div>
    </section>
  );
}
