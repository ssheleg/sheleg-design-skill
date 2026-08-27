import type { ReactNode } from 'react';

export interface AnnotationProps {
  /** `accent` writes in --action; default writes in --ink-mute. */
  tone?: 'mute' | 'accent';
  children: ReactNode;
  className?: string;
}

export function Annotation({ tone = 'mute', children, className }: AnnotationProps) {
  return (
    <span
      className={['td-annotation', `td-annotation--${tone}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
