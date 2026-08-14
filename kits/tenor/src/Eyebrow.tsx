import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  /** A two-digit ordinal rendered before the label: 01, 02, 03. */
  index?: string;
  className?: string;
}

/**
 * The mono micro-label: 10-11px, uppercase, tracked .12em, --ink-soft. It names
 * a section or numbers a step without adding a heading level, which is why it is
 * a <p> and not an <h2>.
 */
export function Eyebrow({ children, index, className }: EyebrowProps) {
  return (
    <p className={['tn-eyebrow', className].filter(Boolean).join(' ')}>
      {index !== undefined && <span className="tn-eyebrow__index">{index}</span>}
      {children}
    </p>
  );
}
