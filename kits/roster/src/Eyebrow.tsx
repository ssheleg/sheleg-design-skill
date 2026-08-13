import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  className?: string;
}

/**
 * The small tracked line above a section head. It is a `<p>`, never an `<h2>`: the
 * reference marks all sixteen of its eyebrows as level-two headings and hides its
 * real `h1`, so its document outline says "eyebrow" where the page says "section
 * head". This pack keeps the outline and the page in agreement.
 */
export function Eyebrow({ children, className }: EyebrowProps) {
  return <p className={['ro-eyebrow', className].filter(Boolean).join(' ')}>{children}</p>;
}
