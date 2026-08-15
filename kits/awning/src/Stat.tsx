export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a window, a plan, a region. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['aw-stat', className].filter(Boolean).join(' ')}>
      <span className="aw-stat__label">{label}</span>
      <span className="aw-stat__value">{value}</span>
      {source ? <span className="aw-stat__sub">{source}</span> : null}
    </div>
  );
}
