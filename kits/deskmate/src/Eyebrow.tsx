import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  /** `dusk` swaps the wash for the on-dusk pair; the shape never changes. */
  surface?: 'light' | 'dusk';
  className?: string;
}

export function Eyebrow({ children, surface = 'light', className }: EyebrowProps) {
  return (
    <span
      className={['dm-eyebrow', `dm-eyebrow--${surface}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
