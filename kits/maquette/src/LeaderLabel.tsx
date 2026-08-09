export interface LeaderLabelProps {
  label: string;
  /** Which side the dotted leader runs to. */
  side?: 'top' | 'left' | 'right';
  className?: string;
}

/**
 * A mono caption on a cream chip with a 1px dotted `--leader` running to the
 * block it names.
 *
 * The label stays at `--t-label` 13px at **every** viewport width. Scaling it
 * with the drawing makes it illegible at exactly the size where the drawing is
 * hardest to read; below 640px the labels move outside the model's bounding box
 * with longer leaders instead.
 */
export function LeaderLabel({ label, side = 'top', className }: LeaderLabelProps) {
  return (
    <span className={['mq-leader', `mq-leader--${side}`, className].filter(Boolean).join(' ')}>
      <span className="mq-leader__line" aria-hidden="true" />
      <span className="mq-leader__chip">{label}</span>
    </span>
  );
}
