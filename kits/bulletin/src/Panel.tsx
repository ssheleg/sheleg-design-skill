import type { ReactNode } from 'react';

export interface PanelProps {
  /** The page's densest claim. One per page — the pack says so. */
  children: ReactNode;
  className?: string;
}

export function Panel({ children, className }: PanelProps) {
  return <div className={['bl-panel', className].filter(Boolean).join(' ')}>{children}</div>;
}
