import type { ReactNode } from 'react';

export interface BubbleProps {
  /** The quoted question. Set in the display face — that is the point. */
  question: string;
  /** Where it was asked: a platform name, a subreddit, a date. */
  source?: string;
  /** `paper` is a stranger's card; `slab` is the answering side of a pair. */
  surface?: 'paper' | 'slab';
  /** Mirrors the cut corner for the answering side and for RTL. */
  mirrored?: boolean;
  children?: ReactNode;
  className?: string;
}

export function Bubble({
  question,
  source,
  surface = 'paper',
  mirrored = false,
  children,
  className,
}: BubbleProps) {
  return (
    <div
      className={[
        'ch-bubble',
        `ch-bubble--${surface}`,
        mirrored ? 'ch-bubble--mirrored' : null,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <p className="ch-bubble__q">{question}</p>
      {source && <p className="ch-bubble__src">{source}</p>}
      {children}
    </div>
  );
}
