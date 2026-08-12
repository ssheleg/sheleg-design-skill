import type { ReactNode } from 'react';

export interface MonoBadgeProps {
  children: ReactNode;
  className?: string;
}

export function MonoBadge({ children, className }: MonoBadgeProps) {
  return (
    <span className={['ds-badge', className].filter(Boolean).join(' ')}>{children}</span>
  );
}
