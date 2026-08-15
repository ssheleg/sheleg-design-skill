/** The pack's state vocabulary, and the only reason a semantic colour appears. */
export type Status = 'running' | 'ok' | 'warn' | 'danger' | 'idle';

export interface StatusDotProps {
  status: Status;
  /** Rendered beside the dot. Omit it only when the row already says the state. */
  label?: string;
  className?: string;
}

const FALLBACK_LABEL: Record<Status, string> = {
  running: 'Running',
  ok: 'Done',
  warn: 'Needs a human',
  danger: 'Failed',
  idle: 'Idle',
};

export function StatusDot({ status, label, className }: StatusDotProps) {
  return (
    <span
      className={['lg-status', `lg-status--${status}`, className].filter(Boolean).join(' ')}
    >
      <span
        className="lg-status__dot"
        role="img"
        aria-label={label === undefined ? FALLBACK_LABEL[status] : undefined}
      />
      {label !== undefined && <span className="lg-status__label">{label}</span>}
    </span>
  );
}
