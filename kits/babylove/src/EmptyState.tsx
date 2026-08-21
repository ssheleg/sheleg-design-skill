import type { ReactNode } from 'react';

export interface EmptyStateProps {
  /** What is not here — stated as the thing, not as an apology. */
  title: string;
  /** The one action that would fill it, if there is one. */
  action?: ReactNode;
  className?: string;
}

export function EmptyState({ title, action, className }: EmptyStateProps) {
  return (
    <div className={['bl-empty', className].filter(Boolean).join(' ')}>
      <p className="bl-heading--3">{title}</p>
      {action}
    </div>
  );
}
