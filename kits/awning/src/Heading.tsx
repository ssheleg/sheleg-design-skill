import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = page title (`dsp`), 2 = section (`t1`), 3 = card title (`t3`). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag className={['aw-h', `aw-h--${level}`, className].filter(Boolean).join(' ')}>
      {children}
    </Tag>
  );
}
