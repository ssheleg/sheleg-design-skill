import type { ReactNode } from 'react';

export interface OrgNodeProps {
  name: string;
  /** The runtime behind the role — Claude, Codex, Cursor, Hermes. */
  model?: string;
  /** Live nodes announce themselves with a word, never with the ring alone. */
  live?: boolean;
  /** The word a live node announces. Required reading, not decoration. */
  liveLabel?: string;
  icon?: ReactNode;
  className?: string;
}

export function OrgNode({
  name,
  model,
  live = false,
  liveLabel = 'Active',
  icon,
  className,
}: OrgNodeProps) {
  return (
    <div
      className={['pc-node', live ? 'pc-node--live' : undefined, className]
        .filter(Boolean)
        .join(' ')}
    >
      {icon !== undefined && <span className="pc-node__icon">{icon}</span>}
      <span className="pc-node__body">
        <span className="pc-node__name">{name}</span>
        {model !== undefined && (
          <span className="pc-node__model">
            <span className="pc-node__dot" aria-hidden="true" />
            {model}
          </span>
        )}
      </span>
      {live && <span className="pc-node__live">{liveLabel}</span>}
    </div>
  );
}
