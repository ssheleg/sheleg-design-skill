export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['sv-stat', className].filter(Boolean).join(' ')}>
      <span className="sv-stat__label">{label}</span>
      <span className="sv-stat__value">{value}</span>
      {source !== undefined && <span className="sv-stat__source">{source}</span>}
    </div>
  );
}
