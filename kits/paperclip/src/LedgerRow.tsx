import type { ReactNode } from 'react';

export interface LedgerRowProps {
  name: string;
  /** The runtime the spend belongs to. */
  model?: string;
  /** Spent, already formatted — the component never does currency maths. */
  spent: string;
  /** The ceiling, already formatted. */
  budget: string;
  /** 0–1. Drives scaleX, never width. */
  fraction: number;
  /** Said out loud when the row is over its ceiling — the colour is not the message. */
  note?: string;
  icon?: ReactNode;
  className?: string;
}

export function LedgerRow({
  name,
  model,
  spent,
  budget,
  fraction,
  note,
  icon,
  className,
}: LedgerRowProps) {
  const clamped = Math.min(1, Math.max(0, fraction));
  return (
    <div className={['pc-ledger', className].filter(Boolean).join(' ')}>
      <span className="pc-ledger__agent">
        {icon !== undefined && <span className="pc-ledger__icon">{icon}</span>}
        <span className="pc-ledger__id">
          <span className="pc-ledger__name">{name}</span>
          {model !== undefined && <span className="pc-ledger__model">{model}</span>}
        </span>
      </span>
      <span className="pc-ledger__track">
        <span
          className="pc-ledger__fill"
          style={{ transform: `scaleX(${clamped})` }}
          role="img"
          aria-label={`${spent} of ${budget}`}
        />
      </span>
      <span className="pc-ledger__cost">
        <span className="pc-ledger__spent">{spent}</span>
        <span className="pc-ledger__budget">/ {budget}</span>
        {note !== undefined && <span className="pc-ledger__note">{note}</span>}
      </span>
    </div>
  );
}
