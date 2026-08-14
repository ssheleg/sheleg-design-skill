export interface ScheduleLaneProps {
  name: string;
  /** The cadence, written the way the machine states it: `every 8h`. */
  cadence?: string;
  /** Tick positions along the lane, 0–1. */
  marks: number[];
  /** Index into `marks` that is running now, if any. */
  activeIndex?: number;
  /** What the active tick is doing. Required whenever `activeIndex` is set. */
  activeLabel?: string;
  className?: string;
}

export function ScheduleLane({
  name,
  cadence,
  marks,
  activeIndex,
  activeLabel,
  className,
}: ScheduleLaneProps) {
  const awake = activeIndex !== undefined;
  return (
    <div
      className={['pc-lane', awake ? 'pc-lane--awake' : 'pc-lane--asleep', className]
        .filter(Boolean)
        .join(' ')}
    >
      <span className="pc-lane__label">
        <span className="pc-lane__name">{name}</span>
        {cadence !== undefined && <span className="pc-lane__cadence">{cadence}</span>}
      </span>
      <span className="pc-lane__track">
        <span className="pc-lane__line" aria-hidden="true" />
        {marks.map((at, i) => (
          <span
            key={i}
            className={[
              'pc-lane__mark',
              i === activeIndex ? 'pc-lane__mark--active' : undefined,
            ]
              .filter(Boolean)
              .join(' ')}
            style={{ left: `${Math.min(1, Math.max(0, at)) * 100}%` }}
          />
        ))}
        {awake && activeLabel !== undefined && (
          <span
            className="pc-lane__work"
            style={{ left: `${Math.min(1, Math.max(0, marks[activeIndex] ?? 0)) * 100}%` }}
          >
            {activeLabel}
          </span>
        )}
      </span>
    </div>
  );
}
