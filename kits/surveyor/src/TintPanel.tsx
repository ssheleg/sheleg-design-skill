import type { ReactNode } from 'react';

export interface TintPanelProps {
  /** Tense as tint: `present` is mint (what ships), `future` is pink (what is
      coming), `cool` is the neutral grey step. */
  tone?: 'present' | 'future' | 'cool';
  children: ReactNode;
  className?: string;
}

export function TintPanel({ tone = 'present', children, className }: TintPanelProps) {
  return (
    <section className={['sv-panel', `sv-panel--${tone}`, className].filter(Boolean).join(' ')}>
      {children}
    </section>
  );
}
