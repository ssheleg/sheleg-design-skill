import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = `--t-h1`, 2 = `--t-h2` section heading, 3 = `--t-h3` sub-head. */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

/**
 * The monospaced display face at the pack's three section sizes, all tracking
 * at the one authored `-0.02em`.
 *
 * `text-wrap: balance` matters more here than in a proportional pack: every
 * glyph is the same width, so a ragged last line is visible as a measured gap
 * rather than as ordinary rag.
 */
export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['cy-heading', `cy-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
