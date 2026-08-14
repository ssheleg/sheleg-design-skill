export type Status = 'good' | 'warn' | 'danger' | 'info' | 'live' | 'idle';

export interface StatusDotProps {
  status: Status;
  /** The word. Required by the pack: a dot never carries the meaning alone. */
  label: string;
  className?: string;
}

/**
 * A 6px dot plus its word. `live` is the only one that pulses, and it means work
 * is happening right now — it never appears beside a finished state.
 */
export function StatusDot({ status, label, className }: StatusDotProps) {
  return (
    <span className={['ora-status', `ora-status--${status}`, className].filter(Boolean).join(' ')}>
      <span className="ora-status__dot" aria-hidden="true" />
      <span className="ora-status__label">{label}</span>
    </span>
  );
}
