import type { ReactNode } from 'react';

export interface MicroProps {
  children: ReactNode;
  /** `caps` is the +0.18em register; `tight` the +0.14em one. They are both measured. */
  register?: 'caps' | 'tight';
  className?: string;
}

/** 11px uppercase, tracked open. The pack's most repeated object. */
export function Micro({ children, register = 'caps', className }: MicroProps) {
  return (
    <span className={['ok-micro', `ok-micro--${register}`, className].filter(Boolean).join(' ')}>
      {children}
    </span>
  );
}
