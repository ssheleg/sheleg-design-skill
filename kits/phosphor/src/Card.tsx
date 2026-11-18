import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a source, a count, a date. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  return (
    <div className={['ph-card', className].filter(Boolean).join(' ')}>
      {(title || meta) && (
        <div className="ph-card__head">
          {title && <h3 className="ph-card__title">{title}</h3>}
          {meta && <span className="ph-card__meta">{meta}</span>}
        </div>
      )}
      <div className="ph-card__body">{children}</div>
    </div>
  );
}
