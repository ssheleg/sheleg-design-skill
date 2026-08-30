export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a platform, a window, a prompt set. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['ch-stat', className].filter(Boolean).join(' ')}>
      <div className="ch-stat__value">{value}</div>
      <div className="ch-stat__label">{label}</div>
      {source && <div className="ch-stat__source">{source}</div>}
    </div>
  );
}
