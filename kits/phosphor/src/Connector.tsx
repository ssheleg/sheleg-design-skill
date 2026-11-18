export interface ConnectorProps {
  /** What the connector carries to the next panel, set in mono beside it. */
  carries?: string;
  className?: string;
}

/** The drawn arrow between two panels: one 3px stroke, round caps, a soft phosphor drop-shadow. */
export function Connector({ carries, className }: ConnectorProps) {
  return (
    <div className={['ph-connector', className].filter(Boolean).join(' ')}>
      <svg className="ph-connector__arrow" viewBox="0 0 120 110" aria-hidden="true">
        <path d="M20 8 C 70 20, 96 50, 82 96 M66 84 L82 98 L96 82" pathLength="240" />
      </svg>
      {carries && <span className="ph-connector__carries">{carries}</span>}
    </div>
  );
}
