export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a window, a channel, a query. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['ic-stat', className].filter(Boolean).join(' ')}>
      <span className="ic-stat__label">{label}</span>
      <span className="ic-stat__value">{value}</span>
      {source !== undefined && <span className="ic-stat__source">{source}</span>}
    </div>
  );
}
