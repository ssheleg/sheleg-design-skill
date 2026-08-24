import type { ReactNode } from 'react';

export interface LabelProps {
  children: ReactNode;
  /** `chrome` is nav and button furniture; `eyebrow` opens a section. */
  role?: 'chrome' | 'eyebrow';
  className?: string;
}

/** Every label in this pack is the monospace. It is how a reader tells a control
 *  from a statement without reading either. */
export function Label({ children, role = 'chrome', className }: LabelProps) {
  return (
    <span className={['rl-label', `rl-label--${role}`, className].filter(Boolean).join(' ')}>
      {children}
    </span>
  );
}
