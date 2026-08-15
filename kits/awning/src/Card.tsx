import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a count, an id, a timestamp. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  return (
    <div className={['aw-card', className].filter(Boolean).join(' ')}>
      {title ? (
        <div className="aw-card__head">
          <span className="aw-card__title">{title}</span>
          {meta ? <span className="aw-card__meta">{meta}</span> : null}
        </div>
      ) : null}
      {children}
    </div>
  );
}
