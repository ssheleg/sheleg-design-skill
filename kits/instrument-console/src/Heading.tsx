import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = hero (clamped to a 5.25rem ceiling), 2 = section, 3 = panel title. */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = `h${level}` as 'h1' | 'h2' | 'h3';
  return (
    <Tag
      className={['ic-heading', `ic-heading--${level}`, className].filter(Boolean).join(' ')}
    >
      {children}
    </Tag>
  );
}
