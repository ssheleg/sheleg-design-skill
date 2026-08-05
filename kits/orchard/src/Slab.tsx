import type { ReactNode } from 'react';

/** Oat explains, sage invites, cacao emphasises. */
export type SlabFill = 'oat' | 'sage' | 'cacao';

export interface SlabProps {
  fill?: SlabFill;
  children: ReactNode;
  className?: string;
}

export function Slab({ fill = 'oat', children, className }: SlabProps) {
  return (
    <section
      className={['orch-slab', `orch-slab--${fill}`, className].filter(Boolean).join(' ')}
    >
      <div className="orch-slab__inner">{children}</div>
    </section>
  );
}
