export interface StatProps {
  value: string;
  label: string;
  /** Who produced the figure. Optional in the API, required by the pack. */
  source?: string;
  className?: string;
}

/**
 * A figure on the paper, with no tile around it: a mono label, the number in
 * the display face, and the source underneath in the same block. `source` is
 * optional only because the spine's shape is identical in every kit — in this
 * pack a claim with no source in the same block is a ban.
 */
export function Stat({ value, label, source, className }: StatProps) {
  return (
    <div className={['fn-stat', className].filter(Boolean).join(' ')}>
      <span className="fn-stat__label">{label}</span>
      <span className="fn-stat__value">{value}</span>
      {source !== undefined && <span className="fn-stat__source">{source}</span>}
    </div>
  );
}
