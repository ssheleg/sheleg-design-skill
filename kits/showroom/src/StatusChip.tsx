/** The four states this pack ships. There is no fifth and no confidence number. */
export type Status = 'good' | 'warning' | 'danger' | 'neutral';

export interface StatusChipProps {
  status: Status;
  /** The word inside the chip. Required, and that is the whole design. */
  label: string;
  className?: string;
}

/**
 * A tinted chip with its word **inside** it — never a bare coloured dot.
 *
 * `label` is required because this is where the pack's colour rule becomes API.
 * `--good` and `--danger` separate by 33.7 at full colour and by only **4.9
 * under deuteranopia**; for that reader the word is not a helpful extra, it is
 * the only thing carrying the meaning. An API that let you omit it would be an
 * API that lets you ship the bug.
 */
export function StatusChip({ status, label, className }: StatusChipProps) {
  return (
    <span className={['sw-status', `sw-status--${status}`, className].filter(Boolean).join(' ')}>
      {label}
    </span>
  );
}
