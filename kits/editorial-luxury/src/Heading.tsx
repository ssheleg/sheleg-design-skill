import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = the display headline, 2 = a section title, 3 = a card or block title. */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['el-heading', `el-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
