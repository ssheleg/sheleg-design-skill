import type { ReactNode } from 'react';

export interface SectionBadgeProps {
  /** 1–12. Each is a two-stop ramp with its own hand-picked label ink. */
  gradient?: number;
  children: ReactNode;
  className?: string;
}

/**
 * A label, never a control. It has no hover, no focus and no href — the entire
 * chromatic budget of this pack is spent on things that cannot be clicked.
 */
export function SectionBadge({ gradient = 1, children, className }: SectionBadgeProps) {
  const n = String(Math.min(12, Math.max(1, gradient))).padStart(2, '0');
  return (
    <span className={['pc-badge', `pc-badge--g${n}`, className].filter(Boolean).join(' ')}>
      {children}
    </span>
  );
}
