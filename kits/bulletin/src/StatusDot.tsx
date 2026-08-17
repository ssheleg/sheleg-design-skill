export type Status = 'good' | 'warn' | 'danger' | 'info';

export interface StatusDotProps {
  status: Status;
  /** The word. The pack forbids status by colour alone, so this is required. */
  label: string;
  className?: string;
}

export function StatusDot({ status, label, className }: StatusDotProps) {
  return (
    <span className={['bl-status', `bl-status--${status}`, className].filter(Boolean).join(' ')}>
      <span className="bl-status__dot" aria-hidden="true" />
      {label}
    </span>
  );
}
