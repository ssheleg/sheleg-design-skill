export interface StatProps {
  value: string;
  label: string;
  /**
   * Where the figure came from. Optional in the spine's API; in this pack it is
   * not optional in practice — see Stat.md, and prefer `SourcedNumber`.
   */
  source?: string;
  className?: string;
}

export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['br-stat', className].filter(Boolean).join(' ')}>
      <span className="br-stat__label">{label}</span>
      <span className="br-stat__value">{value}</span>
      {source !== undefined && <span className="br-stat__source">{source}</span>}
    </div>
  );
}
