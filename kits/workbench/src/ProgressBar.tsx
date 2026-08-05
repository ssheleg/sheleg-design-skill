export interface ProgressBarProps {
  value: number;
  max?: number;
  /** Names what is progressing. Rendered above the track with the readout. */
  label?: string;
  /** Anything but `accent` is a state claim, not decoration. */
  tone?: 'accent' | 'ok' | 'warn' | 'danger';
  className?: string;
}

export function ProgressBar({
  value,
  max = 100,
  label,
  tone = 'accent',
  className,
}: ProgressBarProps) {
  const safeMax = max > 0 ? max : 1;
  const clamped = Math.min(Math.max(value, 0), safeMax);
  const percent = Math.round((clamped / safeMax) * 100);
  return (
    <div
      className={['wb-progress', `wb-progress--${tone}`, className].filter(Boolean).join(' ')}
    >
      {label !== undefined && (
        <div className="wb-progress__head">
          <span className="wb-progress__label">{label}</span>
          <span className="wb-progress__readout">{percent}%</span>
        </div>
      )}
      <div
        className="wb-progress__track"
        role="progressbar"
        aria-valuenow={clamped}
        aria-valuemin={0}
        aria-valuemax={safeMax}
        aria-label={label}
      >
        <div className="wb-progress__fill" style={{ width: `${percent}%` }} />
      </div>
    </div>
  );
}
