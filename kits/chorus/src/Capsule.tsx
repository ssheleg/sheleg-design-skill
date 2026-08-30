import type { ReactNode } from 'react';

export interface CapsuleProps {
  /** `outline` is the drawn one; the three fills are the measured set. */
  tone?: 'outline' | 'coral' | 'periwinkle' | 'parchment';
  /** Degrees of tilt. The reference scatters them; keep it under 12. */
  tilt?: number;
  children?: ReactNode;
  className?: string;
}

export function Capsule({ tone = 'outline', tilt = 0, children, className }: CapsuleProps) {
  return (
    <span
      className={['ch-capsule', `ch-capsule--${tone}`, className].filter(Boolean).join(' ')}
      style={{ transform: tilt ? `rotate(${tilt}deg)` : undefined }}
    >
      {children}
    </span>
  );
}
