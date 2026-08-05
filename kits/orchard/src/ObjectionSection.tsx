import type { ReactNode } from 'react';

export interface ObjectionSectionProps {
  /**
   * The reader's suspicion in the reader's own words — "Isn't this just an
   * expensive multivitamin?" — never the brand's benefit rewritten as a question.
   */
  objection: string;
  /** The answer, as a plain stack. `Card` per point; nothing decorated. */
  children: ReactNode;
  className?: string;
}

export function ObjectionSection({ objection, children, className }: ObjectionSectionProps) {
  return (
    <section className={['orch-objection', className].filter(Boolean).join(' ')}>
      <h2 className="orch-objection__heading">{objection}</h2>
      <div className="orch-objection__stack">{children}</div>
    </section>
  );
}
