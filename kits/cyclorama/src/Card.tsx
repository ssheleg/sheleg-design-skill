import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a count, an id, a timestamp. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

/**
 * The one opaque surface in this pack — `--surface`, `--radius-lg`, 32px of
 * padding, no border and no shadow, because there are no shadows anywhere in
 * this system.
 *
 * Use it where content must stop competing with the cycling field. Everywhere
 * else the field simply shows: a card placed for decoration puts an opaque
 * rectangle over the pack's signature and switches it off locally.
 */
export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['cy-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="cy-card__head">
          {title !== undefined && <h3 className="cy-card__title">{title}</h3>}
          {meta !== undefined && <span className="cy-card__meta">{meta}</span>}
        </div>
      )}
      <div className="cy-card__body">{children}</div>
    </section>
  );
}
