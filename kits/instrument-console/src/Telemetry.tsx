export interface TelemetryItem {
  /** Stable id — rows key on this, never on the array index. */
  id: string;
  label: string;
  value: string;
  /** The mono annotation under the value: a unit, a window, a limit. */
  note?: string;
  /** Anything but `neutral` is a status claim, not decoration. */
  tone?: 'neutral' | 'ok' | 'warn';
}

export interface TelemetryProps {
  items: TelemetryItem[];
  /** Names the readout. Set above the first row. */
  caption?: string;
  className?: string;
}

export function Telemetry({ items, caption, className }: TelemetryProps) {
  return (
    <div className={['ic-tlm', className].filter(Boolean).join(' ')}>
      {caption !== undefined && <p className="ic-tlm__caption">{caption}</p>}
      <dl className="ic-tlm__list">
        {items.map((item) => (
          <div
            key={item.id}
            className={['ic-tlm__row', `ic-tlm__row--${item.tone ?? 'neutral'}`].join(' ')}
          >
            <dt className="ic-tlm__label">{item.label}</dt>
            <dd className="ic-tlm__value">
              <span className="ic-tlm__reading">{item.value}</span>
              {item.note !== undefined && <span className="ic-tlm__note">{item.note}</span>}
            </dd>
          </div>
        ))}
      </dl>
    </div>
  );
}
