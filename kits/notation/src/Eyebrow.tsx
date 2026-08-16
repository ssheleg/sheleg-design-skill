import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  className?: string;
}

export function Eyebrow({ children, className }: EyebrowProps) {
  return <span className={['nt-eyebrow', className].filter(Boolean).join(' ')}>{children}</span>;
}
