import type { ReactNode } from 'react';

export interface TaggedBoxProps {
  tag: string;
  children: ReactNode;
  className?: string;
}

export function TaggedBox({ tag, children, className }: TaggedBoxProps) {
  return (
    <div className={['al-tagged', className].filter(Boolean).join(' ')}>
      <span className="al-tagged__tag">{tag}</span>
      {children}
    </div>
  );
}
