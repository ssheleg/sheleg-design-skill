import type { ReactNode } from 'react';

export interface LedgerProps {
  /** The group label: uppercase, +0.14em, with a square bullet ahead of it. */
  label?: string;
  /** The date the figures were last true. A ledger with no date is a poster. */
  updated?: string;
  /** Rendered beside the live square, e.g. "All systems ok". Never a bare dot. */
  status?: string;
  children: ReactNode;
  className?: string;
}

/**
 * The pack's signature element: a dark panel of dotted-leader rows. The scan
 * line that crosses it on the live site is motion and stays in the pack — a kit
 * is the static half.
 */
export function Ledger({ label, updated, status, children, className }: LedgerProps) {
  return (
    <section
      data-surface="panel"
      className={['sb-ledger', className].filter(Boolean).join(' ')}
    >
      {label !== undefined && (
        <p className="sb-ledger__label">
          <span className="sb-ledger__bullet" aria-hidden="true" />
          {label}
        </p>
      )}
      <div className="sb-ledger__rows">{children}</div>
      {(updated !== undefined || status !== undefined) && (
        <div className="sb-ledger__foot">
          {updated !== undefined && <div>Last updated: {updated}</div>}
          {status !== undefined && (
            <div className="sb-ledger__status">
              <span className="sb-ledger__live" aria-hidden="true" />
              {status}
            </div>
          )}
        </div>
      )}
    </section>
  );
}
