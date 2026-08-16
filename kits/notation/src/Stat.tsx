export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a report. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['nt-stat', className].filter(Boolean).join(' ')}>
      <span className="nt-stat__label">{label}</span>
      <span className="nt-stat__value">{value}</span>
      {source !== undefined && <span className="nt-stat__source">{source}</span>}
    </div>
  );
}
