export interface BenchmarkRowProps {
  label: string;
  value: string;
  /** A second column — a baseline to compare the value against. */
  baseline?: string;
  className?: string;
}

/**
 * A row of a benchmark table: the label in mono, the numbers right-aligned in
 * mono, a `1px --line` bottom rule.
 *
 * Numbers are right-aligned because that is the only way a column of them can
 * be compared at a glance, and they are mono because every figure on this page
 * is. This pack argues from measurements; the table is where it does that.
 */
export function BenchmarkRow({ label, value, baseline, className }: BenchmarkRowProps) {
  return (
    <div className={['pr-bench', className].filter(Boolean).join(' ')}>
      <span className="pr-bench__label">{label}</span>
      {baseline !== undefined && <span className="pr-bench__baseline">{baseline}</span>}
      <span className="pr-bench__value">{value}</span>
    </div>
  );
}
