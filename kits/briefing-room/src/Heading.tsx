import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = section divider (96px), 2 = slide label (64px), 3 = subhead (36px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag className={['br-heading', `br-heading--${level}`, className].filter(Boolean).join(' ')}>
      {children}
    </Tag>
  );
}
