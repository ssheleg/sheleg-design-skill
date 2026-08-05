import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned furniture on the title row: a date, a stage, a segment. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

/**
 * A bounded region of a slide. It has no hover state, on purpose — see Card.md.
 */
export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['br-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="br-card__head">
          {title !== undefined && <h3 className="br-card__title">{title}</h3>}
          {meta !== undefined && <span className="br-card__meta">{meta}</span>}
        </div>
      )}
      <div className="br-card__body">{children}</div>
    </section>
  );
}
