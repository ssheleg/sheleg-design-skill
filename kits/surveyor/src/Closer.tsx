import type { ReactNode } from 'react';

export interface CloserProps {
  /** The heading — white on the brand teal is legal at heading sizes only. */
  title: string;
  /** One line of support copy, kept at heading scale. */
  support?: string;
  /** One white outline control. */
  action: ReactNode;
  className?: string;
}

export function Closer({ title, support, action, className }: CloserProps) {
  return (
    <section className={['sv-closer', className].filter(Boolean).join(' ')}>
      <h2 className="sv-closer__title">{title}</h2>
      {support !== undefined && <p className="sv-closer__support">{support}</p>}
      <span className="sv-closer__action">{action}</span>
    </section>
  );
}
