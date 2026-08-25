import type { ReactNode } from 'react';

export interface GridProps {
  children: ReactNode;
  className?: string;
}

/** The dot field. It goes UNDER a section — never inside a panel, never as a border. */
export function Grid({ children, className }: GridProps) {
  return (
    <div className={['ok-grid', className].filter(Boolean).join(' ')} data-grid="">
      {children}
    </div>
  );
}
