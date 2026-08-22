export interface StatProps {
  value: string;
  label: string;
  /** Where the figure came from — a query, a window, a dashboard. */
  source?: string;
  className?: string;
}

/** The reference renders `0+` under GITHUB STARS when its fetch does not return.
 *  A confident wrong number is worse than an absent one, so an empty `value`
 *  renders the skeleton and never a zero. */
export function Stat({ value, label, source, className }: StatProps) {
  const pending = value.trim() === '';
  return (
    <div className={['pb-stat', pending ? 'pb-stat--pending' : undefined, className].filter(Boolean).join(' ')}>
      {pending ? (
        <span className="pb-stat__skeleton" aria-hidden="true" />
      ) : (
        <span className="pb-stat__value">{value}</span>
      )}
      <span className="pb-stat__label">{label}</span>
      {source && <span className="pb-stat__source">{source}</span>}
      {pending && <span className="pb-sr">{label} is still loading</span>}
    </div>
  );
}
