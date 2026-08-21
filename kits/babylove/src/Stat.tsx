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
    <div className={['bl-stat', className].filter(Boolean).join(' ')}>
      <div className="bl-stat__value">{value}</div>
      <div className="bl-stat__label">{label}</div>
      {source && <div className="bl-stat__source">{source}</div>}
    </div>
  );
}
