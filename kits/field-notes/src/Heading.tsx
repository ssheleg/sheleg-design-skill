import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = 44px, 2 = 40px section heading, 3 = 30px sub-head. */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

/**
 * The display face at the pack's three section sizes, all tracking at the one
 * authored `-0.025em`. Write the text as a claim — "The answer is a path, not a
 * vibe" — not as a label; the pack's headings are sentences that argue.
 */
export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['fn-heading', `fn-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
