import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = hero claim (57→80px), 2 = section (48→64px), 3 = category (34→45px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['at-heading', `at-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
