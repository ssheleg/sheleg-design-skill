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
    <section className={['ps-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="ps-card__head">
          {title !== undefined && <h3 className="ps-card__title">{title}</h3>}
          {meta !== undefined && <span className="ps-card__meta">{meta}</span>}
        </div>
      )}
      <div className="ps-card__body">{children}</div>
    </section>
  );
}
