export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

/**
 * The metric at `--t-metric` (up to 104px) in the display face, its label above
 * in mono at `--ink-soft`, and the source below it.
 *
 * The figure is set in the monospaced display face on purpose: digits line up
 * in a column without `tabular-nums`, because every glyph in this pack's
 * display face is one advance wide.
 */
export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['cy-stat', className].filter(Boolean).join(' ')}>
      <span className="cy-stat__label">{label}</span>
      <span className="cy-stat__value">{value}</span>
      {source !== undefined && <span className="cy-stat__source">{source}</span>}
    </div>
  );
}
