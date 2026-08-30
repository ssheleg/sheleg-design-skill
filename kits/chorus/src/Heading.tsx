import type { ReactNode } from 'react';

export interface HeadingProps {
  /** 1 = display (56px, Outfit), 2 = section (44px, Inter), 3 = card head (18px). */
  level?: 1 | 2 | 3;
  children: ReactNode;
  className?: string;
}

export function Heading({ level = 2, children, className }: HeadingProps) {
  const Tag = (['h1', 'h2', 'h3'] as const)[level - 1];
  return (
    <Tag className={['ch-h', `ch-h--${level}`, className].filter(Boolean).join(' ')}>
      {children}
    </Tag>
  );
}
