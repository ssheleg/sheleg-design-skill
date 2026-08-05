import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row, set in mono: a commit, a date. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

/**
 * A lighter sheet on a hairline ring. It has **no hover state at all** — see
 * `Card.md`, and do not add one: the pack's reason is that a page built from
 * hairlines has nothing to lift off.
 */
export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['fn-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="fn-card__head">
          {title !== undefined && <h3 className="fn-card__title">{title}</h3>}
          {meta !== undefined && <span className="fn-card__meta">{meta}</span>}
        </div>
      )}
      <div className="fn-card__body">{children}</div>
    </section>
  );
}
