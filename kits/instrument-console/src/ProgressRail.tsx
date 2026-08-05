export interface RailAct {
  /** Stable id — the rail keys on this, never on the array index. */
  id: string;
  label: string;
}

export interface ProgressRailProps {
  acts: RailAct[];
  /** The act the reader is on. Marked `aria-current="step"`. */
  currentId: string;
  /** Accessible name for the rail. */
  label?: string;
  className?: string;
}

export function ProgressRail({
  acts,
  currentId,
  label = 'Act progress',
  className,
}: ProgressRailProps) {
  return (
    <ol className={['ic-rail', className].filter(Boolean).join(' ')} aria-label={label}>
      {acts.map((act) => {
        const current = act.id === currentId;
        return (
          <li
            key={act.id}
            className={['ic-rail__act', current ? 'ic-rail__act--current' : undefined]
              .filter(Boolean)
              .join(' ')}
            aria-current={current ? 'step' : undefined}
          >
            <span className="ic-rail__label">{act.label}</span>
            <span className="ic-rail__tick" aria-hidden="true" />
          </li>
        );
      })}
    </ol>
  );
}
