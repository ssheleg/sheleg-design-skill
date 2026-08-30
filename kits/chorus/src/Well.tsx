import type { ReactNode } from 'react';

export interface WellProps {
  /** `paper` holds an illustration; `product` holds a dark app screen. */
  tone?: 'paper' | 'product';
  children: ReactNode;
  className?: string;
}

export function Well({ tone = 'paper', children, className }: WellProps) {
  return (
    <div className={['ch-well', `ch-well--${tone}`, className].filter(Boolean).join(' ')}>
      {children}
    </div>
  );
}
