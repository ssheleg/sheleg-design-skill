import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = page title (28px), 2 = section (20px), 3 = card title (15px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = (['h1', 'h2', 'h3'] as const)[level - 1];
  return <Tag className={['pb-h', `pb-h--${level}`, className].filter(Boolean).join(' ')}>{children}</Tag>;
}
