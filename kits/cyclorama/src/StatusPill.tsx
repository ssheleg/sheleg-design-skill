/**
 * The four states this pack ships. There is no fifth, and there is no
 * confidence number: a percentage with nothing behind it is exactly what a
 * named state exists instead of.
 */
export type Status = 'live' | 'good' | 'warning' | 'danger';

export interface StatusPillProps {
  status: Status;
  /** The word beside the mark. It is required, and that is the whole point. */
  label: string;
  className?: string;
}

/**
 * A mark **and its word** — `● Listening`, never a bare dot.
 *
 * `label` is a required prop because this component is where the pack's
 * colour-blindness rule is made structural instead of optional. The numbers
 * behind that rule: `--good` and `--danger` separate by only 7.2 under
 * protanopia and 5.9 under deuteranopia, and `--signal` sits 6.8 from
 * `--accent` under protanopia — a pair the repository's palette gate cannot
 * even see, because `--signal` is not one of the names it treats as semantic.
 *
 * So the word is not decoration and it is not an accessibility afterthought:
 * it is the only thing carrying the meaning for a reader who cannot separate
 * the two marks. An API that let you omit it would be an API that lets you
 * ship the bug.
 */
export function StatusPill({ status, label, className }: StatusPillProps) {
  return (
    <span className={['cy-status', `cy-status--${status}`, className].filter(Boolean).join(' ')}>
      <i className="cy-status__mark" aria-hidden="true" />
      <span className="cy-status__label">{label}</span>
    </span>
  );
}
