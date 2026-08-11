export type Status = 'good' | 'warn' | 'danger' | 'info';

export interface StatusChipProps {
  status: Status;
  /** Required, not optional. Status is never by colour alone in this pack. */
  label: string;
  /** On a dark panel the measured on-dark set applies instead of the paper one. */
  onPanel?: boolean;
  className?: string;
}

export function StatusChip({ status, label, onPanel = false, className }: StatusChipProps) {
  return (
    <span
      className={[
        'sb-status',
        `sb-status--${status}`,
        onPanel ? 'sb-status--on-panel' : undefined,
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {label}
    </span>
  );
}
