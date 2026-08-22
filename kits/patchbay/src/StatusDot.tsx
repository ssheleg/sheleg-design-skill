export interface StatusDotProps {
  state: 'ok' | 'warn' | 'danger';
  /** Mandatory. The word carries the state; the dot only repeats it. */
  label: string;
  className?: string;
}

export function StatusDot({ state, label, className }: StatusDotProps) {
  return (
    <span className={['pb-status', `pb-status--${state}`, className].filter(Boolean).join(' ')}>
      <span className="pb-status__dot" aria-hidden="true" />
      {label}
    </span>
  );
}
