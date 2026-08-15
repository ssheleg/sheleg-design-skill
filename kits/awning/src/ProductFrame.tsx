import type { ReactNode } from 'react';

export interface ProductFrameProps {
  /** Describe what the shot shows — this is the accessible name, not decoration. */
  label: string;
  children: ReactNode;
  className?: string;
}

export function ProductFrame({ label, children, className }: ProductFrameProps) {
  return (
    <figure
      className={['aw-frame', className].filter(Boolean).join(' ')}
      role="img"
      aria-label={label}
    >
      {children}
    </figure>
  );
}
