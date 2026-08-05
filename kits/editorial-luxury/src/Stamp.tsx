import type { ReactNode } from 'react';

/**
 * `red` is the pack's negative and nothing else — the "without" column of a
 * comparison, a rejected verdict. `terra` is the rare editorial highlight.
 */
export type StampTone = 'accent' | 'terra' | 'red';

export interface StampProps {
  children: ReactNode;
  tone?: StampTone;
  className?: string;
}

export function Stamp({ children, tone = 'accent', className }: StampProps) {
  return (
    <span className={['el-stamp', `el-stamp--${tone}`, className].filter(Boolean).join(' ')}>
      {children}
    </span>
  );
}
