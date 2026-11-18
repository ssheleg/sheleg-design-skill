import type { ReactNode } from 'react';

export interface ChatLineProps {
  /** Speaker name, set in mono above the line. */
  who: string;
  /** Initials for the disc when no portrait is passed. */
  initials?: string;
  /** A portrait or a Duotone in place of the initials disc. */
  avatar?: ReactNode;
  /** An agent's line takes the phosphor border and its glow. */
  agent?: boolean;
  /** A system notice: centred mono phosphor, no bubble. */
  system?: boolean;
  children: ReactNode;
  className?: string;
}

export function ChatLine({ who, initials, avatar, agent = false, system = false, children, className }: ChatLineProps) {
  const cls = ['ph-line', agent ? 'ph-line--agent' : null, system ? 'ph-line--system' : null, className]
    .filter(Boolean)
    .join(' ');
  if (system) {
    return (
      <div className={cls}>
        <p className="ph-line__text">{children}</p>
      </div>
    );
  }
  return (
    <div className={cls}>
      {avatar ?? (
        <span className="ph-line__face" aria-hidden="true">
          {initials ?? who.slice(0, 2).toUpperCase()}
        </span>
      )}
      <div>
        <b className="ph-line__who">{who}</b>
        <p className="ph-line__text">{children}</p>
      </div>
    </div>
  );
}
