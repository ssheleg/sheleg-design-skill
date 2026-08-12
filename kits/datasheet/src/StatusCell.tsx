import type { ReactNode } from 'react';

export type Reading = 'success' | 'danger' | 'warning' | 'info';

export interface StatusCellProps {
  label: string;
  /** The verdict, written out. The tint never carries the meaning on its own. */
  children: ReactNode;
  reading: Reading;
  className?: string;
}

export function StatusCell({ label, children, reading, className }: StatusCellProps) {
  return (
    <div
      className={['ds-cell', 'ds-cell--status', `ds-cell--${reading}`, className]
        .filter(Boolean)
        .join(' ')}
    >
      <span className="ds-cell__label">{label}</span>
      <span className="ds-cell__value">{children}</span>
    </div>
  );
}
