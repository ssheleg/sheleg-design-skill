import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** The quiet line beside the title: a dose, a cadence, a sample size. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['orch-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="orch-card__head">
          {title !== undefined && <h3 className="orch-card__title">{title}</h3>}
          {meta !== undefined && <span className="orch-card__meta">{meta}</span>}
        </div>
      )}
      <div className="orch-card__body">{children}</div>
    </section>
  );
}
