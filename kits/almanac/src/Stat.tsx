export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a report. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['al-stat', className].filter(Boolean).join(' ')}>
      <span className="al-stat__label">{label}</span>
      <span className="al-stat__value">{value}</span>
      {source !== undefined && <span className="al-stat__source">{source}</span>}
    </div>
  );
}
