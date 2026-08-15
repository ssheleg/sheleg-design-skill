import type { ReactNode } from 'react';

export interface KickerProps {
  children: ReactNode;
  /** `accent` is the default and the pack's motif; `muted` is for a second one nearby. */
  tone?: 'accent' | 'muted';
  className?: string;
}

export function Kicker({ children, tone = 'accent', className }: KickerProps) {
  return (
    <p className={['lg-kicker', `lg-kicker--${tone}`, className].filter(Boolean).join(' ')}>
      {children}
    </p>
  );
}
