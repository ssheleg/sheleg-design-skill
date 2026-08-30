import type { ReactNode } from 'react';

export interface SlabProps {
  children: ReactNode;
  className?: string;
}

export function Slab({ children, className }: SlabProps) {
  return (
    <section
      data-chorus-surface="slab"
      className={['ch-slab', className].filter(Boolean).join(' ')}
    >
      {children}
    </section>
  );
}
