import type { ReactNode } from 'react';

export interface EmptyProps {
  /** One line in --ink, 16px/500. */
  title: string;
  /** One sentence in --ink-mute. */
  hint?: string;
  /** One quiet control that starts the demo — this pack always has one to offer. */
  action?: ReactNode;
  className?: string;
}

export function Empty({ title, hint, action, className }: EmptyProps) {
  return (
    <div className={['sv-empty', className].filter(Boolean).join(' ')}>
      <span className="sv-empty__title">{title}</span>
      {hint !== undefined && <span className="sv-empty__hint">{hint}</span>}
      {action !== undefined && <span className="sv-empty__action">{action}</span>}
    </div>
  );
}
