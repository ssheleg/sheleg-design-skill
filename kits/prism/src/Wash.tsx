import type { ReactNode } from 'react';

export interface WashProps {
  children?: ReactNode;
  className?: string;
}

/**
 * The prism: one static gradient across the first viewport, four stops at
 * 100deg, with a **hard bottom edge**.
 *
 * The edge is the argument. Any page can put a pastel gradient behind a hero;
 * this one bounds it — the prettiness happens once, and underneath it the page
 * is plain white with monospaced type and numbers on it.
 *
 * It never animates. No hue rotation, no pan, no scroll-linked shift: animating
 * the wash is the one change that would turn this pack into `cyclorama`, badly.
 * The four stops sit above 18:1 against `--ink`, so a headline over it needs no
 * scrim.
 */
export function Wash({ children, className }: WashProps) {
  return <div className={['pr-wash', className].filter(Boolean).join(' ')}>{children}</div>;
}
