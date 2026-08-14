import type { ReactNode } from 'react';

export interface SplitHeadlineProps {
  /** The premise. Rendered in --ink-faint. */
  muted: string;
  /** The claim. Rendered in --ink. */
  claim: string;
  /** 1 renders an <h1> at the hero slope, 2 an <h2> at the section slope. */
  level?: 1 | 2;
  className?: string;
}

/**
 * One sentence, two clauses, two values: the premise in --ink-faint and the
 * claim in --ink, so the reader parses the emphasis before reading a word.
 *
 * Use it once per page. Both halves are block-level spans inside a single
 * heading element, so the sentence stays one string to a screen reader.
 */
export function SplitHeadline({ muted, claim, level = 1, className }: SplitHeadlineProps) {
  const Tag = level === 1 ? 'h1' : 'h2';
  return (
    <Tag className={['tn-split', `tn-split--${level}`, className].filter(Boolean).join(' ')}>
      <span className="tn-split__muted">{muted}</span>
      <span className="tn-split__claim">{claim}</span>
    </Tag>
  );
}

export type SplitHeadlineChildren = ReactNode;
