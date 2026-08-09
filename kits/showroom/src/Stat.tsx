export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['sw-stat', className].filter(Boolean).join(' ')}>
      <span className="sw-stat__label">{label}</span>
      <span className="sw-stat__value">{value}</span>
      {source !== undefined && <span className="sw-stat__source">{source}</span>}
    </div>
  );
}
