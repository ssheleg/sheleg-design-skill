import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  /** `micro` tracks +0.175em; `control` tracks +0.06em. They are not interchangeable. */
  register?: 'micro' | 'control';
  className?: string;
}

export function Eyebrow({ children, register = 'micro', className }: EyebrowProps) {
  return (
    <span
      className={['np-eyebrow', `np-eyebrow--${register}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
