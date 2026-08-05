import type { ReactNode } from 'react';

export interface CardProps {
  title?: string;
  /** Right-aligned metadata on the title row: a date, an issue number, a byline. */
  meta?: string;
  children: ReactNode;
  className?: string;
}

export function Card({ title, meta, children, className }: CardProps) {
  const head = title !== undefined || meta !== undefined;
  return (
    <section className={['el-card', className].filter(Boolean).join(' ')}>
      {head && (
        <div className="el-card__head">
          {title !== undefined && <h3 className="el-card__title">{title}</h3>}
          {meta !== undefined && <span className="el-card__meta">{meta}</span>}
        </div>
      )}
      <div className="el-card__body">{children}</div>
    </section>
  );
}
