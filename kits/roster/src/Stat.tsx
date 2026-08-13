export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['ro-stat', className].filter(Boolean).join(' ')}>
      <span className="ro-stat__label">{label}</span>
      <span className="ro-stat__value">{value}</span>
      {source !== undefined && <span className="ro-stat__source">{source}</span>}
    </div>
  );
}
