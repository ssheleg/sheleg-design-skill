export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a report. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['rt-stat', className].filter(Boolean).join(' ')}>
      <span className="rt-stat__label">{label}</span>
      <span className="rt-stat__value">{value}</span>
      {source !== undefined && <span className="rt-stat__source">{source}</span>}
    </div>
  );
}
