import type { ReactNode } from 'react';

export interface BandProps {
  /** One flat pastel per act. The pack forbids a gradient here. */
  tone?: 'paper' | 'peach' | 'sky' | 'lilac' | 'lemon' | 'ink';
  children: ReactNode;
  className?: string;
}

export function Band({ tone = 'paper', children, className }: BandProps) {
  return (
    <section
      className={['bl-band', `bl-band--${tone}`, className].filter(Boolean).join(' ')}
      data-surface={tone === 'ink' ? 'ink' : undefined}
    >
      <div className="bl-band__inner">{children}</div>
    </section>
  );
}
