export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['ora-stat', className].filter(Boolean).join(' ')}>
      <span className="ora-stat__label">{label}</span>
      <span className="ora-stat__value">{value}</span>
      {source !== undefined && <span className="ora-stat__source">{source}</span>}
    </div>
  );
}
