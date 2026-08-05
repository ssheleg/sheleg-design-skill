import type { ReactNode } from 'react';

export interface GlassNavProps {
  children: ReactNode;
  /** The landmark's accessible name — "Main", "Product". */
  label?: string;
  className?: string;
}

export function GlassNav({ children, label, className }: GlassNavProps) {
  return (
    <nav
      className={['orch-glassnav', className].filter(Boolean).join(' ')}
      aria-label={label}
    >
      {children}
    </nav>
  );
}
