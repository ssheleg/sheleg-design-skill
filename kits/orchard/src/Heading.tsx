import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = section heading (44px), 2 = slab heading (32px), 3 = sub-claim (28px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['orch-heading', `orch-heading--${level}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </Tag>
  );
}
