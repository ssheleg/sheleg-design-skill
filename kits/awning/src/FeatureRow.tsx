import type { ReactNode } from 'react';

export interface FeatureRowProps {
  title: string;
  children: ReactNode;
  /** A short mono index — `01`, `02` — when the row belongs to an ordered set. */
  index?: string;
  className?: string;
}

export function FeatureRow({ title, children, index, className }: FeatureRowProps) {
  return (
    <div className={['aw-feature', className].filter(Boolean).join(' ')}>
      {index ? <span className="aw-feature__index">{index}</span> : null}
      <div className="aw-feature__body">
        <span className="aw-feature__title">{title}</span>
        <p className="aw-feature__text">{children}</p>
      </div>
    </div>
  );
}
