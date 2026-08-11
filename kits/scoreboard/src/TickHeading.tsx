import type { ReactNode } from 'react';

export interface TickHeadingProps {
  /** 2 = section, 3 = sub-head. A tick never precedes the page title. */
  level?: 2 | 3;
  children: ReactNode;
  className?: string;
}

/**
 * A 3x18px accent bar, a 10px gap, then the heading. The pack's most
 * recognisable motif and the one place the raw accent is correct at full
 * strength — it is a mark, not a word.
 */
export function TickHeading({ level = 2, children, className }: TickHeadingProps) {
  const Tag = `h${level}` as 'h2' | 'h3';
  return (
    <div className={['sb-tick-heading', className].filter(Boolean).join(' ')}>
      <span className="sb-tick-heading__tick" aria-hidden="true" />
      <Tag className={['sb-heading', `sb-heading--${level}`].join(' ')}>{children}</Tag>
    </div>
  );
}
