import type { ReactNode } from 'react';

export interface MarkerProps {
  children: ReactNode;
  className?: string;
}

export function Marker({ children, className }: MarkerProps) {
  return (
    <mark className={['td-marker', className].filter(Boolean).join(' ')}>{children}</mark>
  );
}
