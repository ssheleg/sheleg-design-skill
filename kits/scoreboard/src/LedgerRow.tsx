export interface LedgerRowProps {
  /** Left column, two lines at most. It does not wrap past that. */
  label: string;
  /** The figure. Set in the pixel face, right-aligned on a fixed column. */
  value: string;
  /** No figure yet: the row survives and an em dash holds the column. */
  pending?: boolean;
  className?: string;
}

/**
 * Label, a dotted leader, and a pixel numeral on a fixed column. A row that
 * wraps is not a row — the leader absorbs every width change instead.
 */
export function LedgerRow({ label, value, pending = false, className }: LedgerRowProps) {
  return (
    <div className={['sb-row', className].filter(Boolean).join(' ')}>
      <span className="sb-row__label">{label}</span>
      <span className="sb-row__leader" aria-hidden="true" />
      <span className={['sb-row__value', pending ? 'sb-row__value--pending' : undefined]
        .filter(Boolean)
        .join(' ')}
      >
        {pending ? '—' : value}
      </span>
    </div>
  );
}
