import type { ReactNode } from 'react';

export interface EmptyProps {
  title: string;
  body?: string;
  action?: ReactNode;
  className?: string;
}

export function Empty({ title, body, action, className }: EmptyProps) {
  return (
    <div className={['ch-empty', className].filter(Boolean).join(' ')}>
      <span aria-hidden="true" className="ch-empty__bubble" />
      <p className="ch-empty__title">{title}</p>
      {body && <p className="ch-empty__body">{body}</p>}
      {action && <div className="ch-empty__action">{action}</div>}
    </div>
  );
}
