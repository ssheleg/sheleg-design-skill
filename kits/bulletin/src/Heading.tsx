import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = hero (84px), 2 = section (48px), 3 = card title (20px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['bl-heading', `bl-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
