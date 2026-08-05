export interface StatProps {
  value: string;
  label: string;
  /**
   * Where the figure comes from. Optional because the spine says so; in this
   * pack an unsourced number is a ban, so fill it.
   */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['at-stat', className].filter(Boolean).join(' ')}>
      <span className="at-stat__value">{value}</span>
      <span className="at-stat__label">{label}</span>
      {source !== undefined && <span className="at-stat__source">{source}</span>}
    </div>
  );
}
