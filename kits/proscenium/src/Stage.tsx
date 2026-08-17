import type { ReactNode } from 'react';

export interface StageProps {
  children: ReactNode;
  className?: string;
}

/** The one dark act. One per page — see Stage.md. */
export function Stage({ children, className }: StageProps) {
  return (
    <section className={['ps-stage', className].filter(Boolean).join(' ')}>
      <div className="ps-stage__inner">{children}</div>
    </section>
  );
}
