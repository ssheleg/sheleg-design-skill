export type Status = 'ok' | 'warn' | 'danger' | 'neutral';

export interface StatusDotProps {
  status: Status;
  /** The word. Never omit it: this pack states status is never by colour alone. */
  label: string;
  className?: string;
}

export function StatusDot({ status, label, className }: StatusDotProps) {
  return (
    <span
      className={['nt-status', `nt-status--${status}`, className].filter(Boolean).join(' ')}
    >
      <span className="nt-status__dot" aria-hidden="true" />
      {label}
    </span>
  );
}
