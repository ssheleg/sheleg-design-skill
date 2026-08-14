export type LayerTone = 'good' | 'warn' | 'bad' | 'na';

export interface LayerSegment {
  /** The layer's name, printed under its segment. */
  label: string;
  /** Points scored. `null` means the layer does not apply to this product. */
  score: number | null;
  /** Points available. Decides the segment's share of the track. */
  outOf: number;
  tone: LayerTone;
}

export interface LayerBarProps {
  segments: LayerSegment[];
  className?: string;
}

/**
 * The weighted score bar. A segment that does not apply is hatched and reads
 * `N/A`, never an empty track — an empty track reads as zero, which is a
 * different verdict.
 */
export function LayerBar({ segments, className }: LayerBarProps) {
  const total = segments.reduce((sum, s) => sum + s.outOf, 0) || 1;
  return (
    <div className={['ora-layerbar', className].filter(Boolean).join(' ')}>
      <div className="ora-layerbar__track">
        {segments.map((s) => (
          <div
            key={s.label}
            className={['ora-layerbar__slot', `ora-layerbar__slot--${s.tone}`].join(' ')}
            style={{ flexBasis: `${(s.outOf / total) * 100}%` }}
          >
            <span
              className="ora-layerbar__fill"
              style={{ transform: `scaleX(${s.score === null ? 0 : s.score / (s.outOf || 1)})` }}
            />
          </div>
        ))}
      </div>
      <div className="ora-layerbar__legend">
        {segments.map((s) => (
          <div
            key={s.label}
            className="ora-layerbar__item"
            style={{ flexBasis: `${(s.outOf / total) * 100}%` }}
          >
            <span className="ora-layerbar__name">{s.label}</span>
            <span className="ora-layerbar__count">
              {s.score === null ? 'N/A' : `${s.score}/${s.outOf}`}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
