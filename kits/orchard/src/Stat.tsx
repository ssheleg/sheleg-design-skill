export interface StatProps {
  value: string;
  label: string;
  /** The study, cohort or window the figure comes from. On a health page, omit it and the figure is a claim without its citation. */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['orch-stat', className].filter(Boolean).join(' ')}>
      <span className="orch-stat__value">{value}</span>
      <span className="orch-stat__label">{label}</span>
      {source !== undefined && <span className="orch-stat__source">{source}</span>}
    </div>
  );
}
