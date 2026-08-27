import type { ReactNode } from 'react';

export interface EmptyProps {
  title: string;
  /** One sentence saying what would fill this, or what to change. */
  detail?: string;
  action?: ReactNode;
  className?: string;
}

export function Empty({ title, detail, action, className }: EmptyProps) {
  return (
    <div className={['dm-empty', className].filter(Boolean).join(' ')}>
      <p className="dm-empty__title">{title}</p>
      {detail !== undefined && <p className="dm-empty__detail">{detail}</p>}
      {action !== undefined && <div className="dm-empty__action">{action}</div>}
    </div>
  );
}
