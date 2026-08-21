import type { ReactNode } from 'react';

export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['or-stat', className].filter(Boolean).join(' ')}>
      <div className="or-stat__value">{value}</div>
      <div className="or-stat__label">{label}</div>
      {source && <div className="or-stat__source">{source}</div>}
    </div>
  );
}
