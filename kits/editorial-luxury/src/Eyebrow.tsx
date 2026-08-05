import type { ReactNode } from 'react';

export interface EyebrowProps {
  children: ReactNode;
  /** `accent` puts the kicker in sage — for the one label that is the signal. */
  tone?: 'neutral' | 'accent';
  className?: string;
}

export function Eyebrow({ children, tone = 'neutral', className }: EyebrowProps) {
  return (
    <span
      className={[
        'el-eyebrow',
        tone === 'accent' ? 'el-eyebrow--accent' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
