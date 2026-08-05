export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a sample, a window, a named study. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['el-stat', className].filter(Boolean).join(' ')}>
      <span className="el-stat__label">{label}</span>
      <span className="el-stat__value">{value}</span>
      {source !== undefined && <span className="el-stat__source">{source}</span>}
    </div>
  );
}
