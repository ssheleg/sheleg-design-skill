import type { ReactNode } from 'react';

export interface FrameProps {
  children: ReactNode;
  className?: string;
}

/** The one object per screen allowed to wear --shadow-frame. */
export function Frame({ children, className }: FrameProps) {
  return (
    <figure className={['np-frame', className].filter(Boolean).join(' ')}>
      {children}
    </figure>
  );
}
