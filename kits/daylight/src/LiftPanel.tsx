import type { ReactNode } from 'react';

export interface LiftPanelProps {
  children: ReactNode;
  className?: string;
}

export function LiftPanel({ children, className }: LiftPanelProps) {
  return <div className={['dy-lift', className].filter(Boolean).join(' ')}>{children}</div>;
}
