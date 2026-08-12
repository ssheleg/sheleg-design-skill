import type { ReactNode } from 'react';

export interface CellProps {
  /** The 9px uppercase label. Always present: a value with no label is a number nobody can use. */
  label: string;
  children: ReactNode;
  /** Set for machine output — ids, IPs, hashes, timestamps. */
  mono?: boolean;
  className?: string;
}

export function Cell({ label, children, mono = false, className }: CellProps) {
  return (
    <div className={['ds-cell', className].filter(Boolean).join(' ')}>
      <span className="ds-cell__label">{label}</span>
      <span className={['ds-cell__value', mono ? 'ds-cell__value--mono' : undefined]
        .filter(Boolean)
        .join(' ')}>
        {children}
      </span>
    </div>
  );
}
